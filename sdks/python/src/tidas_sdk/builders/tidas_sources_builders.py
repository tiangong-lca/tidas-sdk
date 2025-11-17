# Auto-generated builder classes for TIDAS entities
# DO NOT EDIT - Regenerate using scripts/generate_builders.py

from __future__ import annotations

from typing import List, Literal, Optional
from pydantic import AnyUrl, AwareDatetime, BaseModel, ConfigDict, Field, RootModel, field_validator
from enum import (
    Enum,
)
from tidas_sdk.types.tidas_sources_category import (
    Sources,
    TidasSourcesText,
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

from tidas_sdk.types.tidas_sources import *


class CommonClassBuilder(BaseModel):
    """Builder for CommonClass.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = CommonClassBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    field_level: Optional[Literal['0']] = Field(None, alias='@level')
    field_classId: Optional[Sources] = Field(None, alias='@classId')
    text: Optional[TidasSourcesText] = Field(None, alias='#text')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> CommonClass:
        """Build the final CommonClass instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonClass.model_validate(data)

    def build_dump(self, indent: int = 2) -> str:
        """Dump builder state including nested builders for debugging.
        
        Warning: This is for debugging only. The output structure differs
        from the final model. Use build() to create the actual model.
        
        Returns:
            JSON string with full builder state including nested builders
        """
        import json
        
        def _dump_builder(obj, depth=0, seen=None):
            """Recursively dump builder objects."""
            if seen is None:
                seen = set()
            
            # Prevent infinite recursion
            obj_id = id(obj)
            if obj_id in seen or depth > 20:
                return "<circular>"
            
            if isinstance(obj, BaseModel):
                seen.add(obj_id)
                result = {}
                
                # Dump regular fields from __dict__
                for field_name, field_value in obj.__dict__.items():
                    if field_value is None:
                        continue
                    if field_name.startswith("_"):
                        # Private field - include without underscore
                        clean_name = field_name[1:]
                        result[clean_name] = _dump_builder(field_value, depth+1, seen)
                    else:
                        result[field_name] = _dump_builder(field_value, depth+1, seen)
                
                seen.remove(obj_id)
                return result
            elif isinstance(obj, list):
                return [_dump_builder(item, depth+1, seen) for item in obj]
            elif isinstance(obj, dict):
                return {k: _dump_builder(v, depth+1, seen) for k, v in obj.items()}
            else:
                return obj
        
        return json.dumps(_dump_builder(self), indent=indent, default=str)

class CommonClassificationBuilder(BaseModel):
    """Builder for CommonClassification.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = CommonClassificationBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    common_other: Optional[str] = Field(None, alias='common:other')
    _common_class: Optional[CommonClassBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
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

    def build_dump(self, indent: int = 2) -> str:
        """Dump builder state including nested builders for debugging.
        
        Warning: This is for debugging only. The output structure differs
        from the final model. Use build() to create the actual model.
        
        Returns:
            JSON string with full builder state including nested builders
        """
        import json
        
        def _dump_builder(obj, depth=0, seen=None):
            """Recursively dump builder objects."""
            if seen is None:
                seen = set()
            
            # Prevent infinite recursion
            obj_id = id(obj)
            if obj_id in seen or depth > 20:
                return "<circular>"
            
            if isinstance(obj, BaseModel):
                seen.add(obj_id)
                result = {}
                
                # Dump regular fields from __dict__
                for field_name, field_value in obj.__dict__.items():
                    if field_value is None:
                        continue
                    if field_name.startswith("_"):
                        # Private field - include without underscore
                        clean_name = field_name[1:]
                        result[clean_name] = _dump_builder(field_value, depth+1, seen)
                    else:
                        result[field_name] = _dump_builder(field_value, depth+1, seen)
                
                seen.remove(obj_id)
                return result
            elif isinstance(obj, list):
                return [_dump_builder(item, depth+1, seen) for item in obj]
            elif isinstance(obj, dict):
                return {k: _dump_builder(v, depth+1, seen) for k, v in obj.items()}
            else:
                return obj
        
        return json.dumps(_dump_builder(self), indent=indent, default=str)

class ClassificationInformationBuilder(BaseModel):
    """Hierachical classification of the Source foreseen to be used to structure the Source content of the database. (Note: This entry is NOT required for the identification of a Source. It should nevertheless be avoided to use identical names for Source in the same class. (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = ClassificationInformationBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    _common_classification: Optional[CommonClassificationBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
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

    def build_dump(self, indent: int = 2) -> str:
        """Dump builder state including nested builders for debugging.
        
        Warning: This is for debugging only. The output structure differs
        from the final model. Use build() to create the actual model.
        
        Returns:
            JSON string with full builder state including nested builders
        """
        import json
        
        def _dump_builder(obj, depth=0, seen=None):
            """Recursively dump builder objects."""
            if seen is None:
                seen = set()
            
            # Prevent infinite recursion
            obj_id = id(obj)
            if obj_id in seen or depth > 20:
                return "<circular>"
            
            if isinstance(obj, BaseModel):
                seen.add(obj_id)
                result = {}
                
                # Dump regular fields from __dict__
                for field_name, field_value in obj.__dict__.items():
                    if field_value is None:
                        continue
                    if field_name.startswith("_"):
                        # Private field - include without underscore
                        clean_name = field_name[1:]
                        result[clean_name] = _dump_builder(field_value, depth+1, seen)
                    else:
                        result[field_name] = _dump_builder(field_value, depth+1, seen)
                
                seen.remove(obj_id)
                return result
            elif isinstance(obj, list):
                return [_dump_builder(item, depth+1, seen) for item in obj]
            elif isinstance(obj, dict):
                return {k: _dump_builder(v, depth+1, seen) for k, v in obj.items()}
            else:
                return obj
        
        return json.dumps(_dump_builder(self), indent=indent, default=str)

class ReferenceToDigitalFileBuilder(BaseModel):
    """Link to a digital file of the source (www-address or intranet-path; relative or absolue path). (Info: Allows direct access to e.g. complete reports of further documentation, which may also be digitally attached to this data set and exchanged jointly with the XML file.) (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = ReferenceToDigitalFileBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    field_uri: Optional[AnyUrl] = Field(None, alias='@uri')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> ReferenceToDigitalFile:
        """Build the final ReferenceToDigitalFile instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return ReferenceToDigitalFile.model_validate(data)

    def build_dump(self, indent: int = 2) -> str:
        """Dump builder state including nested builders for debugging.
        
        Warning: This is for debugging only. The output structure differs
        from the final model. Use build() to create the actual model.
        
        Returns:
            JSON string with full builder state including nested builders
        """
        import json
        
        def _dump_builder(obj, depth=0, seen=None):
            """Recursively dump builder objects."""
            if seen is None:
                seen = set()
            
            # Prevent infinite recursion
            obj_id = id(obj)
            if obj_id in seen or depth > 20:
                return "<circular>"
            
            if isinstance(obj, BaseModel):
                seen.add(obj_id)
                result = {}
                
                # Dump regular fields from __dict__
                for field_name, field_value in obj.__dict__.items():
                    if field_value is None:
                        continue
                    if field_name.startswith("_"):
                        # Private field - include without underscore
                        clean_name = field_name[1:]
                        result[clean_name] = _dump_builder(field_value, depth+1, seen)
                    else:
                        result[field_name] = _dump_builder(field_value, depth+1, seen)
                
                seen.remove(obj_id)
                return result
            elif isinstance(obj, list):
                return [_dump_builder(item, depth+1, seen) for item in obj]
            elif isinstance(obj, dict):
                return {k: _dump_builder(v, depth+1, seen) for k, v in obj.items()}
            else:
                return obj
        
        return json.dumps(_dump_builder(self), indent=indent, default=str)

class DataSetInformationBuilder(BaseModel):
    """Builder for DataSetInformation.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = DataSetInformationBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    common_UUID: Optional[str] = Field(None, alias='common:UUID')
    common_shortName: Optional[StringMultiLang] = Field(None, alias='common:shortName')
    sourceCitation: Optional[str] = None
    publicationType: Optional[PublicationType] = None
    sourceDescriptionOrComment: Optional[FTMultiLang] = None
    referenceToContact: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None
    referenceToLogo: Optional[GlobalReferenceType | list[GlobalReferenceType]] = None
    common_other: Optional[str] = Field(None, alias='common:other')
    _classificationInformation: Optional[ClassificationInformationBuilder] = None
    _referenceToDigitalFile: Optional[ReferenceToDigitalFileBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def classificationInformation(self) -> ClassificationInformationBuilder:
        """Access classificationInformation builder (auto-initialized)."""
        if self._classificationInformation is None:
            self._classificationInformation = ClassificationInformationBuilder()
        return self._classificationInformation

    @property
    def referenceToDigitalFile(self) -> ReferenceToDigitalFileBuilder:
        """Access referenceToDigitalFile builder (auto-initialized)."""
        if self._referenceToDigitalFile is None:
            self._referenceToDigitalFile = ReferenceToDigitalFileBuilder()
        return self._referenceToDigitalFile

    @field_validator('common_shortName', mode='before')
    @classmethod
    def _convert_string_multilang(cls, v):
        """Auto-convert dict or list[dict] to StringMultiLang."""
        if v is None or isinstance(v, StringMultiLang):
            return v
        
        ml = StringMultiLang()
        if isinstance(v, dict):
            ml.items.append(MultiLangItemString(**v))
        elif isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    ml.items.append(MultiLangItemString(**item))
        return ml

    @field_validator('sourceDescriptionOrComment', mode='before')
    @classmethod
    def _convert_ft_multilang(cls, v):
        """Auto-convert dict or list[dict] to FTMultiLang."""
        if v is None or isinstance(v, FTMultiLang):
            return v
        
        ml = FTMultiLang()
        if isinstance(v, dict):
            ml.items.append(MultiLangItem(**v))
        elif isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    ml.items.append(MultiLangItem(**item))
        return ml

    def set_shortName(self, text: str, lang: str = 'en') -> 'DataSetInformationBuilder':
        """Set common_shortName text for a specific language."""
        if self.common_shortName is None:
            self.common_shortName = StringMultiLang()

        # Update existing or add new
        for item in self.common_shortName.items:
            if item.lang == lang:
                item.text = text
                return self

        self.common_shortName.items.append(MultiLangItemString(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_shortName(self, lang: str = 'en') -> Optional[str]:
        """Get common_shortName text for a specific language."""
        if not self.common_shortName:
            return None
        for item in self.common_shortName.items:
            if item.lang == lang:
                return item.text
        return None

    def set_sourceDescriptionOrComment(self, text: str, lang: str = 'en') -> 'DataSetInformationBuilder':
        """Set sourceDescriptionOrComment text for a specific language."""
        if self.sourceDescriptionOrComment is None:
            self.sourceDescriptionOrComment = FTMultiLang()

        # Update existing or add new
        for item in self.sourceDescriptionOrComment.items:
            if item.lang == lang:
                item.text = text
                return self

        self.sourceDescriptionOrComment.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_sourceDescriptionOrComment(self, lang: str = 'en') -> Optional[str]:
        """Get sourceDescriptionOrComment text for a specific language."""
        if not self.sourceDescriptionOrComment:
            return None
        for item in self.sourceDescriptionOrComment.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> DataSetInformation:
        """Build the final DataSetInformation instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_classificationInformation', None)
        data.pop('_referenceToDigitalFile', None)

        # Build nested objects
        if self._classificationInformation is not None:
            data['classificationInformation'] = self._classificationInformation.build()
        if self._referenceToDigitalFile is not None:
            data['referenceToDigitalFile'] = self._referenceToDigitalFile.build()

        return DataSetInformation.model_validate(data)

    def build_dump(self, indent: int = 2) -> str:
        """Dump builder state including nested builders for debugging.
        
        Warning: This is for debugging only. The output structure differs
        from the final model. Use build() to create the actual model.
        
        Returns:
            JSON string with full builder state including nested builders
        """
        import json
        
        def _dump_builder(obj, depth=0, seen=None):
            """Recursively dump builder objects."""
            if seen is None:
                seen = set()
            
            # Prevent infinite recursion
            obj_id = id(obj)
            if obj_id in seen or depth > 20:
                return "<circular>"
            
            if isinstance(obj, BaseModel):
                seen.add(obj_id)
                result = {}
                
                # Dump regular fields from __dict__
                for field_name, field_value in obj.__dict__.items():
                    if field_value is None:
                        continue
                    if field_name.startswith("_"):
                        # Private field - include without underscore
                        clean_name = field_name[1:]
                        result[clean_name] = _dump_builder(field_value, depth+1, seen)
                    else:
                        result[field_name] = _dump_builder(field_value, depth+1, seen)
                
                seen.remove(obj_id)
                return result
            elif isinstance(obj, list):
                return [_dump_builder(item, depth+1, seen) for item in obj]
            elif isinstance(obj, dict):
                return {k: _dump_builder(v, depth+1, seen) for k, v in obj.items()}
            else:
                return obj
        
        return json.dumps(_dump_builder(self), indent=indent, default=str)

class SourceInformationBuilder(BaseModel):
    """Builder for SourceInformation.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = SourceInformationBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    common_other: Optional[str] = Field(None, alias='common:other')
    _dataSetInformation: Optional[DataSetInformationBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def dataSetInformation(self) -> DataSetInformationBuilder:
        """Access dataSetInformation builder (auto-initialized)."""
        if self._dataSetInformation is None:
            self._dataSetInformation = DataSetInformationBuilder()
        return self._dataSetInformation

    def build(self) -> SourceInformation:
        """Build the final SourceInformation instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_dataSetInformation', None)

        # Build nested objects
        if self._dataSetInformation is not None:
            data['dataSetInformation'] = self._dataSetInformation.build()

        return SourceInformation.model_validate(data)

    def build_dump(self, indent: int = 2) -> str:
        """Dump builder state including nested builders for debugging.
        
        Warning: This is for debugging only. The output structure differs
        from the final model. Use build() to create the actual model.
        
        Returns:
            JSON string with full builder state including nested builders
        """
        import json
        
        def _dump_builder(obj, depth=0, seen=None):
            """Recursively dump builder objects."""
            if seen is None:
                seen = set()
            
            # Prevent infinite recursion
            obj_id = id(obj)
            if obj_id in seen or depth > 20:
                return "<circular>"
            
            if isinstance(obj, BaseModel):
                seen.add(obj_id)
                result = {}
                
                # Dump regular fields from __dict__
                for field_name, field_value in obj.__dict__.items():
                    if field_value is None:
                        continue
                    if field_name.startswith("_"):
                        # Private field - include without underscore
                        clean_name = field_name[1:]
                        result[clean_name] = _dump_builder(field_value, depth+1, seen)
                    else:
                        result[field_name] = _dump_builder(field_value, depth+1, seen)
                
                seen.remove(obj_id)
                return result
            elif isinstance(obj, list):
                return [_dump_builder(item, depth+1, seen) for item in obj]
            elif isinstance(obj, dict):
                return {k: _dump_builder(v, depth+1, seen) for k, v in obj.items()}
            else:
                return obj
        
        return json.dumps(_dump_builder(self), indent=indent, default=str)

class DataEntryByBuilder(BaseModel):
    """Builder for DataEntryBy.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = DataEntryByBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    common_timeStamp: Optional[AwareDatetime] = Field(None, alias='common:timeStamp')
    common_referenceToDataSetFormat: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToDataSetFormat')
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> DataEntryBy:
        """Build the final DataEntryBy instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return DataEntryBy.model_validate(data)

    def build_dump(self, indent: int = 2) -> str:
        """Dump builder state including nested builders for debugging.
        
        Warning: This is for debugging only. The output structure differs
        from the final model. Use build() to create the actual model.
        
        Returns:
            JSON string with full builder state including nested builders
        """
        import json
        
        def _dump_builder(obj, depth=0, seen=None):
            """Recursively dump builder objects."""
            if seen is None:
                seen = set()
            
            # Prevent infinite recursion
            obj_id = id(obj)
            if obj_id in seen or depth > 20:
                return "<circular>"
            
            if isinstance(obj, BaseModel):
                seen.add(obj_id)
                result = {}
                
                # Dump regular fields from __dict__
                for field_name, field_value in obj.__dict__.items():
                    if field_value is None:
                        continue
                    if field_name.startswith("_"):
                        # Private field - include without underscore
                        clean_name = field_name[1:]
                        result[clean_name] = _dump_builder(field_value, depth+1, seen)
                    else:
                        result[field_name] = _dump_builder(field_value, depth+1, seen)
                
                seen.remove(obj_id)
                return result
            elif isinstance(obj, list):
                return [_dump_builder(item, depth+1, seen) for item in obj]
            elif isinstance(obj, dict):
                return {k: _dump_builder(v, depth+1, seen) for k, v in obj.items()}
            else:
                return obj
        
        return json.dumps(_dump_builder(self), indent=indent, default=str)

class PublicationAndOwnershipBuilder(BaseModel):
    """Information related to publication and version management of the data set including copyright and access restrictions. (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = PublicationAndOwnershipBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    common_dataSetVersion: Optional[str] = Field(None, alias='common:dataSetVersion')
    common_referenceToPrecedingDataSetVersion: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToPrecedingDataSetVersion')
    common_permanentDataSetURI: Optional[AnyUrl] = Field(None, alias='common:permanentDataSetURI')
    common_referenceToOwnershipOfDataSet: Optional[GlobalReferenceType | list[GlobalReferenceType]] = Field(None, alias='common:referenceToOwnershipOfDataSet')
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> PublicationAndOwnership:
        """Build the final PublicationAndOwnership instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return PublicationAndOwnership.model_validate(data)

    def build_dump(self, indent: int = 2) -> str:
        """Dump builder state including nested builders for debugging.
        
        Warning: This is for debugging only. The output structure differs
        from the final model. Use build() to create the actual model.
        
        Returns:
            JSON string with full builder state including nested builders
        """
        import json
        
        def _dump_builder(obj, depth=0, seen=None):
            """Recursively dump builder objects."""
            if seen is None:
                seen = set()
            
            # Prevent infinite recursion
            obj_id = id(obj)
            if obj_id in seen or depth > 20:
                return "<circular>"
            
            if isinstance(obj, BaseModel):
                seen.add(obj_id)
                result = {}
                
                # Dump regular fields from __dict__
                for field_name, field_value in obj.__dict__.items():
                    if field_value is None:
                        continue
                    if field_name.startswith("_"):
                        # Private field - include without underscore
                        clean_name = field_name[1:]
                        result[clean_name] = _dump_builder(field_value, depth+1, seen)
                    else:
                        result[field_name] = _dump_builder(field_value, depth+1, seen)
                
                seen.remove(obj_id)
                return result
            elif isinstance(obj, list):
                return [_dump_builder(item, depth+1, seen) for item in obj]
            elif isinstance(obj, dict):
                return {k: _dump_builder(v, depth+1, seen) for k, v in obj.items()}
            else:
                return obj
        
        return json.dumps(_dump_builder(self), indent=indent, default=str)

class AdministrativeInformationBuilder(BaseModel):
    """Information on data set management and administration. (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = AdministrativeInformationBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    common_other: Optional[str] = Field(None, alias='common:other')
    _dataEntryBy: Optional[DataEntryByBuilder] = None
    _publicationAndOwnership: Optional[PublicationAndOwnershipBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
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

    def build_dump(self, indent: int = 2) -> str:
        """Dump builder state including nested builders for debugging.
        
        Warning: This is for debugging only. The output structure differs
        from the final model. Use build() to create the actual model.
        
        Returns:
            JSON string with full builder state including nested builders
        """
        import json
        
        def _dump_builder(obj, depth=0, seen=None):
            """Recursively dump builder objects."""
            if seen is None:
                seen = set()
            
            # Prevent infinite recursion
            obj_id = id(obj)
            if obj_id in seen or depth > 20:
                return "<circular>"
            
            if isinstance(obj, BaseModel):
                seen.add(obj_id)
                result = {}
                
                # Dump regular fields from __dict__
                for field_name, field_value in obj.__dict__.items():
                    if field_value is None:
                        continue
                    if field_name.startswith("_"):
                        # Private field - include without underscore
                        clean_name = field_name[1:]
                        result[clean_name] = _dump_builder(field_value, depth+1, seen)
                    else:
                        result[field_name] = _dump_builder(field_value, depth+1, seen)
                
                seen.remove(obj_id)
                return result
            elif isinstance(obj, list):
                return [_dump_builder(item, depth+1, seen) for item in obj]
            elif isinstance(obj, dict):
                return {k: _dump_builder(v, depth+1, seen) for k, v in obj.items()}
            else:
                return obj
        
        return json.dumps(_dump_builder(self), indent=indent, default=str)

class SourceDataSetBuilder(BaseModel):
    """Builder for SourceDataSet.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = SourceDataSetBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    field_xmlns_common: Optional[Literal['http://lca.jrc.it/ILCD/Common']] = Field(None, alias='@xmlns:common')
    field_xmlns: Optional[Literal['http://lca.jrc.it/ILCD/Source']] = Field(None, alias='@xmlns')
    field_xmlns_xsi: Optional[Literal['http://www.w3.org/2001/XMLSchema-instance']] = Field(None, alias='@xmlns:xsi')
    field_version: Optional[Literal['1.1']] = Field(None, alias='@version')
    field_xsi_schemaLocation: Optional[Literal['http://lca.jrc.it/ILCD/Source ../../schemas/ILCD_SourceDataSet.xsd']] = Field(None, alias='@xsi:schemaLocation')
    common_other: Optional[str] = Field(None, alias='common:other')
    _sourceInformation: Optional[SourceInformationBuilder] = None
    _administrativeInformation: Optional[AdministrativeInformationBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def sourceInformation(self) -> SourceInformationBuilder:
        """Access sourceInformation builder (auto-initialized)."""
        if self._sourceInformation is None:
            self._sourceInformation = SourceInformationBuilder()
        return self._sourceInformation

    @property
    def administrativeInformation(self) -> AdministrativeInformationBuilder:
        """Access administrativeInformation builder (auto-initialized)."""
        if self._administrativeInformation is None:
            self._administrativeInformation = AdministrativeInformationBuilder()
        return self._administrativeInformation

    def build(self) -> SourceDataSet:
        """Build the final SourceDataSet instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_sourceInformation', None)
        data.pop('_administrativeInformation', None)

        # Build nested objects
        if self._sourceInformation is not None:
            data['sourceInformation'] = self._sourceInformation.build()
        if self._administrativeInformation is not None:
            data['administrativeInformation'] = self._administrativeInformation.build()

        return SourceDataSet.model_validate(data)

    def build_dump(self, indent: int = 2) -> str:
        """Dump builder state including nested builders for debugging.
        
        Warning: This is for debugging only. The output structure differs
        from the final model. Use build() to create the actual model.
        
        Returns:
            JSON string with full builder state including nested builders
        """
        import json
        
        def _dump_builder(obj, depth=0, seen=None):
            """Recursively dump builder objects."""
            if seen is None:
                seen = set()
            
            # Prevent infinite recursion
            obj_id = id(obj)
            if obj_id in seen or depth > 20:
                return "<circular>"
            
            if isinstance(obj, BaseModel):
                seen.add(obj_id)
                result = {}
                
                # Dump regular fields from __dict__
                for field_name, field_value in obj.__dict__.items():
                    if field_value is None:
                        continue
                    if field_name.startswith("_"):
                        # Private field - include without underscore
                        clean_name = field_name[1:]
                        result[clean_name] = _dump_builder(field_value, depth+1, seen)
                    else:
                        result[field_name] = _dump_builder(field_value, depth+1, seen)
                
                seen.remove(obj_id)
                return result
            elif isinstance(obj, list):
                return [_dump_builder(item, depth+1, seen) for item in obj]
            elif isinstance(obj, dict):
                return {k: _dump_builder(v, depth+1, seen) for k, v in obj.items()}
            else:
                return obj
        
        return json.dumps(_dump_builder(self), indent=indent, default=str)

class ModelBuilder(BaseModel):
    """Builder for Model.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = ModelBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    _sourceDataSet: Optional[SourceDataSetBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def sourceDataSet(self) -> SourceDataSetBuilder:
        """Access sourceDataSet builder (auto-initialized)."""
        if self._sourceDataSet is None:
            self._sourceDataSet = SourceDataSetBuilder()
        return self._sourceDataSet

    def build(self) -> Model:
        """Build the final Model instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_sourceDataSet', None)

        # Build nested objects
        if self._sourceDataSet is not None:
            data['sourceDataSet'] = self._sourceDataSet.build()

        return Model.model_validate(data)

    def build_dump(self, indent: int = 2) -> str:
        """Dump builder state including nested builders for debugging.
        
        Warning: This is for debugging only. The output structure differs
        from the final model. Use build() to create the actual model.
        
        Returns:
            JSON string with full builder state including nested builders
        """
        import json
        
        def _dump_builder(obj, depth=0, seen=None):
            """Recursively dump builder objects."""
            if seen is None:
                seen = set()
            
            # Prevent infinite recursion
            obj_id = id(obj)
            if obj_id in seen or depth > 20:
                return "<circular>"
            
            if isinstance(obj, BaseModel):
                seen.add(obj_id)
                result = {}
                
                # Dump regular fields from __dict__
                for field_name, field_value in obj.__dict__.items():
                    if field_value is None:
                        continue
                    if field_name.startswith("_"):
                        # Private field - include without underscore
                        clean_name = field_name[1:]
                        result[clean_name] = _dump_builder(field_value, depth+1, seen)
                    else:
                        result[field_name] = _dump_builder(field_value, depth+1, seen)
                
                seen.remove(obj_id)
                return result
            elif isinstance(obj, list):
                return [_dump_builder(item, depth+1, seen) for item in obj]
            elif isinstance(obj, dict):
                return {k: _dump_builder(v, depth+1, seen) for k, v in obj.items()}
            else:
                return obj
        
        return json.dumps(_dump_builder(self), indent=indent, default=str)

# Rebuild models to resolve forward references
CommonClassBuilder.model_rebuild()
CommonClassificationBuilder.model_rebuild()
ClassificationInformationBuilder.model_rebuild()
ReferenceToDigitalFileBuilder.model_rebuild()
DataSetInformationBuilder.model_rebuild()
SourceInformationBuilder.model_rebuild()
DataEntryByBuilder.model_rebuild()
PublicationAndOwnershipBuilder.model_rebuild()
AdministrativeInformationBuilder.model_rebuild()
SourceDataSetBuilder.model_rebuild()
ModelBuilder.model_rebuild()
