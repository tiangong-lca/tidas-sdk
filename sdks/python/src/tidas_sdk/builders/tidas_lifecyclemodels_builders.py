# Auto-generated builder classes for TIDAS entities
# DO NOT EDIT - Regenerate using scripts/generate_builders.py

from __future__ import annotations

from typing import List, Literal, Optional
from pydantic import AnyUrl, AwareDatetime, BaseModel, ConfigDict, Field, RootModel
from enum import (
    Enum,
)
from tidas_sdk.types.tidas_processes_category import (
    Processes,
    TidasProcessesText,
)
from tidas_sdk.types.tidas_data_types import (
    CASNumber,
    FT,
    FTMultiLang,
    GIS,
    GlobalReferenceType,
    GlobalReferenceTypeOrArray,
    Int1,
    Int5,
    Int6,
    LevelType,
    MatR,
    MatV,
    MultiLangItem,
    MultiLangItemST,
    MultiLangItemString,
    Perc,
    Real,
    ST,
    STMultiLang,
    String,
    StringMultiLang,
    UUID,
    Year,
)

from tidas_sdk.types.tidas_lifecyclemodels import (
    AdministrativeInformation,
    ClassificationInformation,
    CommonClas,
    CommonClas1,
    CommonClas2,
    CommonClas3,
    CommonClassification,
    CommonCommissionerAndGoal,
    Compliance,
    Compliance1,
    Compliance1Item,
    ComplianceDeclarations,
    Connections,
    Connections1,
    DataEntryBy,
    DataGenerator,
    DataSetInformation,
    DataSourcesTreatmentEtc,
    DownstreamProces,
    DownstreamProcess,
    Group,
    GroupDeclarations,
    GroupItem,
    Groups,
    LifeCycleModelDataSet,
    LifeCycleModelInformation,
    MemberOf,
    MemberOfItem,
    Model,
    ModellingAndValidation,
    Name,
    OutputExchange,
    OutputExchange1,
    OutputExchangeItem,
    OutputExchangeItem1,
    Parameter,
    Parameter1,
    ParameterItem,
    ParameterItem1,
    Parameters,
    Parameters1,
    ProcessInstance,
    ProcessInstanceItem,
    Processes,
    PublicationAndOwnership,
    QuantitativeReference,
    Review,
    ReviewItem,
    Technology,
    Validation,
)


class DownstreamProcessBuilder(BaseModel):
    """Process instance that is connected downstream with this process instance, with its connected input product or waste (flow) exchange internal ID, the flow UUID and optionally the exchange's "location" (if any). Finally, the dominant flow exchange may be identified, where two different flow data sets are connected, in support e.g. of graphical model display. (Builder)"""

    field_id: Optional[str] = Field(None, alias='@id')
    field_flowUUID: Optional[str] = Field(None, alias='@flowUUID')
    field_location: Optional[str] = Field(None, alias='@location')
    field_dominant: Optional[FieldDominant] = Field(None, alias='@dominant')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> DownstreamProcess:
        """Build the final DownstreamProcess instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return DownstreamProcess.model_validate(data)

class DownstreamProcesBuilder(BaseModel):
    """Builder for DownstreamProces."""

    field_id: Optional[str] = Field(None, alias='@id')
    field_flowUUID: Optional[str] = Field(None, alias='@flowUUID')
    field_location: Optional[str] = Field(None, alias='@location')
    field_dominant: Optional[FieldDominant] = Field(None, alias='@dominant')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> DownstreamProces:
        """Build the final DownstreamProces instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return DownstreamProces.model_validate(data)

