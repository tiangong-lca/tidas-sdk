/**
 * This file was automatically generated from tidas_data_types
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSON Schema file,
 * and run the generation script to regenerate this file.
 */

export type CASNumber = string;
export type FT = string;
export type StringMultiLang =
  | { '@xml:lang': string; '#text': string }[]
  | { '@xml:lang': string; '#text': string };
export type Int1 = string;
export type Int5 = string;
export type Int6 = string;
export type LevelType = Int1;
export type Perc = string;
export type MatR = string;
export type MatV = string;
export type Real = string;
export type ST = string;
export type String = string;
export type STMultiLang =
  | { '@xml:lang': string; '#text': string }[]
  | { '@xml:lang': string; '#text': string };
export type FTMultiLang =
  | { '@xml:lang': string; '#text': string }[]
  | { '@xml:lang': string; '#text': string };
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
export type GIS = string;
export type UUID = string;
export type Year = number;
export type dateTime = string;
