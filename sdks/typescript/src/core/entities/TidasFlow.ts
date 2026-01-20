import { TidasEntity } from '../base/TidasEntity';
import { FlowSchema } from '../../schemas';
import { Flow } from '../../types';
import { ValidationConfig } from '../config/ValidationConfig';
import { MultiLangArray } from '../../types/multi-lang-types';
import {
  ensureArray,
  formatNumber,
  joinTexts,
  pickShortDescription,
} from '../../utils/markdown';

/**
 * TIDAS Flow entity - pure data container
 * Represents material/energy flows in LCA with schema validation
 */
export class TidasFlow extends TidasEntity<Flow> {
  constructor(
    initialData?: Partial<Flow>,
    validationConfig?: Partial<ValidationConfig>
  ) {
    super(FlowSchema as any, initialData, validationConfig);
  }

  // TypeScript accessor for flowDataSet - enables intellisense and type checking
  get flowDataSet(): Flow['flowDataSet'] {
    return (this._data as Flow).flowDataSet;
  }

  set flowDataSet(value: Flow['flowDataSet']) {
    (this._data as Flow).flowDataSet = value;
  }

  protected initializeDefaults(): void {
    // Set required namespace attributes for TIDAS schema compliance
    this.setNestedValue('flowDataSet.@xmlns', 'http://lca.jrc.it/ILCD/Flow');
    this.setNestedValue(
      'flowDataSet.@xmlns:common',
      'http://lca.jrc.it/ILCD/Common'
    );
    this.setNestedValue(
      'flowDataSet.@xmlns:xsi',
      'http://www.w3.org/2001/XMLSchema-instance'
    );
    this.setNestedValue('flowDataSet.@version', '1.1');
    this.setNestedValue(
      'flowDataSet.@xsi:schemaLocation',
      'http://lca.jrc.it/ILCD/Flow ../../schemas/ILCD_FlowDataSet.xsd'
    );

    // Ensure required nested structure exists
    this.ensureNestedStructure([
      'flowDataSet',
      'flowDataSet.flowInformation',
      'flowDataSet.flowInformation.dataSetInformation',
      'flowDataSet.flowInformation.dataSetInformation.classificationInformation',
      'flowDataSet.flowInformation.quantitativeReference',
      'flowDataSet.modellingAndValidation',
      'flowDataSet.modellingAndValidation.LCIMethod',
      'flowDataSet.administrativeInformation',
      'flowDataSet.administrativeInformation.dataEntryBy',
      'flowDataSet.administrativeInformation.publicationAndOwnership',
      'flowDataSet.flowProperties',
    ]);

    // Set required fields with default values if they don't exist
    if (
      !this.getNestedValue(
        'flowDataSet.flowInformation.dataSetInformation.common:UUID'
      )
    ) {
      this.setNestedValue(
        'flowDataSet.flowInformation.dataSetInformation.common:UUID',
        crypto.randomUUID()
      );
    }

    if (
      !this.getNestedValue(
        'flowDataSet.administrativeInformation.dataEntryBy.common:timeStamp'
      )
    ) {
      this.setNestedValue(
        'flowDataSet.administrativeInformation.dataEntryBy.common:timeStamp',
        new Date().toISOString()
      );
    }

    // if (
    //   !this.getNestedValue(
    //     'flowDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'flowDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion',
    //     '1.0.0'
    //   );
    // }

    // Set required reference fields with default values
    // if (
    //   !this.getNestedValue(
    //     'flowDataSet.administrativeInformation.dataEntryBy.common:referenceToDataSetFormat'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'flowDataSet.administrativeInformation.dataEntryBy.common:referenceToDataSetFormat',
    //     {
    //       '@type': 'source data set',
    //       '@refObjectId': '00000000-0000-0000-0000-000000000000',
    //       '@version': '00.00.000',
    //       '@uri': '',
    //       'common:shortDescription': new MultiLangArray(),
    //     }
    //   );
    // }

    // if (
    //   !this.getNestedValue(
    //     'flowDataSet.administrativeInformation.publicationAndOwnership.common:referenceToOwnershipOfDataSet'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'flowDataSet.administrativeInformation.publicationAndOwnership.common:referenceToOwnershipOfDataSet',
    //     {
    //       '@type': 'contact data set',
    //       '@refObjectId': this.getNestedValue(
    //         'flowDataSet.flowInformation.dataSetInformation.common:UUID'
    //       ),
    //       '@version': '00.00.000',
    //       '@uri': '',
    //       'common:shortDescription': new MultiLangArray(),
    //     }
    //   );
    // }

    // Initialize empty arrays for multi-language text fields
    if (
      !this.getNestedValue(
        'flowDataSet.flowInformation.dataSetInformation.common:name'
      )
    ) {
      this.setNestedValue(
        'flowDataSet.flowInformation.dataSetInformation.common:name',
        new MultiLangArray()
      );
    }

    if (
      !this.getNestedValue(
        'flowDataSet.flowInformation.dataSetInformation.common:shortName'
      )
    ) {
      this.setNestedValue(
        'flowDataSet.flowInformation.dataSetInformation.common:shortName',
        new MultiLangArray()
      );
    }

    if (
      !this.getNestedValue(
        'flowDataSet.flowInformation.dataSetInformation.common:synonyms'
      )
    ) {
      this.setNestedValue(
        'flowDataSet.flowInformation.dataSetInformation.common:synonyms',
        new MultiLangArray()
      );
    }

    if (
      !this.getNestedValue(
        'flowDataSet.flowInformation.dataSetInformation.common:generalComment'
      )
    ) {
      this.setNestedValue(
        'flowDataSet.flowInformation.dataSetInformation.common:generalComment',
        new MultiLangArray()
      );
    }

    // Initialize required classification structure
    // if (
    //   !this.getNestedValue(
    //     'flowDataSet.flowInformation.dataSetInformation.classificationInformation.common:classification'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'flowDataSet.flowInformation.dataSetInformation.classificationInformation.common:classification',
    //     {
    //       'common:class': {
    //         '@level': '0',
    //         '@classId': '00000000-0000-0000-0000-000000000000',
    //         '#text': 'General flow',
    //       },
    //     }
    //   );
    // }

    // Initialize flow properties array
    if (!this.getNestedValue('flowDataSet.flowProperties')) {
      this.setNestedValue('flowDataSet.flowProperties', []);
    }

    // Set flow type if not specified
    // if (
    //   !this.getNestedValue(
    //     'flowDataSet.modellingAndValidation.LCIMethod.flowType'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'flowDataSet.modellingAndValidation.LCIMethod.flowType',
    //     'Elementary flow'
    //   );
    // }
  }

