import { createProcess,createContact } from '../../src/core/factories';

const tidasData = createContact()
console.log(tidasData.contactDataSet)
tidasData.contactDataSet.administrativeInformation.publicationAndOwnership['common:dataSetVersion'] = '1.0.0'
console.log(tidasData.contactDataSet)


const defaultProcess = createProcess();
console.log(JSON.stringify(defaultProcess, null, 2));

const processJson = {
  processDataSet: {
    '@xmlns': 'http://lca.jrc.it/ILCD/Process',
    '@version': '1.1',
    exchanges: {
      exchange: [
        {
          allocations: {
            allocation: {},
          },
          exchangeDirection: 'input',
          '@dataSetInternalID': '0',
          referenceToFlowDataSet: {},
          referencesToDataSource: {
            referenceToDataSource: {},
          },
        },
        {
          allocations: {
            allocation: {},
          },
          exchangeDirection: 'output',
          '@dataSetInternalID': '1',
          referenceToFlowDataSet: {},
          referencesToDataSource: {
            referenceToDataSource: {},
          },
        },
        {
          allocations: {
            allocation: {},
          },
          exchangeDirection: 'output',
          '@dataSetInternalID': '2',
          referenceToFlowDataSet: {
            '@uri': '../flows/ebe375d5-efe7-42bb-bd33-2eccc1d87fce.xml',
            '@type': 'flow data set',
            '@version': '01.01.000',
            '@refObjectId': 'ebe375d5-efe7-42bb-bd33-2eccc1d87fce',
            'common:shortDescription': [
              {
                '#text':
                  'Al coil of 0.05mm cathode etched foil; Processing technology for etching aluminum foil; Production mix, in the factory; 0.05mm',
                '@xml:lang': 'en',
              },
              {
                '#text':
                  '铝箔线圈; 蚀刻铝箔的处理工艺; 生产混合，在工厂; 0.05mm',
                '@xml:lang': 'zh',
              },
            ],
          },
          referencesToDataSource: {
            referenceToDataSource: {},
          },
        },
      ],
    },
    '@locations': '../ILCDLocations.xml',
    '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    '@xmlns:common': 'http://lca.jrc.it/ILCD/Common',
    processInformation: {
      time: {
        'common:referenceYear': '1111',
        'common:dataSetValidUntil': '1111',
        'common:timeRepresentativenessDescription': {
          '#text': '时间代表性',
          '@xml:lang': 'en',
        },
      },
      geography: {
        locationOfOperationSupplyOrProduction: {
          '@location': 'GLO',
          descriptionOfRestrictions: {
            '#text': '地理代表性描述',
            '@xml:lang': 'en',
          },
        },
        subLocationOfOperationSupplyOrProduction: {
          '@subLocation': 'GLO',
          descriptionOfRestrictions: {
            '#text': '地理代表性描述',
            '@xml:lang': 'en',
          },
        },
      },
      technology: {
        technologicalApplicability: {
          '#text': '产品或工艺的技术用途',
          '@xml:lang': 'en',
        },
        referenceToTechnologyPictogramme: {
          '@uri': '../sources/5008494f-cd72-4dee-8d92-1925f83a6dba.xml',
          '@type': 'source data set',
          '@refObjectId': '5008494f-cd72-4dee-8d92-1925f83a6dba',
          'common:shortDescription': [
            {
              '#text': 'Review Report of Transportation of molten aluminum',
              '@xml:lang': 'en',
            },
            {
              '#text': '过程“铝液运输”的审查报告',
              '@xml:lang': 'zh',
            },
          ],
        },
        technologyDescriptionAndIncludedProcesses: {
          '#text': '技术描述及背景系统',
          '@xml:lang': 'en',
        },
        referenceToTechnologyFlowDiagrammOrPicture: {
          '@uri': '../sources/897aee92-f687-4121-a6e2-efa8f24643b9.xml',
          '@type': 'source data set',
          '@refObjectId': '897aee92-f687-4121-a6e2-efa8f24643b9',
          'common:shortDescription': [
            {
              '#text': 'Review Report of Transportation of Alumina',
              '@xml:lang': 'en',
            },
            {
              '#text': '过程“氧化铝运输”的审查报告',
              '@xml:lang': 'zh',
            },
          ],
        },
      },
      dataSetInformation: {
        name: {
          baseName: {
            '#text': 'edit-全部字段',
            '@xml:lang': 'en',
          },
          mixAndLocationTypes: {
            '#text': '混合和位置类型',
            '@xml:lang': 'en',
          },
          treatmentStandardsRoutes: {
            '#text': '处理、标准、路线',
            '@xml:lang': 'en',
          },
          functionalUnitFlowProperties: {
            '#text': '定量产品或过程属性',
            '@xml:lang': 'en',
          },
        },
        'common:UUID': 'ccc669ec-bee6-49b5-be7e-c02004cf3042',
        'common:synonyms': {
          '#text': '同义词',
          '@xml:lang': 'en',
        },
        'common:generalComment': {
          '#text': '数据集一般性说明',
          '@xml:lang': 'en',
        },
        identifierOfSubDataSet: '子数据集标识符',
        classificationInformation: {
          'common:classification': {
            'common:class': [
              {
                '#text': 'Mining and quarrying',
                '@level': '0',
                '@classId': 'B',
              },
              {
                '#text': 'Mining of coal and lignite',
                '@level': '1',
                '@classId': '05',
              },
              {
                '#text': 'Mining of hard coal',
                '@level': '2',
                '@classId': '051',
              },
              {
                '#text': 'Mining of hard coal',
                '@level': '3',
                '@classId': '0510',
              },
            ],
          },
        },
        referenceToExternalDocumentation: {
          '@uri': '../sources/897aee92-f687-4121-a6e2-efa8f24643b9.xml',
          '@type': 'source data set',
          '@version': '01.01.000',
          '@refObjectId': '897aee92-f687-4121-a6e2-efa8f24643b9',
          'common:shortDescription': [
            {
              '#text': 'Review Report of Transportation of Alumina',
              '@xml:lang': 'en',
            },
            {
              '#text': '过程“氧化铝运输”的审查报告',
              '@xml:lang': 'zh',
            },
          ],
        },
      },
      mathematicalRelations: {
        modelDescription: {
          '#text': '模型描述',
          '@xml:lang': 'en',
        },
        variableParameter: {
          '@name': '1',
          comment: [
            {
              '#text': '备注，单位，默认值',
              '@xml:lang': 'en',
            },
          ],
          formula: '2',
          meanValue: '3',
          maximumValue: '5',
          minimumValue: '4',
          uncertaintyDistributionType: 'log-normal',
          relativeStandardDeviation95In: '6',
        },
      },
    },
    '@xsi:schemaLocation':
      'http://lca.jrc.it/ILCD/Process ../../schemas/ILCD_ProcessDataSet.xsd',
    modellingAndValidation: {
      completeness: {
        completenessProductModel: 'Relevant flows missing',
        completenessElementaryFlows: {
          '@type': 'Summer smog',
          '@value': 'Relevant flows missing',
        },
        completenessOtherProblemField: {
          '#text': '8',
          '@xml:lang': 'en',
        },
      },
      LCIMethodAndAllocation: {
        typeOfDataSet: 'Unit process, single operation',
        LCIMethodPrinciple: 'Attributional',
        modellingConstants: {
          '#text': '3',
          '@xml:lang': 'en',
        },
        LCIMethodApproaches: 'Allocation - gross calorific value',
        referenceToLCAMethodDetails: {
          '@uri': '../sources/897aee92-f687-4121-a6e2-efa8f24643b9.xml',
          '@type': 'source data set',
          '@version': '01.01.000',
          '@refObjectId': '897aee92-f687-4121-a6e2-efa8f24643b9',
          'common:shortDescription': [
            {
              '#text': 'Review Report of Transportation of Alumina',
              '@xml:lang': 'en',
            },
            {
              '#text': '过程“氧化铝运输”的审查报告',
              '@xml:lang': 'zh',
            },
          ],
        },
        deviationsFromLCIMethodPrinciple: {
          '#text': '1',
          '@xml:lang': 'en',
        },
        deviationsFromModellingConstants: {
          '#text': '4',
          '@xml:lang': 'en',
        },
        deviationsFromLCIMethodApproaches: {
          '#text': '2',
          '@xml:lang': 'en',
        },
      },
      dataSourcesTreatmentAndRepresentativeness: {
        samplingProcedure: {
          '#text': '4',
          '@xml:lang': 'en',
        },
        dataCollectionPeriod: [
          {
            '#text': '5',
            '@xml:lang': 'en',
          },
        ],
        referenceToDataSource: {
          '@uri': '../sources/897aee92-f687-4121-a6e2-efa8f24643b9.xml',
          '@type': 'source data set',
          '@version': '01.01.000',
          '@refObjectId': '897aee92-f687-4121-a6e2-efa8f24643b9',
          'common:shortDescription': [
            {
              '#text': 'Review Report of Transportation of Alumina',
              '@xml:lang': 'en',
            },
            {
              '#text': '过程“氧化铝运输”的审查报告',
              '@xml:lang': 'zh',
            },
          ],
        },
        uncertaintyAdjustments: {
          '#text': '6',
          '@xml:lang': 'en',
        },
        annualSupplyOrProductionVolume: {
          '#text': '3',
          '@xml:lang': 'en',
        },
        referenceToDataHandlingPrinciples: {
          '@uri': '../sources/897aee92-f687-4121-a6e2-efa8f24643b9.xml',
          '@type': 'source data set',
          '@version': '01.01.000',
          '@refObjectId': '897aee92-f687-4121-a6e2-efa8f24643b9',
          'common:shortDescription': [
            {
              '#text': 'Review Report of Transportation of Alumina',
              '@xml:lang': 'en',
            },
            {
              '#text': '过程“氧化铝运输”的审查报告',
              '@xml:lang': 'zh',
            },
          ],
        },
        dataCutOffAndCompletenessPrinciples: {
          '#text': '5',
          '@xml:lang': 'en',
        },
        percentageSupplyOrProductionCovered: '1',
        dataSelectionAndCombinationPrinciples: {
          '#text': '7',
          '@xml:lang': 'en',
        },
        dataTreatmentAndExtrapolationsPrinciples: {
          '#text': '9',
          '@xml:lang': 'en',
        },
        deviationsFromCutOffAndCompletenessPrinciples: {
          '#text': '6',
          '@xml:lang': 'en',
        },
        deviationsFromSelectionAndCombinationPrinciples: {
          '#text': '8',
          '@xml:lang': 'en',
        },
        deviationsFromTreatmentAndExtrapolationPrinciples: {
          '#text': '10',
          '@xml:lang': 'en',
        },
      },
    },
    administrativeInformation: {
      dataEntryBy: {
        'common:timeStamp': '2025-09-09T17:45:30+08:00',
        'common:referenceToDataSetFormat': {},
        'common:referenceToDataSetUseApproval': {},
        'common:referenceToConvertedOriginalDataSetFrom': {},
        'common:referenceToPersonOrEntityEnteringTheData': {},
      },
      publicationAndOwnership: {
        'common:dataSetVersion': '01.01.000',
        'common:permanentDataSetURI':
          'https://lcdn.tiangong.earth/datasetdetail/process.xhtml?uuid=ccc669ec-bee6-49b5-be7e-c02004cf3042&version=01.01.000',
      },
    },
  },
};

defaultProcess.processDataSet.processInformation.dataSetInformation.classificationInformation =
  {
    'common:classification': {
      'common:class': [],
    },
  };
console.log(JSON.stringify(defaultProcess, null, 2));

// const process = createProcess(processJson);
// console.log(JSON.stringify(process, null, 2));

// const validation = process.validate();
// console.log(validation);

// const enhancedValidation = process.validateEnhanced();
// console.log(enhancedValidation);
