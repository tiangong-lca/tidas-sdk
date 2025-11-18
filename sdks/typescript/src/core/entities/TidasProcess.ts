import { TidasEntity } from '../base/TidasEntity';
import { ProcessSchema } from '../../schemas';
import { Process } from '../../types';
import { ValidationConfig } from '../config/ValidationConfig';
import { MultiLangArray } from '../../types/multi-lang-types';

/**
 * TIDAS Process entity - pure data container
 * Represents unit processes/activities in LCA with schema validation
 */
export class TidasProcess extends TidasEntity<Process> {
  constructor(
    initialData?: Partial<Process>,
    validationConfig?: Partial<ValidationConfig>
  ) {
    super(ProcessSchema as any, initialData, validationConfig);
  }

  // TypeScript accessor for processDataSet - enables intellisense and type checking
  get processDataSet(): Process['processDataSet'] {
    return (this._data as Process).processDataSet;
  }

  set processDataSet(value: Process['processDataSet']) {
    (this._data as Process).processDataSet = value;
  }

  protected initializeDefaults(): void {
    // Set required namespace attributes for TIDAS schema compliance
    this.setNestedValue(
      'processDataSet.@xmlns',
      'http://lca.jrc.it/ILCD/Process'
    );
    this.setNestedValue(
      'processDataSet.@xmlns:common',
      'http://lca.jrc.it/ILCD/Common'
    );
    this.setNestedValue(
      'processDataSet.@xmlns:xsi',
      'http://www.w3.org/2001/XMLSchema-instance'
    );
    this.setNestedValue('processDataSet.@version', '1.1');
    this.setNestedValue(
      'processDataSet.@xsi:schemaLocation',
      'http://lca.jrc.it/ILCD/Process ../../schemas/ILCD_ProcessDataSet.xsd'
    );

    // Ensure required nested structure exists
    this.ensureNestedStructure([
      'processDataSet',
      'processDataSet.processInformation',
      'processDataSet.processInformation.dataSetInformation',
      'processDataSet.processInformation.dataSetInformation.classificationInformation',
      'processDataSet.processInformation.quantitativeReference',
      'processDataSet.processInformation.time',
      'processDataSet.processInformation.geography',
      'processDataSet.processInformation.technology',
      'processDataSet.modellingAndValidation',
      'processDataSet.modellingAndValidation.LCIMethodAndAllocation',
      'processDataSet.modellingAndValidation.dataSourcesTreatmentAndRepresentativeness',
      'processDataSet.modellingAndValidation.validation',
      'processDataSet.modellingAndValidation.complianceDeclarations',
      'processDataSet.administrativeInformation',
      'processDataSet.administrativeInformation.dataEntryBy',
      'processDataSet.administrativeInformation.publicationAndOwnership',
      'processDataSet.exchanges',
    ]);

    // Set required fields with default values if they don't exist
    if (
      !this.getNestedValue(
        'processDataSet.processInformation.dataSetInformation.common:UUID'
      )
    ) {
      this.setNestedValue(
        'processDataSet.processInformation.dataSetInformation.common:UUID',
        crypto.randomUUID()
      );
    }

    if (
      !this.getNestedValue(
        'processDataSet.administrativeInformation.dataEntryBy.common:timeStamp'
      )
    ) {
      this.setNestedValue(
        'processDataSet.administrativeInformation.dataEntryBy.common:timeStamp',
        new Date().toISOString()
      );
    }

    // if (
    //   !this.getNestedValue(
    //     'processDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'processDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion',
    //     '1.0.0'
    //   );
    // }

    // Set required reference fields with default values
    // if (
    //   !this.getNestedValue(
    //     'processDataSet.administrativeInformation.dataEntryBy.common:referenceToDataSetFormat'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'processDataSet.administrativeInformation.dataEntryBy.common:referenceToDataSetFormat',
    //     {
    //       '@type': 'source data set',
    //       '@refObjectId': '00000000-0000-0000-0000-000000000000',
    //       '@version': '00.00.000',
    //       '@uri': '',
    //       'common:shortDescription': new MultiLangArray(),
    //     }
    //   );
    // }

    // if (
    //   !this.getNestedValue(
    //     'processDataSet.administrativeInformation.publicationAndOwnership.common:referenceToOwnershipOfDataSet'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'processDataSet.administrativeInformation.publicationAndOwnership.common:referenceToOwnershipOfDataSet',
    //     {
    //       '@type': 'contact data set',
    //       '@refObjectId': this.getNestedValue(
    //         'processDataSet.processInformation.dataSetInformation.common:UUID'
    //       ),
    //       '@version': '00.00.000',
    //       '@uri': '',
    //       'common:shortDescription': new MultiLangArray(),
    //     }
    //   );
    // }

    // Initialize empty arrays for multi-language text fields
    if (
      !this.getNestedValue(
        'processDataSet.processInformation.dataSetInformation.common:name'
      )
    ) {
      this.setNestedValue(
        'processDataSet.processInformation.dataSetInformation.common:name',
        new MultiLangArray()
      );
    }

    if (
      !this.getNestedValue(
        'processDataSet.processInformation.dataSetInformation.common:shortName'
      )
    ) {
      this.setNestedValue(
        'processDataSet.processInformation.dataSetInformation.common:shortName',
        new MultiLangArray()
      );
    }

    if (
      !this.getNestedValue(
        'processDataSet.processInformation.dataSetInformation.common:synonyms'
      )
    ) {
      this.setNestedValue(
        'processDataSet.processInformation.dataSetInformation.common:synonyms',
        new MultiLangArray()
      );
    }

    if (
      !this.getNestedValue(
        'processDataSet.processInformation.dataSetInformation.common:generalComment'
      )
    ) {
      this.setNestedValue(
        'processDataSet.processInformation.dataSetInformation.common:generalComment',
        new MultiLangArray()
      );
    }

    // Initialize required classification structure
    // if (
    //   !this.getNestedValue(
    //     'processDataSet.processInformation.dataSetInformation.classificationInformation.common:classification'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'processDataSet.processInformation.dataSetInformation.classificationInformation.common:classification',
    //     {
    //       'common:class': {
    //         '@level': '0',
    //         '@classId': '00000000-0000-0000-0000-000000000000',
    //         '#text': 'General process',
    //       },
    //     }
    //   );
    // }

    // Initialize exchanges array
    if (!this.getNestedValue('processDataSet.exchanges')) {
      this.setNestedValue('processDataSet.exchanges', []);
    }

    // Set default process type
    // if (
    //   !this.getNestedValue(
    //     'processDataSet.modellingAndValidation.LCIMethodAndAllocation.typeOfDataSet'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'processDataSet.modellingAndValidation.LCIMethodAndAllocation.typeOfDataSet',
    //     'Unit process, single operation'
    //   );
    // }

    // Set default LCI method type
    // if (
    //   !this.getNestedValue(
    //     'processDataSet.modellingAndValidation.LCIMethodAndAllocation.LCIMethodPrinciple'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'processDataSet.modellingAndValidation.LCIMethodAndAllocation.LCIMethodPrinciple',
    //     'Attributional'
    //   );
    // }

    // Initialize time period
    // if (
    //   !this.getNestedValue(
    //     'processDataSet.processInformation.time.common:referenceYear'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'processDataSet.processInformation.time.common:referenceYear',
    //     new Date().getFullYear()
    //   );
    // }

    // Initialize geography - ensure required location is set
    // this.setNestedValue(
    //   'processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction.@location',
    //   'GLO'
    // );

    // Initialize technology
    if (
      !this.getNestedValue(
        'processDataSet.processInformation.technology.technologyDescriptionAndIncludedProcesses'
      )
    ) {
      this.setNestedValue(
        'processDataSet.processInformation.technology.technologyDescriptionAndIncludedProcesses',
        []
      );
    }

    // Set default quantitative reference type
    // if (
    //   !this.getNestedValue(
    //     'processDataSet.processInformation.quantitativeReference.@type'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'processDataSet.processInformation.quantitativeReference.@type',
    //     'Reference flow(s)'
    //   );
    // }
  }
}
