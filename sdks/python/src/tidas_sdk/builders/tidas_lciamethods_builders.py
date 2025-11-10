# Auto-generated builder classes for TIDAS entities
# DO NOT EDIT - Regenerate using scripts/generate_builders.py

from __future__ import annotations

from typing import List, Literal, Optional
from pydantic import AnyUrl, AwareDatetime, BaseModel, ConfigDict, Field, RootModel
from enum import (
    Enum,
)
from tidas_sdk.types.tidas_lciamethods_category import (
    Lciamethods,
    TidasLciamethodsText,
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

from tidas_sdk.types.tidas_lciamethods import (
    AdministrativeInformation,
    CharacterisationFactors,
    ClassificationInformation,
    CommonClas,
    CommonClas1,
    CommonClas2,
    CommonClassification,
    CommonCommissionerAndGoal,
    CommonMethod,
    CommonMethodItem,
    CommonScope,
    CommonScopeItem,
    Completeness,
    Compliance,
    Compliance1,
    Compliance1Item,
    ComplianceDeclarations,
    DataEntryBy,
    DataGenerator,
    DataSetInformation,
    DataSources,
    Factor,
    FactorItem,
    Geography,
    ImpactLocation,
    ImpactModel,
    IntervensionSubLocation,
    InterventionLocation,
    LCIAMethodDataSet,
    LCIAMethodInformation,
    LCIAMethodNormalisationAndWeighting,
    Model,
    ModellingAndValidation,
    PublicationAndOwnership,
    QuantitativeReference,
    RecommendationBy,
    ReferenceToDataSource,
    Review,
    Time,
    Validation,
)


class CommonClasBuilder(BaseModel):
    """Builder for CommonClas."""

    field_level: Optional[Literal['0']] = Field(None, alias='@level')
    field_classId: Optional[Lciamethods] = Field(None, alias='@classId')
    text: Optional[TidasLciamethodsText] = Field(None, alias='#text')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> CommonClas:
        """Build the final CommonClas instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonClas.model_validate(data)

class CommonClas1Builder(BaseModel):
    """Builder for CommonClas1."""

    field_level: Optional[Literal['1']] = Field(None, alias='@level')
    field_classId: Optional[Lciamethods] = Field(None, alias='@classId')
    text: Optional[TidasLciamethodsText] = Field(None, alias='#text')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> CommonClas1:
        """Build the final CommonClas1 instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonClas1.model_validate(data)

class CommonClas2Builder(BaseModel):
    """Builder for CommonClas2."""

    field_level: Optional[Literal['2']] = Field(None, alias='@level')
    field_classId: Optional[Lciamethods] = Field(None, alias='@classId')
    text: Optional[TidasLciamethodsText] = Field(None, alias='#text')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> CommonClas2:
        """Build the final CommonClas2 instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonClas2.model_validate(data)

class CommonClassificationBuilder(BaseModel):
    """Optional statistical or other classification of the data set. Typically also used for structuring LCA databases. (Builder)"""

    common_other: Optional[str] = Field(None, alias='common:other')
    _common_class: List[CommonClas | CommonClas1 | CommonClas2Builder] = []

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def common_class(self) -> List[CommonClas | CommonClas1 | CommonClas2Builder]:
        """Access common_class builder list."""
        return self._common_class

    def add_common_cla(self) -> CommonClas | CommonClas1 | CommonClas2Builder:
        """Add and return a new CommonClas | CommonClas1 | CommonClas2 builder."""
        builder = CommonClas | CommonClas1 | CommonClas2Builder()
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
    """Builder for ClassificationInformation."""

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

class CommonMethodBuilder(BaseModel):
    """Validation method(s) used in the respective "Scope of review". (Builder)"""

    field_name: Optional[FieldName1] = Field(None, alias='@name')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> CommonMethod:
        """Build the final CommonMethod instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonMethod.model_validate(data)

class CommonMethodItemBuilder(BaseModel):
    """Builder for CommonMethodItem."""

    field_name: Optional[FieldName1] = Field(None, alias='@name')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> CommonMethodItem:
        """Build the final CommonMethodItem instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonMethodItem.model_validate(data)

class CommonScopeBuilder(BaseModel):
    """Scope of review regarding which aspects and components of the data set was reviewed or verified. In case of aggregated e.g. LCI results also and on which level of detail (e.g. LCI results only, included unit processes, ...) the review / verification was performed. (Builder)"""

    field_name: Optional[FieldName] = Field(None, alias='@name')
    _common_method: Optional[CommonMethodBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def common_method(self) -> CommonMethodBuilder:
        """Access common_method builder (auto-initialized)."""
        if self._common_method is None:
            self._common_method = CommonMethodBuilder()
        return self._common_method

    def build(self) -> CommonScope:
        """Build the final CommonScope instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_common_method', None)

        # Build nested objects
        if self._common_method is not None:
            data['common:method'] = self._common_method.build()

        return CommonScope.model_validate(data)

class CommonScopeItemBuilder(BaseModel):
    """Builder for CommonScopeItem."""

    field_name: Optional[FieldName] = Field(None, alias='@name')
    common_method: Optional[CommonMethod1 | list[CommonMethodItem1]] = Field(None, alias='common:method')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> CommonScopeItem:
        """Build the final CommonScopeItem instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonScopeItem.model_validate(data)

class DataSetInformationBuilder(BaseModel):
    """Builder for DataSetInformation."""

    common_UUID: Optional[str] = Field(None, alias='common:UUID')
    common_name: Optional[StringMultiLang] = Field(None, alias='common:name')
    methodology: Optional[str] = None
    impactCategory: Optional[ImpactCategory] = None
    areaOfProtection: Optional[AreaOfProtection] = None
    impactIndicator: Optional[str] = None
    common_generalComment: Optional[FTMultiLang] = Field(None, alias='common:generalComment')
    referenceToExternalDocumentation: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None
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
    """This section allows to refer to the LCIA method(ology)'s quantitative reference, which is always the unit, in which the characterisation factors of the impact indicator are measured, e.g. "kg CO2-Equivalents". (Builder)"""

    referenceQuantity: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> QuantitativeReference:
        """Build the final QuantitativeReference instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return QuantitativeReference.model_validate(data)

class TimeBuilder(BaseModel):
    """Builder for Time."""

    referenceYear: Optional[STMultiLang] = None
    duration: Optional[STMultiLang] = None
    timeRepresentativenessDescription: Optional[FTMultiLang] = None
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def set_referenceYear(self, text: str, lang: str = 'en') -> 'TimeBuilder':
        """Set referenceYear text for a specific language."""
        if self.referenceYear is None:
            self.referenceYear = STMultiLang()

        # Update existing or add new
        for item in self.referenceYear.items:
            if item.lang == lang:
                item.text = text
                return self

        self.referenceYear.items.append(MultiLangItemST(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_referenceYear(self, lang: str = 'en') -> Optional[str]:
        """Get referenceYear text for a specific language."""
        if not self.referenceYear:
            return None
        for item in self.referenceYear.items:
            if item.lang == lang:
                return item.text
        return None

    def set_duration(self, text: str, lang: str = 'en') -> 'TimeBuilder':
        """Set duration text for a specific language."""
        if self.duration is None:
            self.duration = STMultiLang()

        # Update existing or add new
        for item in self.duration.items:
            if item.lang == lang:
                item.text = text
                return self

        self.duration.items.append(MultiLangItemST(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_duration(self, lang: str = 'en') -> Optional[str]:
        """Get duration text for a specific language."""
        if not self.duration:
            return None
        for item in self.duration.items:
            if item.lang == lang:
                return item.text
        return None

    def set_timeRepresentativenessDescription(self, text: str, lang: str = 'en') -> 'TimeBuilder':
        """Set timeRepresentativenessDescription text for a specific language."""
        if self.timeRepresentativenessDescription is None:
            self.timeRepresentativenessDescription = FTMultiLang()

        # Update existing or add new
        for item in self.timeRepresentativenessDescription.items:
            if item.lang == lang:
                item.text = text
                return self

        self.timeRepresentativenessDescription.items.append(MultiLangItemFT(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_timeRepresentativenessDescription(self, lang: str = 'en') -> Optional[str]:
        """Get timeRepresentativenessDescription text for a specific language."""
        if not self.timeRepresentativenessDescription:
            return None
        for item in self.timeRepresentativenessDescription.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> Time:
        """Build the final Time instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return Time.model_validate(data)

class InterventionLocationBuilder(BaseModel):
    """Specific, country, or region of the elementary flows' / exchanges' occurence for which the LCIA method(ology) is valid / modelled. [Note: Entry can be of type "two-letter ISO 3166 country code" for countries, "seven-letter regional codes" for regions or continents, or "market areas and market organisations", as predefined for the ILCD. Also a name for e.g. a specific plant etc. can be given here (e.g. "FR, Lyon, XY Company, Z Site"; user defined). ] (Builder)"""

    text: Optional[str] = Field(None, alias='#text')
    field_latitudeAndLongitude: Optional[str] = Field(None, alias='@latitudeAndLongitude')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> InterventionLocation:
        """Build the final InterventionLocation instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return InterventionLocation.model_validate(data)

class IntervensionSubLocationBuilder(BaseModel):
    """Geographical sub-unit(s) of "Intervention location(s)" that further specify the specifically modelled sub-locations. Such sub-locations can be e.g. sites of a company, specific catchments modleled, countries of a continent, or locations in a country. Information on limited representativeness should be provided if applicable. (Builder)"""

    text: Optional[str] = Field(None, alias='#text')
    field_latitudeAndLongitude: Optional[str] = Field(None, alias='@latitudeAndLongitude')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> IntervensionSubLocation:
        """Build the final IntervensionSubLocation instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return IntervensionSubLocation.model_validate(data)

class ImpactLocationBuilder(BaseModel):
    """Location or region where the impact is modelled to take place. [Note: Entry can be of type "two-letter ISO 3166 country code" for countries, "seven-letter regional codes" for regions or continents, or "market areas and market organisations", as predefined for the ILCD. Also a name for e.g. a specific catchment etc. can be given here, user defined).] (Builder)"""

    text: Optional[str] = Field(None, alias='#text')
    field_latitudeAndLongitude: Optional[str] = Field(None, alias='@latitudeAndLongitude')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> ImpactLocation:
        """Build the final ImpactLocation instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return ImpactLocation.model_validate(data)

class GeographyBuilder(BaseModel):
    """Builder for Geography."""

    geographicalRepresentativenessDescription: Optional[FTMultiLang] = None
    common_other: Optional[str] = Field(None, alias='common:other')
    _interventionLocation: Optional[InterventionLocationBuilder] = None
    _intervensionSubLocation: Optional[IntervensionSubLocationBuilder] = None
    _impactLocation: Optional[ImpactLocationBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def interventionLocation(self) -> InterventionLocationBuilder:
        """Access interventionLocation builder (auto-initialized)."""
        if self._interventionLocation is None:
            self._interventionLocation = InterventionLocationBuilder()
        return self._interventionLocation

    @property
    def intervensionSubLocation(self) -> IntervensionSubLocationBuilder:
        """Access intervensionSubLocation builder (auto-initialized)."""
        if self._intervensionSubLocation is None:
            self._intervensionSubLocation = IntervensionSubLocationBuilder()
        return self._intervensionSubLocation

    @property
    def impactLocation(self) -> ImpactLocationBuilder:
        """Access impactLocation builder (auto-initialized)."""
        if self._impactLocation is None:
            self._impactLocation = ImpactLocationBuilder()
        return self._impactLocation

    def set_geographicalRepresentativenessDescription(self, text: str, lang: str = 'en') -> 'GeographyBuilder':
        """Set geographicalRepresentativenessDescription text for a specific language."""
        if self.geographicalRepresentativenessDescription is None:
            self.geographicalRepresentativenessDescription = FTMultiLang()

        # Update existing or add new
        for item in self.geographicalRepresentativenessDescription.items:
            if item.lang == lang:
                item.text = text
                return self

        self.geographicalRepresentativenessDescription.items.append(MultiLangItemFT(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_geographicalRepresentativenessDescription(self, lang: str = 'en') -> Optional[str]:
        """Get geographicalRepresentativenessDescription text for a specific language."""
        if not self.geographicalRepresentativenessDescription:
            return None
        for item in self.geographicalRepresentativenessDescription.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> Geography:
        """Build the final Geography instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_interventionLocation', None)
        data.pop('_intervensionSubLocation', None)
        data.pop('_impactLocation', None)

        # Build nested objects
        if self._interventionLocation is not None:
            data['interventionLocation'] = self._interventionLocation.build()
        if self._intervensionSubLocation is not None:
            data['intervensionSubLocation'] = self._intervensionSubLocation.build()
        if self._impactLocation is not None:
            data['impactLocation'] = self._impactLocation.build()

        return Geography.model_validate(data)

class ImpactModelBuilder(BaseModel):
    """Provides information about the general representativiness of the data set and about its composition of single LCIA-methods. (Builder)"""

    modelName: Optional[str] = None
    modelDescription: Optional[FTMultiLang] = None
    referenceToModelSource: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None
    referenceToIncludedMethods: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None
    consideredMechanisms: Optional[STMultiLang] = None
    referenceToMethodologyFlowChart: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def set_modelDescription(self, text: str, lang: str = 'en') -> 'ImpactModelBuilder':
        """Set modelDescription text for a specific language."""
        if self.modelDescription is None:
            self.modelDescription = FTMultiLang()

        # Update existing or add new
        for item in self.modelDescription.items:
            if item.lang == lang:
                item.text = text
                return self

        self.modelDescription.items.append(MultiLangItemFT(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_modelDescription(self, lang: str = 'en') -> Optional[str]:
        """Get modelDescription text for a specific language."""
        if not self.modelDescription:
            return None
        for item in self.modelDescription.items:
            if item.lang == lang:
                return item.text
        return None

    def set_consideredMechanisms(self, text: str, lang: str = 'en') -> 'ImpactModelBuilder':
        """Set consideredMechanisms text for a specific language."""
        if self.consideredMechanisms is None:
            self.consideredMechanisms = STMultiLang()

        # Update existing or add new
        for item in self.consideredMechanisms.items:
            if item.lang == lang:
                item.text = text
                return self

        self.consideredMechanisms.items.append(MultiLangItemST(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_consideredMechanisms(self, lang: str = 'en') -> Optional[str]:
        """Get consideredMechanisms text for a specific language."""
        if not self.consideredMechanisms:
            return None
        for item in self.consideredMechanisms.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> ImpactModel:
        """Build the final ImpactModel instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return ImpactModel.model_validate(data)

class ReferenceToDataSourceBuilder(BaseModel):
    """Builder for ReferenceToDataSource."""

    referenceToDataSource: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> ReferenceToDataSource:
        """Build the final ReferenceToDataSource instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return ReferenceToDataSource.model_validate(data)

class FactorItemBuilder(BaseModel):
    """Builder for FactorItem."""

    referenceToFlowDataSet: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None
    location: Optional[str] = None
    exchangeDirection: Optional[ExchangeDirection] = None
    meanValue: Optional[str] = None
    minimumValue: Optional[str] = None
    maximumValue: Optional[str] = None
    uncertaintyType: Optional[UncertaintyDistributionType] = None
    relativeStandardDeviation95In: Optional[str] = None
    dataDerivationTypeStatus: Optional[DataDerivationTypeStatus] = None
    deviatingRecommendation: Optional[DeviatingRecommendation] = None
    generalComment: Optional[StringMultiLang] = None
    _referenceToDataSource: Optional[ReferenceToDataSourceBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def referenceToDataSource(self) -> ReferenceToDataSourceBuilder:
        """Access referenceToDataSource builder (auto-initialized)."""
        if self._referenceToDataSource is None:
            self._referenceToDataSource = ReferenceToDataSourceBuilder()
        return self._referenceToDataSource

    def set_generalComment(self, text: str, lang: str = 'en') -> 'FactorItemBuilder':
        """Set generalComment text for a specific language."""
        if self.generalComment is None:
            self.generalComment = StringMultiLang()

        # Update existing or add new
        for item in self.generalComment.items:
            if item.lang == lang:
                item.text = text
                return self

        self.generalComment.items.append(MultiLangItemString(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_generalComment(self, lang: str = 'en') -> Optional[str]:
        """Get generalComment text for a specific language."""
        if not self.generalComment:
            return None
        for item in self.generalComment.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> FactorItem:
        """Build the final FactorItem instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_referenceToDataSource', None)

        # Build nested objects
        if self._referenceToDataSource is not None:
            data['referenceToDataSource'] = self._referenceToDataSource.build()

        return FactorItem.model_validate(data)

class FactorBuilder(BaseModel):
    """Builder for Factor."""

    referenceToFlowDataSet: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None
    location: Optional[str] = None
    exchangeDirection: Optional[ExchangeDirection] = None
    meanValue: Optional[str] = None
    minimumValue: Optional[str] = None
    maximumValue: Optional[str] = None
    uncertaintyDistributionType: Optional[UncertaintyDistributionType] = None
    relativeStandardDeviation95In: Optional[str] = None
    dataDerivationTypeStatus: Optional[DataDerivationTypeStatus] = None
    deviatingRecommendation: Optional[DeviatingRecommendation] = None
    referenceToDataSource: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None
    generalComment: Optional[StringMultiLang] = None
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def set_generalComment(self, text: str, lang: str = 'en') -> 'FactorBuilder':
        """Set generalComment text for a specific language."""
        if self.generalComment is None:
            self.generalComment = StringMultiLang()

        # Update existing or add new
        for item in self.generalComment.items:
            if item.lang == lang:
                item.text = text
                return self

        self.generalComment.items.append(MultiLangItemString(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_generalComment(self, lang: str = 'en') -> Optional[str]:
        """Get generalComment text for a specific language."""
        if not self.generalComment:
            return None
        for item in self.generalComment.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> Factor:
        """Build the final Factor instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return Factor.model_validate(data)

class CharacterisationFactorsBuilder(BaseModel):
    """Flow / Exchanges list with corresponding impact factors according to the respective LCIA method. (Builder)"""

    common_other: Optional[str] = Field(None, alias='common:other')
    _factor: Optional[FactorBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def factor(self) -> FactorBuilder:
        """Access factor builder (auto-initialized)."""
        if self._factor is None:
            self._factor = FactorBuilder()
        return self._factor

    def build(self) -> CharacterisationFactors:
        """Build the final CharacterisationFactors instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_factor', None)

        # Build nested objects
        if self._factor is not None:
            data['factor'] = self._factor.build()

        return CharacterisationFactors.model_validate(data)

class ReviewBuilder(BaseModel):
    """Type of review that has been performed regarding independency and type of review process. (Builder)"""

    field_type: Optional[FieldType] = Field(None, alias='@type')
    common_reviewDetails: Optional[FTMultiLang] = Field(None, alias='common:reviewDetails')
    common_referenceToNameOfReviewerAndInstitution: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToNameOfReviewerAndInstitution')
    common_otherReviewDetails: Optional[FTMultiLang] = Field(None, alias='common:otherReviewDetails')
    common_referenceToCompleteReviewReport: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToCompleteReviewReport')
    common_other: Optional[str] = Field(None, alias='common:other')
    _common_scope: Optional[CommonScopeBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def common_scope(self) -> CommonScopeBuilder:
        """Access common_scope builder (auto-initialized)."""
        if self._common_scope is None:
            self._common_scope = CommonScopeBuilder()
        return self._common_scope

    def set_reviewDetails(self, text: str, lang: str = 'en') -> 'ReviewBuilder':
        """Set common_reviewDetails text for a specific language."""
        if self.common_reviewDetails is None:
            self.common_reviewDetails = FTMultiLang()

        # Update existing or add new
        for item in self.common_reviewDetails.items:
            if item.lang == lang:
                item.text = text
                return self

        self.common_reviewDetails.items.append(MultiLangItemFT(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_reviewDetails(self, lang: str = 'en') -> Optional[str]:
        """Get common_reviewDetails text for a specific language."""
        if not self.common_reviewDetails:
            return None
        for item in self.common_reviewDetails.items:
            if item.lang == lang:
                return item.text
        return None

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

        # Remove private builder fields
        data.pop('_common_scope', None)

        # Build nested objects
        if self._common_scope is not None:
            data['common:scope'] = self._common_scope.build()

        return Review.model_validate(data)

class ValidationBuilder(BaseModel):
    """Review information on LCIA method. (Builder)"""

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
    """Expert(s), that compiled and modelled the data set as well as internal administrative information linked to the data generation activity. (Builder)"""

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

class PublicationAndOwnershipBuilder(BaseModel):
    """Information related to publication and version management of the data set including copyright and access restrictions. (Builder)"""

    common_dateOfLastRevision: Optional[AwareDatetime] = Field(None, alias='common:dateOfLastRevision')
    common_dataSetVersion: Optional[str] = Field(None, alias='common:dataSetVersion')
    common_referenceToPrecedingDataSetVersion: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToPrecedingDataSetVersion')
    common_permanentDataSetURI: Optional[AnyUrl] = Field(None, alias='common:permanentDataSetURI')
    common_workflowAndPublicationStatus: Optional[CommonWorkflowAndPublicationStatus] = Field(None, alias='common:workflowAndPublicationStatus')
    common_referenceToUnchangedRepublication: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToUnchangedRepublication')
    common_referenceToOwnershipOfDataSet: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToOwnershipOfDataSet')
    common_copyright: Optional[CommonCopyright] = Field(None, alias='common:copyright')
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

class RecommendationByBuilder(BaseModel):
    """Builder for RecommendationBy."""

    referenceToEntity: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None
    level: Optional[Level] = None
    meaning: Optional[FTMultiLang] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def set_meaning(self, text: str, lang: str = 'en') -> 'RecommendationByBuilder':
        """Set meaning text for a specific language."""
        if self.meaning is None:
            self.meaning = FTMultiLang()

        # Update existing or add new
        for item in self.meaning.items:
            if item.lang == lang:
                item.text = text
                return self

        self.meaning.items.append(MultiLangItemFT(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_meaning(self, lang: str = 'en') -> Optional[str]:
        """Get meaning text for a specific language."""
        if not self.meaning:
            return None
        for item in self.meaning.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> RecommendationBy:
        """Build the final RecommendationBy instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return RecommendationBy.model_validate(data)

class DataEntryByBuilder(BaseModel):
    """Staff or entity, that documented the generated data set, entering the information into the database; plus administrative information linked to the data entry activity. (Builder)"""

    common_timeStamp: Optional[AwareDatetime] = Field(None, alias='common:timeStamp')
    common_referenceToDataSetFormat: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToDataSetFormat')
    common_referenceToConvertedOriginalDataSetFrom: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToConvertedOriginalDataSetFrom')
    common_referenceToPersonOrEntityEnteringTheData: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToPersonOrEntityEnteringTheData')
    common_other: Optional[str] = Field(None, alias='common:other')
    _recommendationBy: Optional[RecommendationByBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def recommendationBy(self) -> RecommendationByBuilder:
        """Access recommendationBy builder (auto-initialized)."""
        if self._recommendationBy is None:
            self._recommendationBy = RecommendationByBuilder()
        return self._recommendationBy

    def build(self) -> DataEntryBy:
        """Build the final DataEntryBy instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_recommendationBy', None)

        # Build nested objects
        if self._recommendationBy is not None:
            data['recommendationBy'] = self._recommendationBy.build()

        return DataEntryBy.model_validate(data)

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

class LCIAMethodNormalisationAndWeightingBuilder(BaseModel):
    """LCIA methodological modelling aspects (Builder)"""

    typeOfDataSet: Optional[TypeOfDataSet] = None
    LCIAMethodPrinciple_1: Optional[LCIAMethodPrinciple] = Field(None, alias='LCIAMethodPrinciple')
    deviationsFromLCIAMethodPrinciple: Optional[FTMultiLang] = None
    normalisation: Optional[Normalisation] = None
    referenceToUsableNormalisationDataSets: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None
    normalisationDescription: Optional[STMultiLang] = None
    referenceToIncludedNormalisationDataSets: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None
    weighting: Optional[Weighting] = None
    referenceToUsableWeightingDataSets: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None
    weightingDescription: Optional[STMultiLang] = None
    referenceToIncludedWeightingDataSets: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def set_deviationsFromLCIAMethodPrinciple(self, text: str, lang: str = 'en') -> 'LCIAMethodNormalisationAndWeightingBuilder':
        """Set deviationsFromLCIAMethodPrinciple text for a specific language."""
        if self.deviationsFromLCIAMethodPrinciple is None:
            self.deviationsFromLCIAMethodPrinciple = FTMultiLang()

        # Update existing or add new
        for item in self.deviationsFromLCIAMethodPrinciple.items:
            if item.lang == lang:
                item.text = text
                return self

        self.deviationsFromLCIAMethodPrinciple.items.append(MultiLangItemFT(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_deviationsFromLCIAMethodPrinciple(self, lang: str = 'en') -> Optional[str]:
        """Get deviationsFromLCIAMethodPrinciple text for a specific language."""
        if not self.deviationsFromLCIAMethodPrinciple:
            return None
        for item in self.deviationsFromLCIAMethodPrinciple.items:
            if item.lang == lang:
                return item.text
        return None

    def set_normalisationDescription(self, text: str, lang: str = 'en') -> 'LCIAMethodNormalisationAndWeightingBuilder':
        """Set normalisationDescription text for a specific language."""
        if self.normalisationDescription is None:
            self.normalisationDescription = STMultiLang()

        # Update existing or add new
        for item in self.normalisationDescription.items:
            if item.lang == lang:
                item.text = text
                return self

        self.normalisationDescription.items.append(MultiLangItemST(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_normalisationDescription(self, lang: str = 'en') -> Optional[str]:
        """Get normalisationDescription text for a specific language."""
        if not self.normalisationDescription:
            return None
        for item in self.normalisationDescription.items:
            if item.lang == lang:
                return item.text
        return None

    def set_weightingDescription(self, text: str, lang: str = 'en') -> 'LCIAMethodNormalisationAndWeightingBuilder':
        """Set weightingDescription text for a specific language."""
        if self.weightingDescription is None:
            self.weightingDescription = STMultiLang()

        # Update existing or add new
        for item in self.weightingDescription.items:
            if item.lang == lang:
                item.text = text
                return self

        self.weightingDescription.items.append(MultiLangItemST(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_weightingDescription(self, lang: str = 'en') -> Optional[str]:
        """Get weightingDescription text for a specific language."""
        if not self.weightingDescription:
            return None
        for item in self.weightingDescription.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> LCIAMethodNormalisationAndWeighting:
        """Build the final LCIAMethodNormalisationAndWeighting instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return LCIAMethodNormalisationAndWeighting.model_validate(data)

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

class DataSourcesBuilder(BaseModel):
    """Data sources used for the model and the underlying substance and other data. (Builder)"""

    referenceToDataSource: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> DataSources:
        """Build the final DataSources instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return DataSources.model_validate(data)

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

class CompletenessBuilder(BaseModel):
    """Builder for Completeness."""

    completenessImpactCoverage: Optional[str] = None
    inventoryItems: Optional[str] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    def build(self) -> Completeness:
        """Build the final Completeness instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return Completeness.model_validate(data)

class ModellingAndValidationBuilder(BaseModel):
    """Covers the five sub-sections 1) LCIA method, normalisation, weighting 2) Data sources 3) Completeness, 4) Validation, and 5) Compliance declarations. (Builder)"""

    useAdviceForDataSet: Optional[STMultiLang] = None
    common_other: Optional[str] = Field(None, alias='common:other')
    _LCIAMethodNormalisationAndWeighting_1: Optional[LCIAMethodNormalisationAndWeightingBuilder] = None
    _dataSources: Optional[DataSourcesBuilder] = None
    _completeness: Optional[CompletenessBuilder] = None
    _validation: Optional[ValidationBuilder] = None
    _complianceDeclarations: Optional[ComplianceDeclarationsBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def LCIAMethodNormalisationAndWeighting_1(self) -> LCIAMethodNormalisationAndWeightingBuilder:
        """Access LCIAMethodNormalisationAndWeighting_1 builder (auto-initialized)."""
        if self._LCIAMethodNormalisationAndWeighting_1 is None:
            self._LCIAMethodNormalisationAndWeighting_1 = LCIAMethodNormalisationAndWeightingBuilder()
        return self._LCIAMethodNormalisationAndWeighting_1

    @property
    def dataSources(self) -> DataSourcesBuilder:
        """Access dataSources builder (auto-initialized)."""
        if self._dataSources is None:
            self._dataSources = DataSourcesBuilder()
        return self._dataSources

    @property
    def completeness(self) -> CompletenessBuilder:
        """Access completeness builder (auto-initialized)."""
        if self._completeness is None:
            self._completeness = CompletenessBuilder()
        return self._completeness

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

    def set_useAdviceForDataSet(self, text: str, lang: str = 'en') -> 'ModellingAndValidationBuilder':
        """Set useAdviceForDataSet text for a specific language."""
        if self.useAdviceForDataSet is None:
            self.useAdviceForDataSet = STMultiLang()

        # Update existing or add new
        for item in self.useAdviceForDataSet.items:
            if item.lang == lang:
                item.text = text
                return self

        self.useAdviceForDataSet.items.append(MultiLangItemST(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_useAdviceForDataSet(self, lang: str = 'en') -> Optional[str]:
        """Get useAdviceForDataSet text for a specific language."""
        if not self.useAdviceForDataSet:
            return None
        for item in self.useAdviceForDataSet.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> ModellingAndValidation:
        """Build the final ModellingAndValidation instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_LCIAMethodNormalisationAndWeighting_1', None)
        data.pop('_dataSources', None)
        data.pop('_completeness', None)
        data.pop('_validation', None)
        data.pop('_complianceDeclarations', None)

        # Build nested objects
        if self._LCIAMethodNormalisationAndWeighting_1 is not None:
            data['LCIAMethodNormalisationAndWeighting'] = self._LCIAMethodNormalisationAndWeighting_1.build()
        if self._dataSources is not None:
            data['dataSources'] = self._dataSources.build()
        if self._completeness is not None:
            data['completeness'] = self._completeness.build()
        if self._validation is not None:
            data['validation'] = self._validation.build()
        if self._complianceDeclarations is not None:
            data['complianceDeclarations'] = self._complianceDeclarations.build()

        return ModellingAndValidation.model_validate(data)

class LCIAMethodDataSetBuilder(BaseModel):
    """Builder for LCIAMethodDataSet."""

    field_xmlns: Optional[Literal['http://lca.jrc.it/ILCD/LCIAMethod']] = Field(None, alias='@xmlns')
    field_xmlns_common: Optional[Literal['http://lca.jrc.it/ILCD/Common']] = Field(None, alias='@xmlns:common')
    field_xmlns_xsi: Optional[Literal['http://www.w3.org/2001/XMLSchema-instance']] = Field(None, alias='@xmlns:xsi')
    field_version: Optional[Literal['1.1']] = Field(None, alias='@version')
    field_xsi_schemaLocation: Optional[Literal['http://lca.jrc.it/ILCD/LCIAMethod ../../schemas/ILCD_LCIAMethodDataSet.xsd']] = Field(None, alias='@xsi:schemaLocation')
    common_other: Optional[str] = Field(None, alias='common:other')
    _LCIAMethodInformation_1: Optional[LCIAMethodInformationBuilder] = None
    _modellingAndValidation: Optional[ModellingAndValidationBuilder] = None
    _administrativeInformation: Optional[AdministrativeInformationBuilder] = None
    _characterisationFactors: Optional[CharacterisationFactorsBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def LCIAMethodInformation_1(self) -> LCIAMethodInformationBuilder:
        """Access LCIAMethodInformation_1 builder (auto-initialized)."""
        if self._LCIAMethodInformation_1 is None:
            self._LCIAMethodInformation_1 = LCIAMethodInformationBuilder()
        return self._LCIAMethodInformation_1

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

    @property
    def characterisationFactors(self) -> CharacterisationFactorsBuilder:
        """Access characterisationFactors builder (auto-initialized)."""
        if self._characterisationFactors is None:
            self._characterisationFactors = CharacterisationFactorsBuilder()
        return self._characterisationFactors

    def build(self) -> LCIAMethodDataSet:
        """Build the final LCIAMethodDataSet instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_LCIAMethodInformation_1', None)
        data.pop('_modellingAndValidation', None)
        data.pop('_administrativeInformation', None)
        data.pop('_characterisationFactors', None)

        # Build nested objects
        if self._LCIAMethodInformation_1 is not None:
            data['LCIAMethodInformation'] = self._LCIAMethodInformation_1.build()
        if self._modellingAndValidation is not None:
            data['modellingAndValidation'] = self._modellingAndValidation.build()
        if self._administrativeInformation is not None:
            data['administrativeInformation'] = self._administrativeInformation.build()
        if self._characterisationFactors is not None:
            data['characterisationFactors'] = self._characterisationFactors.build()

        return LCIAMethodDataSet.model_validate(data)

class ModelBuilder(BaseModel):
    """Builder for Model."""

    _LCIAMethodDataSet_1: Optional[LCIAMethodDataSetBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,  # Can be overridden per instance
    )

    @property
    def LCIAMethodDataSet_1(self) -> LCIAMethodDataSetBuilder:
        """Access LCIAMethodDataSet_1 builder (auto-initialized)."""
        if self._LCIAMethodDataSet_1 is None:
            self._LCIAMethodDataSet_1 = LCIAMethodDataSetBuilder()
        return self._LCIAMethodDataSet_1

    def build(self) -> Model:
        """Build the final Model instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_LCIAMethodDataSet_1', None)

        # Build nested objects
        if self._LCIAMethodDataSet_1 is not None:
            data['LCIAMethodDataSet'] = self._LCIAMethodDataSet_1.build()

        return Model.model_validate(data)

class LCIAMethodInformationBuilder(BaseModel):
    """Builder for LCIAMethodInformation."""

    common_other: Optional[str] = Field(None, alias='common:other')
    _dataSetInformation: Optional[DataSetInformationBuilder] = None
    _quantitativeReference: Optional[QuantitativeReferenceBuilder] = None
    _time: Optional[TimeBuilder] = None
    _geography: Optional[GeographyBuilder] = None
    _impactModel: Optional[ImpactModelBuilder] = None

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
    def time(self) -> TimeBuilder:
        """Access time builder (auto-initialized)."""
        if self._time is None:
            self._time = TimeBuilder()
        return self._time

    @property
    def geography(self) -> GeographyBuilder:
        """Access geography builder (auto-initialized)."""
        if self._geography is None:
            self._geography = GeographyBuilder()
        return self._geography

    @property
    def impactModel(self) -> ImpactModelBuilder:
        """Access impactModel builder (auto-initialized)."""
        if self._impactModel is None:
            self._impactModel = ImpactModelBuilder()
        return self._impactModel

    def build(self) -> LCIAMethodInformation:
        """Build the final LCIAMethodInformation instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_dataSetInformation', None)
        data.pop('_quantitativeReference', None)
        data.pop('_time', None)
        data.pop('_geography', None)
        data.pop('_impactModel', None)

        # Build nested objects
        if self._dataSetInformation is not None:
            data['dataSetInformation'] = self._dataSetInformation.build()
        if self._quantitativeReference is not None:
            data['quantitativeReference'] = self._quantitativeReference.build()
        if self._time is not None:
            data['time'] = self._time.build()
        if self._geography is not None:
            data['geography'] = self._geography.build()
        if self._impactModel is not None:
            data['impactModel'] = self._impactModel.build()

        return LCIAMethodInformation.model_validate(data)
