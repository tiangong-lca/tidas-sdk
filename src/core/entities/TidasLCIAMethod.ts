import { TidasEntity } from '../base/TidasEntity';
import { LCIAMethodSchema } from '../../schemas';
import { LCIAMethod } from '../../types';

/**
 * TIDAS LCIAMethod entity - pure data container
 * Represents impact assessment methods in LCA with schema validation
 */
export class TidasLCIAMethod extends TidasEntity<LCIAMethod> {
  
  constructor(initialData?: Partial<LCIAMethod>) {
    super(LCIAMethodSchema as any, initialData);
  }

  // TypeScript accessor for LCIAMethodDataSet - enables intellisense and type checking
  get LCIAMethodDataSet(): LCIAMethod['LCIAMethodDataSet'] {
    return (this._data as LCIAMethod).LCIAMethodDataSet;
  }

  set LCIAMethodDataSet(value: LCIAMethod['LCIAMethodDataSet']) {
    (this._data as LCIAMethod).LCIAMethodDataSet = value;
  }

  protected initializeDefaults(): void {
    // Set required namespace attributes for TIDAS schema compliance
    this.setNestedValue('LCIAMethodDataSet.@xmlns', 'http://lca.jrc.it/ILCD/LCIAMethod');
    this.setNestedValue('LCIAMethodDataSet.@xmlns:common', 'http://lca.jrc.it/ILCD/Common');
    this.setNestedValue('LCIAMethodDataSet.@xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance');
    this.setNestedValue('LCIAMethodDataSet.@version', '1.1');
    this.setNestedValue('LCIAMethodDataSet.@xsi:schemaLocation', 'http://lca.jrc.it/ILCD/LCIAMethod ../../schemas/ILCD_LCIAMethodDataSet.xsd');
    
    // Ensure required nested structure exists
    this.ensureNestedStructure([
      'LCIAMethodDataSet',
      'LCIAMethodDataSet.LCIAMethodInformation',
      'LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation',
      'LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.classificationInformation',
      'LCIAMethodDataSet.LCIAMethodInformation.quantitativeReference',
      'LCIAMethodDataSet.modellingAndValidation',
      'LCIAMethodDataSet.modellingAndValidation.complianceDeclarations',
      'LCIAMethodDataSet.administrativeInformation',
      'LCIAMethodDataSet.administrativeInformation.dataEntryBy',
      'LCIAMethodDataSet.administrativeInformation.publicationAndOwnership',
      'LCIAMethodDataSet.characterisationFactors'
    ]);
    
    // Set required fields with default values if they don't exist
    if (!this.getNestedValue('LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.common:UUID')) {
      this.setNestedValue('LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.common:UUID', crypto.randomUUID());
    }
    
    if (!this.getNestedValue('LCIAMethodDataSet.administrativeInformation.dataEntryBy.common:timeStamp')) {
      this.setNestedValue('LCIAMethodDataSet.administrativeInformation.dataEntryBy.common:timeStamp', new Date().toISOString());
    }
    
    if (!this.getNestedValue('LCIAMethodDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion')) {
      this.setNestedValue('LCIAMethodDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion', '1.0.0');
    }
    
    // Set required reference fields with default values
    if (!this.getNestedValue('LCIAMethodDataSet.administrativeInformation.dataEntryBy.common:referenceToDataSetFormat')) {
      this.setNestedValue('LCIAMethodDataSet.administrativeInformation.dataEntryBy.common:referenceToDataSetFormat', {
        '@type': 'source data set',
        '@refObjectId': '00000000-0000-0000-0000-000000000000',
        '@version': '00.00.000',
        '@uri': '',
        'common:shortDescription': [{'@xml:lang': 'en', '#text': 'ILCD format'}]
      });
    }
    
    if (!this.getNestedValue('LCIAMethodDataSet.administrativeInformation.publicationAndOwnership.common:referenceToOwnershipOfDataSet')) {
      this.setNestedValue('LCIAMethodDataSet.administrativeInformation.publicationAndOwnership.common:referenceToOwnershipOfDataSet', {
        '@type': 'contact data set',
        '@refObjectId': this.getNestedValue('LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.common:UUID'),
        '@version': '00.00.000',
        '@uri': '',
        'common:shortDescription': [{'@xml:lang': 'en', '#text': 'Own data set'}]
      });
    }
    
    // Initialize empty arrays for multi-language text fields
    if (!this.getNestedValue('LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.common:name')) {
      this.setNestedValue('LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.common:name', []);
    }
    
    if (!this.getNestedValue('LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.common:shortName')) {
      this.setNestedValue('LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.common:shortName', []);
    }
    
    if (!this.getNestedValue('LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.common:synonyms')) {
      this.setNestedValue('LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.common:synonyms', []);
    }
    
    if (!this.getNestedValue('LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.common:generalComment')) {
      this.setNestedValue('LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.common:generalComment', []);
    }
    
    // Initialize required classification structure
    if (!this.getNestedValue('LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.classificationInformation.common:classification')) {
      this.setNestedValue('LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.classificationInformation.common:classification', {
        'common:class': {
          '@level': '0',
          '@classId': '00000000-0000-0000-0000-000000000000',
          '#text': 'General LCIA method'
        }
      });
    }
    
    // Initialize characterisation factors array
    if (!this.getNestedValue('LCIAMethodDataSet.characterisationFactors')) {
      this.setNestedValue('LCIAMethodDataSet.characterisationFactors', []);
    }
    
    // Set default method type
    if (!this.getNestedValue('LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.typeOfDataSet')) {
      this.setNestedValue('LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.typeOfDataSet', 'Mid-point indicator');
    }
    
    // Set default impact category
    if (!this.getNestedValue('LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.impactCategory')) {
      this.setNestedValue('LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.impactCategory', [{'@xml:lang': 'en', '#text': 'Environmental impact'}]);
    }
    
    // Set default area of protection
    if (!this.getNestedValue('LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.areaOfProtection')) {
      this.setNestedValue('LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.areaOfProtection', [{'@xml:lang': 'en', '#text': 'Natural environment'}]);
    }
    
    // Set reference quantity
    if (!this.getNestedValue('LCIAMethodDataSet.LCIAMethodInformation.quantitativeReference.referenceQuantity')) {
      this.setNestedValue('LCIAMethodDataSet.LCIAMethodInformation.quantitativeReference.referenceQuantity', '0');
    }
    
    // Set default copyright protection
    if (!this.getNestedValue('LCIAMethodDataSet.administrativeInformation.publicationAndOwnership.common:copyright')) {
      this.setNestedValue('LCIAMethodDataSet.administrativeInformation.publicationAndOwnership.common:copyright', false);
    }
    
    // Set default access restrictions
    if (!this.getNestedValue('LCIAMethodDataSet.administrativeInformation.publicationAndOwnership.common:accessRestrictions')) {
      this.setNestedValue('LCIAMethodDataSet.administrativeInformation.publicationAndOwnership.common:accessRestrictions', []);
    }
  }
}