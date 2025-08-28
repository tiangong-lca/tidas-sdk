import { createProcess, suggestData } from '@tiangong-lca/tidas-sdk';
import * as dotenv from 'dotenv';
import * as path from 'path';
import * as fs from 'fs';

dotenv.config();

const processEntity = createProcess({
  processDataSet: {
    '@xmlns:common': 'http://lca.jrc.it/ILCD/Common',
    '@xmlns': 'http://lca.jrc.it/ILCD/Process',
    '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    '@version': '1.1',
    processInformation: {
      dataSetInformation: {
        'common:UUID': 'ab051324-d573-4f92-bedd-8bcb43f17cf3',
        name: {
          baseName: [
            { '@xml:lang': 'en', '#text': 'steel production' },
            { '@xml:lang': 'zh', '#text': '钢铁生产' },
          ],
          treatmentStandardsRoutes: [{ '@xml:lang': 'en', '#text': 'none' }],
          mixAndLocationTypes: [
            { '@xml:lang': 'en', '#text': 'production mix' },
            { '@xml:lang': 'zh', '#text': '生产混合' },
          ],
        },
        'common:generalComment': [
          {
            '@xml:lang': 'en',
            '#text': 'Basic steel process',
          },
        ],
        classificationInformation: {
          'common:classification': {
            'common:class': [
              { '@level': '0', '@classId': '1', '#text': 'Process' },
              { '@level': '1', '@classId': '1.1', '#text': 'Steel' },
              { '@level': '2', '@classId': '1.1.1', '#text': 'Production' },
              { '@level': '3', '@classId': '1.1.1.1', '#text': 'BOF' },
            ],
          },
        },
      },
    },
  },
});

(async () => {
  const suggestResult = await suggestData(processEntity, 'process', {
    outputDiffSummary: true,
    outputDiffHTML: true,
    maxRetries: 1,
    modelConfig: {
      model: process.env.OPENAI_CHAT_MODEL,
      apiKey: process.env.OPENAI_API_KEY,
      baseURL: process.env.OPENAI_BASE_URL,
    },
  });

  const improvedData = suggestResult.data;

  console.log('improvedData:', JSON.stringify(improvedData, null, 2));

  const diffSummary = suggestResult.diffSummary;

  console.log('diffSummary:', diffSummary);

  const diffHTML = suggestResult.diffHTML;

  console.log('diffHTML:', diffHTML);

  // save HTML to file
  const outputPath = path.join(__dirname, 'ai-suggestion.html');
  fs.writeFileSync(outputPath, diffHTML || '', 'utf-8');
  console.log(`HTML diff saved to: ${outputPath}`);
})();
