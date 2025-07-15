import { TidasEntity } from '../base/TidasEntity';
import { FlowSchema } from '../../schemas';
import { Flow } from '../../types';
import { ValidationConfig } from '../config/ValidationConfig';

/**
 * TIDAS Flow entity - pure data container
 * Represents material/energy flows in LCA with schema validation
 */
export class TidasFlow extends TidasEntity<Flow> {
  
  constructor(initialData?: Partial<Flow>, validationConfig?: Partial<ValidationConfig>) {
    super(FlowSchema as any, initialData, validationConfig);
  }

  // TypeScript accessor for flowDataSet - enables intellisense and type checking
  get flowDataSet(): Flow['flowDataSet'] {
    return (this._data as Flow).flowDataSet;
  }

  set flowDataSet(value: Flow['flowDataSet']) {
    (this._data as Flow).flowDataSet = value;
  }

  protected initializeDefaults(): void {
    // Set required namespace attributes for TIDAS schema compliance
    this.setNestedValue('flowDataSet.@xmlns', 'http://lca.jrc.it/ILCD/Flow');
    this.setNestedValue('flowDataSet.@xmlns:common', 'http://lca.jrc.it/ILCD/Common');
    this.setNestedValue('flowDataSet.@xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance');
    this.setNestedValue('flowDataSet.@version', '1.1');
    this.setNestedValue('flowDataSet.@xsi:schemaLocation', 'http://lca.jrc.it/ILCD/Flow ../../schemas/ILCD_FlowDataSet.xsd');
    
    // Ensure required nested structure exists
    this.ensureNestedStructure([
      'flowDataSet',
      'flowDataSet.flowInformation',
      'flowDataSet.flowInformation.dataSetInformation',
      'flowDataSet.flowInformation.dataSetInformation.classificationInformation',
      'flowDataSet.flowInformation.quantitativeReference',
      'flowDataSet.modellingAndValidation',
      'flowDataSet.modellingAndValidation.LCIMethod',
      'flowDataSet.administrativeInformation',
      'flowDataSet.administrativeInformation.dataEntryBy',
      'flowDataSet.administrativeInformation.publicationAndOwnership',
      'flowDataSet.flowProperties'
    ]);
    
    // Set required fields with default values if they don't exist
    if (!this.getNestedValue('flowDataSet.flowInformation.dataSetInformation.common:UUID')) {
      this.setNestedValue('flowDataSet.flowInformation.dataSetInformation.common:UUID', crypto.randomUUID());
    }
    
    if (!this.getNestedValue('flowDataSet.administrativeInformation.dataEntryBy.common:timeStamp')) {
      this.setNestedValue('flowDataSet.administrativeInformation.dataEntryBy.common:timeStamp', new Date().toISOString());
    }
    
    if (!this.getNestedValue('flowDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion')) {
      this.setNestedValue('flowDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion', '1.0.0');
    }
    
    // Set required reference fields with default values
    if (!this.getNestedValue('flowDataSet.administrativeInformation.dataEntryBy.common:referenceToDataSetFormat')) {
      this.setNestedValue('flowDataSet.administrativeInformation.dataEntryBy.common:referenceToDataSetFormat', {
        '@type': 'source data set',
        '@refObjectId': '00000000-0000-0000-0000-000000000000',
        '@version': '00.00.000',
        '@uri': '',
        'common:shortDescription': [{'@xml:lang': 'en', '#text': 'ILCD format'}]
      });
    }
    
    if (!this.getNestedValue('flowDataSet.administrativeInformation.publicationAndOwnership.common:referenceToOwnershipOfDataSet')) {
      this.setNestedValue('flowDataSet.administrativeInformation.publicationAndOwnership.common:referenceToOwnershipOfDataSet', {
        '@type': 'contact data set',
        '@refObjectId': this.getNestedValue('flowDataSet.flowInformation.dataSetInformation.common:UUID'),
        '@version': '00.00.000',
        '@uri': '',
        'common:shortDescription': [{'@xml:lang': 'en', '#text': 'Own data set'}]
      });
    }
    
    // Initialize empty arrays for multi-language text fields
    if (!this.getNestedValue('flowDataSet.flowInformation.dataSetInformation.common:name')) {
      this.setNestedValue('flowDataSet.flowInformation.dataSetInformation.common:name', []);
    }
    
    if (!this.getNestedValue('flowDataSet.flowInformation.dataSetInformation.common:shortName')) {
      this.setNestedValue('flowDataSet.flowInformation.dataSetInformation.common:shortName', []);
    }
    
    if (!this.getNestedValue('flowDataSet.flowInformation.dataSetInformation.common:synonyms')) {
      this.setNestedValue('flowDataSet.flowInformation.dataSetInformation.common:synonyms', []);
    }
    
    if (!this.getNestedValue('flowDataSet.flowInformation.dataSetInformation.common:generalComment')) {
      this.setNestedValue('flowDataSet.flowInformation.dataSetInformation.common:generalComment', []);
    }
    
    // Initialize required classification structure
    if (!this.getNestedValue('flowDataSet.flowInformation.dataSetInformation.classificationInformation.common:classification')) {
      this.setNestedValue('flowDataSet.flowInformation.dataSetInformation.classificationInformation.common:classification', {
        'common:class': {
          '@level': '0',
          '@classId': '00000000-0000-0000-0000-000000000000',
          '#text': 'General flow'
        }
      });
    }
    
    // Initialize flow properties array
    if (!this.getNestedValue('flowDataSet.flowProperties')) {
      this.setNestedValue('flowDataSet.flowProperties', []);
    }
    
    // Set flow type if not specified
    if (!this.getNestedValue('flowDataSet.modellingAndValidation.LCIMethod.flowType')) {
      this.setNestedValue('flowDataSet.modellingAndValidation.LCIMethod.flowType', 'Elementary flow');
    }
  }
}