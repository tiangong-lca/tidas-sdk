import { CHINESE_CHARACTER_RE } from './constants';
import type { ValidationIssue } from './report';

interface ClassificationValidationResult {
  valid: boolean;
  errors?: string[];
}

function makeIssue(
  category: string,
  filePath: string,
  location: string,
  message: string,
  issueCode = 'schema_error'
): ValidationIssue {
  return {
    issue_code: issueCode,
    severity: 'error',
    category,
    file_path: filePath,
    location,
    message,
    context: {},
  };
}

function asRecord(value: unknown) {
  return value && typeof value === 'object' && !Array.isArray(value)
    ? (value as Record<string, unknown>)
    : null;
}

function ensureArray<T>(value: T | T[] | undefined | null) {
  if (Array.isArray(value)) {
    return value;
  }
  if (value === undefined || value === null) {
    return [];
  }
  return [value];
}

export function validateElementaryFlowsClassificationHierarchy(
  classItems: Array<Record<string, unknown>>
): ClassificationValidationResult {
  const errors: string[] = [];

  classItems.forEach((item, index) => {
    const level = Number(item['@level']);
    if (level !== index) {
      errors.push(
        `Elementary flow classification level sorting error: at index ${index}, expected level ${index}, got ${level}`
      );
    }
  });

  for (let index = 1; index < classItems.length; index += 1) {
    const parentId = String(classItems[index - 1]?.['@catId'] ?? '');
    const childId = String(classItems[index]?.['@catId'] ?? '');
    if (!childId.startsWith(parentId)) {
      errors.push(
        `Elementary flow classification code error: child code '${childId}' does not start with parent code '${parentId}'`
      );
    }
  }

  return errors.length > 0 ? { valid: false, errors } : { valid: true };
}

export function validateProductFlowsClassificationHierarchy(
  classItems: Array<Record<string, unknown>>
): ClassificationValidationResult {
  const errors: string[] = [];

  classItems.forEach((item, index) => {
    const level = Number(item['@level']);
    if (level !== index) {
      errors.push(
        `Product flow classification level sorting error: at index ${index}, expected level ${index}, got ${level}`
      );
    }
  });

  for (let index = 1; index < classItems.length; index += 1) {
    const parentId = String(classItems[index - 1]?.['@classId'] ?? '');
    const childId = String(classItems[index]?.['@classId'] ?? '');
    if (!childId.startsWith(parentId)) {
      errors.push(
        `Product flow classification code error: child code '${childId}' does not start with parent code '${parentId}'`
      );
    }
  }

  return errors.length > 0 ? { valid: false, errors } : { valid: true };
}

export function validateProcessesClassificationHierarchy(
  classItems: Array<Record<string, unknown>>
): ClassificationValidationResult {
  const errors: string[] = [];
  const level0ToLevel1Mapping: Record<string, string[]> = {
    A: ['01', '02', '03'],
    B: ['05', '06', '07', '08', '09'],
    C: Array.from({ length: 24 }, (_, index) =>
      String(index + 10).padStart(2, '0')
    ),
    D: ['35'],
    E: ['36', '37', '38', '39'],
    F: ['41', '42', '43'],
    G: ['46', '47'],
    H: ['49', '50', '51', '52', '53'],
    I: ['55', '56'],
    J: ['58', '59', '60'],
    K: ['61', '62', '63'],
    L: ['64', '65', '66'],
    M: ['68'],
    N: ['69', '70', '71', '72', '73', '74', '75'],
    O: ['77', '78', '79', '80', '81', '82'],
    P: ['84'],
    Q: ['85'],
    R: ['86', '87', '88'],
    S: ['90', '91', '92', '93'],
    T: ['94', '95', '96'],
    U: ['97', '98'],
    V: ['99'],
  };

  classItems.forEach((item, index) => {
    const level = Number(item['@level']);
    if (level !== index) {
      errors.push(
        `Processes classification level sorting error: at index ${index}, expected level ${index}, got ${level}`
      );
    }
  });

  for (let index = 1; index < classItems.length; index += 1) {
    const parent = classItems[index - 1] ?? {};
    const child = classItems[index] ?? {};
    const parentLevel = Number(parent['@level']);
    const childLevel = Number(child['@level']);
    const parentId = String(parent['@classId'] ?? '');
    const childId = String(child['@classId'] ?? '');

    if (parentLevel === 0 && childLevel === 1) {
      const validCodes = level0ToLevel1Mapping[parentId] ?? [];
      if (!validCodes.includes(childId)) {
        errors.push(
          `Processes classification code error: level 1 code '${childId}' does not correspond to level 0 code '${parentId}'`
        );
      }
      continue;
    }

    if (!childId.startsWith(parentId)) {
      errors.push(
        `Processes classification code error: child code '${childId}' does not start with parent code '${parentId}'`
      );
    }
  }

  return errors.length > 0 ? { valid: false, errors } : { valid: true };
}

