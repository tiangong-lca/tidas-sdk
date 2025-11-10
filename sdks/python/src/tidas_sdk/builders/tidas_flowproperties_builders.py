# Auto-generated builder classes for TIDAS entities
# DO NOT EDIT - Regenerate using scripts/generate_builders.py

from __future__ import annotations

from typing import List, Literal, Optional
from pydantic import AnyUrl, AwareDatetime, BaseModel, ConfigDict, Field, RootModel
from enum import (
    Enum,
)
from tidas_sdk.types.tidas_flowproperties_category import (
    Flowproperties,
    TidasFlowpropertiesText,
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

from tidas_sdk.types.tidas_flowproperties import (
    AdministrativeInformation,
    ClassificationInformation,
    CommonClass,
    CommonClassification,
    Compliance,
    Compliance1,
    Compliance1Item,
    ComplianceDeclarations,
    DataEntryBy,
    DataSetInformation,
    DataSourcesTreatmentAndRepresentativeness,
    DateTime,
    FlowPropertiesInformation,
    FlowPropertyDataSet,
    Model,
    ModellingAndValidation,
    PublicationAndOwnership,
    QuantitativeReference,
)


class DateTimeBuilder(BaseModel):
    """Builder for DateTime."""

    root: Optional[AwareDatetime] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> DateTime:
        """Build the final DateTime instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return DateTime.model_validate(data)

class CommonClassBuilder(BaseModel):
    """Builder for CommonClass."""

    field_level: Optional[str] = Field(None, alias='@level')
    field_classId: Optional[Flowproperties] = Field(None, alias='@classId')
    text: Optional[TidasFlowpropertiesText] = Field(None, alias='#text')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> CommonClass:
        """Build the final CommonClass instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonClass.model_validate(data)

class CommonClassificationBuilder(BaseModel):
    """Optional statistical or other classification of the data set. Typically also used for structuring LCA databases. (Builder)"""

    common_other: Optional[str] = Field(None, alias='common:other')
    _common_class: Optional[CommonClassBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def common_class(self) -> CommonClassBuilder:
        """Access common_class builder (auto-initialized)."""
        if self._common_class is None:
            self._common_class = CommonClassBuilder()
        return self._common_class

    def build(self) -> CommonClassification:
        """Build the final CommonClassification instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_common_class', None)

        # Build nested objects
        if self._common_class is not None:
            data['common:class'] = self._common_class.build()

        return CommonClassification.model_validate(data)

class ClassificationInformationBuilder(BaseModel):
    """Hierachical classification of the Flow property foreseen to be used to structure the Flow property content of the database. (Note: This entry is NOT required for the identification of the Flow property data set. It should nevertheless be avoided to use identical names for Flow properties in the same class. (Builder)"""

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

class DataSetInformationBuilder(BaseModel):
    """Builder for DataSetInformation."""

    common_UUID: Optional[str] = Field(None, alias='common:UUID')
    common_name: Optional[StringMultiLang] = Field(None, alias='common:name')
    common_synonyms: Optional[FTMultiLang] = Field(None, alias='common:synonyms')
    common_generalComment: Optional[FTMultiLang] = Field(None, alias='common:generalComment')
    common_other: Optional[str] = Field(None, alias='common:other')
    _classificationInformation: Optional[ClassificationInformationBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def classificationInformation(self) -> ClassificationInformationBuilder:
        """Access classificationInformation builder (auto-initialized)."""
        if self._classificationInformation is None:
            self._classificationInformation = ClassificationInformationBuilder()
        return self._classificationInformation

    def set_name(self, text: str, lang: str = 'en') -> 'DataSetInformationBuilder':
        """Set common_name text for a specific language."""
        if self.common_name is None:
            self.common_name = StringMultiLang()

        # Update existing or add new
        for item in self.common_name.items:
            if item.lang == lang:
                item.text = text
                return self

        self.common_name.items.append(MultiLangItemString(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_name(self, lang: str = 'en') -> Optional[str]:
        """Get common_name text for a specific language."""
        if not self.common_name:
            return None
        for item in self.common_name.items:
            if item.lang == lang:
                return item.text
        return None

    def set_synonyms(self, text: str, lang: str = 'en') -> 'DataSetInformationBuilder':
        """Set common_synonyms text for a specific language."""
        if self.common_synonyms is None:
            self.common_synonyms = FTMultiLang()

        # Update existing or add new
        for item in self.common_synonyms.items:
            if item.lang == lang:
                item.text = text
                return self

        self.common_synonyms.items.append(MultiLangItemFT(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_synonyms(self, lang: str = 'en') -> Optional[str]:
        """Get common_synonyms text for a specific language."""
        if not self.common_synonyms:
            return None
        for item in self.common_synonyms.items:
            if item.lang == lang:
                return item.text
        return None

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
        data.pop('_classificationInformation', None)

        # Build nested objects
        if self._classificationInformation is not None:
            data['classificationInformation'] = self._classificationInformation.build()

        return DataSetInformation.model_validate(data)

class QuantitativeReferenceBuilder(BaseModel):
    """This section allows to refer to the Flow property's quantitative reference, which is always a unit (i.e. that unit, in which the property is measured, e.g. "MJ" for energy-related Flow properties). (Builder)"""

    referenceToReferenceUnitGroup: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> QuantitativeReference:
        """Build the final QuantitativeReference instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return QuantitativeReference.model_validate(data)

class FlowPropertiesInformationBuilder(BaseModel):
    """Builder for FlowPropertiesInformation."""

    common_other: Optional[str] = Field(None, alias='common:other')
    _dataSetInformation: Optional[DataSetInformationBuilder] = None
    _quantitativeReference: Optional[QuantitativeReferenceBuilder] = None

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

    def build(self) -> FlowPropertiesInformation:
        """Build the final FlowPropertiesInformation instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_dataSetInformation', None)
        data.pop('_quantitativeReference', None)

        # Build nested objects
        if self._dataSetInformation is not None:
            data['dataSetInformation'] = self._dataSetInformation.build()
        if self._quantitativeReference is not None:
            data['quantitativeReference'] = self._quantitativeReference.build()

        return FlowPropertiesInformation.model_validate(data)

class DataSourcesTreatmentAndRepresentativenessBuilder(BaseModel):
    """Builder for DataSourcesTreatmentAndRepresentativeness."""

    referenceToDataSource: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> DataSourcesTreatmentAndRepresentativeness:
        """Build the final DataSourcesTreatmentAndRepresentativeness instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return DataSourcesTreatmentAndRepresentativeness.model_validate(data)

class ComplianceBuilder(BaseModel):
    """One compliance declaration. Multiple declarations may be provided. (Builder)"""

    common_referenceToComplianceSystem: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToComplianceSystem')
    common_approvalOfOverallCompliance: Optional[CommonApprovalOfOverallCompliance] = Field(None, alias='common:approvalOfOverallCompliance')

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
    """Statements on compliance of several data set aspects with compliance requirements as defined by the referenced compliance system (e.g. an EPD scheme, handbook of a national or international data network such as the ILCD, etc.). (Builder)"""

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
    """Covers the five sub-sections 1) LCI method (not used), 2) Data sources, treatment and representativeness (only 3 fields), 3) Completeness (not used), 4) Validation, and 5) Compliance. (Builder)"""

    common_other: Optional[str] = Field(None, alias='common:other')
    _dataSourcesTreatmentAndRepresentativeness: Optional[DataSourcesTreatmentAndRepresentativenessBuilder] = None
    _complianceDeclarations: Optional[ComplianceDeclarationsBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def dataSourcesTreatmentAndRepresentativeness(self) -> DataSourcesTreatmentAndRepresentativenessBuilder:
        """Access dataSourcesTreatmentAndRepresentativeness builder (auto-initialized)."""
        if self._dataSourcesTreatmentAndRepresentativeness is None:
            self._dataSourcesTreatmentAndRepresentativeness = DataSourcesTreatmentAndRepresentativenessBuilder()
        return self._dataSourcesTreatmentAndRepresentativeness

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
        data.pop('_dataSourcesTreatmentAndRepresentativeness', None)
        data.pop('_complianceDeclarations', None)

        # Build nested objects
        if self._dataSourcesTreatmentAndRepresentativeness is not None:
            data['dataSourcesTreatmentAndRepresentativeness'] = self._dataSourcesTreatmentAndRepresentativeness.build()
        if self._complianceDeclarations is not None:
            data['complianceDeclarations'] = self._complianceDeclarations.build()

        return ModellingAndValidation.model_validate(data)

class DataEntryByBuilder(BaseModel):
    """Staff or entity, that documented the generated data set, entering the information into the database; plus administrative information linked to the data entry activity. (Builder)"""

    common_timeStamp: Optional[AwareDatetime] = Field(None, alias='common:timeStamp')
    common_referenceToDataSetFormat: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToDataSetFormat')
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
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> PublicationAndOwnership:
        """Build the final PublicationAndOwnership instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return PublicationAndOwnership.model_validate(data)

