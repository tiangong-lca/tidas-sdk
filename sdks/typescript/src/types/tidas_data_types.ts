/**
 * This file was automatically generated from tidas_data_types
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSON Schema file,
 * and run the generation script to regenerate this file.
 */

/**
 * CAS Number, leading zeros are requried.
 *
 * @pattern ^[0-9]{2,7}-[0-9]{2}-[0-9]$
 */
export type CASNumber = string;
/**
 * Free text with an unlimited length.
 */
export type FT = string;
export interface LocalizedTextItem {
  '@xml:lang': string;
  '#text': string;
}
export interface LocalizedText500Item {
  '@xml:lang': string;
  /**
   * @maxLength 500
   */
  '#text': string;
}
export interface LocalizedText1000Item {
  '@xml:lang': string;
  /**
   * @maxLength 1000
   */
  '#text': string;
}
/**
 * Multi-language string with a maximum length of 500 characters
 */
export type StringMultiLang = LocalizedText500Item[] | LocalizedText500Item;
/**
 * 1-digit integer number
 *
 * @pattern ^[0-9]$
 */
export type Int1 = string;
/**
 * 5-digit integer number
 *
 * @pattern ^(0|[1-9]\d{0,4})$
 */
export type Int5 = string;
/**
 * 6-digit integer number
 *
 * @pattern ^(0|[1-9]\d{0,5})$
 */
export type Int6 = string;
/**
 * 1-digit integer number, must be equal to or greater than 0
 */
export type LevelType = Int1;
/**
 * percentage amount
 *
 * @pattern ^(100(\.0{1,3})?|([0-9]|[1-9][0-9])(\.\d{1,3})?)$
 */
export type Perc = string;
/**
 * Mathematical rule
 */
export type MatR = string;
/**
 * Mathematical variable or parameter
 */
export type MatV = string;
/**
 * 38-digit real number
 *
 * @pattern [+-]?(\d+(\.\d*)?|\.\d+)([Ee][+-]?\d+)?$
 */
export type Real = string;
/**
 * Short text with a maximum length of 1000 characters
 *
 * @maxLength 1000
 */
export type ST = string;
/**
 * String with a maximum length of 500 characters. Must have a minimum length of 1.
 *
 * @minLength 1
 * @maxLength 500
 */
export type String = string;
/**
 * Multi-lang short text with a maximum length of 1000 characters.
 */
export type STMultiLang = LocalizedText1000Item[] | LocalizedText1000Item;
/**
 * Multi-lang free text with an unlimited length.
 */
export type FTMultiLang = LocalizedTextItem[] | LocalizedTextItem;
/**
 * JSON representation of an arbitrary XML element payload.
 */
export type AnyXmlElement =
  | null
  | string
  | number
  | boolean
  | AnyXmlElement[]
  | { [key: string]: AnyXmlElement };
/**
 * ILCD common:other extension container. The container must include at least one non-common extension element; namespace declarations are allowed but do not count as extension content.
 */
export type CommonOther = { [key: string]: string | AnyXmlElement };
/**
 * Represents a reference to another dataset or file. In TIDAS, references must include type, refObjectId, version, uri, and shortDescription.
 */
export type GlobalReferenceType =
  | {
      '@type': string;
      '@refObjectId': string;
      '@version': string;
      '@uri': string;
      'common:shortDescription': STMultiLang;
    }
  | {
      '@type': string;
      '@refObjectId': string;
      '@version': string;
      '@uri': string;
      'common:shortDescription': STMultiLang;
    }[];
/**
 * Global geographical reference in Latitude and LongitudeExamples: "+42.42;-180", "0;0", "13.22 ; -3"
 *
 * @pattern ^\s*[+-]?((90(\.0+)?)|([0-8]?\d(\.\d+)?))\s*;\s*[+-]?((180(\.0+)?)|((1[0-7]\d|[0-9]?\d)(\.\d+)?))\s*$
 */
export type GIS = string;
/**
 * Unique Universal Identifier, 16-byte hex number
 *
 * @pattern ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
 */
export type UUID = string;
/**
 * 4-digit year
 *
 * @minimum 1000
 * @maximum 9999
 */
export type Year = number;
/**
 * Date and time format acc. to ISO 8601
 *
 * @format date-time
 */
export type dateTime = string;
