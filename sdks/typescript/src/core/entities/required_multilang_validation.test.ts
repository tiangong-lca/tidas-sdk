import {
  createContact,
  createFlowProperty,
  createSource,
} from '../factories';

const ml = { '@xml:lang': 'en', '#text': 'x' };

const ref = (type: string, id: string, version = '1.0.0') => ({
  '@type': type,
  '@refObjectId': id,
  '@version': version,
  '@uri': '',
  'common:shortDescription': ml,
});

const clone = <T>(value: T): any => JSON.parse(JSON.stringify(value));

const contactBase = {
  contactDataSet: {
    '@xmlns': 'http://lca.jrc.it/ILCD/Contact',
    '@xmlns:common': 'http://lca.jrc.it/ILCD/Common',
    '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    '@version': '1.1',
    '@xsi:schemaLocation':
      'http://lca.jrc.it/ILCD/Contact ../../schemas/ILCD_ContactDataSet.xsd',
    contactInformation: {
      dataSetInformation: {
        'common:UUID': '11111111-1111-4111-8111-111111111111',
        'common:shortName': ml,
        'common:name': ml,
        classificationInformation: {
          'common:classification': {
            'common:class': {
              '@level': '0',
              '@classId': 'cls',
              '#text': 'Class',
            },
          },
        },
      },
    },
    administrativeInformation: {
      dataEntryBy: {
        'common:timeStamp': '2026-04-07T00:00:00.000Z',
        'common:referenceToDataSetFormat': ref(
          'source data set',
          '22222222-2222-4222-8222-222222222222'
        ),
      },
      publicationAndOwnership: {
        'common:dataSetVersion': '1.0.0',
        'common:referenceToOwnershipOfDataSet': ref(
          'contact data set',
          '11111111-1111-4111-8111-111111111111'
        ),
      },
    },
  },
};

const sourceBase = {
  sourceDataSet: {
    '@xmlns:common': 'http://lca.jrc.it/ILCD/Common',
    '@xmlns': 'http://lca.jrc.it/ILCD/Source',
    '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    '@version': '1.1',
    '@xsi:schemaLocation':
      'http://lca.jrc.it/ILCD/Source ../../schemas/ILCD_SourceDataSet.xsd',
    sourceInformation: {
      dataSetInformation: {
        'common:UUID': '33333333-3333-4333-8333-333333333333',
        'common:shortName': ml,
        classificationInformation: {
          'common:classification': {
            'common:class': {
              '@level': '0',
              '@classId': 'cls',
              '#text': 'Class',
            },
          },
        },
      },
    },
    administrativeInformation: {
      dataEntryBy: {
        'common:timeStamp': '2026-04-07T00:00:00.000Z',
        'common:referenceToDataSetFormat': ref(
          'source data set',
          '22222222-2222-4222-8222-222222222222'
        ),
      },
      publicationAndOwnership: {
        'common:dataSetVersion': '1.0.0',
        'common:referenceToOwnershipOfDataSet': ref(
          'contact data set',
          '44444444-4444-4444-8444-444444444444'
        ),
      },
    },
  },
};

const flowPropertyBase = {
  flowPropertyDataSet: {
    '@xmlns': 'http://lca.jrc.it/ILCD/FlowProperty',
    '@xmlns:common': 'http://lca.jrc.it/ILCD/Common',
    '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    '@version': '1.1',
    '@xsi:schemaLocation':
      'http://lca.jrc.it/ILCD/FlowProperty ../../schemas/ILCD_FlowPropertyDataSet.xsd',
    flowPropertiesInformation: {
      dataSetInformation: {
        'common:UUID': '55555555-5555-4555-8555-555555555555',
        'common:name': ml,
        classificationInformation: {
          'common:classification': {
            'common:class': {
              '@level': '0',
              '@classId': 'cls',
              '#text': 'Class',
            },
          },
        },
      },
      quantitativeReference: {
        referenceToReferenceUnitGroup: ref(
          'unit group data set',
          '66666666-6666-4666-8666-666666666666'
        ),
      },
    },
    modellingAndValidation: {
      complianceDeclarations: {
        compliance: {
          'common:referenceToComplianceSystem': ref(
            'source data set',
            '77777777-7777-4777-8777-777777777777'
          ),
          'common:approvalOfOverallCompliance': 'Fully compliant',
        },
      },
    },
    administrativeInformation: {
      dataEntryBy: {
        'common:timeStamp': '2026-04-07T00:00:00.000Z',
        'common:referenceToDataSetFormat': ref(
          'source data set',
          '22222222-2222-4222-8222-222222222222'
        ),
      },
      publicationAndOwnership: {
        'common:dataSetVersion': '1.0.0',
        'common:referenceToOwnershipOfDataSet': ref(
          'contact data set',
          '44444444-4444-4444-8444-444444444444'
        ),
      },
    },
  },
};

describe('required multi-language field validation', () => {
  it('still accepts optional localized fields initialized as empty arrays', () => {
    expect(createContact(clone(contactBase)).validateEnhanced().success).toBe(
      true
    );
    expect(createSource(clone(sourceBase)).validateEnhanced().success).toBe(
      true
    );
    expect(
      createFlowProperty(clone(flowPropertyBase)).validateEnhanced().success
    ).toBe(true);
  });

  it.each([
    [
      'contact short name',
      () => {
        const data = clone(contactBase);
        delete data.contactDataSet.contactInformation.dataSetInformation[
          'common:shortName'
        ];
        return createContact(data);
      },
      'contactDataSet.contactInformation.dataSetInformation.common:shortName',
    ],
    [
      'contact name',
      () => {
        const data = clone(contactBase);
        delete data.contactDataSet.contactInformation.dataSetInformation[
          'common:name'
        ];
        return createContact(data);
      },
      'contactDataSet.contactInformation.dataSetInformation.common:name',
    ],
    [
      'source short name',
      () => {
        const data = clone(sourceBase);
        delete data.sourceDataSet.sourceInformation.dataSetInformation[
          'common:shortName'
        ];
        return createSource(data);
      },
      'sourceDataSet.sourceInformation.dataSetInformation.common:shortName',
    ],
    [
      'flow property name',
      () => {
        const data = clone(flowPropertyBase);
        delete data.flowPropertyDataSet.flowPropertiesInformation
          .dataSetInformation['common:name'];
        return createFlowProperty(data);
      },
      'flowPropertyDataSet.flowPropertiesInformation.dataSetInformation.common:name',
    ],
  ])('fails validateEnhanced() when %s is missing', (_, buildEntity, path) => {
    const entity = buildEntity();
    const result = entity.validateEnhanced();

    expect(result.success).toBe(false);
    if (result.success) return;

    expect(
      result.error.issues.some((issue) => issue.path.join('.') === path)
    ).toBe(true);
  });

  it('treats normalized empty required localized fields as critical in weak mode', () => {
    const data = clone(contactBase);
    delete data.contactDataSet.contactInformation.dataSetInformation[
      'common:name'
    ];

    const result = createContact(data, { mode: 'weak' }).validateEnhanced();

    expect(result.success).toBe(false);
  });
});