class OutputExchangeItemBuilder(BaseModel):
    """Builder for OutputExchangeItem."""

    field_dominant: Optional[FieldDominant] = Field(None, alias='@dominant')
    field_flowUUID: Optional[str] = Field(None, alias='@flowUUID')
    downstreamProcess: Optional[DownstreamProcess1 | list[DownstreamProces1]] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> OutputExchangeItem:
        """Build the final OutputExchangeItem instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return OutputExchangeItem.model_validate(data)

class OutputExchangeBuilder(BaseModel):
    """Reference to process data set UUID of one of the connecting output product or waste flow exchanges of this process instance. I.e. which (flow) exchange on output side of this process instance is to be connected to another process instance's input product or waste (flow) exchange? (Builder)"""

    field_dominant: Optional[FieldDominant] = Field(None, alias='@dominant')
    field_flowUUID: Optional[str] = Field(None, alias='@flowUUID')
    _downstreamProcess: Optional[DownstreamProcessBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def downstreamProcess(self) -> DownstreamProcessBuilder:
        """Access downstreamProcess builder (auto-initialized)."""
        if self._downstreamProcess is None:
            self._downstreamProcess = DownstreamProcessBuilder()
        return self._downstreamProcess

    def build(self) -> OutputExchange:
        """Build the final OutputExchange instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_downstreamProcess', None)

        # Build nested objects
        if self._downstreamProcess is not None:
            data['downstreamProcess'] = self._downstreamProcess.build()

        return OutputExchange.model_validate(data)

class ConnectionsBuilder(BaseModel):
    """Connection information among process instances, via connecting product or waste flow exchanges. (Builder)"""

    _outputExchange: Optional[OutputExchangeBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def outputExchange(self) -> OutputExchangeBuilder:
        """Access outputExchange builder (auto-initialized)."""
        if self._outputExchange is None:
            self._outputExchange = OutputExchangeBuilder()
        return self._outputExchange

    def build(self) -> Connections:
        """Build the final Connections instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_outputExchange', None)

        # Build nested objects
        if self._outputExchange is not None:
            data['outputExchange'] = self._outputExchange.build()

        return Connections.model_validate(data)

class GroupBuilder(BaseModel):
    """Definition for each group. (Builder)"""

    field_id: Optional[str] = Field(None, alias='@id')
    groupName: Optional[StringMultiLang] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def set_groupName(self, text: str, lang: str = 'en') -> 'GroupBuilder':
        """Set groupName text for a specific language."""
        if self.groupName is None:
            self.groupName = StringMultiLang()

        # Update existing or add new
        for item in self.groupName.items:
            if item.lang == lang:
                item.text = text
                return self

        self.groupName.items.append(MultiLangItemString(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_groupName(self, lang: str = 'en') -> Optional[str]:
        """Get groupName text for a specific language."""
        if not self.groupName:
            return None
        for item in self.groupName.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> Group:
        """Build the final Group instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return Group.model_validate(data)

class MemberOfBuilder(BaseModel):
    """Refers to one user-definable group, to which this process instance belongs. (Builder)"""

    field_groupId: Optional[str] = Field(None, alias='@groupId')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> MemberOf:
        """Build the final MemberOf instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return MemberOf.model_validate(data)

class MemberOfItemBuilder(BaseModel):
    """Builder for MemberOfItem."""

    field_groupId: Optional[str] = Field(None, alias='@groupId')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> MemberOfItem:
        """Build the final MemberOfItem instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return MemberOfItem.model_validate(data)

class GroupsBuilder(BaseModel):
    """Group(s) to which this process instance belongs. (Builder)"""

    _memberOf: Optional[MemberOfBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def memberOf(self) -> MemberOfBuilder:
        """Access memberOf builder (auto-initialized)."""
        if self._memberOf is None:
            self._memberOf = MemberOfBuilder()
        return self._memberOf

    def build(self) -> Groups:
        """Build the final Groups instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_memberOf', None)

        # Build nested objects
        if self._memberOf is not None:
            data['memberOf'] = self._memberOf.build()

        return Groups.model_validate(data)

class ParameterBuilder(BaseModel):
    """Value of the parameter. (Builder)"""

    field_name: Optional[str] = Field(None, alias='@name')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> Parameter:
        """Build the final Parameter instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return Parameter.model_validate(data)

class ParameterItemBuilder(BaseModel):
    """Builder for ParameterItem."""

    field_name: Optional[str] = Field(None, alias='@name')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> ParameterItem:
        """Build the final ParameterItem instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return ParameterItem.model_validate(data)

class ParametersBuilder(BaseModel):
    """Set of parameters of this process instance with parameter values (changed or unchanged from those in the underlying process data set). (Builder)"""

    _parameter: Optional[ParameterBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def parameter(self) -> ParameterBuilder:
        """Access parameter builder (auto-initialized)."""
        if self._parameter is None:
            self._parameter = ParameterBuilder()
        return self._parameter

    def build(self) -> Parameters:
        """Build the final Parameters instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_parameter', None)

        # Build nested objects
        if self._parameter is not None:
            data['parameter'] = self._parameter.build()

        return Parameters.model_validate(data)

class ProcessInstanceItemBuilder(BaseModel):
    """Builder for ProcessInstanceItem."""

    field_dataSetInternalID: Optional[str] = Field(None, alias='@dataSetInternalID')
    field_multiplicationFactor: Optional[str] = Field(None, alias='@multiplicationFactor')
    referenceToProcess: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None
    scalingFactors: Optional[str] = None
    common_other: Optional[str] = Field(None, alias='common:other')
    _groups: Optional[GroupsBuilder] = None
    _parameters: Optional[ParametersBuilder] = None
    _connections: Optional[ConnectionsBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def groups(self) -> GroupsBuilder:
        """Access groups builder (auto-initialized)."""
        if self._groups is None:
            self._groups = GroupsBuilder()
        return self._groups

    @property
    def parameters(self) -> ParametersBuilder:
        """Access parameters builder (auto-initialized)."""
        if self._parameters is None:
            self._parameters = ParametersBuilder()
        return self._parameters

    @property
    def connections(self) -> ConnectionsBuilder:
        """Access connections builder (auto-initialized)."""
        if self._connections is None:
            self._connections = ConnectionsBuilder()
        return self._connections

    def build(self) -> ProcessInstanceItem:
        """Build the final ProcessInstanceItem instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_groups', None)
        data.pop('_parameters', None)
        data.pop('_connections', None)

        # Build nested objects
        if self._groups is not None:
            data['groups'] = self._groups.build()
        if self._parameters is not None:
            data['parameters'] = self._parameters.build()
        if self._connections is not None:
            data['connections'] = self._connections.build()

        return ProcessInstanceItem.model_validate(data)

class OutputExchange1Builder(BaseModel):
    """Reference to process data set UUID of one of the connecting output product or waste flow exchanges of this process instance. I.e. which (flow) exchange on output side of this process instance is to be connected to another process instance's input product or waste (flow) exchange? (Builder)"""

    field_dominant: Optional[FieldDominant] = Field(None, alias='@dominant')
    field_flowUUID: Optional[str] = Field(None, alias='@flowUUID')
    downstreamProcess: Optional[DownstreamProcess2 | list[DownstreamProces2]] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> OutputExchange1:
        """Build the final OutputExchange1 instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return OutputExchange1.model_validate(data)

class OutputExchangeItem1Builder(BaseModel):
    """Builder for OutputExchangeItem1."""

    field_dominant: Optional[FieldDominant] = Field(None, alias='@dominant')
    field_flowUUID: Optional[str] = Field(None, alias='@flowUUID')
    downstreamProcess: Optional[DownstreamProcess3 | list[DownstreamProces3]] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> OutputExchangeItem1:
        """Build the final OutputExchangeItem1 instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return OutputExchangeItem1.model_validate(data)

class Connections1Builder(BaseModel):
    """Connection information among process instances, via connecting product or waste flow exchanges. (Builder)"""

    _outputExchange: Optional[OutputExchange1Builder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def outputExchange(self) -> OutputExchange1Builder:
        """Access outputExchange builder (auto-initialized)."""
        if self._outputExchange is None:
            self._outputExchange = OutputExchange1Builder()
        return self._outputExchange

    def build(self) -> Connections1:
        """Build the final Connections1 instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_outputExchange', None)

        # Build nested objects
        if self._outputExchange is not None:
            data['outputExchange'] = self._outputExchange.build()

        return Connections1.model_validate(data)

class ParameterItem1Builder(BaseModel):
    """Builder for ParameterItem1."""

    field_name: Optional[str] = Field(None, alias='@name')
    parameter: Optional[str] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> ParameterItem1:
        """Build the final ParameterItem1 instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return ParameterItem1.model_validate(data)

class Parameter1Builder(BaseModel):
    """Value of the parameter. (Builder)"""

    field_name: Optional[str] = Field(None, alias='@name')
    parameter: Optional[str] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> Parameter1:
        """Build the final Parameter1 instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return Parameter1.model_validate(data)

class Parameters1Builder(BaseModel):
    """Set of parameters of this process instance with parameter values (changed or unchanged from those in the underlying process data set). (Builder)"""

    _parameter: Optional[Parameter1Builder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def parameter(self) -> Parameter1Builder:
        """Access parameter builder (auto-initialized)."""
        if self._parameter is None:
            self._parameter = Parameter1Builder()
        return self._parameter

    def build(self) -> Parameters1:
        """Build the final Parameters1 instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_parameter', None)

        # Build nested objects
        if self._parameter is not None:
            data['parameter'] = self._parameter.build()

        return Parameters1.model_validate(data)

class ProcessInstanceBuilder(BaseModel):
    """Instances (occurrences) of the same process data set in this life cycle model. Each process data set may occur in different places within the model, with different parameter settings and connected to different other process instances. (Builder)"""

    field_dataSetInternalID: Optional[str] = Field(None, alias='@dataSetInternalID')
    field_multiplicationFactor: Optional[str] = Field(None, alias='@multiplicationFactor')
    referenceToProcess: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None
    scalingFactors: Optional[str] = None
    groups: Optional[Groups1] = None
    common_other: Optional[str] = Field(None, alias='common:other')
    _parameters: Optional[Parameters1Builder] = None
    _connections: Optional[Connections1Builder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def parameters(self) -> Parameters1Builder:
        """Access parameters builder (auto-initialized)."""
        if self._parameters is None:
            self._parameters = Parameters1Builder()
        return self._parameters

    @property
    def connections(self) -> Connections1Builder:
        """Access connections builder (auto-initialized)."""
        if self._connections is None:
            self._connections = Connections1Builder()
        return self._connections

    def build(self) -> ProcessInstance:
        """Build the final ProcessInstance instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_parameters', None)
        data.pop('_connections', None)

        # Build nested objects
        if self._parameters is not None:
            data['parameters'] = self._parameters.build()
        if self._connections is not None:
            data['connections'] = self._connections.build()

        return ProcessInstance.model_validate(data)

class ProcessesBuilder(BaseModel):
    """"Process data set(s)" included in this life cycle model as separate data set(s). (Builder)"""

    _processInstance: List[ProcessInstanceItemBuilder] = []

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def processInstance(self) -> List[ProcessInstanceItemBuilder]:
        """Access processInstance builder list."""
        return self._processInstance

    def add_processInstance(self) -> ProcessInstanceItemBuilder:
        """Add and return a new ProcessInstanceItem builder."""
        builder = ProcessInstanceItemBuilder()
        self._processInstance.append(builder)
        return builder

    def build(self) -> Processes:
        """Build the final Processes instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_processInstance', None)

        # Build array fields
        if self._processInstance:
            data['processInstance'] = [item.build() for item in self._processInstance]

        return Processes.model_validate(data)

class CommonClasBuilder(BaseModel):
    """Builder for CommonClas."""

    field_level: Optional[Literal['0']] = Field(None, alias='@level')
    text: Optional[TidasProcessesText] = Field(None, alias='#text')
    _field_classId: Optional[ProcessesBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def field_classId(self) -> ProcessesBuilder:
        """Access field_classId builder (auto-initialized)."""
        if self._field_classId is None:
            self._field_classId = ProcessesBuilder()
        return self._field_classId

    def build(self) -> CommonClas:
        """Build the final CommonClas instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_field_classId', None)

        # Build nested objects
        if self._field_classId is not None:
            data['@classId'] = self._field_classId.build()

        return CommonClas.model_validate(data)

class CommonClas1Builder(BaseModel):
    """Builder for CommonClas1."""

    field_level: Optional[Literal['1']] = Field(None, alias='@level')
    text: Optional[TidasProcessesText] = Field(None, alias='#text')
    _field_classId: Optional[ProcessesBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def field_classId(self) -> ProcessesBuilder:
        """Access field_classId builder (auto-initialized)."""
        if self._field_classId is None:
            self._field_classId = ProcessesBuilder()
        return self._field_classId

    def build(self) -> CommonClas1:
        """Build the final CommonClas1 instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_field_classId', None)

        # Build nested objects
        if self._field_classId is not None:
            data['@classId'] = self._field_classId.build()

        return CommonClas1.model_validate(data)

class CommonClas2Builder(BaseModel):
    """Builder for CommonClas2."""

    field_level: Optional[Literal['2']] = Field(None, alias='@level')
    text: Optional[TidasProcessesText] = Field(None, alias='#text')
    _field_classId: Optional[ProcessesBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def field_classId(self) -> ProcessesBuilder:
        """Access field_classId builder (auto-initialized)."""
        if self._field_classId is None:
            self._field_classId = ProcessesBuilder()
        return self._field_classId

    def build(self) -> CommonClas2:
        """Build the final CommonClas2 instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_field_classId', None)

        # Build nested objects
        if self._field_classId is not None:
            data['@classId'] = self._field_classId.build()

        return CommonClas2.model_validate(data)

class CommonClas3Builder(BaseModel):
    """Builder for CommonClas3."""

    field_level: Optional[Literal['3']] = Field(None, alias='@level')
    text: Optional[TidasProcessesText] = Field(None, alias='#text')
    _field_classId: Optional[ProcessesBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def field_classId(self) -> ProcessesBuilder:
        """Access field_classId builder (auto-initialized)."""
        if self._field_classId is None:
            self._field_classId = ProcessesBuilder()
        return self._field_classId

    def build(self) -> CommonClas3:
        """Build the final CommonClas3 instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_field_classId', None)

        # Build nested objects
        if self._field_classId is not None:
            data['@classId'] = self._field_classId.build()

        return CommonClas3.model_validate(data)

class CommonClassificationBuilder(BaseModel):
    """Optional statistical or other classification of the data set. Typically also used for structuring LCA databases. (Builder)"""

    common_other: Optional[str] = Field(None, alias='common:other')
    _common_class: List[CommonClas | CommonClas1 | CommonClas2 | CommonClas3Builder] = []

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def common_class(self) -> List[CommonClas | CommonClas1 | CommonClas2 | CommonClas3Builder]:
        """Access common_class builder list."""
        return self._common_class

    def add_common_cla(self) -> CommonClas | CommonClas1 | CommonClas2 | CommonClas3Builder:
        """Add and return a new CommonClas | CommonClas1 | CommonClas2 | CommonClas3 builder."""
        builder = CommonClas | CommonClas1 | CommonClas2 | CommonClas3Builder()
        self._common_class.append(builder)
        return builder

    def build(self) -> CommonClassification:
        """Build the final CommonClassification instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_common_class', None)

        # Build array fields
        if self._common_class:
            data['common:class'] = [item.build() for item in self._common_class]

        return CommonClassification.model_validate(data)

class ClassificationInformationBuilder(BaseModel):
    """Hierarchical or flat classification of the good, service or function that is provided by this life cycle model; typically used to structure database contents in LCA software, among other purposes. (Note: This entry is NOT required for the identification of a Life cycle model, but it should nevertheless be avoided to use identical names for Life cycle model data sets in the same class. The ILCD classifications are defined in the ILCDClassifications.xml file, for common use.) (Builder)"""

    _common_classification: Optional[CommonClassificationBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def common_classification(self) -> CommonClassificationBuilder:
        """Access common_classification builder (auto-initialized)."""
        if self._common_classification is None:
            self._common_classification = CommonClassificationBuilder()
        return self._common_classification

    def build(self) -> ClassificationInformation:
        """Build the final ClassificationInformation instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_common_classification', None)

        # Build nested objects
        if self._common_classification is not None:
            data['common:classification'] = self._common_classification.build()

        return ClassificationInformation.model_validate(data)

class QuantitativeReferenceBuilder(BaseModel):
    """This section names the quantitative reference of this data set, i.e. the reference to which the inputs and outputs of all process instances of the life cycle model quantitatively relate. (Builder)"""

    referenceToReferenceProcess: Optional[str] = None
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> QuantitativeReference:
        """Build the final QuantitativeReference instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return QuantitativeReference.model_validate(data)

class NameBuilder(BaseModel):
    """General descriptive, specifying, structured name of the Life cycle model data set. Note: Ensure proper name structuring and observe restriction to 100 characters for each of the four name fields. (Builder)"""

    baseName: Optional[StringMultiLang] = None
    treatmentStandardsRoutes: Optional[StringMultiLang] = None
    mixAndLocationTypes: Optional[StringMultiLang] = None
    functionalUnitFlowProperties: Optional[StringMultiLang] = None
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def set_baseName(self, text: str, lang: str = 'en') -> 'NameBuilder':
        """Set baseName text for a specific language."""
        if self.baseName is None:
            self.baseName = StringMultiLang()

        # Update existing or add new
        for item in self.baseName.items:
            if item.lang == lang:
                item.text = text
                return self

        self.baseName.items.append(MultiLangItemString(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_baseName(self, lang: str = 'en') -> Optional[str]:
        """Get baseName text for a specific language."""
        if not self.baseName:
            return None
        for item in self.baseName.items:
            if item.lang == lang:
                return item.text
        return None

    def set_treatmentStandardsRoutes(self, text: str, lang: str = 'en') -> 'NameBuilder':
        """Set treatmentStandardsRoutes text for a specific language."""
        if self.treatmentStandardsRoutes is None:
            self.treatmentStandardsRoutes = StringMultiLang()

        # Update existing or add new
        for item in self.treatmentStandardsRoutes.items:
            if item.lang == lang:
                item.text = text
                return self

        self.treatmentStandardsRoutes.items.append(MultiLangItemString(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_treatmentStandardsRoutes(self, lang: str = 'en') -> Optional[str]:
        """Get treatmentStandardsRoutes text for a specific language."""
        if not self.treatmentStandardsRoutes:
            return None
        for item in self.treatmentStandardsRoutes.items:
            if item.lang == lang:
                return item.text
        return None

    def set_mixAndLocationTypes(self, text: str, lang: str = 'en') -> 'NameBuilder':
        """Set mixAndLocationTypes text for a specific language."""
        if self.mixAndLocationTypes is None:
            self.mixAndLocationTypes = StringMultiLang()

        # Update existing or add new
        for item in self.mixAndLocationTypes.items:
            if item.lang == lang:
                item.text = text
                return self

        self.mixAndLocationTypes.items.append(MultiLangItemString(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_mixAndLocationTypes(self, lang: str = 'en') -> Optional[str]:
        """Get mixAndLocationTypes text for a specific language."""
        if not self.mixAndLocationTypes:
            return None
        for item in self.mixAndLocationTypes.items:
            if item.lang == lang:
                return item.text
        return None

    def set_functionalUnitFlowProperties(self, text: str, lang: str = 'en') -> 'NameBuilder':
        """Set functionalUnitFlowProperties text for a specific language."""
        if self.functionalUnitFlowProperties is None:
            self.functionalUnitFlowProperties = StringMultiLang()

        # Update existing or add new
        for item in self.functionalUnitFlowProperties.items:
            if item.lang == lang:
                item.text = text
                return self

        self.functionalUnitFlowProperties.items.append(MultiLangItemString(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_functionalUnitFlowProperties(self, lang: str = 'en') -> Optional[str]:
        """Get functionalUnitFlowProperties text for a specific language."""
        if not self.functionalUnitFlowProperties:
            return None
        for item in self.functionalUnitFlowProperties.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> Name:
        """Build the final Name instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return Name.model_validate(data)

class DataSetInformationBuilder(BaseModel):
    """General data set information, to identify the life cycle model, document a general comment about it, and to reference resulting aggregated process data sets that are based on this ife cycle model and to reference a potential background report. (Builder)"""

    common_UUID: Optional[str] = Field(None, alias='common:UUID')
    referenceToResultingProcess: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None
    common_generalComment: Optional[FTMultiLang] = Field(None, alias='common:generalComment')
    referenceToExternalDocumentation: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None
    common_other: Optional[str] = Field(None, alias='common:other')
    _name: Optional[NameBuilder] = None
    _classificationInformation: Optional[ClassificationInformationBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def name(self) -> NameBuilder:
        """Access name builder (auto-initialized)."""
        if self._name is None:
            self._name = NameBuilder()
        return self._name

    @property
    def classificationInformation(self) -> ClassificationInformationBuilder:
        """Access classificationInformation builder (auto-initialized)."""
        if self._classificationInformation is None:
            self._classificationInformation = ClassificationInformationBuilder()
        return self._classificationInformation

    def set_generalComment(self, text: str, lang: str = 'en') -> 'DataSetInformationBuilder':
        """Set common_generalComment text for a specific language."""
        if self.common_generalComment is None:
            self.common_generalComment = FTMultiLang()

        # Update existing or add new
        for item in self.common_generalComment.items:
            if item.lang == lang:
                item.text = text
                return self

        self.common_generalComment.items.append(MultiLangItemFT(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_generalComment(self, lang: str = 'en') -> Optional[str]:
        """Get common_generalComment text for a specific language."""
        if not self.common_generalComment:
            return None
        for item in self.common_generalComment.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> DataSetInformation:
        """Build the final DataSetInformation instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_name', None)
        data.pop('_classificationInformation', None)

        # Build nested objects
        if self._name is not None:
            data['name'] = self._name.build()
        if self._classificationInformation is not None:
            data['classificationInformation'] = self._classificationInformation.build()

        return DataSetInformation.model_validate(data)

class GroupItemBuilder(BaseModel):
    """Builder for GroupItem."""

    field_id: Optional[str] = Field(None, alias='@id')
    groupName: Optional[StringMultiLang] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def set_groupName(self, text: str, lang: str = 'en') -> 'GroupItemBuilder':
        """Set groupName text for a specific language."""
        if self.groupName is None:
            self.groupName = StringMultiLang()

        # Update existing or add new
        for item in self.groupName.items:
            if item.lang == lang:
                item.text = text
                return self

        self.groupName.items.append(MultiLangItemString(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_groupName(self, lang: str = 'en') -> Optional[str]:
        """Get groupName text for a specific language."""
        if not self.groupName:
            return None
        for item in self.groupName.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> GroupItem:
        """Build the final GroupItem instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return GroupItem.model_validate(data)

class GroupDeclarationsBuilder(BaseModel):
    """Section to define groups to which process instances can declare to belong to, in the context of this Life cycle model data set. Groups are user-defined and could be e.g. life cycle stages, foreground/background, ... (Builder)"""

    _group: Optional[GroupBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def group(self) -> GroupBuilder:
        """Access group builder (auto-initialized)."""
        if self._group is None:
            self._group = GroupBuilder()
        return self._group

    def build(self) -> GroupDeclarations:
        """Build the final GroupDeclarations instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_group', None)

        # Build nested objects
        if self._group is not None:
            data['group'] = self._group.build()

        return GroupDeclarations.model_validate(data)

class TechnologyBuilder(BaseModel):
    """Provides information about the technological representativeness of the data set. (Builder)"""

    referenceToDiagram: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None
    common_other: Optional[str] = Field(None, alias='common:other')
    _groupDeclarations: Optional[GroupDeclarationsBuilder] = None
    _processes: Optional[ProcessesBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def groupDeclarations(self) -> GroupDeclarationsBuilder:
        """Access groupDeclarations builder (auto-initialized)."""
        if self._groupDeclarations is None:
            self._groupDeclarations = GroupDeclarationsBuilder()
        return self._groupDeclarations

    @property
    def processes(self) -> ProcessesBuilder:
        """Access processes builder (auto-initialized)."""
        if self._processes is None:
            self._processes = ProcessesBuilder()
        return self._processes

    def build(self) -> Technology:
        """Build the final Technology instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_groupDeclarations', None)
        data.pop('_processes', None)

        # Build nested objects
        if self._groupDeclarations is not None:
            data['groupDeclarations'] = self._groupDeclarations.build()
        if self._processes is not None:
            data['processes'] = self._processes.build()

        return Technology.model_validate(data)

class LifeCycleModelInformationBuilder(BaseModel):
    """This section comprises the following sub-sections: 1) "Key data set information", 2) "Quantitative reference", 3) "Technology". (Builder)"""

    _dataSetInformation: Optional[DataSetInformationBuilder] = None
    _quantitativeReference: Optional[QuantitativeReferenceBuilder] = None
    _technology: Optional[TechnologyBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def dataSetInformation(self) -> DataSetInformationBuilder:
        """Access dataSetInformation builder (auto-initialized)."""
        if self._dataSetInformation is None:
            self._dataSetInformation = DataSetInformationBuilder()
        return self._dataSetInformation

    @property
    def quantitativeReference(self) -> QuantitativeReferenceBuilder:
        """Access quantitativeReference builder (auto-initialized)."""
        if self._quantitativeReference is None:
            self._quantitativeReference = QuantitativeReferenceBuilder()
        return self._quantitativeReference

    @property
    def technology(self) -> TechnologyBuilder:
        """Access technology builder (auto-initialized)."""
        if self._technology is None:
            self._technology = TechnologyBuilder()
        return self._technology

    def build(self) -> LifeCycleModelInformation:
        """Build the final LifeCycleModelInformation instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_dataSetInformation', None)
        data.pop('_quantitativeReference', None)
        data.pop('_technology', None)

        # Build nested objects
        if self._dataSetInformation is not None:
            data['dataSetInformation'] = self._dataSetInformation.build()
        if self._quantitativeReference is not None:
            data['quantitativeReference'] = self._quantitativeReference.build()
        if self._technology is not None:
            data['technology'] = self._technology.build()

        return LifeCycleModelInformation.model_validate(data)

class DataSourcesTreatmentEtcBuilder(BaseModel):
    """Data selection, completeness, and treatment principles and procedures, data sources and market coverage information. (Builder)"""

    useAdviceForDataSet: Optional[FTMultiLang] = None
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def set_useAdviceForDataSet(self, text: str, lang: str = 'en') -> 'DataSourcesTreatmentEtcBuilder':
        """Set useAdviceForDataSet text for a specific language."""
        if self.useAdviceForDataSet is None:
            self.useAdviceForDataSet = FTMultiLang()

        # Update existing or add new
        for item in self.useAdviceForDataSet.items:
            if item.lang == lang:
                item.text = text
                return self

        self.useAdviceForDataSet.items.append(MultiLangItemFT(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_useAdviceForDataSet(self, lang: str = 'en') -> Optional[str]:
        """Get useAdviceForDataSet text for a specific language."""
        if not self.useAdviceForDataSet:
            return None
        for item in self.useAdviceForDataSet.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> DataSourcesTreatmentEtc:
        """Build the final DataSourcesTreatmentEtc instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return DataSourcesTreatmentEtc.model_validate(data)

class ReviewBuilder(BaseModel):
    """Review information on this life cycle model data set (Builder)"""

    common_referenceToNameOfReviewerAndInstitution: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToNameOfReviewerAndInstitution')
    common_otherReviewDetails: Optional[FTMultiLang] = Field(None, alias='common:otherReviewDetails')
    common_referenceToCompleteReviewReport: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToCompleteReviewReport')
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def set_otherReviewDetails(self, text: str, lang: str = 'en') -> 'ReviewBuilder':
        """Set common_otherReviewDetails text for a specific language."""
        if self.common_otherReviewDetails is None:
            self.common_otherReviewDetails = FTMultiLang()

        # Update existing or add new
        for item in self.common_otherReviewDetails.items:
            if item.lang == lang:
                item.text = text
                return self

        self.common_otherReviewDetails.items.append(MultiLangItemFT(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_otherReviewDetails(self, lang: str = 'en') -> Optional[str]:
        """Get common_otherReviewDetails text for a specific language."""
        if not self.common_otherReviewDetails:
            return None
        for item in self.common_otherReviewDetails.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> Review:
        """Build the final Review instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return Review.model_validate(data)

class ReviewItemBuilder(BaseModel):
    """Builder for ReviewItem."""

    common_referenceToNameOfReviewerAndInstitution: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToNameOfReviewerAndInstitution')
    common_otherReviewDetails: Optional[FTMultiLang] = Field(None, alias='common:otherReviewDetails')
    common_referenceToCompleteReviewReport: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToCompleteReviewReport')
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def set_otherReviewDetails(self, text: str, lang: str = 'en') -> 'ReviewItemBuilder':
        """Set common_otherReviewDetails text for a specific language."""
        if self.common_otherReviewDetails is None:
            self.common_otherReviewDetails = FTMultiLang()

        # Update existing or add new
        for item in self.common_otherReviewDetails.items:
            if item.lang == lang:
                item.text = text
                return self

        self.common_otherReviewDetails.items.append(MultiLangItemFT(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_otherReviewDetails(self, lang: str = 'en') -> Optional[str]:
        """Get common_otherReviewDetails text for a specific language."""
        if not self.common_otherReviewDetails:
            return None
        for item in self.common_otherReviewDetails.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> ReviewItem:
        """Build the final ReviewItem instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return ReviewItem.model_validate(data)

class ValidationBuilder(BaseModel):
    """Review / validation information on data set. (Builder)"""

    common_other: Optional[str] = Field(None, alias='common:other')
    _review: Optional[ReviewBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def review(self) -> ReviewBuilder:
        """Access review builder (auto-initialized)."""
        if self._review is None:
            self._review = ReviewBuilder()
        return self._review

    def build(self) -> Validation:
        """Build the final Validation instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_review', None)

        # Build nested objects
        if self._review is not None:
            data['review'] = self._review.build()

        return Validation.model_validate(data)

class ComplianceBuilder(BaseModel):
    """One compliance declaration. Multiple declarations may be provided. (Builder)"""

    common_referenceToComplianceSystem: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToComplianceSystem')
    common_approvalOfOverallCompliance: Optional[CommonApprovalOfOverallCompliance] = Field(None, alias='common:approvalOfOverallCompliance')
    common_nomenclatureCompliance: Optional[CommonNomenclatureCompliance] = Field(None, alias='common:nomenclatureCompliance')
    common_methodologicalCompliance: Optional[CommonMethodologicalCompliance] = Field(None, alias='common:methodologicalCompliance')
    common_reviewCompliance: Optional[CommonReviewCompliance] = Field(None, alias='common:reviewCompliance')
    common_documentationCompliance: Optional[CommonDocumentationCompliance] = Field(None, alias='common:documentationCompliance')
    common_qualityCompliance: Optional[CommonQualityCompliance] = Field(None, alias='common:qualityCompliance')
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> Compliance:
        """Build the final Compliance instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return Compliance.model_validate(data)

class Compliance1ItemBuilder(BaseModel):
    """Builder for Compliance1Item."""

    common_referenceToComplianceSystem: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToComplianceSystem')
    common_approvalOfOverallCompliance: Optional[CommonApprovalOfOverallCompliance] = Field(None, alias='common:approvalOfOverallCompliance')
    common_nomenclatureCompliance: Optional[CommonNomenclatureCompliance] = Field(None, alias='common:nomenclatureCompliance')
    common_methodologicalCompliance: Optional[CommonMethodologicalCompliance] = Field(None, alias='common:methodologicalCompliance')
    common_reviewCompliance: Optional[CommonReviewCompliance] = Field(None, alias='common:reviewCompliance')
    common_documentationCompliance: Optional[CommonDocumentationCompliance] = Field(None, alias='common:documentationCompliance')
    common_qualityCompliance: Optional[CommonQualityCompliance] = Field(None, alias='common:qualityCompliance')
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> Compliance1Item:
        """Build the final Compliance1Item instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return Compliance1Item.model_validate(data)

class Compliance1Builder(BaseModel):
    """Builder for Compliance1."""

    _root: List[Compliance1ItemBuilder] = []

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def root(self) -> List[Compliance1ItemBuilder]:
        """Access root builder list."""
        return self._root

    def add_root(self) -> Compliance1ItemBuilder:
        """Add and return a new Compliance1Item builder."""
        builder = Compliance1ItemBuilder()
        self._root.append(builder)
        return builder

    def build(self) -> Compliance1:
        """Build the final Compliance1 instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_root', None)

        # Build array fields
        if self._root:
            data['root'] = [item.build() for item in self._root]

        return Compliance1.model_validate(data)

class ComplianceDeclarationsBuilder(BaseModel):
    """One or more declarations of compliance to selected standards, schemes and other references, e.g. ISO 14040, ISO 14044, ILCD, EF, EN 15804, ... (Builder)"""

    common_other: Optional[str] = Field(None, alias='common:other')
    _compliance: Optional[ComplianceBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def compliance(self) -> ComplianceBuilder:
        """Access compliance builder (auto-initialized)."""
        if self._compliance is None:
            self._compliance = ComplianceBuilder()
        return self._compliance

    def build(self) -> ComplianceDeclarations:
        """Build the final ComplianceDeclarations instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_compliance', None)

        # Build nested objects
        if self._compliance is not None:
            data['compliance'] = self._compliance.build()

        return ComplianceDeclarations.model_validate(data)

class ModellingAndValidationBuilder(BaseModel):
    """This section covers the following sub-sections: 1) "Data sources, treatment and representativeness", 2) "Validation", and 3) "Compliance". (Builder)"""

    common_other: Optional[str] = Field(None, alias='common:other')
    _dataSourcesTreatmentEtc: Optional[DataSourcesTreatmentEtcBuilder] = None
    _validation: Optional[ValidationBuilder] = None
    _complianceDeclarations: Optional[ComplianceDeclarationsBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def dataSourcesTreatmentEtc(self) -> DataSourcesTreatmentEtcBuilder:
        """Access dataSourcesTreatmentEtc builder (auto-initialized)."""
        if self._dataSourcesTreatmentEtc is None:
            self._dataSourcesTreatmentEtc = DataSourcesTreatmentEtcBuilder()
        return self._dataSourcesTreatmentEtc

    @property
    def validation(self) -> ValidationBuilder:
        """Access validation builder (auto-initialized)."""
        if self._validation is None:
            self._validation = ValidationBuilder()
        return self._validation

    @property
    def complianceDeclarations(self) -> ComplianceDeclarationsBuilder:
        """Access complianceDeclarations builder (auto-initialized)."""
        if self._complianceDeclarations is None:
            self._complianceDeclarations = ComplianceDeclarationsBuilder()
        return self._complianceDeclarations

    def build(self) -> ModellingAndValidation:
        """Build the final ModellingAndValidation instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_dataSourcesTreatmentEtc', None)
        data.pop('_validation', None)
        data.pop('_complianceDeclarations', None)

        # Build nested objects
        if self._dataSourcesTreatmentEtc is not None:
            data['dataSourcesTreatmentEtc'] = self._dataSourcesTreatmentEtc.build()
        if self._validation is not None:
            data['validation'] = self._validation.build()
        if self._complianceDeclarations is not None:
            data['complianceDeclarations'] = self._complianceDeclarations.build()

        return ModellingAndValidation.model_validate(data)

class CommonCommissionerAndGoalBuilder(BaseModel):
    """Extract of the information items linked to goal and scope of LCIA method modeling. (Builder)"""

    common_referenceToCommissioner: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToCommissioner')
    common_project: Optional[StringMultiLang] = Field(None, alias='common:project')
    common_intendedApplications: Optional[FTMultiLang] = Field(None, alias='common:intendedApplications')
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def set_project(self, text: str, lang: str = 'en') -> 'CommonCommissionerAndGoalBuilder':
        """Set common_project text for a specific language."""
        if self.common_project is None:
            self.common_project = StringMultiLang()

        # Update existing or add new
        for item in self.common_project.items:
            if item.lang == lang:
                item.text = text
                return self

        self.common_project.items.append(MultiLangItemString(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_project(self, lang: str = 'en') -> Optional[str]:
        """Get common_project text for a specific language."""
        if not self.common_project:
            return None
        for item in self.common_project.items:
            if item.lang == lang:
                return item.text
        return None

    def set_intendedApplications(self, text: str, lang: str = 'en') -> 'CommonCommissionerAndGoalBuilder':
        """Set common_intendedApplications text for a specific language."""
        if self.common_intendedApplications is None:
            self.common_intendedApplications = FTMultiLang()

        # Update existing or add new
        for item in self.common_intendedApplications.items:
            if item.lang == lang:
                item.text = text
                return self

        self.common_intendedApplications.items.append(MultiLangItemFT(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_intendedApplications(self, lang: str = 'en') -> Optional[str]:
        """Get common_intendedApplications text for a specific language."""
        if not self.common_intendedApplications:
            return None
        for item in self.common_intendedApplications.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> CommonCommissionerAndGoal:
        """Build the final CommonCommissionerAndGoal instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonCommissionerAndGoal.model_validate(data)

class DataGeneratorBuilder(BaseModel):
    """"Contact data set" of the person(s), working group(s), organisation(s) or database network, that generated the data set, i.e. being technically responsible for its correctness regarding methods, inventory, and documentative information. (Builder)"""

    common_referenceToPersonOrEntityGeneratingTheDataSet: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToPersonOrEntityGeneratingTheDataSet')
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> DataGenerator:
        """Build the final DataGenerator instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return DataGenerator.model_validate(data)

class DataEntryByBuilder(BaseModel):
    """"Contact data set" of the responsible person or entity that has documented this data set, i.e. entered the data and the descriptive information. (Builder)"""

    common_timeStamp: Optional[AwareDatetime] = Field(None, alias='common:timeStamp')
    common_referenceToDataSetFormat: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToDataSetFormat')
    common_referenceToPersonOrEntityEnteringTheData: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToPersonOrEntityEnteringTheData')
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> DataEntryBy:
        """Build the final DataEntryBy instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return DataEntryBy.model_validate(data)

class PublicationAndOwnershipBuilder(BaseModel):
    """Information related to publication and version management of the data set including copyright and access restrictions. (Builder)"""

    common_dataSetVersion: Optional[str] = Field(None, alias='common:dataSetVersion')
    common_referenceToPrecedingDataSetVersion: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToPrecedingDataSetVersion')
    common_permanentDataSetURI: Optional[AnyUrl] = Field(None, alias='common:permanentDataSetURI')
    common_referenceToOwnershipOfDataSet: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToOwnershipOfDataSet')
    common_copyright: Optional[CommonCopyright] = Field(None, alias='common:copyright')
    common_referenceToEntitiesWithExclusiveAccess: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToEntitiesWithExclusiveAccess')
    common_licenseType: Optional[CommonLicenseType] = Field(None, alias='common:licenseType')
    common_accessRestrictions: Optional[FTMultiLang] = Field(None, alias='common:accessRestrictions')
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def set_accessRestrictions(self, text: str, lang: str = 'en') -> 'PublicationAndOwnershipBuilder':
        """Set common_accessRestrictions text for a specific language."""
        if self.common_accessRestrictions is None:
            self.common_accessRestrictions = FTMultiLang()

        # Update existing or add new
        for item in self.common_accessRestrictions.items:
            if item.lang == lang:
                item.text = text
                return self

        self.common_accessRestrictions.items.append(MultiLangItemFT(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_accessRestrictions(self, lang: str = 'en') -> Optional[str]:
        """Get common_accessRestrictions text for a specific language."""
        if not self.common_accessRestrictions:
            return None
        for item in self.common_accessRestrictions.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> PublicationAndOwnership:
        """Build the final PublicationAndOwnership instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return PublicationAndOwnership.model_validate(data)

class AdministrativeInformationBuilder(BaseModel):
    """Information required for data set management and administration. (Builder)"""

    common_other: Optional[str] = Field(None, alias='common:other')
    _common_commissionerAndGoal: Optional[CommonCommissionerAndGoalBuilder] = None
    _dataGenerator: Optional[DataGeneratorBuilder] = None
    _dataEntryBy: Optional[DataEntryByBuilder] = None
    _publicationAndOwnership: Optional[PublicationAndOwnershipBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def common_commissionerAndGoal(self) -> CommonCommissionerAndGoalBuilder:
        """Access common_commissionerAndGoal builder (auto-initialized)."""
        if self._common_commissionerAndGoal is None:
            self._common_commissionerAndGoal = CommonCommissionerAndGoalBuilder()
        return self._common_commissionerAndGoal

    @property
    def dataGenerator(self) -> DataGeneratorBuilder:
        """Access dataGenerator builder (auto-initialized)."""
        if self._dataGenerator is None:
            self._dataGenerator = DataGeneratorBuilder()
        return self._dataGenerator

    @property
    def dataEntryBy(self) -> DataEntryByBuilder:
        """Access dataEntryBy builder (auto-initialized)."""
        if self._dataEntryBy is None:
            self._dataEntryBy = DataEntryByBuilder()
        return self._dataEntryBy

    @property
    def publicationAndOwnership(self) -> PublicationAndOwnershipBuilder:
        """Access publicationAndOwnership builder (auto-initialized)."""
        if self._publicationAndOwnership is None:
            self._publicationAndOwnership = PublicationAndOwnershipBuilder()
        return self._publicationAndOwnership

    def build(self) -> AdministrativeInformation:
        """Build the final AdministrativeInformation instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_common_commissionerAndGoal', None)
        data.pop('_dataGenerator', None)
        data.pop('_dataEntryBy', None)
        data.pop('_publicationAndOwnership', None)

        # Build nested objects
        if self._common_commissionerAndGoal is not None:
            data['common:commissionerAndGoal'] = self._common_commissionerAndGoal.build()
        if self._dataGenerator is not None:
            data['dataGenerator'] = self._dataGenerator.build()
        if self._dataEntryBy is not None:
            data['dataEntryBy'] = self._dataEntryBy.build()
        if self._publicationAndOwnership is not None:
            data['publicationAndOwnership'] = self._publicationAndOwnership.build()

        return AdministrativeInformation.model_validate(data)

class ModelBuilder(BaseModel):
    """Builder for Model."""

    _lifeCycleModelDataSet: Optional[LifeCycleModelDataSetBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def lifeCycleModelDataSet(self) -> LifeCycleModelDataSetBuilder:
        """Access lifeCycleModelDataSet builder (auto-initialized)."""
        if self._lifeCycleModelDataSet is None:
            self._lifeCycleModelDataSet = LifeCycleModelDataSetBuilder()
        return self._lifeCycleModelDataSet

    def build(self) -> Model:
        """Build the final Model instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_lifeCycleModelDataSet', None)

        # Build nested objects
        if self._lifeCycleModelDataSet is not None:
            data['lifeCycleModelDataSet'] = self._lifeCycleModelDataSet.build()

        return Model.model_validate(data)

class LifeCycleModelDataSetBuilder(BaseModel):
    """Builder for LifeCycleModelDataSet."""

    field_xmlns: Optional[Literal['http://eplca.jrc.ec.europa.eu/ILCD/LifeCycleModel/2017']] = Field(None, alias='@xmlns')
    field_xmlns_acme: Optional[Literal['http://acme.com/custom']] = Field(None, alias='@xmlns:acme')
    field_xmlns_common: Optional[Literal['http://lca.jrc.it/ILCD/Common']] = Field(None, alias='@xmlns:common')
    field_xmlns_xsi: Optional[Literal['http://www.w3.org/2001/XMLSchema-instance']] = Field(None, alias='@xmlns:xsi')
    field_locations: Optional[Literal['../ILCDLocations.xml']] = Field(None, alias='@locations')
    field_version: Optional[Literal['1.1']] = Field(None, alias='@version')
    field_xsi_schemaLocation: Optional[Literal['http://eplca.jrc.ec.europa.eu/ILCD/LifeCycleModel/2017 ../../schemas/ILCD_LifeCycleModelDataSet.xsd']] = Field(None, alias='@xsi:schemaLocation')
    common_other: Optional[str] = Field(None, alias='common:other')
    _lifeCycleModelInformation: Optional[LifeCycleModelInformationBuilder] = None
    _modellingAndValidation: Optional[ModellingAndValidationBuilder] = None
    _administrativeInformation: Optional[AdministrativeInformationBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def lifeCycleModelInformation(self) -> LifeCycleModelInformationBuilder:
        """Access lifeCycleModelInformation builder (auto-initialized)."""
        if self._lifeCycleModelInformation is None:
            self._lifeCycleModelInformation = LifeCycleModelInformationBuilder()
        return self._lifeCycleModelInformation

    @property
    def modellingAndValidation(self) -> ModellingAndValidationBuilder:
        """Access modellingAndValidation builder (auto-initialized)."""
        if self._modellingAndValidation is None:
            self._modellingAndValidation = ModellingAndValidationBuilder()
        return self._modellingAndValidation

    @property
    def administrativeInformation(self) -> AdministrativeInformationBuilder:
        """Access administrativeInformation builder (auto-initialized)."""
        if self._administrativeInformation is None:
            self._administrativeInformation = AdministrativeInformationBuilder()
        return self._administrativeInformation

    def build(self) -> LifeCycleModelDataSet:
        """Build the final LifeCycleModelDataSet instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_lifeCycleModelInformation', None)
        data.pop('_modellingAndValidation', None)
        data.pop('_administrativeInformation', None)

        # Build nested objects
        if self._lifeCycleModelInformation is not None:
            data['lifeCycleModelInformation'] = self._lifeCycleModelInformation.build()
        if self._modellingAndValidation is not None:
            data['modellingAndValidation'] = self._modellingAndValidation.build()
        if self._administrativeInformation is not None:
            data['administrativeInformation'] = self._administrativeInformation.build()

        return LifeCycleModelDataSet.model_validate(data)