  toMarkdown(lang: string = 'en'): string {
    const dataset = this.flowDataSet;
    const flowInfo = dataset?.flowInformation;
    const dataInfo = flowInfo?.dataSetInformation;

    const title = this.composeTitle(dataInfo, lang);
    const lines: string[] = [`# ${title}`, '', '**Entity:** Flow'];

    const uuid = dataInfo?.['common:UUID'];
    if (uuid) lines.push(`**UUID:** \`${uuid}\``);

    const version = this.dataSetVersion(dataset);
    if (version) lines.push(`**Version:** ${version}`);

    const { name: refPropName, value: refPropValue } = this.referencePropertySummary(dataset, lang);
    if (refPropName || refPropValue) lines.push(`**Reference Property:** ${refPropName ?? 'N/A'}`);
    if (refPropValue) lines.push(`**Property Mean:** ${refPropValue}`);

    const method = this.methodology(dataset);
    if (method) lines.push(method);

    const cas = (dataInfo as any)?.CASNumber;
    if (cas) lines.push(`**CAS:** ${cas}`);

    const classification = this.classificationPath(dataInfo);
    if (classification) lines.push(`**Classification:** ${classification}`);

    const synonyms = joinTexts((dataInfo as any)?.['common:synonyms'], lang);
    if (synonyms) lines.push(`**Synonyms:** ${synonyms}`);

    if (lines[lines.length - 1] !== '') lines.push('');

    const description = joinTexts((dataInfo as any)?.['common:generalComment'], lang);
    if (description) lines.push('## Description', '', description, '');

    const geography = this.geography(flowInfo, lang);
    if (geography) lines.push('## Geography', '', geography, '');

    const technology = this.technology(flowInfo, lang);
    if (technology) lines.push('## Technology', '', technology, '');

    const flowProps = this.flowProperties(dataset, lang);
    if (flowProps.length) lines.push('## Flow Properties', '', ...flowProps, '');

    if (lines[lines.length - 1] === '') lines.pop();
    return lines.join('\n');
  }

