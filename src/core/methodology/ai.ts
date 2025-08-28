import { ChatOpenAI } from '@langchain/openai';
import { PromptTemplate } from '@langchain/core/prompts';
import { JsonOutputParser } from '@langchain/core/output_parsers';
import {
  generateSchema,
  validateSchema,
  Schema,
} from '../../utils/object-utils';
import {
  listRulePathsFromMethodology,
  getRuleFromMethodologyByPath,
  readMethodologyFile,
  methodologyFilesMapping,
} from './base';

/**
 * Model configuration object
 * @param model - The model to use
 * @param apiKey - The API key to use
 * @param baseURL - The base URL to use
 */
export type ModelConfig = {
  model?: string;
  apiKey?: string;
  baseURL?: string;
};

async function getModel(modelConfig: ModelConfig) {
  const chat_model = new ChatOpenAI({
    model: modelConfig.model || process.env.OPENAI_CHAT_MODEL,
    configuration: {
      apiKey: modelConfig.apiKey || process.env.OPENAI_API_KEY,
      baseURL: modelConfig.baseURL || process.env.OPENAI_BASE_URL,
    },
  });
  return chat_model;
}

/**
 * Custom extractor
 *
 * Extracts JSON content from a string where
 * JSON is embedded between ```json and ``` tags.
 */
const extractJson = (output: any, schema: Schema, returnSingle = true): any => {
  const text =
    typeof output === 'string'
      ? output
      : ((output.content || output.toString()) as string);
  // Define the regular expression pattern to match JSON blocks
  const pattern = /```json(.*?)```/gs;

  // Find all non-overlapping matches of the pattern in the string
  const matches = text.match(pattern);

  if (!matches || matches.length === 0) {
    throw new Error('No JSON blocks found in AI response');
  }

  // Process each match, attempting to parse it as JSON
  try {
    const results = matches.map((match) => {
      // Remove the markdown code block syntax to isolate the JSON string
      const jsonStr = match.replace(/```json|```/g, '').trim();

      let jsonData;
      try {
        jsonData = JSON.parse(jsonStr);
      } catch (parseError) {
        console.error('Invalid JSON format Error:', JSON.stringify(parseError));
        throw new Error(`Invalid JSON format: ${jsonStr.substring(0, 100)}...`);
      }

      const isValid = validateSchema(jsonData, schema);
      if (!isValid) {
        throw new Error(`JSON does not match expected schema`);
      }

      return jsonData;
    });

    return returnSingle && results.length === 1 ? results[0] : results;
  } catch (error) {
    console.error('JSON extraction failed:', error);
    throw new Error(
      `Failed to extract valid JSON: ${(error as Error).message}`
    );
  }
};

async function fixJsonDataWithAI(
  data: any,
  originalData: any,
  modelConfig?: ModelConfig
) {
  const fixPrompt = `
    There are two JSON objects, first one is the original data, second one is the data after some modifications.

    Due to some content processing, the structure of the second JSON data has changed compared to the first one. Please modify the second JSON data according to the first JSON data, so that its structure matches the first JSON data.

    The first JSON data is:
    {originalData}

    The second JSON data is:
    {data}

    Output your answer as JSON that
    matches the given schema: \`\`\`json\n{schema}\n\`\`\`.
    Make sure to wrap the answer in \`\`\`json and \`\`\` tags
    `;
  const schema = generateSchema(originalData);
  const model = await getModel(modelConfig || {});
  const parser = new JsonOutputParser();
  const prompt = new PromptTemplate({
    template: fixPrompt,
    inputVariables: ['originalData', 'data', 'schema'],
  });
  const chain = prompt.pipe(model).pipe(parser);
  const result = await chain.invoke({
    originalData: JSON.stringify(originalData),
    data: JSON.stringify(data),
    schema: JSON.stringify(schema),
  });
  return extractJson(result, schema);
}

/**
 * Extracts valid JSON data from AI response with retry mechanism
 * Combines extractJson and fixJsonDataWithAI functions to ensure the extracted data
 * matches the original data structure
 *
 * @param data - The AI response or data containing JSON
 * @param originalData - The original data structure to match
 * @param schema - The schema to validate against
 * @param maxRetries - Maximum number of retry attempts (default: 3)
 * @returns The extracted and validated JSON data
 */
