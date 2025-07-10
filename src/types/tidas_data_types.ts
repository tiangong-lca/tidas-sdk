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
/**
 * Property '#text' has constraints: @maxLength 500
 */
type StringMultiLangItem = { '@xml:lang': string; '#text': string }[];
/**
 * Property '#text' has constraints: @maxLength 500
 */
type StringMultiLangItem2 = { '@xml:lang': string; '#text': string };
/**
 * Multi-language string with a maximum length of 500 characters
 */
export type StringMultiLang = StringMultiLangItem | StringMultiLangItem2;
/**
 * 1-digit integer number
 *
 * @minimum 0
 * @maximum 9
 */
export type Int1 = string;
/**
 * 5-digit integer number
 *
 * @minimum 0
 * @maximum 99999
 */
export type Int5 = string;
/**
 * 6-digit integer number
 *
 * @minimum 0
 * @maximum 999999
 */
export type Int6 = string;
/**
 * 1-digit integer number, must be equal to or greater than 0
 */
export type LevelType = Int1;
/**
 * percentage amount
 *
 * @pattern ^0\.\d+$
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
 * Property '#text' has constraints: @maxLength 1000
 */
type STMultiLangItem = { '@xml:lang': string; '#text': string }[];
/**
 * Property '#text' has constraints: @maxLength 1000
 */
type STMultiLangItem2 = { '@xml:lang': string; '#text': string };
/**
 * Multi-lang short text with a maximum length of 1000 characters.
 */
export type STMultiLang = STMultiLangItem | STMultiLangItem2;
/**
 * Multi-lang free text with an unlimited length.
 */
export type FTMultiLang =
  | { '@xml:lang': string; '#text': string }[]
  | { '@xml:lang': string; '#text': string };
type GlobalReferenceTypeItem = {
  '@type': string;
  '@refObjectId': string;
  '@version': string;
  '@uri': string;
  'common:shortDescription': STMultiLang;
};
type GlobalReferenceTypeItem2 = {
  '@type': string;
  '@refObjectId': string;
  '@version': string;
  '@uri': string;
  'common:shortDescription': STMultiLang;
}[];
/**
 * Represents a reference to another dataset or file. Either refObjectId and version, or uri, or both have to be specified.
 */
export type GlobalReferenceType =
  | GlobalReferenceTypeItem
  | GlobalReferenceTypeItem2;
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
