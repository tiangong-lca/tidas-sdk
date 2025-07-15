import { TidasEntity } from '../base/TidasEntity';
import { SourceSchema } from '../../schemas';
import { Source } from '../../types';
import { ValidationConfig } from '../config/ValidationConfig';

/**
 * TIDAS Source entity - pure data container
 * Represents data sources and references in LCA with schema validation
 */
export class TidasSource extends TidasEntity<Source> {
  
  constructor(initialData?: Partial<Source>, validationConfig?: Partial<ValidationConfig>) {
    super(SourceSchema as any, initialData, validationConfig);
  }

  // TypeScript accessor for sourceDataSet - enables intellisense and type checking
  get sourceDataSet(): Source['sourceDataSet'] {
    return (this._data as Source).sourceDataSet;
  }

  set sourceDataSet(value: Source['sourceDataSet']) {
    (this._data as Source).sourceDataSet = value;
  }

  protected initializeDefaults(): void {
    // Set required namespace attributes for TIDAS schema compliance
    this.setNestedValue('sourceDataSet.@xmlns', 'http://lca.jrc.it/ILCD/Source');
    this.setNestedValue('sourceDataSet.@xmlns:common', 'http://lca.jrc.it/ILCD/Common');
    this.setNestedValue('sourceDataSet.@xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance');
    this.setNestedValue('sourceDataSet.@version', '1.1');
    this.setNestedValue('sourceDataSet.@xsi:schemaLocation', 'http://lca.jrc.it/ILCD/Source ../../schemas/ILCD_SourceDataSet.xsd');
    
    // Ensure required nested structure exists
    this.ensureNestedStructure([
      'sourceDataSet',
      'sourceDataSet.sourceInformation',
      'sourceDataSet.sourceInformation.dataSetInformation',
      'sourceDataSet.sourceInformation.dataSetInformation.classificationInformation',
      'sourceDataSet.administrativeInformation',
      'sourceDataSet.administrativeInformation.dataEntryBy',
      'sourceDataSet.administrativeInformation.publicationAndOwnership'
    ]);
    
    // Set required fields with default values if they don't exist
    if (!this.getNestedValue('sourceDataSet.sourceInformation.dataSetInformation.common:UUID')) {
      this.setNestedValue('sourceDataSet.sourceInformation.dataSetInformation.common:UUID', crypto.randomUUID());
    }
    
    if (!this.getNestedValue('sourceDataSet.administrativeInformation.dataEntryBy.common:timeStamp')) {
      this.setNestedValue('sourceDataSet.administrativeInformation.dataEntryBy.common:timeStamp', new Date().toISOString());
    }
    
    if (!this.getNestedValue('sourceDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion')) {
      this.setNestedValue('sourceDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion', '1.0.0');
    }
    
    // Set required reference fields with default values
    if (!this.getNestedValue('sourceDataSet.administrativeInformation.dataEntryBy.common:referenceToDataSetFormat')) {
      this.setNestedValue('sourceDataSet.administrativeInformation.dataEntryBy.common:referenceToDataSetFormat', {
        '@type': 'source data set',
        '@refObjectId': '00000000-0000-0000-0000-000000000000',
        '@version': '00.00.000',
        '@uri': '',
        'common:shortDescription': [{'@xml:lang': 'en', '#text': 'ILCD format'}]
      });
    }
    
    if (!this.getNestedValue('sourceDataSet.administrativeInformation.publicationAndOwnership.common:referenceToOwnershipOfDataSet')) {
      this.setNestedValue('sourceDataSet.administrativeInformation.publicationAndOwnership.common:referenceToOwnershipOfDataSet', {
        '@type': 'contact data set',
        '@refObjectId': this.getNestedValue('sourceDataSet.sourceInformation.dataSetInformation.common:UUID'),
        '@version': '00.00.000',
        '@uri': '',
        'common:shortDescription': [{'@xml:lang': 'en', '#text': 'Own data set'}]
      });
    }
    
    // Initialize empty arrays for multi-language text fields
    if (!this.getNestedValue('sourceDataSet.sourceInformation.dataSetInformation.common:shortName')) {
      this.setNestedValue('sourceDataSet.sourceInformation.dataSetInformation.common:shortName', []);
    }
    
    if (!this.getNestedValue('sourceDataSet.sourceInformation.dataSetInformation.sourceCitation')) {
      this.setNestedValue('sourceDataSet.sourceInformation.dataSetInformation.sourceCitation', []);
    }
    
    if (!this.getNestedValue('sourceDataSet.sourceInformation.dataSetInformation.publicationType')) {
      this.setNestedValue('sourceDataSet.sourceInformation.dataSetInformation.publicationType', 'Other');
    }
    
    if (!this.getNestedValue('sourceDataSet.sourceInformation.dataSetInformation.sourceDescriptionOrComment')) {
      this.setNestedValue('sourceDataSet.sourceInformation.dataSetInformation.sourceDescriptionOrComment', []);
    }
    
    // Initialize required classification structure
    if (!this.getNestedValue('sourceDataSet.sourceInformation.dataSetInformation.classificationInformation.common:classification')) {
      this.setNestedValue('sourceDataSet.sourceInformation.dataSetInformation.classificationInformation.common:classification', {
        'common:class': {
          '@level': '0',
          '@classId': '00000000-0000-0000-0000-000000000000',
          '#text': 'General source'
        }
      });
    }
    
    // Set default copyright protection
    if (!this.getNestedValue('sourceDataSet.administrativeInformation.publicationAndOwnership.common:copyright')) {
      this.setNestedValue('sourceDataSet.administrativeInformation.publicationAndOwnership.common:copyright', false);
    }
    
    // Set default access restrictions
    if (!this.getNestedValue('sourceDataSet.administrativeInformation.publicationAndOwnership.common:accessRestrictions')) {
      this.setNestedValue('sourceDataSet.administrativeInformation.publicationAndOwnership.common:accessRestrictions', []);
    }
  }
}