export async function extractValidJsonWithRetry(
  data: any,
  originalData: any,
  schema?: Schema,
  maxRetries: number = 3
): Promise<any> {
  // Use provided schema or generate from original data
  const validationSchema = schema || generateSchema(originalData);

  let lastError: Error | null = null;

  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      console.log(`Attempt ${attempt} of ${maxRetries}: Extracting JSON...`);

      // First try to extract JSON directly
      try {
        const extractedData = extractJson(data, validationSchema, true);

        // Validate the extracted data matches the original structure
        if (validateSchema(extractedData, validationSchema)) {
          console.log(
            `Success on attempt ${attempt}: JSON extracted and validated`
          );
          return extractedData;
        }

        // If validation fails, try to fix the structure
        console.log(
          `Attempt ${attempt}: Structure mismatch, attempting to fix...`
        );
        const fixedData = await fixJsonDataWithAI(extractedData, originalData);

        if (validateSchema(fixedData, validationSchema)) {
          console.log(`Success on attempt ${attempt}: JSON structure fixed`);
          return fixedData;
        }

        throw new Error('Fixed data still does not match original structure');
      } catch (extractError) {
        // If extraction fails completely, try to fix the raw data
        console.log(
          'ExtractError:',
          JSON.stringify(extractError),
          `\nAttempt ${attempt}: Direct extraction failed, using AI to fix...`
        );

        // Convert data to string if needed
        const dataStr = typeof data === 'string' ? data : JSON.stringify(data);

        // Use AI to fix and extract
        const fixedData = await fixJsonDataWithAI(dataStr, originalData);

        if (validateSchema(fixedData, validationSchema)) {
          console.log(
            `Success on attempt ${attempt}: AI fixed and extracted JSON`
          );
          return fixedData;
        }

        throw new Error('AI-fixed data does not match original structure');
      }
    } catch (error) {
      lastError = error as Error;
      console.error(`Attempt ${attempt} failed:`, lastError.message);

      if (attempt < maxRetries) {
        console.log(`Retrying in 1 second...`);
        await new Promise((resolve) => setTimeout(resolve, 1000));
      }
    }
  }

  // All attempts failed
  throw new Error(
    `Failed to extract valid JSON after ${maxRetries} attempts. Last error: ${lastError?.message}`
  );
}

/**
 * Suggests improvements to data based on TIDAS methodology rules.
 *
 * This function uses AI to analyze the provided data against TIDAS methodology rules
 * and suggests optimized content that better complies with the methodology requirements.
 * The function ensures that the data structure remains unchanged while improving the content.
 *
 * @param data - The original data object to be improved. Can be any JSON-serializable object
 *               such as process names, descriptions, or other TIDAS/ILCD data elements.
 * @param methodology - The methodology rules to apply. Can be:
 *                      - A complete methodology object loaded from YAML
 *                      - A specific rule object extracted using getRuleFromMethodologyByPath
 *                      - A custom rule object with description and rules properties
 * @param modelConfig - The configuration for the AI model. Can be:
 *                      - A complete model configuration object
 *                      - A custom model configuration object with model, apiKey, and baseURL properties
 * @returns Promise<any> - The improved data with the same structure as the input but with
 *                        optimized content that better complies with the methodology.
 *                        The returned data is guaranteed to match the original schema.
 *
 * @example
 * ```typescript
 * // Example 1: Improve a process name using specific rules
 * const nameData = [{ '@xml:lang': 'en', '#text': 'Process 1' }];
 * const rule = await getRuleFromMethodologyByPath(methodology, 'processDataSet.processInformation.dataSetInformation.name.baseName');
 * const improvedName = await suggest(nameData, rule);
 * // Returns: [{ '@xml:lang': 'en', '#text': 'Production of Product A using Technology X' }]
 *
 * // Example 2: Improve data using full methodology
 * const processData = { name: 'test', description: 'simple desc' };
 * const improvedData = await suggest(processData, fullMethodology);
 * // Returns data with improved names and descriptions
 * ```
 *
 * @throws {Error} If the AI model fails to generate valid JSON
 * @throws {Error} If the OpenAI API is not configured properly
 */
