import { TidasEntity } from '../base/TidasEntity';
import { ProcessSchema } from '../../schemas';
import { Process } from '../../types';
import { ValidationConfig } from '../config/ValidationConfig';
import { MultiLangArray } from '../../types/multi-lang-types';
import {
  ensureArray,
  formatNumber,
  joinTexts,
  pickShortDescription,
} from '../../utils/markdown';

/**
 * TIDAS Process entity - pure data container
 * Represents unit processes/activities in LCA with schema validation
 */
export class TidasProcess extends TidasEntity<Process> {
  constructor(
    initialData?: Partial<Process>,
    validationConfig?: Partial<ValidationConfig>
  ) {
    super(ProcessSchema as any, initialData, validationConfig);
  }

  // TypeScript accessor for processDataSet - enables intellisense and type checking
  get processDataSet(): Process['processDataSet'] {
    return (this._data as Process).processDataSet;
  }

  set processDataSet(value: Process['processDataSet']) {
    (this._data as Process).processDataSet = value;
  }

  protected initializeDefaults(): void {
    // Set required namespace attributes for TIDAS schema compliance
    this.setNestedValue(
      'processDataSet.@xmlns',
      'http://lca.jrc.it/ILCD/Process'
    );
    this.setNestedValue(
      'processDataSet.@xmlns:common',
      'http://lca.jrc.it/ILCD/Common'
    );
    this.setNestedValue(
      'processDataSet.@xmlns:xsi',
      'http://www.w3.org/2001/XMLSchema-instance'
    );
    this.setNestedValue('processDataSet.@version', '1.1');
    this.setNestedValue(
      'processDataSet.@xsi:schemaLocation',
      'http://lca.jrc.it/ILCD/Process ../../schemas/ILCD_ProcessDataSet.xsd'
    );

    // Ensure required nested structure exists
    this.ensureNestedStructure([
      'processDataSet',
      'processDataSet.processInformation',
      'processDataSet.processInformation.dataSetInformation',
      'processDataSet.processInformation.dataSetInformation.classificationInformation',
      'processDataSet.processInformation.quantitativeReference',
      'processDataSet.processInformation.time',
      'processDataSet.processInformation.geography',
      'processDataSet.processInformation.technology',
      'processDataSet.modellingAndValidation',
      'processDataSet.modellingAndValidation.LCIMethodAndAllocation',
      'processDataSet.modellingAndValidation.dataSourcesTreatmentAndRepresentativeness',
      'processDataSet.modellingAndValidation.validation',
      'processDataSet.modellingAndValidation.complianceDeclarations',
      'processDataSet.administrativeInformation',
      'processDataSet.administrativeInformation.dataEntryBy',
      'processDataSet.administrativeInformation.publicationAndOwnership',
      'processDataSet.exchanges',
    ]);

    // Set required fields with default values if they don't exist
    if (
      !this.getNestedValue(
        'processDataSet.processInformation.dataSetInformation.common:UUID'
      )
    ) {
      this.setNestedValue(
        'processDataSet.processInformation.dataSetInformation.common:UUID',
        crypto.randomUUID()
      );
    }

    if (
      !this.getNestedValue(
        'processDataSet.administrativeInformation.dataEntryBy.common:timeStamp'
      )
    ) {
      this.setNestedValue(
        'processDataSet.administrativeInformation.dataEntryBy.common:timeStamp',
        new Date().toISOString()
      );
    }

    // if (
    //   !this.getNestedValue(
    //     'processDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'processDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion',
    //     '1.0.0'
    //   );
    // }

    // Set required reference fields with default values
    // if (
    //   !this.getNestedValue(
    //     'processDataSet.administrativeInformation.dataEntryBy.common:referenceToDataSetFormat'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'processDataSet.administrativeInformation.dataEntryBy.common:referenceToDataSetFormat',
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
    //     'processDataSet.administrativeInformation.publicationAndOwnership.common:referenceToOwnershipOfDataSet'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'processDataSet.administrativeInformation.publicationAndOwnership.common:referenceToOwnershipOfDataSet',
    //     {
    //       '@type': 'contact data set',
    //       '@refObjectId': this.getNestedValue(
    //         'processDataSet.processInformation.dataSetInformation.common:UUID'
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
        'processDataSet.processInformation.dataSetInformation.common:name'
      )
    ) {
      this.setNestedValue(
        'processDataSet.processInformation.dataSetInformation.common:name',
        new MultiLangArray()
      );
    }

    if (
      !this.getNestedValue(
        'processDataSet.processInformation.dataSetInformation.common:shortName'
      )
    ) {
      this.setNestedValue(
        'processDataSet.processInformation.dataSetInformation.common:shortName',
        new MultiLangArray()
      );
    }

    if (
      !this.getNestedValue(
        'processDataSet.processInformation.dataSetInformation.common:synonyms'
      )
    ) {
      this.setNestedValue(
        'processDataSet.processInformation.dataSetInformation.common:synonyms',
        new MultiLangArray()
      );
    }

    if (
      !this.getNestedValue(
        'processDataSet.processInformation.dataSetInformation.common:generalComment'
      )
    ) {
      this.setNestedValue(
        'processDataSet.processInformation.dataSetInformation.common:generalComment',
        new MultiLangArray()
      );
    }

    // Initialize required classification structure
    // if (
    //   !this.getNestedValue(
    //     'processDataSet.processInformation.dataSetInformation.classificationInformation.common:classification'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'processDataSet.processInformation.dataSetInformation.classificationInformation.common:classification',
    //     {
    //       'common:class': {
    //         '@level': '0',
    //         '@classId': '00000000-0000-0000-0000-000000000000',
    //         '#text': 'General process',
    //       },
    //     }
    //   );
    // }

    // Initialize exchanges array
    if (!this.getNestedValue('processDataSet.exchanges')) {
      this.setNestedValue('processDataSet.exchanges', []);
    }

    // Set default process type
    // if (
    //   !this.getNestedValue(
    //     'processDataSet.modellingAndValidation.LCIMethodAndAllocation.typeOfDataSet'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'processDataSet.modellingAndValidation.LCIMethodAndAllocation.typeOfDataSet',
    //     'Unit process, single operation'
    //   );
    // }

    // Set default LCI method type
    // if (
    //   !this.getNestedValue(
    //     'processDataSet.modellingAndValidation.LCIMethodAndAllocation.LCIMethodPrinciple'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'processDataSet.modellingAndValidation.LCIMethodAndAllocation.LCIMethodPrinciple',
    //     'Attributional'
    //   );
    // }

    // Initialize time period
    // if (
    //   !this.getNestedValue(
    //     'processDataSet.processInformation.time.common:referenceYear'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'processDataSet.processInformation.time.common:referenceYear',
    //     new Date().getFullYear()
    //   );
    // }

    // Initialize geography - ensure required location is set
    // this.setNestedValue(
    //   'processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction.@location',
    //   'GLO'
    // );

    // Initialize technology
    if (
      !this.getNestedValue(
        'processDataSet.processInformation.technology.technologyDescriptionAndIncludedProcesses'
      )
    ) {
      this.setNestedValue(
        'processDataSet.processInformation.technology.technologyDescriptionAndIncludedProcesses',
        []
      );
    }

    // Set default quantitative reference type
    // if (
    //   !this.getNestedValue(
    //     'processDataSet.processInformation.quantitativeReference.@type'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'processDataSet.processInformation.quantitativeReference.@type',
    //     'Reference flow(s)'
    //   );
    // }
  }

  toMarkdown(lang: string = 'en'): string {
    const dataset = this.processDataSet;
    const processInfo = dataset?.processInformation;
    const dataInfo = processInfo?.dataSetInformation;
    const quantRef = processInfo?.quantitativeReference;

    const title = this.composeTitle(dataInfo, lang);
    const lines: string[] = [`# ${title}`, '', '**Entity:** Process'];

    const uuid = dataInfo?.['common:UUID'];
    if (uuid) lines.push(`**UUID:** \`${uuid}\``);

    const version = this.dataSetVersion(dataset);
    if (version) lines.push(`**Version:** ${version}`);

    const [locCode, geoDesc] = this.geography(processInfo, lang);
    if (locCode) lines.push(`**Location:** ${locCode}`);

    const { name: refFlowName, amount: refAmount } = this.referenceFlowSummary(dataset, quantRef, lang);
    if (refFlowName) lines.push(`**Reference Flow:** ${refFlowName}`);
    if (refAmount) lines.push(`**Amount:** ${refAmount}`);

    const classification = this.classificationPath(dataInfo);
    if (classification) lines.push(`**Classification:** ${classification}`);

    const functionalUnit = joinTexts(quantRef?.functionalUnitOrOther, lang);
    if (functionalUnit) lines.push(`**Functional Unit:** ${functionalUnit}`);

    if (lines[lines.length - 1] !== '') lines.push('');

    const description = joinTexts(dataInfo?.['common:generalComment'], lang);
    if (description) lines.push('## Description', '', description, '');

    const timeBlock = this.timeCoverage(processInfo, lang);
    if (timeBlock) lines.push('## Time Coverage', '', timeBlock, '');

    if (geoDesc) lines.push('## Geography', '', geoDesc, '');

    const technology = this.technologyBlock(processInfo, lang);
    if (technology) lines.push('## Technology', '', technology, '');

    const methodology = this.methodology(dataset);
    if (methodology) lines.push('## Methodology', '', methodology, '');

    const dataSources = this.dataSources(dataset, lang);
    if (dataSources) lines.push('## Data Sources', '', dataSources, '');

    const { inputs, outputs } = this.exchangeLists(dataset, lang);
    if (inputs.length) {
      lines.push('## Main Inputs', '', ...inputs, '');
    }
    if (outputs.length) {
      lines.push('## Main Outputs', '', ...outputs, '');
    }

    if (lines[lines.length - 1] === '') lines.pop();
    return lines.join('\n');
  }

  private composeTitle(dataInfo: Process['processDataSet']['processInformation']['dataSetInformation'] | undefined, lang: string): string {
    if (!dataInfo) return 'Process';
    const nameObj = dataInfo.name;
    const parts: string[] = [];
    for (const field of ['baseName', 'mixAndLocationTypes', 'treatmentStandardsRoutes'] as const) {
      const part = joinTexts((nameObj as any)?.[field], lang, ' | ');
      if (part) parts.push(part);
    }
    return parts.length ? parts.join(' | ') : 'Process';
  }

  private referenceFlowSummary(
    dataset: Process['processDataSet'],
    quantRef: Process['processDataSet']['processInformation']['quantitativeReference'] | undefined,
    lang: string
  ): { name?: string; amount?: string } {
    const refId = quantRef?.referenceToReferenceFlow;
    if (refId === undefined || refId === null) return {};
    const exchanges = ensureArray<any>((dataset as any)?.exchanges?.exchange);
    const refExchange = exchanges.find(
      item => String(item?.['@dataSetInternalID'] ?? item?.dataSetInternalId ?? '') === String(refId)
    );
    if (!refExchange) return {};
    const refFlow = (refExchange as any).referenceToFlowDataSet;
    const name = pickShortDescription(refFlow, lang);
    const amount = formatNumber((refExchange as any).meanAmount);
    return { name, amount };
  }

  private classificationPath(
    dataInfo: Process['processDataSet']['processInformation']['dataSetInformation'] | undefined
  ): string | undefined {
    const classes = ensureArray<any>(
      dataInfo?.classificationInformation?.['common:classification']?.['common:class']
    );
    if (!classes.length) return undefined;
    const sorted = classes.slice().sort((a, b) => {
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

  private dataSetVersion(dataset: Process['processDataSet'] | undefined): string | undefined {
    return dataset?.administrativeInformation?.publicationAndOwnership?.['common:dataSetVersion'];
  }

  private timeCoverage(
    processInfo: Process['processDataSet']['processInformation'] | undefined,
    lang: string
  ): string | undefined {
    const timeInfo = processInfo?.time;
    if (!timeInfo) return undefined;
    const year = (timeInfo as any)['common:referenceYear'];
    const until = (timeInfo as any)['common:dataSetValidUntil'];
    const desc = joinTexts((timeInfo as any)['common:timeRepresentativenessDescription'], lang);
    const parts: string[] = [];
    if (year || until) {
      parts.push(`Reference Year: ${year ?? ''}${until ? ` | Valid Until: ${until}` : ''}`.trim());
    }
    if (desc) parts.push(desc);
    return parts.length ? parts.join('\n') : undefined;
  }

  private geography(
    processInfo: Process['processDataSet']['processInformation'] | undefined,
    lang: string
  ): [string | undefined, string | undefined] {
    const location = processInfo?.geography?.locationOfOperationSupplyOrProduction;
    const code = location?.['@location'];
    const restrictions = joinTexts(location?.descriptionOfRestrictions, lang);
    return [code, restrictions];
  }

  private technologyBlock(
    processInfo: Process['processDataSet']['processInformation'] | undefined,
    lang: string
  ): string | undefined {
    const tech = processInfo?.technology;
    if (!tech) return undefined;
    const applicability = joinTexts(tech.technologicalApplicability, lang);
    const description = joinTexts(tech.technologyDescriptionAndIncludedProcesses, lang);
    const parts = [applicability, description].filter(Boolean) as string[];
    return parts.length ? parts.join('\n\n') : undefined;
  }

  private methodology(dataset: Process['processDataSet'] | undefined): string | undefined {
    const lci = dataset?.modellingAndValidation?.LCIMethodAndAllocation;
    if (!lci) return undefined;
    const parts: string[] = [];
    if (lci.typeOfDataSet) parts.push(`**Data Set Type:** ${lci.typeOfDataSet}`);
    if ((lci as any).LCIMethodPrinciple) parts.push(`**LCI Method Principle:** ${(lci as any).LCIMethodPrinciple}`);
    if ((lci as any).LCIMethodApproaches) parts.push(`**LCI Method Approach:** ${(lci as any).LCIMethodApproaches}`);
    return parts.length ? parts.join('\n') : undefined;
  }

  private dataSources(dataset: Process['processDataSet'] | undefined, lang: string): string | undefined {
    const dataSources = dataset?.modellingAndValidation?.dataSourcesTreatmentAndRepresentativeness;
    if (!dataSources) return undefined;
    const sampling = joinTexts((dataSources as any).samplingProcedure, lang);
    const ref = (dataSources as any).referenceToDataSource;
    const refText = pickShortDescription(ref, lang);
    const parts = [sampling, refText].filter(Boolean) as string[];
    return parts.length ? parts.join('\n\n') : undefined;
  }

  private exchangeLists(
    dataset: Process['processDataSet'] | undefined,
    lang: string
  ): { inputs: string[]; outputs: string[] } {
    const exchanges = ensureArray<any>((dataset as any)?.exchanges?.exchange);
    if (!exchanges.length) return { inputs: [], outputs: [] };

    const parseAmount = (item: any) => {
      const parsed = Number(item?.meanAmount);
      return Number.isFinite(parsed) ? parsed : undefined;
    };

    const sorted = exchanges
      .slice()
      .sort((a, b) => {
        const aVal = parseAmount(a);
        const bVal = parseAmount(b);
        if (aVal === undefined && bVal === undefined) return 0;
        if (aVal === undefined) return 1;
        if (bVal === undefined) return -1;
        return bVal - aVal;
      });

    const formatLine = (item: any) => {
      const name = pickShortDescription(item?.referenceToFlowDataSet, lang) ?? `Flow ${item?.['@dataSetInternalID'] ?? ''}`.trim();
      const amount = formatNumber(item?.meanAmount);
      return `- ${name}: ${amount}`;
    };

    const inputs = sorted.filter(item => item?.exchangeDirection === 'Input').map(formatLine).slice(0, 10);
    const outputs = sorted.filter(item => item?.exchangeDirection === 'Output').map(formatLine).slice(0, 10);
    return { inputs, outputs };
  }
}
