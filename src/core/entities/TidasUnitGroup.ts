import { TidasEntity } from '../base/TidasEntity';
import { UnitGroupSchema } from '../../schemas';
import { UnitGroup } from '../../types';

/**
 * TIDAS UnitGroup entity - pure data container
 * Represents measurement unit groups in LCA with schema validation
 */
export class TidasUnitGroup extends TidasEntity<UnitGroup> {
  
  constructor(initialData?: Partial<UnitGroup>) {
    super(UnitGroupSchema as any, initialData);
  }

  // TypeScript accessor for unitGroupDataSet - enables intellisense and type checking
  get unitGroupDataSet(): UnitGroup['unitGroupDataSet'] {
    return (this._data as UnitGroup).unitGroupDataSet;
  }

  set unitGroupDataSet(value: UnitGroup['unitGroupDataSet']) {
    (this._data as UnitGroup).unitGroupDataSet = value;
  }

  protected initializeDefaults(): void {
    // Set required namespace attributes for TIDAS schema compliance
    this.setNestedValue('unitGroupDataSet.@xmlns', 'http://lca.jrc.it/ILCD/UnitGroup');
    this.setNestedValue('unitGroupDataSet.@xmlns:common', 'http://lca.jrc.it/ILCD/Common');
    this.setNestedValue('unitGroupDataSet.@xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance');
    this.setNestedValue('unitGroupDataSet.@version', '1.1');
    this.setNestedValue('unitGroupDataSet.@xsi:schemaLocation', 'http://lca.jrc.it/ILCD/UnitGroup ../../schemas/ILCD_UnitGroupDataSet.xsd');
    
    // Ensure required nested structure exists
    this.ensureNestedStructure([
      'unitGroupDataSet',
      'unitGroupDataSet.unitGroupInformation',
      'unitGroupDataSet.unitGroupInformation.dataSetInformation',
      'unitGroupDataSet.unitGroupInformation.dataSetInformation.classificationInformation',
      'unitGroupDataSet.unitGroupInformation.quantitativeReference',
      'unitGroupDataSet.modellingAndValidation',
      'unitGroupDataSet.modellingAndValidation.complianceDeclarations',
      'unitGroupDataSet.administrativeInformation',
      'unitGroupDataSet.administrativeInformation.dataEntryBy',
      'unitGroupDataSet.administrativeInformation.publicationAndOwnership',
      'unitGroupDataSet.units'
    ]);
    
    // Set required fields with default values if they don't exist
    if (!this.getNestedValue('unitGroupDataSet.unitGroupInformation.dataSetInformation.common:UUID')) {
      this.setNestedValue('unitGroupDataSet.unitGroupInformation.dataSetInformation.common:UUID', crypto.randomUUID());
    }
    
    if (!this.getNestedValue('unitGroupDataSet.administrativeInformation.dataEntryBy.common:timeStamp')) {
      this.setNestedValue('unitGroupDataSet.administrativeInformation.dataEntryBy.common:timeStamp', new Date().toISOString());
    }
    
    if (!this.getNestedValue('unitGroupDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion')) {
      this.setNestedValue('unitGroupDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion', '1.0.0');
    }
    
    // Set required reference fields with default values
    if (!this.getNestedValue('unitGroupDataSet.administrativeInformation.dataEntryBy.common:referenceToDataSetFormat')) {
      this.setNestedValue('unitGroupDataSet.administrativeInformation.dataEntryBy.common:referenceToDataSetFormat', {
        '@type': 'source data set',
        '@refObjectId': '00000000-0000-0000-0000-000000000000',
        '@version': '00.00.000',
        '@uri': '',
        'common:shortDescription': [{'@xml:lang': 'en', '#text': 'ILCD format'}]
      });
    }
    
    if (!this.getNestedValue('unitGroupDataSet.administrativeInformation.publicationAndOwnership.common:referenceToOwnershipOfDataSet')) {
      this.setNestedValue('unitGroupDataSet.administrativeInformation.publicationAndOwnership.common:referenceToOwnershipOfDataSet', {
        '@type': 'contact data set',
        '@refObjectId': this.getNestedValue('unitGroupDataSet.unitGroupInformation.dataSetInformation.common:UUID'),
        '@version': '00.00.000',
        '@uri': '',
        'common:shortDescription': [{'@xml:lang': 'en', '#text': 'Own data set'}]
      });
    }
    
    // Initialize empty arrays for multi-language text fields
    if (!this.getNestedValue('unitGroupDataSet.unitGroupInformation.dataSetInformation.common:name')) {
      this.setNestedValue('unitGroupDataSet.unitGroupInformation.dataSetInformation.common:name', []);
    }
    
    if (!this.getNestedValue('unitGroupDataSet.unitGroupInformation.dataSetInformation.common:shortName')) {
      this.setNestedValue('unitGroupDataSet.unitGroupInformation.dataSetInformation.common:shortName', []);
    }
    
    if (!this.getNestedValue('unitGroupDataSet.unitGroupInformation.dataSetInformation.common:synonyms')) {
      this.setNestedValue('unitGroupDataSet.unitGroupInformation.dataSetInformation.common:synonyms', []);
    }
    
    if (!this.getNestedValue('unitGroupDataSet.unitGroupInformation.dataSetInformation.common:generalComment')) {
      this.setNestedValue('unitGroupDataSet.unitGroupInformation.dataSetInformation.common:generalComment', []);
    }
    
    // Initialize required classification structure
    if (!this.getNestedValue('unitGroupDataSet.unitGroupInformation.dataSetInformation.classificationInformation.common:classification')) {
      this.setNestedValue('unitGroupDataSet.unitGroupInformation.dataSetInformation.classificationInformation.common:classification', {
        'common:class': {
          '@level': '0',
          '@classId': '00000000-0000-0000-0000-000000000000',
          '#text': 'General unit group'
        }
      });
    }
    
    // Initialize units array with at least one default unit
    if (!this.getNestedValue('unitGroupDataSet.units') || !Array.isArray(this.getNestedValue('unitGroupDataSet.units'))) {
      this.setNestedValue('unitGroupDataSet.units', []);
    }
    
    // Add default reference unit if no units exist
    const units = this.getNestedValue('unitGroupDataSet.units');
    if (units.length === 0) {
      this.setNestedValue('unitGroupDataSet.units', [{
        '@dataSetInternalID': '0',
        name: 'unit',
        meanValue: 1.0,
        'common:generalComment': [{'@xml:lang': 'en', '#text': 'Reference unit'}]
      }]);
      
      // Set quantitative reference to the default unit
      this.setNestedValue('unitGroupDataSet.unitGroupInformation.quantitativeReference.referenceToReferenceUnit', '0');
    }
    
    // Set default copyright protection
    if (!this.getNestedValue('unitGroupDataSet.administrativeInformation.publicationAndOwnership.common:copyright')) {
      this.setNestedValue('unitGroupDataSet.administrativeInformation.publicationAndOwnership.common:copyright', false);
    }
    
    // Set default access restrictions
    if (!this.getNestedValue('unitGroupDataSet.administrativeInformation.publicationAndOwnership.common:accessRestrictions')) {
      this.setNestedValue('unitGroupDataSet.administrativeInformation.publicationAndOwnership.common:accessRestrictions', []);
    }
  }
}