async function suggest(
  data: any,
  methodology: any,
  modelConfig?: ModelConfig
): Promise<any> {
  const startTime = Date.now();

  // Prompt template for the AI model
  const suggestPrompt = `
You are an Expert in the field of Life Cycle Assessment (LCA) and the TIDAS methodology.

You are given a JSON Object Data and the corresponding TIDAS methodology which offers the rules for the data.

Your task is to modify the data content according to the methodology rules, optimizing it to better comply with the methodology requirements. 
Provide the optimized JSON result, and ensure that the data structure remains unchanged.

The data is:
{data}

The methodology is:
{methodology}

Output your answer as JSON that
matches the given schema: \`\`\`json\n{schema}\n\`\`\`.
Make sure to wrap the answer in \`\`\`json and \`\`\` tags

`;

  // Initialize the AI model
  const model = await getModel(modelConfig || {});

  // Create the prompt template with input variables
  const prompt = new PromptTemplate({
    template: suggestPrompt,
    inputVariables: ['data', 'methodology', 'schema'],
  });

  // Generate schema from the input data to ensure structure preservation
  const schema = generateSchema(data);

  // Create parser for JSON output
  const parser = new JsonOutputParser();

  // Build the processing chain
  const chain = prompt.pipe(model).pipe(parser);

  // Invoke the AI model with the formatted inputs
  const result = await chain.invoke({
    data: JSON.stringify(data),
    methodology: JSON.stringify(methodology),
    schema: JSON.stringify(schema),
  });

  // Log performance metrics
  const endTime = Date.now();
  console.log(`Suggestion took ${endTime - startTime}ms`);

  return result;
}

/**
 * Reviews data against TIDAS methodology rules and provides structured feedback.
 *
 * This function uses AI to analyze the provided data against TIDAS methodology rules
 * and provides a review with comments and a compliance score. Unlike the suggest function
 * which modifies data, this function only provides assessment and feedback.
 *
 * @param data - The data object to be reviewed. Can be any JSON-serializable object
 *               such as process names, descriptions, or other TIDAS/ILCD data elements.
 * @param methodology - The methodology rules to evaluate against. Can be:
 *                      - A complete methodology object loaded from YAML
 *                      - A specific rule object extracted using getRuleFromMethodologyByPath
 *                      - A custom rule object with description and rules properties
 * @param modelConfig - The configuration for the AI model. Can be:
 *                      - A complete model configuration object
 *                      - A custom model configuration object with model, apiKey, and baseURL properties
 * @returns Promise<{review_comment: string, review_score: number}> - A structured review containing:
 *                        - review_comment: Detailed feedback on compliance and suggestions for improvement
 *                        - review_score: A numerical score from 0-100 indicating compliance level
 *
 * @example
 * ```typescript
 * // Example 1: Review a process name against specific rules
 * const nameData = [{ '@xml:lang': 'en', '#text': 'Process 1' }];
 * const rule = await getRuleFromMethodologyByPath(methodology, 'processDataSet.processInformation.dataSetInformation.name.baseName');
 * const review = await reviewData(nameData, rule);
 * // Returns: {
 * //   review_comment: "The process name 'Process 1' is too generic. It should include specific information about...",
 * //   review_score: 45
 * // }
 *
 * // Example 2: Review complete process data
 * const processData = { name: 'test', description: 'simple desc' };
 * const review = await reviewData(processData, fullMethodology);
 * // Returns comprehensive review with score
 * ```
 *
 * @throws {Error} If the AI model fails to generate valid structured output
 * @throws {Error} If the OpenAI API is not configured properly
 */
