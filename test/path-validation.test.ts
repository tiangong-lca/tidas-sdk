/**
 * Test file for path validation system
 */

import { PathValidator, validatePath, getPathSuggestions, setGlobalPathValidatorConfig } from '../src/core/path-validator';
import { createTypedContact, createTypedFlow, createTypedProcess } from '../src/core/typed-accessors';
import { CONTACT_PATHS, FLOW_PATHS, PROCESS_PATHS } from '../src/core/typed-path-helpers';

describe('Path Validation System', () => {
  let originalConsoleWarn: typeof console.warn;
  let mockConsoleWarn: jest.Mock;

  beforeEach(() => {
    originalConsoleWarn = console.warn;
    mockConsoleWarn = jest.fn();
    console.warn = mockConsoleWarn;
  });

  afterEach(() => {
    console.warn = originalConsoleWarn;
  });

  describe('PathValidator', () => {
    it('should create a validator with default configuration', () => {
      const validator = new PathValidator();
      expect(validator).toBeDefined();
      expect(validator.getValidationConfig().strict).toBe(false);
    });

    it('should create a validator with custom configuration', () => {
      const validator = new PathValidator({ strict: true, maxSuggestions: 10 });
      expect(validator.getValidationConfig().strict).toBe(true);
      expect(validator.getValidationConfig().maxSuggestions).toBe(10);
    });

    it('should set data context and generate valid paths', () => {
      const validator = new PathValidator();
      const contactData = {
        contactDataSet: {
          contactInformation: {
            dataSetInformation: {
              'common:UUID': 'test-uuid',
              'common:name': { '@xml:lang': 'en', '#text': 'Test Name' },
              email: 'test@example.com'
            }
          }
        }
      };

      validator.setDataContext(contactData);
      const validPaths = validator.getValidPaths();
      
      expect(validPaths).toContain('contactDataSet');
      expect(validPaths).toContain('contactDataSet.contactInformation');
      expect(validPaths).toContain('contactDataSet.contactInformation.dataSetInformation');
      expect(validPaths).toContain('contactDataSet.contactInformation.dataSetInformation.common:UUID');
      expect(validPaths).toContain('contactDataSet.contactInformation.dataSetInformation.email');
    });

    it('should validate correct paths', () => {
      const validator = new PathValidator();
      const contactData = {
        contactDataSet: {
          contactInformation: {
            dataSetInformation: {
              'common:UUID': 'test-uuid',
              email: 'test@example.com'
            }
          }
        }
      };

      validator.setDataContext(contactData);
      
      const result = validator.validatePath('contactDataSet.contactInformation.dataSetInformation.email');
      expect(result.isValid).toBe(true);
      expect(result.errors).toHaveLength(0);
    });

    it('should detect common path mistakes', () => {
      const validator = new PathValidator();
      const contactData = {
        contactDataSet: {
          contactInformation: {
            dataSetInformation: {
              email: 'test@example.com'
            }
          }
        }
      };

      validator.setDataContext(contactData);
      
      // Missing dataSetInformation
      const result = validator.validatePath('contactDataSet.contactInformation.email');
      expect(result.isValid).toBe(false);
      expect(result.errors[0].error).toBe('Common path mistake detected');
      expect(result.normalizedPath).toBe('contactDataSet.contactInformation.dataSetInformation.email');
    });

    it('should provide path suggestions', () => {
      const validator = new PathValidator();
      const contactData = {
        contactDataSet: {
          contactInformation: {
            dataSetInformation: {
              'common:UUID': 'test-uuid',
              'common:name': { '@xml:lang': 'en', '#text': 'Test Name' },
              email: 'test@example.com'
            }
          }
        }
      };

      validator.setDataContext(contactData);
      
      const suggestions = validator.getPathSuggestions('email');
      expect(suggestions).toContain('contactDataSet.contactInformation.dataSetInformation.email');
      
      const partialSuggestions = validator.getPathSuggestions('contactDataSet.contact');
      expect(partialSuggestions.length).toBeGreaterThan(0);
    });
  });

  describe('Typed Accessor Integration', () => {
    it('should warn about invalid paths in non-strict mode', () => {
      const contact = createTypedContact();
      
      // Try to set with invalid path
      contact.set('contactDataSet.contactInformation.email', 'test@example.com');
      
      expect(mockConsoleWarn).toHaveBeenCalledWith(
        expect.stringContaining('Path validation warning')
      );
    });

    it('should throw error in strict mode', () => {
      const contact = createTypedContact({}, { strict: true });
      
      expect(() => {
        contact.set('contactDataSet.contactInformation.email', 'test@example.com');
      }).toThrow('Invalid path');
    });

    it('should auto-correct common mistakes', () => {
      const contact = createTypedContact();
      
      // Set with incorrect path - should auto-correct
      contact.set('contactDataSet.contactInformation.email', 'test@example.com');
      
      // Should have used the correct path
      expect(contact.get('contactDataSet.contactInformation.dataSetInformation.email')).toBe('test@example.com');
    });

    it('should provide path suggestions through accessor', () => {
      const contact = createTypedContact();
      
      const suggestions = contact.getPathSuggestions('email');
      expect(suggestions).toContain('contactDataSet.contactInformation.dataSetInformation.email');
    });

    it('should validate paths through accessor', () => {
      const contact = createTypedContact();
      
      const result = contact.validatePath('contactDataSet.contactInformation.dataSetInformation.email');
      expect(result.isValid).toBe(true);
      
      const invalidResult = contact.validatePath('contactDataSet.contactInformation.email');
      expect(invalidResult.isValid).toBe(false);
    });

    it('should toggle strict mode', () => {
      const contact = createTypedContact();
      
      // Should not throw in non-strict mode
      contact.set('contactDataSet.contactInformation.email', 'test@example.com');
      
      // Enable strict mode
      contact.setStrictMode(true);
      
      // Should throw in strict mode
      expect(() => {
        contact.set('contactDataSet.contactInformation.invalidField', 'value');
      }).toThrow();
    });
  });

  describe('Path Constants', () => {
    it('should provide correct contact path constants', () => {
      expect(CONTACT_PATHS.EMAIL).toBe('contactDataSet.contactInformation.dataSetInformation.email');
      expect(CONTACT_PATHS.UUID).toBe('contactDataSet.contactInformation.dataSetInformation.common:UUID');
      expect(CONTACT_PATHS.NAME).toBe('contactDataSet.contactInformation.dataSetInformation.common:name');
    });

    it('should provide correct flow path constants', () => {
      expect(FLOW_PATHS.BASE_NAME).toBe('flowDataSet.flowInformation.dataSetInformation.name.baseName');
      expect(FLOW_PATHS.CAS_NUMBER).toBe('flowDataSet.flowInformation.dataSetInformation.CASNumber');
      expect(FLOW_PATHS.UUID).toBe('flowDataSet.flowInformation.dataSetInformation.common:UUID');
    });

    it('should provide correct process path constants', () => {
      expect(PROCESS_PATHS.BASE_NAME).toBe('processDataSet.processInformation.dataSetInformation.name.baseName');
      expect(PROCESS_PATHS.LOCATION).toBe('processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction.@location');
      expect(PROCESS_PATHS.REFERENCE_YEAR).toBe('processDataSet.processInformation.time.referenceYear');
    });
  });

  describe('Real-world Usage Scenarios', () => {
    it('should prevent common Contact path mistakes', () => {
      const contact = createTypedContact();
      
      // Common mistake: missing dataSetInformation
      contact.set('contactDataSet.contactInformation.email', 'test@example.com');
      
      // Should have been corrected to the right path
      expect(contact.get('contactDataSet.contactInformation.dataSetInformation.email')).toBe('test@example.com');
      expect(mockConsoleWarn).toHaveBeenCalledWith(
        expect.stringContaining('Using suggested path')
      );
    });

    it('should prevent common Flow path mistakes', () => {
      const flow = createTypedFlow();
      
      // Common mistake: missing dataSetInformation
      flow.set('flowDataSet.flowInformation.name.baseName', { '@xml:lang': 'en', '#text': 'Steel' });
      
      // Should have been corrected
      expect(flow.get('flowDataSet.flowInformation.dataSetInformation.name.baseName')).toEqual({ '@xml:lang': 'en', '#text': 'Steel' });
    });

    it('should prevent common Process path mistakes', () => {
      const process = createTypedProcess();
      
      // Common mistake: wrong location path
      process.set('processDataSet.processInformation.location', 'CN');
      
      // Should have been corrected
      expect(process.get('processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction.@location')).toBe('CN');
    });

    it('should handle namespace prefix mistakes', () => {
      const contact = createTypedContact();
      
      // Missing common: prefix
      contact.set('contactDataSet.contactInformation.dataSetInformation.UUID', 'test-uuid');
      
      // Should have been corrected
      expect(contact.get('contactDataSet.contactInformation.dataSetInformation.common:UUID')).toBe('test-uuid');
    });

    it('should provide helpful suggestions for partial paths', () => {
      const contact = createTypedContact();
      
      const emailSuggestions = contact.getPathSuggestions('email');
      expect(emailSuggestions).toContain('contactDataSet.contactInformation.dataSetInformation.email');
      
      const nameSuggestions = contact.getPathSuggestions('name');
      expect(nameSuggestions).toContain('contactDataSet.contactInformation.dataSetInformation.common:name');
      expect(nameSuggestions).toContain('contactDataSet.contactInformation.dataSetInformation.common:shortName');
    });
  });

  describe('Global Configuration', () => {
    it('should allow global configuration', () => {
      setGlobalPathValidatorConfig({ strict: true });
      
      const contact = createTypedContact();
      
      expect(() => {
        contact.set('contactDataSet.contactInformation.invalidField', 'value');
      }).toThrow();
    });

    it('should use global validator functions', () => {
      const contactData = {
        contactDataSet: {
          contactInformation: {
            dataSetInformation: {
              email: 'test@example.com'
            }
          }
        }
      };

      const result = validatePath('contactDataSet.contactInformation.dataSetInformation.email', contactData);
      expect(result.isValid).toBe(true);
      
      const suggestions = getPathSuggestions('email', contactData);
      expect(suggestions).toContain('contactDataSet.contactInformation.dataSetInformation.email');
    });
  });
});