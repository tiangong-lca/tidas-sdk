import { TidasEntity } from '../base/TidasEntity';
import { LifeCycleModelSchema } from '../../schemas';
import { LifeCycleModel } from '../../types';
import { ValidationConfig } from '../config/ValidationConfig';
import { MultiLangArray } from '../../types/multi-lang-types';
import {
  ensureArray,
  formatNumber,
  joinTexts,
  pickShortDescription,
} from '../../utils/markdown';

/**
 * TIDAS LifeCycleModel entity - pure data container
 * Represents system models in LCA with schema validation
 */
export class TidasLifeCycleModel extends TidasEntity<LifeCycleModel> {
  constructor(
    initialData?: Partial<LifeCycleModel>,
    validationConfig?: Partial<ValidationConfig>
  ) {
    super(LifeCycleModelSchema as any, initialData, validationConfig);
  }

  // TypeScript accessor for lifeCycleModelDataSet - enables intellisense and type checking
  get lifeCycleModelDataSet(): LifeCycleModel['lifeCycleModelDataSet'] {
    return (this._data as LifeCycleModel).lifeCycleModelDataSet;
  }

  set lifeCycleModelDataSet(value: LifeCycleModel['lifeCycleModelDataSet']) {
    (this._data as LifeCycleModel).lifeCycleModelDataSet = value;
  }

