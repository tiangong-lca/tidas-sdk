/**
 * Test file for Zod Proxy implementation
 */

import { createZodProxy } from '../src/core/zod-proxy';
import { createZodContact, createZodFlow, createZodProcess, ContactSchema } from '../src/core/zod-factories';
import { z } from 'zod';

describe('ZodProxy', () => {
  describe('Basic Functionality', () => {
    it('should create a proxy that supports property access', () => {
      const testSchema = z.object({
        name: z.string(),
        age: z.number(),
        profile: z.object({
          email: z.string().email(),
          phone: z.string()
        })
      });

      const { proxy } = createZodProxy(testSchema);

      // Test property setting
      proxy.name = 'John Doe';
      proxy.age = 30;
      proxy.profile = {} as any;
      proxy.profile.email = 'john@example.com';
      proxy.profile.phone = '+1-555-0123';

      // Test property getting
      expect(proxy.name).toBe('John Doe');
      expect(proxy.age).toBe(30);
      expect(proxy.profile.email).toBe('john@example.com');
      expect(proxy.profile.phone).toBe('+1-555-0123');
    });

    it('should validate data against schema', () => {
      const testSchema = z.object({
        email: z.string().email(),
        age: z.number().min(0)
      });

      const { proxy, validate } = createZodProxy(testSchema);

      // Set valid data
      proxy.email = 'test@example.com';
      proxy.age = 25;

      const validResult = validate();
      expect(validResult.success).toBe(true);
      expect(validResult.data).toEqual({
        email: 'test@example.com',
        age: 25
      });
    });

    it('should fail validation with invalid data', () => {
      const testSchema = z.object({
        email: z.string().email(),
        age: z.number().min(0)
      });

      const { proxy, validate } = createZodProxy(testSchema, { throwOnValidationError: false });

      // Set invalid data
      proxy.email = 'invalid-email';
      proxy.age = -5;

      const invalidResult = validate();
      expect(invalidResult.success).toBe(false);
      expect(invalidResult.error).toBeDefined();
    });

    it('should build complete object from proxy', () => {
      const testSchema = z.object({
        user: z.object({
          name: z.string(),
          details: z.object({
            age: z.number(),
            location: z.string()
          })
        })
      });

      const { proxy, buildObject } = createZodProxy(testSchema);

      proxy.user = {} as any;
      proxy.user.name = 'Alice';
      proxy.user.details = {} as any;
      proxy.user.details.age = 28;
      proxy.user.details.location = 'New York';

      const builtObject = buildObject();
      expect(builtObject).toEqual({
        user: {
          name: 'Alice',
          details: {
            age: 28,
            location: 'New York'
          }
        }
      });
    });
  });

  describe('Array Support', () => {
    it('should handle arrays with push and pop', () => {
      const testSchema = z.object({
        items: z.array(z.string()),
        users: z.array(z.object({
          name: z.string(),
          age: z.number()
        }))
      });

      const { proxy } = createZodProxy(testSchema);

      // Initialize arrays
      proxy.items = [];
      proxy.users = [];

      // Test push
      const length1 = proxy.items.push('item1', 'item2');
      expect(length1).toBe(2);

      const length2 = proxy.users.push({ name: 'John', age: 30 });
      expect(length2).toBe(1);

      // Test array access
      expect(proxy.items[0]).toBe('item1');
      expect(proxy.items[1]).toBe('item2');
      expect(proxy.users[0].name).toBe('John');
      expect(proxy.users[0].age).toBe(30);

      // Test length
      expect(proxy.items.length).toBe(2);
      expect(proxy.users.length).toBe(1);

      // Test pop
      const popped = proxy.items.pop();
      expect(popped).toBe('item2');
      expect(proxy.items.length).toBe(1);
    });

    it('should handle array indexing', () => {
      const testSchema = z.object({
        matrix: z.array(z.array(z.number()))
      });

      const { proxy, buildObject } = createZodProxy(testSchema);

      proxy.matrix = [];
      proxy.matrix[0] = [];
      proxy.matrix[0][0] = 1;
      proxy.matrix[0][1] = 2;
      proxy.matrix[1] = [];
      proxy.matrix[1][0] = 3;
      proxy.matrix[1][1] = 4;

      const built = buildObject();
      expect(built.matrix).toEqual([[1, 2], [3, 4]]);
    });
  });

  describe('Access Logging', () => {
    it('should log property access', () => {
      const testSchema = z.object({
        name: z.string(),
        nested: z.object({
          value: z.number()
        })
      });

      const { proxy, getAccessLog } = createZodProxy(testSchema, { enableLogging: true });

      proxy.name = 'test';
      proxy.nested = {} as any;
      proxy.nested.value = 42;

      const log = getAccessLog();
      expect(log.length).toBeGreaterThan(0);
      
      // Check that we have set operations
      const setOps = log.filter(entry => entry.type === 'set');
      expect(setOps.length).toBeGreaterThanOrEqual(2);
      
      // Check paths
      const paths = setOps.map(op => op.path);
      expect(paths).toContain('name');
      expect(paths).toContain('nested.value');
    });
  });
});

