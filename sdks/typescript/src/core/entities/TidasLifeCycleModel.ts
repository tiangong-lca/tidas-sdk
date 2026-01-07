import { TidasEntity } from '../base/TidasEntity';
import { LifeCycleModelSchema } from '../../schemas';
import { LifeCycleModel } from '../../types';
import { ValidationConfig } from '../config/ValidationConfig';
import { MultiLangArray } from '../../types/multi-lang-types';

/**
 * TIDAS LifeCycleModel entity - pure data container
 * Represents system models in LCA with schema validation
 */
export class TidasLifeCycleModel extends TidasEntity<LifeCycleModel> {
  constructor(
    initialData?: Partial<LifeCycleModel>,
    validationConfig?: Partial<ValidationConfig>
  ) {
    super(LifeCycleModelSchema as any, initialData, validationConfig);
  }

  // TypeScript accessor for lifeCycleModelDataSet - enables intellisense and type checking
  get lifeCycleModelDataSet(): LifeCycleModel['lifeCycleModelDataSet'] {
    return (this._data as LifeCycleModel).lifeCycleModelDataSet;
  }

  set lifeCycleModelDataSet(value: LifeCycleModel['lifeCycleModelDataSet']) {
    (this._data as LifeCycleModel).lifeCycleModelDataSet = value;
  }

  protected initializeDefaults(): void {
    // Set required namespace attributes for TIDAS schema compliance
    this.setNestedValue(
      'lifeCycleModelDataSet.@xmlns',
      'http://eplca.jrc.ec.europa.eu/ILCD/LifeCycleModel/2017'
    );
    this.setNestedValue(
      'lifeCycleModelDataSet.@xmlns:common',
      'http://lca.jrc.it/ILCD/Common'
    );
    this.setNestedValue(
      'lifeCycleModelDataSet.@xmlns:xsi',
      'http://www.w3.org/2001/XMLSchema-instance'
    );
    this.setNestedValue('lifeCycleModelDataSet.@version', '1.1');
    this.setNestedValue(
      'lifeCycleModelDataSet.@xsi:schemaLocation',
      'http://eplca.jrc.ec.europa.eu/ILCD/LifeCycleModel/2017 ../../schemas/ILCD_LifeCycleModelDataSet.xsd'
    );

    // Ensure required nested structure exists
    this.ensureNestedStructure([
      'lifeCycleModelDataSet',
      'lifeCycleModelDataSet.lifeCycleModelInformation',
      'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation',
      'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.classificationInformation',
      'lifeCycleModelDataSet.lifeCycleModelInformation.quantitativeReference',
      'lifeCycleModelDataSet.modellingAndValidation',
      'lifeCycleModelDataSet.modellingAndValidation.complianceDeclarations',
      'lifeCycleModelDataSet.administrativeInformation',
      'lifeCycleModelDataSet.administrativeInformation.dataEntryBy',
      'lifeCycleModelDataSet.administrativeInformation.publicationAndOwnership',
      'lifeCycleModelDataSet.technology',
    ]);

    // Set required fields with default values if they don't exist
    if (
      !this.getNestedValue(
        'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.common:UUID'
      )
    ) {
      this.setNestedValue(
        'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.common:UUID',
        crypto.randomUUID()
      );
    }

    if (
      !this.getNestedValue(
        'lifeCycleModelDataSet.administrativeInformation.dataEntryBy.common:timeStamp'
      )
    ) {
      this.setNestedValue(
        'lifeCycleModelDataSet.administrativeInformation.dataEntryBy.common:timeStamp',
        new Date().toISOString()
      );
    }

    // if (
    //   !this.getNestedValue(
    //     'lifeCycleModelDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'lifeCycleModelDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion',
    //     '1.0.0'
    //   );
    // }

    // Set required reference fields with default values
    // if (
    //   !this.getNestedValue(
    //     'lifeCycleModelDataSet.administrativeInformation.dataEntryBy.common:referenceToDataSetFormat'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'lifeCycleModelDataSet.administrativeInformation.dataEntryBy.common:referenceToDataSetFormat',
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
    //     'lifeCycleModelDataSet.administrativeInformation.publicationAndOwnership.common:referenceToOwnershipOfDataSet'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'lifeCycleModelDataSet.administrativeInformation.publicationAndOwnership.common:referenceToOwnershipOfDataSet',
    //     {
    //       '@type': 'contact data set',
    //       '@refObjectId': this.getNestedValue(
    //         'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.common:UUID'
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
        'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.common:name'
      )
    ) {
      this.setNestedValue(
        'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.common:name',
        new MultiLangArray()
      );
    }

    if (
      !this.getNestedValue(
        'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.common:shortName'
      )
    ) {
      this.setNestedValue(
        'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.common:shortName',
        new MultiLangArray()
      );
    }

    if (
      !this.getNestedValue(
        'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.common:synonyms'
      )
    ) {
      this.setNestedValue(
        'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.common:synonyms',
        new MultiLangArray()
      );
    }

    if (
      !this.getNestedValue(
        'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.common:generalComment'
      )
    ) {
      this.setNestedValue(
        'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.common:generalComment',
        new MultiLangArray()
      );
    }

    // Initialize required classification structure
    // if (
    //   !this.getNestedValue(
    //     'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.classificationInformation.common:classification'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.classificationInformation.common:classification',
    //     {
    //       'common:class': {
    //         '@level': '0',
    //         '@classId': '00000000-0000-0000-0000-000000000000',
    //         '#text': 'General life cycle model',
    //       },
    //     }
    //   );
    // }

    // Initialize technology array
    if (!this.getNestedValue('lifeCycleModelDataSet.technology')) {
      this.setNestedValue('lifeCycleModelDataSet.technology', []);
    }

    // Set default model type
    // if (
    //   !this.getNestedValue(
    //     'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.typeOfModel'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.typeOfModel',
    //     'Product system model'
    //   );
    // }

    // Set default functional unit or other reference
    if (
      !this.getNestedValue(
        'lifeCycleModelDataSet.lifeCycleModelInformation.quantitativeReference.functionalUnitOrOther'
      )
    ) {
      this.setNestedValue(
        'lifeCycleModelDataSet.lifeCycleModelInformation.quantitativeReference.functionalUnitOrOther',
        new MultiLangArray()
      );
    }

    // Set default copyright protection
    // if (
    //   !this.getNestedValue(
    //     'lifeCycleModelDataSet.administrativeInformation.publicationAndOwnership.common:copyright'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'lifeCycleModelDataSet.administrativeInformation.publicationAndOwnership.common:copyright',
    //     false
    //   );
    // }

    // Set default access restrictions
    // if (
    //   !this.getNestedValue(
    //     'lifeCycleModelDataSet.administrativeInformation.publicationAndOwnership.common:accessRestrictions'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'lifeCycleModelDataSet.administrativeInformation.publicationAndOwnership.common:accessRestrictions',
    //     []
    //   );
    // }
  }
}
