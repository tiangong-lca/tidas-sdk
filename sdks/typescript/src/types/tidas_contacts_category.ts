/**
 * This file was automatically generated from tidas_contacts_category
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSON Schema file,
 * and run the generation script to regenerate this file.
 */

export type ContactsCategory =
  | {
      '@level'?: '0';
      '@classId'?: '1';
      '#text'?: 'Group of organisations, project';
    }
  | { '@level'?: '0'; '@classId'?: '2'; '#text'?: 'Organisations' }
  | { '@level'?: '1'; '@classId'?: '2.1'; '#text'?: 'Private companies' }
  | {
      '@level'?: '1';
      '@classId'?: '2.2';
      '#text'?: 'Governmental organisations';
    }
  | {
      '@level'?: '1';
      '@classId'?: '2.3';
      '#text'?: 'Non-governmental organisations';
    }
  | { '@level'?: '1'; '@classId'?: '2.4'; '#text'?: 'Other organisations' }
  | {
      '@level'?: '0';
      '@classId'?: '3';
      '#text'?: 'Working groups within organisation';
    }
  | { '@level'?: '0'; '@classId'?: '4'; '#text'?: 'Persons' }
  | { '@level'?: '0'; '@classId'?: '5'; '#text'?: 'Other' };
