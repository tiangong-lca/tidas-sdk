/**
 * This file was automatically generated from tidas_data_types
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSON Schema file,
 * and run the generation script to regenerate this file.
 */

/**
 * CAS Number, leading zeros are requried.
 */
export type CASNumber = string;
/**
 * Free text with an unlimited length.
 */
export type FT = string;
/**
 * Multi-language string with a maximum length of 500 characters
 */
export type StringMultiLang =
  | { '@xml:lang': string; '#text': string }[]
  | { '@xml:lang': string; '#text': string };
/**
 * 1-digit integer number
 */
export type Int1 = string;
/**
 * 5-digit integer number
 */
export type Int5 = string;
/**
 * 6-digit integer number
 */
export type Int6 = string;
/**
 * 1-digit integer number, must be equal to or greater than 0
 */
export type LevelType = Int1;
/**
 * percentage amount
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
 */
export type Real = string;
/**
 * Short text with a maximum length of 1000 characters
 */
export type ST = string;
/**
 * String with a maximum length of 500 characters. Must have a minimum length of 1.
 */
export type String = string;
/**
 * Multi-lang short text with a maximum length of 1000 characters.
 */
export type STMultiLang =
  | { '@xml:lang': string; '#text': string }[]
  | { '@xml:lang': string; '#text': string };
/**
 * Multi-lang free text with an unlimited length.
 */
export type FTMultiLang =
  | { '@xml:lang': string; '#text': string }[]
  | { '@xml:lang': string; '#text': string };
/**
 * Represents a reference to another dataset or file. Either refObjectId and version, or uri, or both have to be specified.
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
 */
export type GIS = string;
/**
 * Unique Universal Identifier, 16-byte hex number
 */
export type UUID = string;
/**
 * 4-digit year
 */
export type Year = number;
/**
 * Date and time format acc. to ISO 8601
 */
export type dateTime = string;