  private composeTitle(
    dataInfo: Flow['flowDataSet']['flowInformation']['dataSetInformation'] | undefined,
    lang: string
  ): string {
    if (!dataInfo) return 'Flow';
    const nameObj = dataInfo.name;
    const parts: string[] = [];
    for (const field of ['baseName', 'mixAndLocationTypes', 'treatmentStandardsRoutes'] as const) {
      const part = joinTexts((nameObj as any)?.[field], lang, ' | ');
      if (part) parts.push(part);
    }
    return parts.length ? parts.join(' | ') : 'Flow';
  }

  private referencePropertySummary(
    dataset: Flow['flowDataSet'],
    lang: string
  ): { name?: string; value?: string } {
    const refId = dataset?.flowInformation?.quantitativeReference?.referenceToReferenceFlowProperty;
    if (refId === undefined || refId === null) return {};
    const properties = ensureArray<any>(dataset?.flowProperties?.flowProperty);
    const refItem = properties.find(
      item => String(item?.['@dataSetInternalID'] ?? '') === String(refId)
    );
    if (!refItem) return {};
    const refInfo = (refItem as any).referenceToFlowPropertyDataSet;
    const name = pickShortDescription(refInfo, lang);
    const value = formatNumber((refItem as any).meanValue);
    return { name, value };
  }

  private classificationPath(dataInfo: Flow['flowDataSet']['flowInformation']['dataSetInformation'] | undefined): string | undefined {
    if (!dataInfo?.classificationInformation) return undefined;
    const classification = dataInfo.classificationInformation as any;
    const container =
      classification['common:elementaryFlowCategorization'] ??
      classification['common:classification'] ??
      classification.commonClassification;
    const categories = ensureArray<any>(container?.['common:category'] ?? container?.['common:class']);
    if (!categories.length) return undefined;
    const sorted = categories.slice().sort((a, b) => {
      const aLevel = Number((a as any)['@level']);
      const bLevel = Number((b as any)['@level']);
      if (Number.isNaN(aLevel) && Number.isNaN(bLevel)) return 0;
      if (Number.isNaN(aLevel)) return 1;
      if (Number.isNaN(bLevel)) return -1;
      return aLevel - bLevel;
    });
    const parts = sorted.map(entry => String((entry as any)['#text'] ?? '')).filter(Boolean);
    return parts.length ? parts.join(' > ') : undefined;
  }

  private dataSetVersion(dataset: Flow['flowDataSet'] | undefined): string | undefined {
    return dataset?.administrativeInformation?.publicationAndOwnership?.['common:dataSetVersion'];
  }

  private geography(flowInfo: Flow['flowDataSet']['flowInformation'] | undefined, lang: string): string | undefined {
    const location = flowInfo?.geography?.locationOfSupply;
    if (!location) return undefined;
    return `**Location of Supply:** ${location}`;
  }

  private technology(flowInfo: Flow['flowDataSet']['flowInformation'] | undefined, lang: string): string | undefined {
    return joinTexts(flowInfo?.technology?.technologicalApplicability, lang);
  }

  private flowProperties(dataset: Flow['flowDataSet'] | undefined, lang: string): string[] {
    const items = ensureArray<any>(dataset?.flowProperties?.flowProperty);
    return items.map(item => {
      const ref = (item as any).referenceToFlowPropertyDataSet;
      const name = pickShortDescription(ref, lang) ?? 'Flow property';
      const mean = formatNumber((item as any).meanValue);
      return `- ${name}: ${mean}`;
    });
  }

  private methodology(dataset: Flow['flowDataSet'] | undefined): string | undefined {
    const lci = dataset?.modellingAndValidation?.LCIMethod;
    if (!lci) return undefined;
    return lci.typeOfDataSet ? `**Data Set Type:** ${lci.typeOfDataSet}` : undefined;
  }
}