  protected initializeDefaults(): void {
    // Set required namespace attributes for TIDAS schema compliance
    this.setNestedValue(
      'lifeCycleModelDataSet.@xmlns',
      'http://eplca.jrc.ec.europa.eu/ILCD/LifeCycleModel/2017'
    );
    this.setNestedValue(
      'lifeCycleModelDataSet.@xmlns:common',
      'http://lca.jrc.it/ILCD/Common'
    );
    this.setNestedValue(
      'lifeCycleModelDataSet.@xmlns:xsi',
      'http://www.w3.org/2001/XMLSchema-instance'
    );
    this.setNestedValue('lifeCycleModelDataSet.@version', '1.1');
    this.setNestedValue(
      'lifeCycleModelDataSet.@xsi:schemaLocation',
      'http://eplca.jrc.ec.europa.eu/ILCD/LifeCycleModel/2017 ../../schemas/ILCD_LifeCycleModelDataSet.xsd'
    );

    // Ensure required nested structure exists
    this.ensureNestedStructure([
      'lifeCycleModelDataSet',
      'lifeCycleModelDataSet.lifeCycleModelInformation',
      'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation',
      'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.classificationInformation',
      'lifeCycleModelDataSet.lifeCycleModelInformation.quantitativeReference',
      'lifeCycleModelDataSet.modellingAndValidation',
      'lifeCycleModelDataSet.modellingAndValidation.complianceDeclarations',
      'lifeCycleModelDataSet.administrativeInformation',
      'lifeCycleModelDataSet.administrativeInformation.dataEntryBy',
      'lifeCycleModelDataSet.administrativeInformation.publicationAndOwnership',
      'lifeCycleModelDataSet.technology',
    ]);

    // Set required fields with default values if they don't exist
    if (
      !this.getNestedValue(
        'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.common:UUID'
      )
    ) {
      this.setNestedValue(
        'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.common:UUID',
        crypto.randomUUID()
      );
    }

    if (
      !this.getNestedValue(
        'lifeCycleModelDataSet.administrativeInformation.dataEntryBy.common:timeStamp'
      )
    ) {
      this.setNestedValue(
        'lifeCycleModelDataSet.administrativeInformation.dataEntryBy.common:timeStamp',
        new Date().toISOString()
      );
    }

    // if (
    //   !this.getNestedValue(
    //     'lifeCycleModelDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'lifeCycleModelDataSet.administrativeInformation.publicationAndOwnership.common:dataSetVersion',
    //     '1.0.0'
    //   );
    // }

    // Set required reference fields with default values
    // if (
    //   !this.getNestedValue(
    //     'lifeCycleModelDataSet.administrativeInformation.dataEntryBy.common:referenceToDataSetFormat'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'lifeCycleModelDataSet.administrativeInformation.dataEntryBy.common:referenceToDataSetFormat',
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
    //     'lifeCycleModelDataSet.administrativeInformation.publicationAndOwnership.common:referenceToOwnershipOfDataSet'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'lifeCycleModelDataSet.administrativeInformation.publicationAndOwnership.common:referenceToOwnershipOfDataSet',
    //     {
    //       '@type': 'contact data set',
    //       '@refObjectId': this.getNestedValue(
    //         'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.common:UUID'
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
        'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.common:name'
      )
    ) {
      this.setNestedValue(
        'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.common:name',
        new MultiLangArray()
      );
    }

    if (
      !this.getNestedValue(
        'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.common:shortName'
      )
    ) {
      this.setNestedValue(
        'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.common:shortName',
        new MultiLangArray()
      );
    }

    if (
      !this.getNestedValue(
        'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.common:synonyms'
      )
    ) {
      this.setNestedValue(
        'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.common:synonyms',
        new MultiLangArray()
      );
    }

    if (
      !this.getNestedValue(
        'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.common:generalComment'
      )
    ) {
      this.setNestedValue(
        'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.common:generalComment',
        new MultiLangArray()
      );
    }

    // Initialize required classification structure
    // if (
    //   !this.getNestedValue(
    //     'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.classificationInformation.common:classification'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.classificationInformation.common:classification',
    //     {
    //       'common:class': {
    //         '@level': '0',
    //         '@classId': '00000000-0000-0000-0000-000000000000',
    //         '#text': 'General life cycle model',
    //       },
    //     }
    //   );
    // }

    // Initialize technology array
    if (!this.getNestedValue('lifeCycleModelDataSet.technology')) {
      this.setNestedValue('lifeCycleModelDataSet.technology', []);
    }

    // Set default model type
    // if (
    //   !this.getNestedValue(
    //     'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.typeOfModel'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.typeOfModel',
    //     'Product system model'
    //   );
    // }

    // Set default functional unit or other reference
    if (
      !this.getNestedValue(
        'lifeCycleModelDataSet.lifeCycleModelInformation.quantitativeReference.functionalUnitOrOther'
      )
    ) {
      this.setNestedValue(
        'lifeCycleModelDataSet.lifeCycleModelInformation.quantitativeReference.functionalUnitOrOther',
        new MultiLangArray()
      );
    }

    // Set default copyright protection
    // if (
    //   !this.getNestedValue(
    //     'lifeCycleModelDataSet.administrativeInformation.publicationAndOwnership.common:copyright'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'lifeCycleModelDataSet.administrativeInformation.publicationAndOwnership.common:copyright',
    //     false
    //   );
    // }

    // Set default access restrictions
    // if (
    //   !this.getNestedValue(
    //     'lifeCycleModelDataSet.administrativeInformation.publicationAndOwnership.common:accessRestrictions'
    //   )
    // ) {
    //   this.setNestedValue(
    //     'lifeCycleModelDataSet.administrativeInformation.publicationAndOwnership.common:accessRestrictions',
    //     []
    //   );
    // }
  }

  toMarkdown(lang: string = 'en'): string {
    const dataset = this.lifeCycleModelDataSet;
    const info = dataset?.lifeCycleModelInformation;
    const dataInfo = info?.dataSetInformation;
    const quantRef = info?.quantitativeReference;
    const technology = info?.technology;
    const modelling = dataset?.modellingAndValidation;

    const title = this.composeTitle(dataInfo, lang);
    const lines: string[] = [`# ${title}`, '', '**Entity:** Life Cycle Model'];

    const uuid = dataInfo?.['common:UUID'];
    if (uuid) lines.push(`**UUID:** \`${uuid}\``);

    const version = this.dataSetVersion(dataset);
    if (version) lines.push(`**Version:** ${version}`);

    const { name: refName, id: refId } = this.referenceProcessSummary(quantRef, technology, lang);
    if (refName || refId) {
      lines.push(`**Reference Process:** ${refName ?? 'Reference process'}${refId ? ` (ID ${refId})` : ''}`);
    }

    const resulting = pickShortDescription(dataInfo?.referenceToResultingProcess, lang);
    if (resulting) lines.push(`**Resulting Process:** ${resulting}`);

    const externalDoc = pickShortDescription(dataInfo?.referenceToExternalDocumentation, lang);
    if (externalDoc) lines.push(`**External Documentation:** ${externalDoc}`);

    const classification = this.classificationPath(dataInfo);
    if (classification) lines.push(`**Classification:** ${classification}`);

    const synonyms = joinTexts((dataInfo as any)?.['common:synonyms'], lang);
    if (synonyms) lines.push(`**Synonyms:** ${synonyms}`);

    if (lines[lines.length - 1] !== '') lines.push('');

    const description = joinTexts((dataInfo as any)?.['common:generalComment'], lang);
    if (description) lines.push('## Description', '', description, '');

    const useAdvice = this.useAdvice(modelling, lang);
    if (useAdvice) lines.push('## Use Advice', '', useAdvice, '');

    const processLines = this.processLines(technology, lang);
    if (processLines.length) lines.push('## Process Instances', '', ...processLines, '');

    const diagram = pickShortDescription(technology?.referenceToDiagram, lang);
    if (diagram) lines.push('## Technology', '', `Diagram: ${diagram}`, '');

    if (lines[lines.length - 1] === '') lines.pop();
    return lines.join('\n');
  }

  private composeTitle(
    dataInfo: LifeCycleModel['lifeCycleModelDataSet']['lifeCycleModelInformation']['dataSetInformation'] | undefined,
    lang: string
  ): string {
    if (!dataInfo) return 'Life Cycle Model';
    const nameObj = dataInfo.name;
    const parts: string[] = [];
    for (const field of ['baseName', 'mixAndLocationTypes', 'treatmentStandardsRoutes', 'functionalUnitFlowProperties'] as const) {
      const part = joinTexts((nameObj as any)?.[field], lang, ' | ');
      if (part) parts.push(part);
    }
    return parts.length ? parts.join(' | ') : 'Life Cycle Model';
  }

  private classificationPath(
    dataInfo: LifeCycleModel['lifeCycleModelDataSet']['lifeCycleModelInformation']['dataSetInformation'] | undefined
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

  private dataSetVersion(dataset: LifeCycleModel['lifeCycleModelDataSet'] | undefined): string | undefined {
    return dataset?.administrativeInformation?.publicationAndOwnership?.['common:dataSetVersion'];
  }

  private processInstances(
    technology: LifeCycleModel['lifeCycleModelDataSet']['lifeCycleModelInformation']['technology'] | undefined
  ) {
    return ensureArray<any>(technology?.processes?.processInstance);
  }

  private referenceProcessSummary(
    quantRef: LifeCycleModel['lifeCycleModelDataSet']['lifeCycleModelInformation']['quantitativeReference'] | undefined,
    technology: LifeCycleModel['lifeCycleModelDataSet']['lifeCycleModelInformation']['technology'] | undefined,
    lang: string
  ): { name?: string; id?: string } {
    const refId = quantRef?.referenceToReferenceProcess;
    if (refId === undefined || refId === null) return {};
    const instances = this.processInstances(technology);
    const match = instances.find(item => String(item?.['@dataSetInternalID'] ?? '') === String(refId));
    if (!match) return { id: String(refId) };
    const ref = (match as any).referenceToProcess;
    const name = pickShortDescription(ref, lang);
    return { name, id: String(refId) };
  }

  private processLines(
    technology: LifeCycleModel['lifeCycleModelDataSet']['lifeCycleModelInformation']['technology'] | undefined,
    lang: string
  ): string[] {
    const instances = this.processInstances(technology);
    if (!instances.length) return [];

    const parseId = (item: any) => {
      const val = Number(item?.['@dataSetInternalID']);
      return Number.isFinite(val) ? val : undefined;
    };

    const sorted = instances
      .slice()
      .sort((a, b) => {
        const aId = parseId(a);
        const bId = parseId(b);
        if (aId === undefined && bId === undefined) return 0;
        if (aId === undefined) return 1;
        if (bId === undefined) return -1;
        return aId - bId;
      });

    return sorted.map(item => {
      const instId = (item as any)['@dataSetInternalID'];
      const mult = (item as any)['@multiplicationFactor'];
      const ref = (item as any).referenceToProcess;
      const name = pickShortDescription(ref, lang) ?? 'Process';
      const suffix = mult ? ` ×${formatNumber(mult)}` : '';
      return `- ID ${instId ?? ''}: ${name}${suffix}`;
    });
  }

  private useAdvice(
    modelling: LifeCycleModel['lifeCycleModelDataSet']['modellingAndValidation'] | undefined,
    lang: string
  ): string | undefined {
    return joinTexts(modelling?.dataSourcesTreatmentEtc?.useAdviceForDataSet, lang);
  }
}