async function reviewData(
  data: any,
  methodology: any,
  modelConfig?: ModelConfig
): Promise<{ review_comment: string; review_score: number }> {
  const startTime = Date.now();

  // Review prompt template for the AI model
  const reviewPrompt = `
You are an Expert in the field of Life Cycle Assessment (LCA) and the TIDAS methodology.

You are given a JSON Object Data and the corresponding TIDAS methodology rules to review against.

Your task is to:
1. Analyze the data against the methodology rules
2. Identify areas of compliance and non-compliance
3. Provide specific, actionable feedback
4. Assign a compliance score from 0-100

The data to review is:
{data}

The methodology rules are:
{methodology}

Provide a detailed review with the following structure:
- review_comment: A comprehensive review comment that includes:
  * What aspects comply well with the methodology
  * What aspects need improvement
  * Specific suggestions for improvement
  * Overall assessment of data quality
- review_score: A numerical score from 0-100 where:
  * 0-30: Poor compliance, major issues
  * 31-50: Below average, significant improvements needed
  * 51-70: Average compliance, some improvements recommended
  * 71-85: Good compliance, minor improvements possible
  * 86-100: Excellent compliance with methodology

Output your answer as JSON in this exact format:
\`\`\`json
{{
  "review_comment": "Your detailed review here",
  "review_score": 75
}}
\`\`\`
`;

  // Initialize the AI model with structured output
  const model = await getModel(modelConfig || {});

  // Define the output schema using Zod
  const { z } = await import('zod');
  const reviewSchema = z.object({
    review_comment: z
      .string()
      .describe(
        'Detailed review comment with compliance assessment and suggestions'
      ),
    review_score: z
      .number()
      .min(0)
      .max(100)
      .describe('Compliance score from 0-100'),
  });

  // Configure model with structured output
  const modelWithStructure = model.withStructuredOutput(reviewSchema, {
    name: 'review_output',
  });

  // Create the prompt template with input variables
  const prompt = new PromptTemplate({
    template: reviewPrompt,
    inputVariables: ['data', 'methodology'],
  });

  // Build the processing chain
  const chain = prompt.pipe(modelWithStructure);

  try {
    // Invoke the AI model with the formatted inputs
    const result = await chain.invoke({
      data: JSON.stringify(data, null, 2),
      methodology: JSON.stringify(methodology, null, 2),
    });

    // Log performance metrics
    const endTime = Date.now();
    console.log(`Review completed in ${endTime - startTime}ms`);
    console.log(`Review score: ${result.review_score}/100`);

    return result;
  } catch (error) {
    console.error('Review failed:', error);

    // Fallback to parsing from regular output if structured output fails
    try {
      const prompt = new PromptTemplate({
        template: reviewPrompt,
        inputVariables: ['data', 'methodology'],
      });

      const chain = prompt.pipe(model);
      const result = await chain.invoke({
        data: JSON.stringify(data, null, 2),
        methodology: JSON.stringify(methodology, null, 2),
      });

      // Extract JSON from the response
      const text = result.content as string;
      const jsonMatch = text.match(/```json\s*([\s\S]*?)\s*```/);
      if (jsonMatch && jsonMatch[1]) {
        const parsed = JSON.parse(jsonMatch[1]);

        // Validate the structure
        if (
          typeof parsed.review_comment === 'string' &&
          typeof parsed.review_score === 'number' &&
          parsed.review_score >= 0 &&
          parsed.review_score <= 100
        ) {
          const endTime = Date.now();
          console.log(
            `Review completed in ${endTime - startTime}ms (fallback mode)`
          );
          console.log(`Review score: ${parsed.review_score}/100`);
          return parsed;
        }
      }

      throw new Error(
        'Failed to extract valid review structure from AI response'
      );
    } catch (fallbackError) {
      throw new Error(`Review failed: ${(fallbackError as Error).message}`);
    }
  }
}

/**
 * Suggests improvements for an entire object based on all applicable methodology rules.
 *
 * This function analyzes a complete data object against all relevant methodology rules,
 * applies AI suggestions to each applicable field, and returns a new object with improvements.
 *
 * @param data - The complete data object to improve (TidasEntity or plain object)
 * @param methodologyType - The type of methodology to use:
 *                         - A string key from methodologyFilesMapping (e.g., 'processes', 'flows')
 *                         - A methodology object already loaded
 * @param options - Optional configuration:
 *                 - parallelRequests: Number of parallel AI requests (default: 1)
 *                 - skipPaths: Array of paths to skip
 *                 - maxRetries: Maximum retries per rule (default: 1)
 * @returns Promise<any> - Improved data object with the same structure as input
 *
 * @example
 * ```typescript
 * // Example: Improve an entire Process object
 * const process = createProcess();
 * process.processDataSet.processInformation.dataSetInformation['common:UUID'] = 'test-123';
 * const improvedData = await suggestEntireObject(process, 'processes');
 *
 * // Create a new Process with improved data
 * const improvedProcess = createProcess();
 * Object.assign(improvedProcess, improvedData);
 * ```
 */
