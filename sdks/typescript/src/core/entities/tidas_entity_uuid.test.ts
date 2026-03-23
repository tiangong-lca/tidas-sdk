import { TidasContact } from './TidasContact';
import { TidasFlow } from './TidasFlow';

const UUID_V4_PATTERN =
  /^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;

describe('entity UUID defaults', () => {
  it('generates UUIDs for entities without relying on direct global crypto access', () => {
    const flow = new TidasFlow();
    const contact = new TidasContact();

    expect(
      UUID_V4_PATTERN.test(
        flow.flowDataSet.flowInformation.dataSetInformation['common:UUID']
      )
    ).toBe(true);
    expect(
      UUID_V4_PATTERN.test(
        contact.contactDataSet.contactInformation.dataSetInformation[
          'common:UUID'
        ]
      )
    ).toBe(true);
  });
});
