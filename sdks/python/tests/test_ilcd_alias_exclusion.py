import pytest
from pydantic import ValidationError
from tidas_sdk.core.multilang import MultiLangList
from tidas_sdk.generated.tidas_lciamethods import LCIAMethodDataSetLCIAMethodInformationGeography
from tidas_sdk.generated.tidas_lifecyclemodels import ProcessesProcessInstanceItem, ProcessesProcessInstanceOption1


@pytest.mark.parametrize('model', [ProcessesProcessInstanceItem, ProcessesProcessInstanceOption1])
def test_scaling_aliases_are_exclusive(model):
    data = {'@dataSetInternalID': '1', '@multiplicationFactor': '1', 'referenceToProcess': {
        '@type': 'process data set', '@refObjectId': '00000000-0000-4000-8000-000000000001',
        '@version': '01.00.000', '@uri': '../processes/example.xml',
        'common:shortDescription': MultiLangList([{'@xml:lang': 'en', '#text': 'Process'}, {'@xml:lang': 'zh', '#text': '过程'}]),
    }}
    for key in ('scalingFactor', 'scalingFactors'):
        model.model_validate({**data, key: '2'})
    with pytest.raises(ValidationError, match='Properties must not all be present'):
        model.model_validate({**data, 'scalingFactor': '2', 'scalingFactors': '2'})
    with pytest.raises(ValidationError, match='Properties must not all be present'):
        model.model_validate({**data, 'scaling_factor': '2', 'scaling_factors': '2'})


def test_geography_aliases_are_exclusive():
    model = LCIAMethodDataSetLCIAMethodInformationGeography
    for key in ('interventionSubLocation', 'intervensionSubLocation'):
        model.model_validate({key: 'CN'})
    with pytest.raises(ValidationError, match='Properties must not all be present'):
        model.model_validate({'interventionSubLocation': 'CN', 'intervensionSubLocation': 'CN'})