export async function suggestEntireObject(
  data: any,
  methodologyType: string | Record<string, any>,
  options?: {
    skipPaths?: string[];
    maxRetries?: number;
  }
): Promise<any> {
  const startTime = Date.now();

  // Default options
  const opts = {
    skipPaths: [],
    maxRetries: 1,
    ...options,
  };

  console.log('Starting comprehensive object improvement...');

  // Load methodology if string is provided
  let methodology: Record<string, any>;
  if (typeof methodologyType === 'string') {
    const methodologyPath = methodologyFilesMapping[methodologyType];
    if (!methodologyPath) {
      throw new Error(
        `Unknown methodology type: ${methodologyType}. Available types: ${Object.keys(methodologyFilesMapping).join(', ')}`
      );
    }
    methodology = await readMethodologyFile(methodologyPath);
    console.log(`Loaded methodology: ${methodologyType}`);
  } else {
    methodology = methodologyType;
  }

  // Get all rule paths from the methodology
  const allRulePaths = await listRulePathsFromMethodology(methodology);
  console.log(`Found ${allRulePaths.length} rule paths`);

  // Convert TidasEntity to plain object if needed
  let plainData = data;
  if (data && typeof data.getValue === 'function') {
    // It's a TidasEntity, extract the raw data
    plainData = JSON.parse(JSON.stringify(data));
  }

  // Create a deep copy for modifications
  const improvedData = JSON.parse(JSON.stringify(plainData));

  // Helper function to get value from path
  const getValueByPath = (obj: any, path: string): any => {
    const pathParts = path.split('.');
    let current = obj;

    for (const part of pathParts) {
      if (current && typeof current === 'object' && part in current) {
        current = current[part];
      } else {
        return undefined;
      }
    }

    return current;
  };

  // Helper function to set value at path
  const setValueByPath = (obj: any, path: string, value: any): void => {
    const pathParts = path.split('.');
    let target = obj;

    for (let i = 0; i < pathParts.length - 1; i++) {
      if (!target[pathParts[i]]) {
        target[pathParts[i]] = {};
      }
      target = target[pathParts[i]];
    }

    target[pathParts[pathParts.length - 1]] = value;
  };

  // Process rule for a single path
  const processPath = async (
    path: string
  ): Promise<{ path: string; original: any; suggested: any } | null> => {
    // Skip if in skip list
    if (opts.skipPaths && opts.skipPaths.includes(path)) {
      console.log(`Skipping path (user request): ${path}`);
      return null;
    }

    try {
      // Get rule for this path
      const rule = await getRuleFromMethodologyByPath(methodology, path);
      if (!rule) {
        return null;
      }

      // Extract value at this path from the data
      const currentValue = getValueByPath(plainData, path);

      // Skip if no value at this path
      if (currentValue === undefined || currentValue === null) {
        console.log(`Skipping path (no data): ${path}`);
        return null;
      }

      console.log(`Processing: ${path}`);

      // Apply suggestion with retry
      for (let retry = 1; retry <= opts.maxRetries; retry++) {
        try {
          const suggestedValue = await suggest(currentValue, rule);

          // Validate structure is preserved
          const originalSchema = generateSchema(currentValue);
          if (validateSchema(suggestedValue, originalSchema)) {
            console.log(`  ✓ Improved: ${path}`);
            return {
              path,
              original: currentValue,
              suggested: suggestedValue,
            };
          }
        } catch (error) {
          console.log(
            `  Retry ${retry}/${opts.maxRetries} failed: ${(error as Error).message}`
          );
          if (retry < opts.maxRetries) {
            await new Promise((resolve) => setTimeout(resolve, 1000));
          }
        }
      }
    } catch (error) {
      console.error(`Error processing ${path}:`, (error as Error).message);
    }

    return null;
  };

  // Process all paths in parallel
  console.log('Processing all paths in parallel...');
  const results = await Promise.all(
    allRulePaths.map((path) => processPath(path))
  );

  // Filter out null results and apply improvements
  const improvements = results.filter((r) => r !== null) as {
    path: string;
    original: any;
    suggested: any;
  }[];

  // Apply all improvements to the improvedData object
  for (const improvement of improvements) {
    setValueByPath(improvedData, improvement.path, improvement.suggested);
  }

  const endTime = Date.now();
  console.log(
    `\nCompleted ${methodologyType} Suggestion in ${endTime - startTime}ms`
  );
  console.log(
    `Applied ${improvements.length} improvements out of ${allRulePaths.length} possible paths`
  );

  return improvedData;
}

// Export other functions that might be used externally
export { extractJson, fixJsonDataWithAI, suggest, reviewData, getModel };
