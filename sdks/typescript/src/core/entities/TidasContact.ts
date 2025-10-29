import { TidasEntity } from '../base/TidasEntity';
import { ContactSchema } from '../../schemas';
import { Contact } from '../../types';
import { ValidationConfig } from '../config/ValidationConfig';
import { MultiLangArray } from '../../types/multi-lang-types';

/**
 * TIDAS Contact entity - simplified pure data container
 * Provides direct access to TIDAS Contact structure with schema validation
 */
export class TidasContact extends TidasEntity<Contact> {
  constructor(
    initialData?: Partial<Contact>,
    validationConfig?: Partial<ValidationConfig>
  ) {
    super(ContactSchema as any, initialData, validationConfig);
  }

  // TypeScript accessor for contactDataSet - enables intellisense and type checking
  get contactDataSet(): Contact['contactDataSet'] {
    return (this._data as Contact).contactDataSet;
  }

  set contactDataSet(value: Contact['contactDataSet']) {
    (this._data as Contact).contactDataSet = value;
  }

  protected initializeDefaults(): void {
    // Set required namespace attributes for TIDAS schema compliance
    this.setNestedValue(
      'contactDataSet.@xmlns',
      'http://lca.jrc.it/ILCD/Contact'
    );
    this.setNestedValue(
      'contactDataSet.@xmlns:common',
      'http://lca.jrc.it/ILCD/Common'
    );
    this.setNestedValue(
      'contactDataSet.@xmlns:xsi',
      'http://www.w3.org/2001/XMLSchema-instance'
    );
    this.setNestedValue('contactDataSet.@version', '1.1');
    this.setNestedValue(
      'contactDataSet.@xsi:schemaLocation',
      'http://lca.jrc.it/ILCD/Contact ../../schemas/ILCD_ContactDataSet.xsd'
    );

    // Ensure required nested structure exists
    this.ensureNestedStructure([
      'contactDataSet',
      'contactDataSet.contactInformation',
      'contactDataSet.contactInformation.dataSetInformation',
      'contactDataSet.contactInformation.dataSetInformation.classificationInformation',
      'contactDataSet.administrativeInformation',
      'contactDataSet.administrativeInformation.dataEntryBy',
      'contactDataSet.administrativeInformation.publicationAndOwnership',
    ]);

    // Set required fields with default values if they don't exist
    if (
      !this.getNestedValue(
        'contactDataSet.contactInformation.dataSetInformation.common:UUID'
      )
    ) {
      this.setNestedValue(
        'contactDataSet.contactInformation.dataSetInformation.common:UUID',
        crypto.randomUUID()
      );
    }

    if (
      !this.getNestedValue(
        'contactDataSet.administrativeInformation.dataEntryBy.common:timeStamp'
      )
    ) {
      this.setNestedValue(
        'contactDataSet.administrativeInformation.dataEntryBy.common:timeStamp',
        new Date().toISOString()
      );
    }

    // if (
    //   !this.getNestedValue(
    //     'contactDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'contactDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion',
    //     '1.0.0'
    //   );
    // }

    // Set required reference fields with default values
    // if (
    //   !this.getNestedValue(
    //     'contactDataSet.administrativeInformation.dataEntryBy.common:referenceToDataSetFormat'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'contactDataSet.administrativeInformation.dataEntryBy.common:referenceToDataSetFormat',
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
    //     'contactDataSet.administrativeInformation.publicationAndOwnership.common:referenceToOwnershipOfDataSet'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'contactDataSet.administrativeInformation.publicationAndOwnership.common:referenceToOwnershipOfDataSet',
    //     {
    //       '@type': 'contact data set',
    //       '@refObjectId': this.getNestedValue(
    //         'contactDataSet.contactInformation.dataSetInformation.common:UUID'
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
        'contactDataSet.contactInformation.dataSetInformation.common:name'
      )
    ) {
      this.setNestedValue(
        'contactDataSet.contactInformation.dataSetInformation.common:name',
        new MultiLangArray()
      );
    }
    if (
      !this.getNestedValue(
        'contactDataSet.contactInformation.dataSetInformation.common:shortName'
      )
    ) {
      this.setNestedValue(
        'contactDataSet.contactInformation.dataSetInformation.common:shortName',
        new MultiLangArray()
      );
    }
    if (
      !this.getNestedValue(
        'contactDataSet.contactInformation.dataSetInformation.common:synonyms'
      )
    ) {
      this.setNestedValue(
        'contactDataSet.contactInformation.dataSetInformation.common:synonyms',
        new MultiLangArray()
      );
    }
    if (
      !this.getNestedValue(
        'contactDataSet.contactInformation.dataSetInformation.common:generalComment'
      )
    ) {
      this.setNestedValue(
        'contactDataSet.contactInformation.dataSetInformation.common:generalComment',
        new MultiLangArray()
      );
    }

    // Initialize required classification structure
    // if (
    //   !this.getNestedValue(
    //     'contactDataSet.contactInformation.dataSetInformation.classificationInformation.common:classification'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'contactDataSet.contactInformation.dataSetInformation.classificationInformation.common:classification',
    //     {
    //       'common:class': {
    //         '@level': '0',
    //         '@classId': '00000000-0000-0000-0000-000000000000',
    //         '#text': 'General contact',
    //       },
    //     }
    //   );
    // }
  }
}