export function validateSourcesClassificationHierarchy(
  classItems:
    | Array<Record<string, unknown>>
    | Record<string, unknown>
    | undefined
): ClassificationValidationResult {
  const normalizedItems = ensureArray(classItems);
  const errors: string[] = [];

  normalizedItems.forEach((item, index) => {
    const level = Number(item['@level']);
    if (!Number.isFinite(level)) {
      errors.push(
        `Sources classification level parsing error: missing or invalid '@level' at index ${index}`
      );
      return;
    }
    if (level !== index) {
      errors.push(
        `Sources classification level sorting error: at index ${index}, expected level ${index}, got ${level}`
      );
    }
  });

  for (let index = 1; index < normalizedItems.length; index += 1) {
    const parentId = normalizedItems[index - 1]?.['@classId'];
    const childId = normalizedItems[index]?.['@classId'];
    if (typeof parentId !== 'string' || typeof childId !== 'string') {
      errors.push(
        `Sources classification code error: missing '@classId' for parent index ${index - 1} or child index ${index}`
      );
      continue;
    }
    if (!childId.startsWith(parentId)) {
      errors.push(
        `Sources classification code error: child code '${childId}' does not start with parent code '${parentId}'`
      );
    }
  }

  return errors.length > 0 ? { valid: false, errors } : { valid: true };
}

export function validateLocalizedTextLanguageConstraints(
  node: unknown,
  currentPath = ''
): string[] {
  const errors: string[] = [];
  const currentNode = asRecord(node);

  if (currentNode) {
    const language = currentNode['@xml:lang'];
    const text = currentNode['#text'];
    const location = currentPath || '<root>';

    if (typeof language === 'string' && typeof text === 'string') {
      const normalizedLanguage = language.toLowerCase();
      const hasChinese = CHINESE_CHARACTER_RE.test(text);

      if (
        (normalizedLanguage === 'zh' || normalizedLanguage.startsWith('zh-')) &&
        !hasChinese
      ) {
        errors.push(
          `Localized text error at ${location}: @xml:lang '${language}' must include at least one Chinese character`
        );
      }

      if (
        (normalizedLanguage === 'en' || normalizedLanguage.startsWith('en-')) &&
        hasChinese
      ) {
        errors.push(
          `Localized text error at ${location}: @xml:lang '${language}' must not contain Chinese characters`
        );
      }
    }

    for (const [key, value] of Object.entries(currentNode)) {
      const childPath = currentPath ? `${currentPath}/${key}` : key;
      errors.push(
        ...validateLocalizedTextLanguageConstraints(value, childPath)
      );
    }
    return errors;
  }

  if (Array.isArray(node)) {
    node.forEach((value, index) => {
      const childPath = currentPath ? `${currentPath}/${index}` : String(index);
      errors.push(
        ...validateLocalizedTextLanguageConstraints(value, childPath)
      );
    });
  }

  return errors;
}

function collectFlowClassificationStructureIssues(
  items: unknown,
  category: string,
  filePath: string,
  locationBase: string,
  requiredIdKey: '@classId' | '@catId'
) {
  if (!Array.isArray(items)) {
    return [];
  }

  const issues: ValidationIssue[] = [];

  items.forEach((item, index) => {
    const record = asRecord(item);
    if (!record) {
      return;
    }

    for (const fieldName of ['@level', requiredIdKey, '#text'] as const) {
      if (record[fieldName] !== undefined) {
        continue;
      }

      issues.push(
        makeIssue(
          category,
          filePath,
          `${locationBase}/${index}`,
          `Schema Error at ${locationBase}/${index}: '${fieldName}' is a required property`
        )
      );
    }
  });

  return issues;
}

export function collectLocalizedTextIssues(
  jsonItem: unknown,
  category: string,
  filePath: string
) {
  return validateLocalizedTextLanguageConstraints(jsonItem).map((message) => {
    const location =
      message.startsWith('Localized text error at ') && message.includes(':')
        ? message.split('Localized text error at ', 2)[1]!.split(':', 1)[0]!
        : '<root>';

    return makeIssue(
      category,
      filePath,
      location,
      message,
      'localized_text_language_error'
    );
  });
}

export function collectFlowSchemaGapIssues(
  jsonItem: unknown,
  category: string,
  filePath: string
) {
  if (category !== 'flows') {
    return [];
  }

  const flowDataSet = asRecord(asRecord(jsonItem)?.flowDataSet);
  const modellingAndValidation = asRecord(flowDataSet?.modellingAndValidation);
  const lciMethod = asRecord(modellingAndValidation?.LCIMethod);
  const dataSetType = lciMethod?.typeOfDataSet;
  const dataSetInformation = asRecord(
    asRecord(flowDataSet?.flowInformation)?.dataSetInformation
  );
  const classificationInformation = asRecord(
    dataSetInformation?.classificationInformation
  );

  if (dataSetType === 'Product flow') {
    const classes = asRecord(
      classificationInformation?.['common:classification']
    )?.['common:class'];
    return collectFlowClassificationStructureIssues(
      classes,
      category,
      filePath,
      'flowDataSet/flowInformation/dataSetInformation/classificationInformation/common:classification/common:class',
      '@classId'
    );
  }

  if (dataSetType === 'Elementary flow') {
    const categories = asRecord(
      classificationInformation?.['common:elementaryFlowCategorization']
    )?.['common:category'];

    return collectFlowClassificationStructureIssues(
      categories,
      category,
      filePath,
      'flowDataSet/flowInformation/dataSetInformation/classificationInformation/common:elementaryFlowCategorization/common:category',
      '@catId'
    );
  }

  return [];
}

