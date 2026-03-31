import { datasetFromXml, datasetToXml, parseXml, unparseXml } from './index';

const SAMPLE_XML = `<?xml version="1.0" encoding="UTF-8"?>
<processDataSet xmlns="http://lca.jrc.it/ILCD/Process"
                xmlns:common="http://lca.jrc.it/ILCD/Common"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                version="1.1"
                locations="../ILCDLocations.xml"
                xsi:schemaLocation="http://lca.jrc.it/ILCD/Process ../../schemas/ILCD_ProcessDataSet.xsd">
  <processInformation>
    <dataSetInformation>
      <common:UUID>123e4567-e89b-12d3-a456-426614174000</common:UUID>
      <name>
        <baseName xml:lang="en">Sample Process</baseName>
      </name>
    </dataSetInformation>
    <quantitativeReference type="Reference flow(s)">
      <referenceToReferenceFlow>1</referenceToReferenceFlow>
      <functionalUnitOrOther xml:lang="en">1 kg of output</functionalUnitOrOther>
    </quantitativeReference>
  </processInformation>
</processDataSet>`;

describe('xml helpers', () => {
  it('parses ILCD XML with attribute and text keys matching TIDAS conventions', () => {
    const parsed = datasetFromXml(SAMPLE_XML);
    const processDataSet = parsed.processDataSet as Record<string, unknown>;
    const processInformation = processDataSet.processInformation as Record<
      string,
      unknown
    >;
    const dataSetInformation = processInformation.dataSetInformation as Record<
      string,
      unknown
    >;
    const name = dataSetInformation.name as Record<string, unknown>;
    const baseName = name.baseName as Record<string, unknown>;
    const quantitativeReference =
      processInformation.quantitativeReference as Record<string, unknown>;
    const functionalUnitOrOther =
      quantitativeReference.functionalUnitOrOther as Record<string, unknown>;

    expect(processDataSet['@xmlns']).toBe('http://lca.jrc.it/ILCD/Process');
    expect(dataSetInformation['common:UUID']).toBe(
      '123e4567-e89b-12d3-a456-426614174000'
    );
    expect(baseName['@xml:lang']).toBe('en');
    expect(baseName['#text']).toBe('Sample Process');
    expect(quantitativeReference['@type']).toBe('Reference flow(s)');
    expect(functionalUnitOrOther['#text']).toBe('1 kg of output');
  });

  it('accepts Buffer input and returns the same parsed shape', () => {
    const parsed = parseXml(Buffer.from(SAMPLE_XML, 'utf8')) as Record<
      string,
      unknown
    >;
    expect(parsed.processDataSet).toBeDefined();
  });

  it('round-trips a parsed dataset back into XML', () => {
    const parsed = datasetFromXml(SAMPLE_XML);
    const xml = datasetToXml(parsed);

    expect(xml).toContain('<processDataSet');
    expect(xml).toContain('xml:lang="en"');
    expect(xml).toContain('<common:UUID>123e4567-e89b-12d3-a456-426614174000</common:UUID>');
    expect(xml).toContain('<functionalUnitOrOther xml:lang="en">1 kg of output</functionalUnitOrOther>');
  });

  it('uses pretty XML output by default', () => {
    const xml = unparseXml({
      root: {
        child: {
          '@xml:lang': 'en',
          '#text': 'hello',
        },
      },
    });

    expect(xml).toContain('<?xml version="1.0"');
    expect(xml).toContain('\n');
    expect(xml).toContain('<child xml:lang="en">hello</child>');
  });

  it('rejects empty dataset payloads for XML output', () => {
    expect(() => datasetToXml({})).toThrow(
      'Expected a non-empty object payload for XML output.'
    );
  });
});
