import { TidasEntity } from '../base/TidasEntity';
import { FlowPropertySchema } from '../../schemas';
import { FlowProperty } from '../../types';

/**
 * TIDAS FlowProperty entity - pure data container
 * Represents flow characteristics (mass, energy, etc.) in LCA with schema validation
 */
export class TidasFlowProperty extends TidasEntity<FlowProperty> {
  
  constructor(initialData?: Partial<FlowProperty>) {
    super(FlowPropertySchema as any, initialData);
  }

  // TypeScript accessor for flowPropertyDataSet - enables intellisense and type checking
  get flowPropertyDataSet(): FlowProperty['flowPropertyDataSet'] {
    return (this._data as FlowProperty).flowPropertyDataSet;
  }

  set flowPropertyDataSet(value: FlowProperty['flowPropertyDataSet']) {
    (this._data as FlowProperty).flowPropertyDataSet = value;
  }

  protected initializeDefaults(): void {
    // Set required namespace attributes for TIDAS schema compliance
    this.setNestedValue('flowPropertyDataSet.@xmlns', 'http://lca.jrc.it/ILCD/FlowProperty');
    this.setNestedValue('flowPropertyDataSet.@xmlns:common', 'http://lca.jrc.it/ILCD/Common');
    this.setNestedValue('flowPropertyDataSet.@xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance');
    this.setNestedValue('flowPropertyDataSet.@version', '1.1');
    this.setNestedValue('flowPropertyDataSet.@xsi:schemaLocation', 'http://lca.jrc.it/ILCD/FlowProperty ../../schemas/ILCD_FlowPropertyDataSet.xsd');
    
    // Ensure required nested structure exists
    this.ensureNestedStructure([
      'flowPropertyDataSet',
      'flowPropertyDataSet.flowPropertiesInformation',
      'flowPropertyDataSet.flowPropertiesInformation.dataSetInformation',
      'flowPropertyDataSet.flowPropertiesInformation.dataSetInformation.classificationInformation',
      'flowPropertyDataSet.flowPropertiesInformation.quantitativeReference',
      'flowPropertyDataSet.modellingAndValidation',
      'flowPropertyDataSet.modellingAndValidation.complianceDeclarations',
      'flowPropertyDataSet.administrativeInformation',
      'flowPropertyDataSet.administrativeInformation.dataEntryBy',
      'flowPropertyDataSet.administrativeInformation.publicationAndOwnership'
    ]);
    
    // Set required fields with default values if they don't exist
    if (!this.getNestedValue('flowPropertyDataSet.flowPropertiesInformation.dataSetInformation.common:UUID')) {
      this.setNestedValue('flowPropertyDataSet.flowPropertiesInformation.dataSetInformation.common:UUID', crypto.randomUUID());
    }
    
    if (!this.getNestedValue('flowPropertyDataSet.administrativeInformation.dataEntryBy.common:timeStamp')) {
      this.setNestedValue('flowPropertyDataSet.administrativeInformation.dataEntryBy.common:timeStamp', new Date().toISOString());
    }
    
    if (!this.getNestedValue('flowPropertyDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion')) {
      this.setNestedValue('flowPropertyDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion', '1.0.0');
    }
    
    // Set required reference fields with default values
    if (!this.getNestedValue('flowPropertyDataSet.administrativeInformation.dataEntryBy.common:referenceToDataSetFormat')) {
      this.setNestedValue('flowPropertyDataSet.administrativeInformation.dataEntryBy.common:referenceToDataSetFormat', {
        '@type': 'source data set',
        '@refObjectId': '00000000-0000-0000-0000-000000000000',
        '@version': '00.00.000',
        '@uri': '',
        'common:shortDescription': [{'@xml:lang': 'en', '#text': 'ILCD format'}]
      });
    }
    
    if (!this.getNestedValue('flowPropertyDataSet.administrativeInformation.publicationAndOwnership.common:referenceToOwnershipOfDataSet')) {
      this.setNestedValue('flowPropertyDataSet.administrativeInformation.publicationAndOwnership.common:referenceToOwnershipOfDataSet', {
        '@type': 'contact data set',
        '@refObjectId': this.getNestedValue('flowPropertyDataSet.flowPropertiesInformation.dataSetInformation.common:UUID'),
        '@version': '00.00.000',
        '@uri': '',
        'common:shortDescription': [{'@xml:lang': 'en', '#text': 'Own data set'}]
      });
    }
    
    // Initialize empty arrays for multi-language text fields
    if (!this.getNestedValue('flowPropertyDataSet.flowPropertiesInformation.dataSetInformation.common:name')) {
      this.setNestedValue('flowPropertyDataSet.flowPropertiesInformation.dataSetInformation.common:name', []);
    }
    
    if (!this.getNestedValue('flowPropertyDataSet.flowPropertiesInformation.dataSetInformation.common:synonyms')) {
      this.setNestedValue('flowPropertyDataSet.flowPropertiesInformation.dataSetInformation.common:synonyms', []);
    }
    
    if (!this.getNestedValue('flowPropertyDataSet.flowPropertiesInformation.dataSetInformation.common:generalComment')) {
      this.setNestedValue('flowPropertyDataSet.flowPropertiesInformation.dataSetInformation.common:generalComment', []);
    }
    
    // Initialize required classification structure
    if (!this.getNestedValue('flowPropertyDataSet.flowPropertiesInformation.dataSetInformation.classificationInformation.common:classification')) {
      this.setNestedValue('flowPropertyDataSet.flowPropertiesInformation.dataSetInformation.classificationInformation.common:classification', {
        'common:class': {
          '@level': '0',
          '@classId': '00000000-0000-0000-0000-000000000000',
          '#text': 'General flow property'
        }
      });
    }
    
    // Set required quantitative reference to unit group
    if (!this.getNestedValue('flowPropertyDataSet.flowPropertiesInformation.quantitativeReference.referenceToReferenceUnitGroup')) {
      this.setNestedValue('flowPropertyDataSet.flowPropertiesInformation.quantitativeReference.referenceToReferenceUnitGroup', {
        '@type': 'unit group data set',
        '@refObjectId': '00000000-0000-0000-0000-000000000000',
        '@version': '00.00.000',
        '@uri': '',
        'common:shortDescription': [{'@xml:lang': 'en', '#text': 'Reference unit group'}]
      });
    }
    
    // Set default copyright protection
    if (!this.getNestedValue('flowPropertyDataSet.administrativeInformation.publicationAndOwnership.common:copyright')) {
      this.setNestedValue('flowPropertyDataSet.administrativeInformation.publicationAndOwnership.common:copyright', false);
    }
    
    // Set default access restrictions
    if (!this.getNestedValue('flowPropertyDataSet.administrativeInformation.publicationAndOwnership.common:accessRestrictions')) {
      this.setNestedValue('flowPropertyDataSet.administrativeInformation.publicationAndOwnership.common:accessRestrictions', []);
    }
  }
}