export function collectClassificationIssues(
  jsonItem: unknown,
  category: string,
  filePath: string
) {
  const issues: ValidationIssue[] = [];
  const root = asRecord(jsonItem);

  try {
    if (category === 'flows') {
      const flowDataSet = asRecord(asRecord(root?.flowDataSet));
      const dataSetType = asRecord(flowDataSet?.modellingAndValidation)
        ?.LCIMethod
        ? asRecord(asRecord(flowDataSet?.modellingAndValidation)?.LCIMethod)?.[
            'typeOfDataSet'
          ]
        : undefined;

      if (dataSetType === 'Product flow') {
        const items = asRecord(
          asRecord(
            asRecord(asRecord(flowDataSet?.flowInformation)?.dataSetInformation)
              ?.classificationInformation
          )?.['common:classification']
        )?.['common:class'];

        if (Array.isArray(items)) {
          const result = validateProductFlowsClassificationHierarchy(
            items.filter((item): item is Record<string, unknown> =>
              Boolean(asRecord(item))
            )
          );
          if (!result.valid) {
            issues.push(
              ...(result.errors ?? []).map((message) =>
                makeIssue(
                  category,
                  filePath,
                  '<root>',
                  message,
                  'classification_hierarchy_error'
                )
              )
            );
          }
        }
      } else if (dataSetType === 'Elementary flow') {
        const items = asRecord(
          asRecord(
            asRecord(asRecord(flowDataSet?.flowInformation)?.dataSetInformation)
              ?.classificationInformation
          )?.['common:elementaryFlowCategorization']
        )?.['common:category'];

        if (Array.isArray(items)) {
          const result = validateElementaryFlowsClassificationHierarchy(
            items.filter((item): item is Record<string, unknown> =>
              Boolean(asRecord(item))
            )
          );
          if (!result.valid) {
            issues.push(
              ...(result.errors ?? []).map((message) =>
                makeIssue(
                  category,
                  filePath,
                  '<root>',
                  message,
                  'classification_hierarchy_error'
                )
              )
            );
          }
        }
      }
    } else if (category === 'processes') {
      const items = asRecord(
        asRecord(
          asRecord(asRecord(root?.processDataSet)?.processInformation)
            ?.dataSetInformation
        )?.classificationInformation
      )?.['common:classification'];

      const classes = asRecord(items)?.['common:class'];
      if (Array.isArray(classes)) {
        const result = validateProcessesClassificationHierarchy(
          classes.filter((item): item is Record<string, unknown> =>
            Boolean(asRecord(item))
          )
        );
        if (!result.valid) {
          issues.push(
            ...(result.errors ?? []).map((message) =>
              makeIssue(
                category,
                filePath,
                '<root>',
                message,
                'classification_hierarchy_error'
              )
            )
          );
        }
      }
    } else if (category === 'lifecyclemodels') {
      const items = asRecord(
        asRecord(
          asRecord(root?.lifecycleModelDataSet)?.lifecycleModelInformation
        )?.dataSetInformation
      )?.classificationInformation;

      const classes = asRecord(asRecord(items)?.['common:classification'])?.[
        'common:class'
      ];
      if (Array.isArray(classes)) {
        const result = validateProcessesClassificationHierarchy(
          classes.filter((item): item is Record<string, unknown> =>
            Boolean(asRecord(item))
          )
        );
        if (!result.valid) {
          issues.push(
            ...(result.errors ?? []).map((message) =>
              makeIssue(
                category,
                filePath,
                '<root>',
                message,
                'classification_hierarchy_error'
              )
            )
          );
        }
      }
    } else if (category === 'sources') {
      const classes = asRecord(
        asRecord(
          asRecord(asRecord(root?.sourceDataSet)?.sourceInformation)
            ?.dataSetInformation
        )?.classificationInformation
      );
      const result = validateSourcesClassificationHierarchy(
        asRecord(asRecord(classes)?.['common:classification'])?.[
          'common:class'
        ] as
          | Array<Record<string, unknown>>
          | Record<string, unknown>
          | undefined
      );
      if (!result.valid) {
        issues.push(
          ...(result.errors ?? []).map((message) =>
            makeIssue(
              category,
              filePath,
              '<root>',
              message,
              'classification_hierarchy_error'
            )
          )
        );
      }
    }
  } catch {
    return issues;
  }

  return issues;
}