describe('TIDAS Zod Factories', () => {
  describe('Contact Factory', () => {
    it('should create a contact with property access', () => {
      const contactResult = createZodContact();
      const contact = contactResult.proxy;

      // Initialize structure
      contact.contactDataSet = {} as any;
      contact.contactDataSet.contactInformation = {} as any;
      contact.contactDataSet.contactInformation.dataSetInformation = {} as any;

      // Set properties
      contact.contactDataSet.contactInformation.dataSetInformation.email = 'test@example.com';
      contact.contactDataSet.contactInformation.dataSetInformation.telephone = '+1-555-0123';

      // Test reading
      expect(contact.contactDataSet.contactInformation.dataSetInformation.email).toBe('test@example.com');
      expect(contact.contactDataSet.contactInformation.dataSetInformation.telephone).toBe('+1-555-0123');

      // Test built object
      const built = contactResult.buildObject();
      expect(built.contactDataSet.contactInformation.dataSetInformation.email).toBe('test@example.com');
    });

    it('should support multi-language text helpers', () => {
      const contactResult = createZodContact();
      
      // Use helper to set multi-language text
      contactResult.setMultiLangText('contactDataSet.contactInformation.dataSetInformation.common:name', 'John Doe', 'en');
      contactResult.setMultiLangText('contactDataSet.contactInformation.dataSetInformation.common:name', 'Juan Pérez', 'es');

      // Get text in different languages
      const englishName = contactResult.getMultiLangText('contactDataSet.contactInformation.dataSetInformation.common:name', 'en');
      const spanishName = contactResult.getMultiLangText('contactDataSet.contactInformation.dataSetInformation.common:name', 'es');

      expect(englishName).toBe('John Doe');
      expect(spanishName).toBe('Juan Pérez');
    });

    it('should generate UUID and timestamp', () => {
      const contactResult = createZodContact();
      
      // Generate UUID
      contactResult.generateUUID('contactDataSet.contactInformation.dataSetInformation.common:UUID');
      
      // Generate timestamp
      contactResult.setCurrentTimestamp('contactDataSet.administrativeInformation.dataEntryBy.common:timeStamp');

      const built = contactResult.buildObject();
      
      // Check UUID format
      const uuid = built.contactDataSet.contactInformation.dataSetInformation['common:UUID'];
      expect(uuid).toMatch(/^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i);

      // Check timestamp format (ISO string)
      const timestamp = built.contactDataSet.administrativeInformation.dataEntryBy['common:timeStamp'];
      expect(timestamp).toMatch(/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$/);
    });

    it('should validate against contact schema', () => {
      const contactResult = createZodContact();
      const contact = contactResult.proxy;

      // Set valid contact data
      contact.contactDataSet = {} as any;
      contact.contactDataSet.contactInformation = {} as any;
      contact.contactDataSet.contactInformation.dataSetInformation = {} as any;
      contact.contactDataSet.contactInformation.dataSetInformation['common:UUID'] = '123e4567-e89b-12d3-a456-426614174000';
      contact.contactDataSet.contactInformation.dataSetInformation.email = 'valid@example.com';

      const validation = contactResult.validate();
      expect(validation.success).toBe(true);
    });
  });

  describe('Flow Factory', () => {
    it('should create a flow with property access', () => {
      const flowResult = createZodFlow();
      const flow = flowResult.proxy;

      // Set flow properties
      flow.flowDataSet = {} as any;
      flow.flowDataSet.flowInformation = {} as any;
      flow.flowDataSet.flowInformation.dataSetInformation = {} as any;
      flow.flowDataSet.flowInformation.dataSetInformation.CASNumber = '7439-89-6';
      flow.flowDataSet.flowInformation.dataSetInformation.name.baseName['#text'] = 'Elementary flow';

      expect(flow.flowDataSet.flowInformation.dataSetInformation.CASNumber).toBe('7439-89-6');
      expect(flow.flowDataSet.flowInformation.dataSetInformation.name.baseName['#text']).toBe('Elementary flow');

      const built = flowResult.buildObject();
      expect(built.flowDataSet.flowInformation.dataSetInformation.CASNumber).toBe('7439-89-6');
    });
  });

  describe('Process Factory', () => {
    it('should create a process with complex nested structure', () => {
      const processResult = createZodProcess();
      const process = processResult.proxy;

      // Set complex nested properties
      process.processDataSet = {} as any;
      process.processDataSet.processInformation = {} as any;
      process.processDataSet.processInformation.dataSetInformation = {} as any;
      process.processDataSet.processInformation.dataSetInformation.name = {} as any;
      process.processDataSet.processInformation.geography = {} as any;
      process.processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction = {} as any;
      process.processDataSet.processInformation.time = {} as any;

      // Set values
      process.processDataSet.processInformation.dataSetInformation.name.baseName = {
        '@xml:lang': 'en',
        '#text': 'Steel Production'
      };
      process.processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction['@location'] = 'CN';
      process.processDataSet.processInformation.time.referenceYear = 2024;

      // Test access
      expect(process.processDataSet.processInformation.dataSetInformation.name.baseName['#text']).toBe('Steel Production');
      expect(process.processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction['@location']).toBe('CN');
      expect(process.processDataSet.processInformation.time.referenceYear).toBe('2024');

      const built = processResult.buildObject();
      expect(built.processDataSet.processInformation.dataSetInformation.name.baseName['#text']).toBe('Steel Production');
    });
  });

  describe('Schema Validation', () => {
    it('should use actual Contact schema for validation', () => {
      // Test that ContactSchema can parse a valid contact structure
      const validContact = {
        contactDataSet: {
          contactInformation: {
            dataSetInformation: {
              'common:UUID': '123e4567-e89b-12d3-a456-426614174000',
              email: 'test@example.com'
            }
          }
        }
      };

      const result = ContactSchema.safeParse(validContact);
      expect(result.success).toBe(true);
    });

    it('should reject invalid contact data', () => {
      const invalidContact = {
        contactDataSet: {
          contactInformation: {
            dataSetInformation: {
              email: 'invalid-email' // Invalid email format
            }
          }
        }
      };

      const result = ContactSchema.safeParse(invalidContact);
      expect(result.success).toBe(false);
    });
  });
});