class AdministrativeInformationBuilder(BaseModel):
    """Information on data set management and administration. (Builder)"""

    common_other: Optional[str] = Field(None, alias='common:other')
    _dataEntryBy: Optional[DataEntryByBuilder] = None
    _publicationAndOwnership: Optional[PublicationAndOwnershipBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

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
        data.pop('_dataEntryBy', None)
        data.pop('_publicationAndOwnership', None)

        # Build nested objects
        if self._dataEntryBy is not None:
            data['dataEntryBy'] = self._dataEntryBy.build()
        if self._publicationAndOwnership is not None:
            data['publicationAndOwnership'] = self._publicationAndOwnership.build()

        return AdministrativeInformation.model_validate(data)

class ModelBuilder(BaseModel):
    """Builder for Model."""

    _flowPropertyDataSet: Optional[FlowPropertyDataSetBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def flowPropertyDataSet(self) -> FlowPropertyDataSetBuilder:
        """Access flowPropertyDataSet builder (auto-initialized)."""
        if self._flowPropertyDataSet is None:
            self._flowPropertyDataSet = FlowPropertyDataSetBuilder()
        return self._flowPropertyDataSet

    def build(self) -> Model:
        """Build the final Model instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_flowPropertyDataSet', None)

        # Build nested objects
        if self._flowPropertyDataSet is not None:
            data['flowPropertyDataSet'] = self._flowPropertyDataSet.build()

        return Model.model_validate(data)

class FlowPropertyDataSetBuilder(BaseModel):
    """Builder for FlowPropertyDataSet."""

    field_xmlns: Optional[Literal['http://lca.jrc.it/ILCD/FlowProperty']] = Field(None, alias='@xmlns')
    field_xmlns_common: Optional[Literal['http://lca.jrc.it/ILCD/Common']] = Field(None, alias='@xmlns:common')
    field_xmlns_xsi: Optional[Literal['http://www.w3.org/2001/XMLSchema-instance']] = Field(None, alias='@xmlns:xsi')
    field_version: Optional[Literal['1.1']] = Field(None, alias='@version')
    field_xsi_schemaLocation: Optional[Literal['http://lca.jrc.it/ILCD/FlowProperty ../../schemas/ILCD_FlowPropertyDataSet.xsd']] = Field(None, alias='@xsi:schemaLocation')
    common_other: Optional[str] = Field(None, alias='common:other')
    _flowPropertiesInformation: Optional[FlowPropertiesInformationBuilder] = None
    _modellingAndValidation: Optional[ModellingAndValidationBuilder] = None
    _administrativeInformation: Optional[AdministrativeInformationBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def flowPropertiesInformation(self) -> FlowPropertiesInformationBuilder:
        """Access flowPropertiesInformation builder (auto-initialized)."""
        if self._flowPropertiesInformation is None:
            self._flowPropertiesInformation = FlowPropertiesInformationBuilder()
        return self._flowPropertiesInformation

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

    def build(self) -> FlowPropertyDataSet:
        """Build the final FlowPropertyDataSet instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_flowPropertiesInformation', None)
        data.pop('_modellingAndValidation', None)
        data.pop('_administrativeInformation', None)

        # Build nested objects
        if self._flowPropertiesInformation is not None:
            data['flowPropertiesInformation'] = self._flowPropertiesInformation.build()
        if self._modellingAndValidation is not None:
            data['modellingAndValidation'] = self._modellingAndValidation.build()
        if self._administrativeInformation is not None:
            data['administrativeInformation'] = self._administrativeInformation.build()

        return FlowPropertyDataSet.model_validate(data)
