# Auto-generated builder classes for TIDAS entities
# DO NOT EDIT - Regenerate using scripts/generate_builders.py

from __future__ import annotations

from typing import List, Literal, Optional
from pydantic import AnyUrl, AwareDatetime, BaseModel, ConfigDict, Field, RootModel, field_validator
from enum import (
    Enum,
)
from tidas_sdk.types.tidas_locations_category import (
    Locations,
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

from tidas_sdk.types.tidas_processes import *


class CommonClasBuilder(BaseModel):
    """Builder for CommonClas.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = CommonClasBuilder()
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
    field_classId: Optional[Processes] = Field(None, alias='@classId')
    text: Optional[TidasProcessesText] = Field(None, alias='#text')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> CommonClas:
        """Build the final CommonClas instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonClas.model_validate(data)

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

class CommonClas1Builder(BaseModel):
    """Builder for CommonClas1.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = CommonClas1Builder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    field_level: Optional[Literal['1']] = Field(None, alias='@level')
    field_classId: Optional[Processes] = Field(None, alias='@classId')
    text: Optional[TidasProcessesText] = Field(None, alias='#text')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> CommonClas1:
        """Build the final CommonClas1 instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonClas1.model_validate(data)

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

class CommonClas2Builder(BaseModel):
    """Builder for CommonClas2.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = CommonClas2Builder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    field_level: Optional[Literal['2']] = Field(None, alias='@level')
    field_classId: Optional[Processes] = Field(None, alias='@classId')
    text: Optional[TidasProcessesText] = Field(None, alias='#text')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> CommonClas2:
        """Build the final CommonClas2 instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonClas2.model_validate(data)

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

class CommonClas3Builder(BaseModel):
    """Builder for CommonClas3.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = CommonClas3Builder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    field_level: Optional[Literal['3']] = Field(None, alias='@level')
    field_classId: Optional[Processes] = Field(None, alias='@classId')
    text: Optional[TidasProcessesText] = Field(None, alias='#text')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> CommonClas3:
        """Build the final CommonClas3 instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonClas3.model_validate(data)

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
    """Optional statistical or other classification of the data set. Typically also used for structuring LCA databases. (Builder)
    
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
    _common_class: List[CommonClas | CommonClas1 | CommonClas2 | CommonClas3Builder] = []

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def common_class(self) -> List[CommonClas | CommonClas1 | CommonClas2 | CommonClas3Builder]:
        """Access common_class builder list."""
        return self._common_class

    @common_class.setter
    def common_class(self, value: List[CommonClas | CommonClas1 | CommonClas2 | CommonClas3Builder]) -> None:
        """Set common_class builder list."""
        self._common_class = value

    def add_common_cla(self) -> CommonClas | CommonClas1 | CommonClas2 | CommonClas3Builder:
        """Add and return a new CommonClas | CommonClas1 | CommonClas2 | CommonClas3 builder."""
        builder = CommonClasBuilder()
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
    """Hierarchical or flat classification of the good, service or function that is provided by this life cycle model; typically used to structure database contents in LCA software, among other purposes. (Note: This entry is NOT required for the identification of a Life cycle model, but it should nevertheless be avoided to use identical names for Life cycle model data sets in the same class. The ILCD classifications are defined in the ILCDClassifications.xml file, for common use.) (Builder)
    
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

class CompletenessElementaryFlowsBuilder(BaseModel):
    """Completeness of the elementary flows in the Inputs and Outputs section of this data set from impact perspective, regarding addressing the individual mid-point problem field / impact category given. The completeness refers to the state-of-the-art of scientific knowledge whether or not an individual elementary flow contributes to the respective mid-point topic in a relevant way, which is e.g. the basis for the ILCD reference elementary flows. [Note: The "Completeness" statement does not automatically mean that related LCIA methods exist or reference the elementary flows of this data set. Hence for direct applicability of existing LCIA methods, check the field "Supported LCIA method data sets".] (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = CompletenessElementaryFlowsBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    field_type: Optional[FieldType1] = Field(None, alias='@type')
    field_value: Optional[FieldValue] = Field(None, alias='@value')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> CompletenessElementaryFlows:
        """Build the final CompletenessElementaryFlows instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CompletenessElementaryFlows.model_validate(data)

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

class NameBuilder(BaseModel):
    """General descriptive and specifying name of the process. (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = NameBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    baseName: Optional[StringMultiLang] = None
    treatmentStandardsRoutes: Optional[StringMultiLang] = None
    mixAndLocationTypes: Optional[StringMultiLang] = None
    functionalUnitFlowProperties: Optional[StringMultiLang] = None
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @field_validator('baseName', 'treatmentStandardsRoutes', 'mixAndLocationTypes', 'functionalUnitFlowProperties', mode='before')
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

class CommonMethodBuilder(BaseModel):
    """Validation method(s) used in the respective "Scope of review". (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = CommonMethodBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    field_name: Optional[FieldName1] = Field(None, alias='@name')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> CommonMethod:
        """Build the final CommonMethod instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonMethod.model_validate(data)

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

class CommonMethodItemBuilder(BaseModel):
    """Builder for CommonMethodItem.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = CommonMethodItemBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    field_name: Optional[FieldName1] = Field(None, alias='@name')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> CommonMethodItem:
        """Build the final CommonMethodItem instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonMethodItem.model_validate(data)

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

class CommonScopeBuilder(BaseModel):
    """Scope of review regarding which aspects and components of the data set was reviewed or verified. In case of aggregated e.g. LCI results also and on which level of detail (e.g. LCI results only, included unit processes, ...) the review / verification was performed. (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = CommonScopeBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    field_name: Optional[FieldName] = Field(None, alias='@name')
    _common_method: Optional[CommonMethodBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
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

class CommonScopeItemBuilder(BaseModel):
    """Builder for CommonScopeItem.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = CommonScopeItemBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    field_name: Optional[FieldName] = Field(None, alias='@name')
    common_method: Optional[CommonMethod1 | list[CommonMethodItem1]] = Field(None, alias='common:method')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> CommonScopeItem:
        """Build the final CommonScopeItem instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonScopeItem.model_validate(data)

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

class CommonDataQualityIndicatorBuilder(BaseModel):
    """Data quality indicators serve to provide the reviewed key information on the data set in a defined, computer-readable (and hence searchable) form. This serves to support LCA practitioners to identify/select the highest quality and most appropriate data sets. (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = CommonDataQualityIndicatorBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    field_name: Optional[FieldName6] = Field(None, alias='@name')
    field_value: Optional[FieldValue1] = Field(None, alias='@value')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> CommonDataQualityIndicator:
        """Build the final CommonDataQualityIndicator instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonDataQualityIndicator.model_validate(data)

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

class CommonDataQualityIndicatorItemBuilder(BaseModel):
    """Builder for CommonDataQualityIndicatorItem.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = CommonDataQualityIndicatorItemBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    field_name: Optional[FieldName6] = Field(None, alias='@name')
    field_value: Optional[FieldValue1] = Field(None, alias='@value')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> CommonDataQualityIndicatorItem:
        """Build the final CommonDataQualityIndicatorItem instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonDataQualityIndicatorItem.model_validate(data)

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

class CommonDataQualityIndicatorsBuilder(BaseModel):
    """Data quality indicators serve to provide the reviewed key information on the data set in a defined, computer-readable (and hence searchable) form. This serves to support LCA practitioners to identify/select the highest quality and most appropriate data sets. (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = CommonDataQualityIndicatorsBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    _common_dataQualityIndicator: Optional[CommonDataQualityIndicatorBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def common_dataQualityIndicator(self) -> CommonDataQualityIndicatorBuilder:
        """Access common_dataQualityIndicator builder (auto-initialized)."""
        if self._common_dataQualityIndicator is None:
            self._common_dataQualityIndicator = CommonDataQualityIndicatorBuilder()
        return self._common_dataQualityIndicator

    def build(self) -> CommonDataQualityIndicators:
        """Build the final CommonDataQualityIndicators instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_common_dataQualityIndicator', None)

        # Build nested objects
        if self._common_dataQualityIndicator is not None:
            data['common:dataQualityIndicator'] = self._common_dataQualityIndicator.build()

        return CommonDataQualityIndicators.model_validate(data)

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

class GlobalReferenceTypeBuilder(BaseModel):
    """Builder for GlobalReferenceType.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = GlobalReferenceTypeBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    _root: Optional[GlobalReferenceTypeBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def root(self) -> GlobalReferenceTypeBuilder:
        """Access root builder (auto-initialized)."""
        if self._root is None:
            self._root = GlobalReferenceTypeBuilder()
        return self._root

    def build(self) -> GlobalReferenceType:
        """Build the final GlobalReferenceType instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_root', None)

        # Build nested objects
        if self._root is not None:
            data['root'] = self._root.build()

        return GlobalReferenceType.model_validate(data)

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

class ComplementingProcessesBuilder(BaseModel):
    """Builder for ComplementingProcesses.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = ComplementingProcessesBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    _referenceToComplementingProcess: Optional[GlobalReferenceTypeBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def referenceToComplementingProcess(self) -> GlobalReferenceTypeBuilder:
        """Access referenceToComplementingProcess builder (auto-initialized)."""
        if self._referenceToComplementingProcess is None:
            self._referenceToComplementingProcess = GlobalReferenceTypeBuilder()
        return self._referenceToComplementingProcess

    def build(self) -> ComplementingProcesses:
        """Build the final ComplementingProcesses instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_referenceToComplementingProcess', None)

        # Build nested objects
        if self._referenceToComplementingProcess is not None:
            data['referenceToComplementingProcess'] = self._referenceToComplementingProcess.build()

        return ComplementingProcesses.model_validate(data)

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
    """General data set information. Section covers all single fields in the ISO/TS 14048 "Process description", which are not part of the other sub-sections. In ISO/TS 14048 no own sub-section is foreseen for these entries. (Builder)
    
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
    identifierOfSubDataSet: Optional[str] = None
    common_synonyms: Optional[FTMultiLang] = Field(None, alias='common:synonyms')
    common_generalComment: Optional[FTMultiLang] = Field(None, alias='common:generalComment')
    common_other: Optional[str] = Field(None, alias='common:other')
    _name: Optional[NameBuilder] = None
    _complementingProcesses: Optional[ComplementingProcessesBuilder] = None
    _classificationInformation: Optional[ClassificationInformationBuilder] = None
    _referenceToExternalDocumentation: Optional[GlobalReferenceTypeBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def name(self) -> NameBuilder:
        """Access name builder (auto-initialized)."""
        if self._name is None:
            self._name = NameBuilder()
        return self._name

    @property
    def complementingProcesses(self) -> ComplementingProcessesBuilder:
        """Access complementingProcesses builder (auto-initialized)."""
        if self._complementingProcesses is None:
            self._complementingProcesses = ComplementingProcessesBuilder()
        return self._complementingProcesses

    @property
    def classificationInformation(self) -> ClassificationInformationBuilder:
        """Access classificationInformation builder (auto-initialized)."""
        if self._classificationInformation is None:
            self._classificationInformation = ClassificationInformationBuilder()
        return self._classificationInformation

    @property
    def referenceToExternalDocumentation(self) -> GlobalReferenceTypeBuilder:
        """Access referenceToExternalDocumentation builder (auto-initialized)."""
        if self._referenceToExternalDocumentation is None:
            self._referenceToExternalDocumentation = GlobalReferenceTypeBuilder()
        return self._referenceToExternalDocumentation

    @field_validator('common_synonyms', 'common_generalComment', mode='before')
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

    def set_synonyms(self, text: str, lang: str = 'en') -> 'DataSetInformationBuilder':
        """Set common_synonyms text for a specific language."""
        if self.common_synonyms is None:
            self.common_synonyms = FTMultiLang()

        # Update existing or add new
        for item in self.common_synonyms.items:
            if item.lang == lang:
                item.text = text
                return self

        self.common_synonyms.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
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

        self.common_generalComment.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
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
        data.pop('_complementingProcesses', None)
        data.pop('_classificationInformation', None)
        data.pop('_referenceToExternalDocumentation', None)

        # Build nested objects
        if self._name is not None:
            data['name'] = self._name.build()
        if self._complementingProcesses is not None:
            data['complementingProcesses'] = self._complementingProcesses.build()
        if self._classificationInformation is not None:
            data['classificationInformation'] = self._classificationInformation.build()
        if self._referenceToExternalDocumentation is not None:
            data['referenceToExternalDocumentation'] = self._referenceToExternalDocumentation.build()

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

class QuantitativeReferenceBuilder(BaseModel):
    """This section names the quantitative reference used for this data set, i.e. the reference to which the inputs and outputs quantiatively relate. (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = QuantitativeReferenceBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    field_type: Optional[FieldType] = Field(None, alias='@type')
    referenceToReferenceFlow: Optional[str] = None
    functionalUnitOrOther: Optional[StringMultiLang] = None
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @field_validator('functionalUnitOrOther', mode='before')
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

    def set_functionalUnitOrOther(self, text: str, lang: str = 'en') -> 'QuantitativeReferenceBuilder':
        """Set functionalUnitOrOther text for a specific language."""
        if self.functionalUnitOrOther is None:
            self.functionalUnitOrOther = StringMultiLang()

        # Update existing or add new
        for item in self.functionalUnitOrOther.items:
            if item.lang == lang:
                item.text = text
                return self

        self.functionalUnitOrOther.items.append(MultiLangItemString(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_functionalUnitOrOther(self, lang: str = 'en') -> Optional[str]:
        """Get functionalUnitOrOther text for a specific language."""
        if not self.functionalUnitOrOther:
            return None
        for item in self.functionalUnitOrOther.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> QuantitativeReference:
        """Build the final QuantitativeReference instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return QuantitativeReference.model_validate(data)

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

class TimeBuilder(BaseModel):
    """Builder for Time.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = TimeBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    common_referenceYear: Optional[int] = Field(None, alias='common:referenceYear')
    common_dataSetValidUntil: Optional[int] = Field(None, alias='common:dataSetValidUntil')
    common_timeRepresentativenessDescription: Optional[FTMultiLang] = Field(None, alias='common:timeRepresentativenessDescription')
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @field_validator('common_timeRepresentativenessDescription', mode='before')
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

    def set_timeRepresentativenessDescription(self, text: str, lang: str = 'en') -> 'TimeBuilder':
        """Set common_timeRepresentativenessDescription text for a specific language."""
        if self.common_timeRepresentativenessDescription is None:
            self.common_timeRepresentativenessDescription = FTMultiLang()

        # Update existing or add new
        for item in self.common_timeRepresentativenessDescription.items:
            if item.lang == lang:
                item.text = text
                return self

        self.common_timeRepresentativenessDescription.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_timeRepresentativenessDescription(self, lang: str = 'en') -> Optional[str]:
        """Get common_timeRepresentativenessDescription text for a specific language."""
        if not self.common_timeRepresentativenessDescription:
            return None
        for item in self.common_timeRepresentativenessDescription.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> Time:
        """Build the final Time instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return Time.model_validate(data)

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

class LocationOfOperationSupplyOrProductionBuilder(BaseModel):
    """Location, country or region the data set represents. [Note 1: This field does not refer to e.g. the country in which a specific site is located that is represented by this data set but to the actually represented country, region, or site. Note 2: Entry can be of type "two-letter ISO 3166 country code" for countries, "seven-letter regional codes" for regions or continents, or "market areas and market organisations", as predefined for the ILCD. Also a name for e.g. a specific plant etc. can be given here (e.g. "FR, Lyon, XY Company, Z Site"; user defined). Note 3: The fact whether the entry refers to production or to consumption / supply has to be stated in the name-field "Mix and location types" e.g. as "Production mix".] (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = LocationOfOperationSupplyOrProductionBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    field_location: Optional[Locations] = Field(None, alias='@location')
    field_latitudeAndLongitude: Optional[str] = Field(None, alias='@latitudeAndLongitude')
    descriptionOfRestrictions: Optional[FTMultiLang] = None
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @field_validator('descriptionOfRestrictions', mode='before')
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

    def set_descriptionOfRestrictions(self, text: str, lang: str = 'en') -> 'LocationOfOperationSupplyOrProductionBuilder':
        """Set descriptionOfRestrictions text for a specific language."""
        if self.descriptionOfRestrictions is None:
            self.descriptionOfRestrictions = FTMultiLang()

        # Update existing or add new
        for item in self.descriptionOfRestrictions.items:
            if item.lang == lang:
                item.text = text
                return self

        self.descriptionOfRestrictions.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_descriptionOfRestrictions(self, lang: str = 'en') -> Optional[str]:
        """Get descriptionOfRestrictions text for a specific language."""
        if not self.descriptionOfRestrictions:
            return None
        for item in self.descriptionOfRestrictions.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> LocationOfOperationSupplyOrProduction:
        """Build the final LocationOfOperationSupplyOrProduction instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return LocationOfOperationSupplyOrProduction.model_validate(data)

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

class SubLocationOfOperationSupplyOrProductionBuilder(BaseModel):
    """One or more geographical sub-unit(s) of the stated "Location". Such sub-units can be e.g. the sampling sites of a company-average data set, the countries of a region-average data set, or specific sites in a country-average data set. [Note: For single site data sets this field is empty and the site is named in the "Location" field.] (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = SubLocationOfOperationSupplyOrProductionBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    field_subLocation: Optional[Locations] = Field(None, alias='@subLocation')
    field_latitudeAndLongitude: Optional[str] = Field(None, alias='@latitudeAndLongitude')
    descriptionOfRestrictions: Optional[FTMultiLang] = None
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @field_validator('descriptionOfRestrictions', mode='before')
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

    def set_descriptionOfRestrictions(self, text: str, lang: str = 'en') -> 'SubLocationOfOperationSupplyOrProductionBuilder':
        """Set descriptionOfRestrictions text for a specific language."""
        if self.descriptionOfRestrictions is None:
            self.descriptionOfRestrictions = FTMultiLang()

        # Update existing or add new
        for item in self.descriptionOfRestrictions.items:
            if item.lang == lang:
                item.text = text
                return self

        self.descriptionOfRestrictions.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_descriptionOfRestrictions(self, lang: str = 'en') -> Optional[str]:
        """Get descriptionOfRestrictions text for a specific language."""
        if not self.descriptionOfRestrictions:
            return None
        for item in self.descriptionOfRestrictions.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> SubLocationOfOperationSupplyOrProduction:
        """Build the final SubLocationOfOperationSupplyOrProduction instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return SubLocationOfOperationSupplyOrProduction.model_validate(data)

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

class GeographyBuilder(BaseModel):
    """Builder for Geography.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = GeographyBuilder()
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
    _locationOfOperationSupplyOrProduction: Optional[LocationOfOperationSupplyOrProductionBuilder] = None
    _subLocationOfOperationSupplyOrProduction: Optional[SubLocationOfOperationSupplyOrProductionBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def locationOfOperationSupplyOrProduction(self) -> LocationOfOperationSupplyOrProductionBuilder:
        """Access locationOfOperationSupplyOrProduction builder (auto-initialized)."""
        if self._locationOfOperationSupplyOrProduction is None:
            self._locationOfOperationSupplyOrProduction = LocationOfOperationSupplyOrProductionBuilder()
        return self._locationOfOperationSupplyOrProduction

    @property
    def subLocationOfOperationSupplyOrProduction(self) -> SubLocationOfOperationSupplyOrProductionBuilder:
        """Access subLocationOfOperationSupplyOrProduction builder (auto-initialized)."""
        if self._subLocationOfOperationSupplyOrProduction is None:
            self._subLocationOfOperationSupplyOrProduction = SubLocationOfOperationSupplyOrProductionBuilder()
        return self._subLocationOfOperationSupplyOrProduction

    def build(self) -> Geography:
        """Build the final Geography instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_locationOfOperationSupplyOrProduction', None)
        data.pop('_subLocationOfOperationSupplyOrProduction', None)

        # Build nested objects
        if self._locationOfOperationSupplyOrProduction is not None:
            data['locationOfOperationSupplyOrProduction'] = self._locationOfOperationSupplyOrProduction.build()
        if self._subLocationOfOperationSupplyOrProduction is not None:
            data['subLocationOfOperationSupplyOrProduction'] = self._subLocationOfOperationSupplyOrProduction.build()

        return Geography.model_validate(data)

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

class TechnologyBuilder(BaseModel):
    """Builder for Technology.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = TechnologyBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    technologyDescriptionAndIncludedProcesses: Optional[FTMultiLang] = None
    technologicalApplicability: Optional[FTMultiLang] = None
    common_other: Optional[str] = Field(None, alias='common:other')
    _referenceToIncludedProcesses: Optional[GlobalReferenceTypeBuilder] = None
    _referenceToTechnologyPictogramme: Optional[GlobalReferenceTypeBuilder] = None
    _referenceToTechnologyFlowDiagrammOrPicture: Optional[GlobalReferenceTypeBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def referenceToIncludedProcesses(self) -> GlobalReferenceTypeBuilder:
        """Access referenceToIncludedProcesses builder (auto-initialized)."""
        if self._referenceToIncludedProcesses is None:
            self._referenceToIncludedProcesses = GlobalReferenceTypeBuilder()
        return self._referenceToIncludedProcesses

    @property
    def referenceToTechnologyPictogramme(self) -> GlobalReferenceTypeBuilder:
        """Access referenceToTechnologyPictogramme builder (auto-initialized)."""
        if self._referenceToTechnologyPictogramme is None:
            self._referenceToTechnologyPictogramme = GlobalReferenceTypeBuilder()
        return self._referenceToTechnologyPictogramme

    @property
    def referenceToTechnologyFlowDiagrammOrPicture(self) -> GlobalReferenceTypeBuilder:
        """Access referenceToTechnologyFlowDiagrammOrPicture builder (auto-initialized)."""
        if self._referenceToTechnologyFlowDiagrammOrPicture is None:
            self._referenceToTechnologyFlowDiagrammOrPicture = GlobalReferenceTypeBuilder()
        return self._referenceToTechnologyFlowDiagrammOrPicture

    @field_validator('technologyDescriptionAndIncludedProcesses', 'technologicalApplicability', mode='before')
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

    def set_technologyDescriptionAndIncludedProcesses(self, text: str, lang: str = 'en') -> 'TechnologyBuilder':
        """Set technologyDescriptionAndIncludedProcesses text for a specific language."""
        if self.technologyDescriptionAndIncludedProcesses is None:
            self.technologyDescriptionAndIncludedProcesses = FTMultiLang()

        # Update existing or add new
        for item in self.technologyDescriptionAndIncludedProcesses.items:
            if item.lang == lang:
                item.text = text
                return self

        self.technologyDescriptionAndIncludedProcesses.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_technologyDescriptionAndIncludedProcesses(self, lang: str = 'en') -> Optional[str]:
        """Get technologyDescriptionAndIncludedProcesses text for a specific language."""
        if not self.technologyDescriptionAndIncludedProcesses:
            return None
        for item in self.technologyDescriptionAndIncludedProcesses.items:
            if item.lang == lang:
                return item.text
        return None

    def set_technologicalApplicability(self, text: str, lang: str = 'en') -> 'TechnologyBuilder':
        """Set technologicalApplicability text for a specific language."""
        if self.technologicalApplicability is None:
            self.technologicalApplicability = FTMultiLang()

        # Update existing or add new
        for item in self.technologicalApplicability.items:
            if item.lang == lang:
                item.text = text
                return self

        self.technologicalApplicability.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_technologicalApplicability(self, lang: str = 'en') -> Optional[str]:
        """Get technologicalApplicability text for a specific language."""
        if not self.technologicalApplicability:
            return None
        for item in self.technologicalApplicability.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> Technology:
        """Build the final Technology instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_referenceToIncludedProcesses', None)
        data.pop('_referenceToTechnologyPictogramme', None)
        data.pop('_referenceToTechnologyFlowDiagrammOrPicture', None)

        # Build nested objects
        if self._referenceToIncludedProcesses is not None:
            data['referenceToIncludedProcesses'] = self._referenceToIncludedProcesses.build()
        if self._referenceToTechnologyPictogramme is not None:
            data['referenceToTechnologyPictogramme'] = self._referenceToTechnologyPictogramme.build()
        if self._referenceToTechnologyFlowDiagrammOrPicture is not None:
            data['referenceToTechnologyFlowDiagrammOrPicture'] = self._referenceToTechnologyFlowDiagrammOrPicture.build()

        return Technology.model_validate(data)

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

class VariableParameterBuilder(BaseModel):
    """Builder for VariableParameter.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = VariableParameterBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    field_name: Optional[str] = Field(None, alias='@name')
    formula: Optional[str] = None
    meanValue: Optional[str] = None
    minimumValue: Optional[str] = None
    maximumValue: Optional[str] = None
    uncertaintyDistributionType: Optional[UncertaintyDistributionType] = None
    relativeStandardDeviation95In: Optional[str] = None
    comment: Optional[StringMultiLang] = None
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @field_validator('comment', mode='before')
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

    def set_comment(self, text: str, lang: str = 'en') -> 'VariableParameterBuilder':
        """Set comment text for a specific language."""
        if self.comment is None:
            self.comment = StringMultiLang()

        # Update existing or add new
        for item in self.comment.items:
            if item.lang == lang:
                item.text = text
                return self

        self.comment.items.append(MultiLangItemString(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_comment(self, lang: str = 'en') -> Optional[str]:
        """Get comment text for a specific language."""
        if not self.comment:
            return None
        for item in self.comment.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> VariableParameter:
        """Build the final VariableParameter instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return VariableParameter.model_validate(data)

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

class MathematicalRelationsBuilder(BaseModel):
    """Builder for MathematicalRelations.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = MathematicalRelationsBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    modelDescription: Optional[FTMultiLang] = None
    common_other: Optional[str] = Field(None, alias='common:other')
    _variableParameter: Optional[VariableParameterBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def variableParameter(self) -> VariableParameterBuilder:
        """Access variableParameter builder (auto-initialized)."""
        if self._variableParameter is None:
            self._variableParameter = VariableParameterBuilder()
        return self._variableParameter

    @field_validator('modelDescription', mode='before')
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

    def set_modelDescription(self, text: str, lang: str = 'en') -> 'MathematicalRelationsBuilder':
        """Set modelDescription text for a specific language."""
        if self.modelDescription is None:
            self.modelDescription = FTMultiLang()

        # Update existing or add new
        for item in self.modelDescription.items:
            if item.lang == lang:
                item.text = text
                return self

        self.modelDescription.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_modelDescription(self, lang: str = 'en') -> Optional[str]:
        """Get modelDescription text for a specific language."""
        if not self.modelDescription:
            return None
        for item in self.modelDescription.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> MathematicalRelations:
        """Build the final MathematicalRelations instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_variableParameter', None)

        # Build nested objects
        if self._variableParameter is not None:
            data['variableParameter'] = self._variableParameter.build()

        return MathematicalRelations.model_validate(data)

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

class ProcessInformationBuilder(BaseModel):
    """Corresponds to the ISO/TS 14048 section "Process description". It comprises the following six sub-sections: 1) "Data set information" for data set identification and overarching information items, 2) "Quantitative reference", 3) "Time", 4) "Geography", 5) "Technology" and 6) "Mathematical relations". (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = ProcessInformationBuilder()
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
    _quantitativeReference: Optional[QuantitativeReferenceBuilder] = None
    _time: Optional[TimeBuilder] = None
    _geography: Optional[GeographyBuilder] = None
    _technology: Optional[TechnologyBuilder] = None
    _mathematicalRelations: Optional[MathematicalRelationsBuilder] = None

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
    def technology(self) -> TechnologyBuilder:
        """Access technology builder (auto-initialized)."""
        if self._technology is None:
            self._technology = TechnologyBuilder()
        return self._technology

    @property
    def mathematicalRelations(self) -> MathematicalRelationsBuilder:
        """Access mathematicalRelations builder (auto-initialized)."""
        if self._mathematicalRelations is None:
            self._mathematicalRelations = MathematicalRelationsBuilder()
        return self._mathematicalRelations

    def build(self) -> ProcessInformation:
        """Build the final ProcessInformation instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_dataSetInformation', None)
        data.pop('_quantitativeReference', None)
        data.pop('_time', None)
        data.pop('_geography', None)
        data.pop('_technology', None)
        data.pop('_mathematicalRelations', None)

        # Build nested objects
        if self._dataSetInformation is not None:
            data['dataSetInformation'] = self._dataSetInformation.build()
        if self._quantitativeReference is not None:
            data['quantitativeReference'] = self._quantitativeReference.build()
        if self._time is not None:
            data['time'] = self._time.build()
        if self._geography is not None:
            data['geography'] = self._geography.build()
        if self._technology is not None:
            data['technology'] = self._technology.build()
        if self._mathematicalRelations is not None:
            data['mathematicalRelations'] = self._mathematicalRelations.build()

        return ProcessInformation.model_validate(data)

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

class LCIMethodAndAllocationBuilder(BaseModel):
    """Builder for LCIMethodAndAllocation.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = LCIMethodAndAllocationBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    typeOfDataSet: Optional[TypeOfDataSet] = None
    LCIMethodPrinciple_1: Optional[LCIMethodPrinciple] = Field(None, alias='LCIMethodPrinciple')
    deviationsFromLCIMethodPrinciple: Optional[FTMultiLang] = None
    LCIMethodApproaches_1: Optional[LCIMethodApproaches] = Field(None, alias='LCIMethodApproaches')
    deviationsFromLCIMethodApproaches: Optional[FTMultiLang] = None
    modellingConstants: Optional[FTMultiLang] = None
    deviationsFromModellingConstants: Optional[FTMultiLang] = None
    common_other: Optional[str] = Field(None, alias='common:other')
    _referenceToLCAMethodDetails: Optional[GlobalReferenceTypeBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def referenceToLCAMethodDetails(self) -> GlobalReferenceTypeBuilder:
        """Access referenceToLCAMethodDetails builder (auto-initialized)."""
        if self._referenceToLCAMethodDetails is None:
            self._referenceToLCAMethodDetails = GlobalReferenceTypeBuilder()
        return self._referenceToLCAMethodDetails

    @field_validator('deviationsFromLCIMethodPrinciple', 'deviationsFromLCIMethodApproaches', 'modellingConstants', 'deviationsFromModellingConstants', mode='before')
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

    def set_deviationsFromLCIMethodPrinciple(self, text: str, lang: str = 'en') -> 'LCIMethodAndAllocationBuilder':
        """Set deviationsFromLCIMethodPrinciple text for a specific language."""
        if self.deviationsFromLCIMethodPrinciple is None:
            self.deviationsFromLCIMethodPrinciple = FTMultiLang()

        # Update existing or add new
        for item in self.deviationsFromLCIMethodPrinciple.items:
            if item.lang == lang:
                item.text = text
                return self

        self.deviationsFromLCIMethodPrinciple.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_deviationsFromLCIMethodPrinciple(self, lang: str = 'en') -> Optional[str]:
        """Get deviationsFromLCIMethodPrinciple text for a specific language."""
        if not self.deviationsFromLCIMethodPrinciple:
            return None
        for item in self.deviationsFromLCIMethodPrinciple.items:
            if item.lang == lang:
                return item.text
        return None

    def set_deviationsFromLCIMethodApproaches(self, text: str, lang: str = 'en') -> 'LCIMethodAndAllocationBuilder':
        """Set deviationsFromLCIMethodApproaches text for a specific language."""
        if self.deviationsFromLCIMethodApproaches is None:
            self.deviationsFromLCIMethodApproaches = FTMultiLang()

        # Update existing or add new
        for item in self.deviationsFromLCIMethodApproaches.items:
            if item.lang == lang:
                item.text = text
                return self

        self.deviationsFromLCIMethodApproaches.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_deviationsFromLCIMethodApproaches(self, lang: str = 'en') -> Optional[str]:
        """Get deviationsFromLCIMethodApproaches text for a specific language."""
        if not self.deviationsFromLCIMethodApproaches:
            return None
        for item in self.deviationsFromLCIMethodApproaches.items:
            if item.lang == lang:
                return item.text
        return None

    def set_modellingConstants(self, text: str, lang: str = 'en') -> 'LCIMethodAndAllocationBuilder':
        """Set modellingConstants text for a specific language."""
        if self.modellingConstants is None:
            self.modellingConstants = FTMultiLang()

        # Update existing or add new
        for item in self.modellingConstants.items:
            if item.lang == lang:
                item.text = text
                return self

        self.modellingConstants.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_modellingConstants(self, lang: str = 'en') -> Optional[str]:
        """Get modellingConstants text for a specific language."""
        if not self.modellingConstants:
            return None
        for item in self.modellingConstants.items:
            if item.lang == lang:
                return item.text
        return None

    def set_deviationsFromModellingConstants(self, text: str, lang: str = 'en') -> 'LCIMethodAndAllocationBuilder':
        """Set deviationsFromModellingConstants text for a specific language."""
        if self.deviationsFromModellingConstants is None:
            self.deviationsFromModellingConstants = FTMultiLang()

        # Update existing or add new
        for item in self.deviationsFromModellingConstants.items:
            if item.lang == lang:
                item.text = text
                return self

        self.deviationsFromModellingConstants.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_deviationsFromModellingConstants(self, lang: str = 'en') -> Optional[str]:
        """Get deviationsFromModellingConstants text for a specific language."""
        if not self.deviationsFromModellingConstants:
            return None
        for item in self.deviationsFromModellingConstants.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> LCIMethodAndAllocation:
        """Build the final LCIMethodAndAllocation instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_referenceToLCAMethodDetails', None)

        # Build nested objects
        if self._referenceToLCAMethodDetails is not None:
            data['referenceToLCAMethodDetails'] = self._referenceToLCAMethodDetails.build()

        return LCIMethodAndAllocation.model_validate(data)

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

class DataSourcesTreatmentAndRepresentativenessBuilder(BaseModel):
    """Builder for DataSourcesTreatmentAndRepresentativeness.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = DataSourcesTreatmentAndRepresentativenessBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    dataCutOffAndCompletenessPrinciples: Optional[FTMultiLang] = None
    deviationsFromCutOffAndCompletenessPrinciples: Optional[FTMultiLang] = None
    dataSelectionAndCombinationPrinciples: Optional[FTMultiLang] = None
    deviationsFromSelectionAndCombinationPrinciples: Optional[FTMultiLang] = None
    dataTreatmentAndExtrapolationsPrinciples: Optional[FTMultiLang] = None
    deviationsFromTreatmentAndExtrapolationPrinciples: Optional[FTMultiLang] = None
    percentageSupplyOrProductionCovered: Optional[str] = None
    annualSupplyOrProductionVolume: Optional[StringMultiLang] = None
    samplingProcedure: Optional[FTMultiLang] = None
    dataCollectionPeriod: Optional[StringMultiLang] = None
    uncertaintyAdjustments: Optional[FTMultiLang] = None
    useAdviceForDataSet: Optional[FTMultiLang] = None
    common_other: Optional[str] = Field(None, alias='common:other')
    _referenceToDataHandlingPrinciples: Optional[GlobalReferenceTypeBuilder] = None
    _referenceToDataSource: Optional[GlobalReferenceTypeBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def referenceToDataHandlingPrinciples(self) -> GlobalReferenceTypeBuilder:
        """Access referenceToDataHandlingPrinciples builder (auto-initialized)."""
        if self._referenceToDataHandlingPrinciples is None:
            self._referenceToDataHandlingPrinciples = GlobalReferenceTypeBuilder()
        return self._referenceToDataHandlingPrinciples

    @property
    def referenceToDataSource(self) -> GlobalReferenceTypeBuilder:
        """Access referenceToDataSource builder (auto-initialized)."""
        if self._referenceToDataSource is None:
            self._referenceToDataSource = GlobalReferenceTypeBuilder()
        return self._referenceToDataSource

    @field_validator('annualSupplyOrProductionVolume', 'dataCollectionPeriod', mode='before')
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

    @field_validator('dataCutOffAndCompletenessPrinciples', 'deviationsFromCutOffAndCompletenessPrinciples', 'dataSelectionAndCombinationPrinciples', 'deviationsFromSelectionAndCombinationPrinciples', 'dataTreatmentAndExtrapolationsPrinciples', 'deviationsFromTreatmentAndExtrapolationPrinciples', 'samplingProcedure', 'uncertaintyAdjustments', 'useAdviceForDataSet', mode='before')
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

    def set_dataCutOffAndCompletenessPrinciples(self, text: str, lang: str = 'en') -> 'DataSourcesTreatmentAndRepresentativenessBuilder':
        """Set dataCutOffAndCompletenessPrinciples text for a specific language."""
        if self.dataCutOffAndCompletenessPrinciples is None:
            self.dataCutOffAndCompletenessPrinciples = FTMultiLang()

        # Update existing or add new
        for item in self.dataCutOffAndCompletenessPrinciples.items:
            if item.lang == lang:
                item.text = text
                return self

        self.dataCutOffAndCompletenessPrinciples.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_dataCutOffAndCompletenessPrinciples(self, lang: str = 'en') -> Optional[str]:
        """Get dataCutOffAndCompletenessPrinciples text for a specific language."""
        if not self.dataCutOffAndCompletenessPrinciples:
            return None
        for item in self.dataCutOffAndCompletenessPrinciples.items:
            if item.lang == lang:
                return item.text
        return None

    def set_deviationsFromCutOffAndCompletenessPrinciples(self, text: str, lang: str = 'en') -> 'DataSourcesTreatmentAndRepresentativenessBuilder':
        """Set deviationsFromCutOffAndCompletenessPrinciples text for a specific language."""
        if self.deviationsFromCutOffAndCompletenessPrinciples is None:
            self.deviationsFromCutOffAndCompletenessPrinciples = FTMultiLang()

        # Update existing or add new
        for item in self.deviationsFromCutOffAndCompletenessPrinciples.items:
            if item.lang == lang:
                item.text = text
                return self

        self.deviationsFromCutOffAndCompletenessPrinciples.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_deviationsFromCutOffAndCompletenessPrinciples(self, lang: str = 'en') -> Optional[str]:
        """Get deviationsFromCutOffAndCompletenessPrinciples text for a specific language."""
        if not self.deviationsFromCutOffAndCompletenessPrinciples:
            return None
        for item in self.deviationsFromCutOffAndCompletenessPrinciples.items:
            if item.lang == lang:
                return item.text
        return None

    def set_dataSelectionAndCombinationPrinciples(self, text: str, lang: str = 'en') -> 'DataSourcesTreatmentAndRepresentativenessBuilder':
        """Set dataSelectionAndCombinationPrinciples text for a specific language."""
        if self.dataSelectionAndCombinationPrinciples is None:
            self.dataSelectionAndCombinationPrinciples = FTMultiLang()

        # Update existing or add new
        for item in self.dataSelectionAndCombinationPrinciples.items:
            if item.lang == lang:
                item.text = text
                return self

        self.dataSelectionAndCombinationPrinciples.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_dataSelectionAndCombinationPrinciples(self, lang: str = 'en') -> Optional[str]:
        """Get dataSelectionAndCombinationPrinciples text for a specific language."""
        if not self.dataSelectionAndCombinationPrinciples:
            return None
        for item in self.dataSelectionAndCombinationPrinciples.items:
            if item.lang == lang:
                return item.text
        return None

    def set_deviationsFromSelectionAndCombinationPrinciples(self, text: str, lang: str = 'en') -> 'DataSourcesTreatmentAndRepresentativenessBuilder':
        """Set deviationsFromSelectionAndCombinationPrinciples text for a specific language."""
        if self.deviationsFromSelectionAndCombinationPrinciples is None:
            self.deviationsFromSelectionAndCombinationPrinciples = FTMultiLang()

        # Update existing or add new
        for item in self.deviationsFromSelectionAndCombinationPrinciples.items:
            if item.lang == lang:
                item.text = text
                return self

        self.deviationsFromSelectionAndCombinationPrinciples.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_deviationsFromSelectionAndCombinationPrinciples(self, lang: str = 'en') -> Optional[str]:
        """Get deviationsFromSelectionAndCombinationPrinciples text for a specific language."""
        if not self.deviationsFromSelectionAndCombinationPrinciples:
            return None
        for item in self.deviationsFromSelectionAndCombinationPrinciples.items:
            if item.lang == lang:
                return item.text
        return None

    def set_dataTreatmentAndExtrapolationsPrinciples(self, text: str, lang: str = 'en') -> 'DataSourcesTreatmentAndRepresentativenessBuilder':
        """Set dataTreatmentAndExtrapolationsPrinciples text for a specific language."""
        if self.dataTreatmentAndExtrapolationsPrinciples is None:
            self.dataTreatmentAndExtrapolationsPrinciples = FTMultiLang()

        # Update existing or add new
        for item in self.dataTreatmentAndExtrapolationsPrinciples.items:
            if item.lang == lang:
                item.text = text
                return self

        self.dataTreatmentAndExtrapolationsPrinciples.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_dataTreatmentAndExtrapolationsPrinciples(self, lang: str = 'en') -> Optional[str]:
        """Get dataTreatmentAndExtrapolationsPrinciples text for a specific language."""
        if not self.dataTreatmentAndExtrapolationsPrinciples:
            return None
        for item in self.dataTreatmentAndExtrapolationsPrinciples.items:
            if item.lang == lang:
                return item.text
        return None

    def set_deviationsFromTreatmentAndExtrapolationPrinciples(self, text: str, lang: str = 'en') -> 'DataSourcesTreatmentAndRepresentativenessBuilder':
        """Set deviationsFromTreatmentAndExtrapolationPrinciples text for a specific language."""
        if self.deviationsFromTreatmentAndExtrapolationPrinciples is None:
            self.deviationsFromTreatmentAndExtrapolationPrinciples = FTMultiLang()

        # Update existing or add new
        for item in self.deviationsFromTreatmentAndExtrapolationPrinciples.items:
            if item.lang == lang:
                item.text = text
                return self

        self.deviationsFromTreatmentAndExtrapolationPrinciples.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_deviationsFromTreatmentAndExtrapolationPrinciples(self, lang: str = 'en') -> Optional[str]:
        """Get deviationsFromTreatmentAndExtrapolationPrinciples text for a specific language."""
        if not self.deviationsFromTreatmentAndExtrapolationPrinciples:
            return None
        for item in self.deviationsFromTreatmentAndExtrapolationPrinciples.items:
            if item.lang == lang:
                return item.text
        return None

    def set_annualSupplyOrProductionVolume(self, text: str, lang: str = 'en') -> 'DataSourcesTreatmentAndRepresentativenessBuilder':
        """Set annualSupplyOrProductionVolume text for a specific language."""
        if self.annualSupplyOrProductionVolume is None:
            self.annualSupplyOrProductionVolume = StringMultiLang()

        # Update existing or add new
        for item in self.annualSupplyOrProductionVolume.items:
            if item.lang == lang:
                item.text = text
                return self

        self.annualSupplyOrProductionVolume.items.append(MultiLangItemString(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_annualSupplyOrProductionVolume(self, lang: str = 'en') -> Optional[str]:
        """Get annualSupplyOrProductionVolume text for a specific language."""
        if not self.annualSupplyOrProductionVolume:
            return None
        for item in self.annualSupplyOrProductionVolume.items:
            if item.lang == lang:
                return item.text
        return None

    def set_samplingProcedure(self, text: str, lang: str = 'en') -> 'DataSourcesTreatmentAndRepresentativenessBuilder':
        """Set samplingProcedure text for a specific language."""
        if self.samplingProcedure is None:
            self.samplingProcedure = FTMultiLang()

        # Update existing or add new
        for item in self.samplingProcedure.items:
            if item.lang == lang:
                item.text = text
                return self

        self.samplingProcedure.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_samplingProcedure(self, lang: str = 'en') -> Optional[str]:
        """Get samplingProcedure text for a specific language."""
        if not self.samplingProcedure:
            return None
        for item in self.samplingProcedure.items:
            if item.lang == lang:
                return item.text
        return None

    def set_dataCollectionPeriod(self, text: str, lang: str = 'en') -> 'DataSourcesTreatmentAndRepresentativenessBuilder':
        """Set dataCollectionPeriod text for a specific language."""
        if self.dataCollectionPeriod is None:
            self.dataCollectionPeriod = StringMultiLang()

        # Update existing or add new
        for item in self.dataCollectionPeriod.items:
            if item.lang == lang:
                item.text = text
                return self

        self.dataCollectionPeriod.items.append(MultiLangItemString(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_dataCollectionPeriod(self, lang: str = 'en') -> Optional[str]:
        """Get dataCollectionPeriod text for a specific language."""
        if not self.dataCollectionPeriod:
            return None
        for item in self.dataCollectionPeriod.items:
            if item.lang == lang:
                return item.text
        return None

    def set_uncertaintyAdjustments(self, text: str, lang: str = 'en') -> 'DataSourcesTreatmentAndRepresentativenessBuilder':
        """Set uncertaintyAdjustments text for a specific language."""
        if self.uncertaintyAdjustments is None:
            self.uncertaintyAdjustments = FTMultiLang()

        # Update existing or add new
        for item in self.uncertaintyAdjustments.items:
            if item.lang == lang:
                item.text = text
                return self

        self.uncertaintyAdjustments.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_uncertaintyAdjustments(self, lang: str = 'en') -> Optional[str]:
        """Get uncertaintyAdjustments text for a specific language."""
        if not self.uncertaintyAdjustments:
            return None
        for item in self.uncertaintyAdjustments.items:
            if item.lang == lang:
                return item.text
        return None

    def set_useAdviceForDataSet(self, text: str, lang: str = 'en') -> 'DataSourcesTreatmentAndRepresentativenessBuilder':
        """Set useAdviceForDataSet text for a specific language."""
        if self.useAdviceForDataSet is None:
            self.useAdviceForDataSet = FTMultiLang()

        # Update existing or add new
        for item in self.useAdviceForDataSet.items:
            if item.lang == lang:
                item.text = text
                return self

        self.useAdviceForDataSet.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_useAdviceForDataSet(self, lang: str = 'en') -> Optional[str]:
        """Get useAdviceForDataSet text for a specific language."""
        if not self.useAdviceForDataSet:
            return None
        for item in self.useAdviceForDataSet.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> DataSourcesTreatmentAndRepresentativeness:
        """Build the final DataSourcesTreatmentAndRepresentativeness instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_referenceToDataHandlingPrinciples', None)
        data.pop('_referenceToDataSource', None)

        # Build nested objects
        if self._referenceToDataHandlingPrinciples is not None:
            data['referenceToDataHandlingPrinciples'] = self._referenceToDataHandlingPrinciples.build()
        if self._referenceToDataSource is not None:
            data['referenceToDataSource'] = self._referenceToDataSource.build()

        return DataSourcesTreatmentAndRepresentativeness.model_validate(data)

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

class LCIAResultBuilder(BaseModel):
    """Builder for LCIAResult.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = LCIAResultBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    meanAmount: Optional[str] = None
    uncertaintyDistributionType: Optional[UncertaintyDistributionType1] = None
    relativeStandardDeviation95In: Optional[str] = None
    generalComment: Optional[StringMultiLang] = None
    common_other: Optional[str] = Field(None, alias='common:other')
    _referenceToLCIAMethodDataSet: Optional[GlobalReferenceTypeBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def referenceToLCIAMethodDataSet(self) -> GlobalReferenceTypeBuilder:
        """Access referenceToLCIAMethodDataSet builder (auto-initialized)."""
        if self._referenceToLCIAMethodDataSet is None:
            self._referenceToLCIAMethodDataSet = GlobalReferenceTypeBuilder()
        return self._referenceToLCIAMethodDataSet

    @field_validator('generalComment', mode='before')
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

    def set_generalComment(self, text: str, lang: str = 'en') -> 'LCIAResultBuilder':
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

    def build(self) -> LCIAResult:
        """Build the final LCIAResult instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_referenceToLCIAMethodDataSet', None)

        # Build nested objects
        if self._referenceToLCIAMethodDataSet is not None:
            data['referenceToLCIAMethodDataSet'] = self._referenceToLCIAMethodDataSet.build()

        return LCIAResult.model_validate(data)

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

class AllocationBuilder(BaseModel):
    """specifies one allocation of this exchange (see the attributes of this tag below) (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = AllocationBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    field_internalReferenceToCoProduct: Optional[str] = Field(None, alias='@internalReferenceToCoProduct')
    field_allocatedFraction: Optional[str] = Field(None, alias='@allocatedFraction')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> Allocation:
        """Build the final Allocation instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return Allocation.model_validate(data)

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

class ReviewBuilder(BaseModel):
    """Type of review that has been performed regarding independency and type of review process. (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = ReviewBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    field_type: Optional[FieldType2] = Field(None, alias='@type')
    common_reviewDetails: Optional[FTMultiLang] = Field(None, alias='common:reviewDetails')
    common_otherReviewDetails: Optional[FTMultiLang] = Field(None, alias='common:otherReviewDetails')
    common_other: Optional[str] = Field(None, alias='common:other')
    _common_scope: Optional[CommonScopeBuilder] = None
    _common_dataQualityIndicators: Optional[CommonDataQualityIndicatorsBuilder] = None
    _common_referenceToNameOfReviewerAndInstitution: Optional[GlobalReferenceTypeBuilder] = None
    _common_referenceToCompleteReviewReport: Optional[GlobalReferenceTypeBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def common_scope(self) -> CommonScopeBuilder:
        """Access common_scope builder (auto-initialized)."""
        if self._common_scope is None:
            self._common_scope = CommonScopeBuilder()
        return self._common_scope

    @property
    def common_dataQualityIndicators(self) -> CommonDataQualityIndicatorsBuilder:
        """Access common_dataQualityIndicators builder (auto-initialized)."""
        if self._common_dataQualityIndicators is None:
            self._common_dataQualityIndicators = CommonDataQualityIndicatorsBuilder()
        return self._common_dataQualityIndicators

    @property
    def common_referenceToNameOfReviewerAndInstitution(self) -> GlobalReferenceTypeBuilder:
        """Access common_referenceToNameOfReviewerAndInstitution builder (auto-initialized)."""
        if self._common_referenceToNameOfReviewerAndInstitution is None:
            self._common_referenceToNameOfReviewerAndInstitution = GlobalReferenceTypeBuilder()
        return self._common_referenceToNameOfReviewerAndInstitution

    @property
    def common_referenceToCompleteReviewReport(self) -> GlobalReferenceTypeBuilder:
        """Access common_referenceToCompleteReviewReport builder (auto-initialized)."""
        if self._common_referenceToCompleteReviewReport is None:
            self._common_referenceToCompleteReviewReport = GlobalReferenceTypeBuilder()
        return self._common_referenceToCompleteReviewReport

    @field_validator('common_reviewDetails', 'common_otherReviewDetails', mode='before')
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

    def set_reviewDetails(self, text: str, lang: str = 'en') -> 'ReviewBuilder':
        """Set common_reviewDetails text for a specific language."""
        if self.common_reviewDetails is None:
            self.common_reviewDetails = FTMultiLang()

        # Update existing or add new
        for item in self.common_reviewDetails.items:
            if item.lang == lang:
                item.text = text
                return self

        self.common_reviewDetails.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
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

        self.common_otherReviewDetails.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
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
        data.pop('_common_dataQualityIndicators', None)
        data.pop('_common_referenceToNameOfReviewerAndInstitution', None)
        data.pop('_common_referenceToCompleteReviewReport', None)

        # Build nested objects
        if self._common_scope is not None:
            data['common:scope'] = self._common_scope.build()
        if self._common_dataQualityIndicators is not None:
            data['common:dataQualityIndicators'] = self._common_dataQualityIndicators.build()
        if self._common_referenceToNameOfReviewerAndInstitution is not None:
            data['common:referenceToNameOfReviewerAndInstitution'] = self._common_referenceToNameOfReviewerAndInstitution.build()
        if self._common_referenceToCompleteReviewReport is not None:
            data['common:referenceToCompleteReviewReport'] = self._common_referenceToCompleteReviewReport.build()

        return Review.model_validate(data)

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

class ComplianceBuilder(BaseModel):
    """One compliance declaration. Multiple declarations may be provided. (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = ComplianceBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    common_approvalOfOverallCompliance: Optional[CommonApprovalOfOverallCompliance] = Field(None, alias='common:approvalOfOverallCompliance')
    common_nomenclatureCompliance: Optional[CommonNomenclatureCompliance] = Field(None, alias='common:nomenclatureCompliance')
    common_methodologicalCompliance: Optional[CommonMethodologicalCompliance] = Field(None, alias='common:methodologicalCompliance')
    common_reviewCompliance: Optional[CommonReviewCompliance] = Field(None, alias='common:reviewCompliance')
    common_documentationCompliance: Optional[CommonDocumentationCompliance] = Field(None, alias='common:documentationCompliance')
    common_qualityCompliance: Optional[CommonQualityCompliance] = Field(None, alias='common:qualityCompliance')
    common_other: Optional[str] = Field(None, alias='common:other')
    _common_referenceToComplianceSystem: Optional[GlobalReferenceTypeBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def common_referenceToComplianceSystem(self) -> GlobalReferenceTypeBuilder:
        """Access common_referenceToComplianceSystem builder (auto-initialized)."""
        if self._common_referenceToComplianceSystem is None:
            self._common_referenceToComplianceSystem = GlobalReferenceTypeBuilder()
        return self._common_referenceToComplianceSystem

    def build(self) -> Compliance:
        """Build the final Compliance instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_common_referenceToComplianceSystem', None)

        # Build nested objects
        if self._common_referenceToComplianceSystem is not None:
            data['common:referenceToComplianceSystem'] = self._common_referenceToComplianceSystem.build()

        return Compliance.model_validate(data)

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

class Compliance1ItemBuilder(BaseModel):
    """Builder for Compliance1Item.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = Compliance1ItemBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    common_approvalOfOverallCompliance: Optional[CommonApprovalOfOverallCompliance] = Field(None, alias='common:approvalOfOverallCompliance')
    common_nomenclatureCompliance: Optional[CommonNomenclatureCompliance] = Field(None, alias='common:nomenclatureCompliance')
    common_methodologicalCompliance: Optional[CommonMethodologicalCompliance] = Field(None, alias='common:methodologicalCompliance')
    common_reviewCompliance: Optional[CommonReviewCompliance] = Field(None, alias='common:reviewCompliance')
    common_documentationCompliance: Optional[CommonDocumentationCompliance] = Field(None, alias='common:documentationCompliance')
    common_qualityCompliance: Optional[CommonQualityCompliance] = Field(None, alias='common:qualityCompliance')
    common_other: Optional[str] = Field(None, alias='common:other')
    _common_referenceToComplianceSystem: Optional[GlobalReferenceTypeBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def common_referenceToComplianceSystem(self) -> GlobalReferenceTypeBuilder:
        """Access common_referenceToComplianceSystem builder (auto-initialized)."""
        if self._common_referenceToComplianceSystem is None:
            self._common_referenceToComplianceSystem = GlobalReferenceTypeBuilder()
        return self._common_referenceToComplianceSystem

    def build(self) -> Compliance1Item:
        """Build the final Compliance1Item instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_common_referenceToComplianceSystem', None)

        # Build nested objects
        if self._common_referenceToComplianceSystem is not None:
            data['common:referenceToComplianceSystem'] = self._common_referenceToComplianceSystem.build()

        return Compliance1Item.model_validate(data)

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

class Compliance1Builder(BaseModel):
    """Builder for Compliance1.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = Compliance1Builder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    _root: List[Compliance1ItemBuilder] = []

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def root(self) -> List[Compliance1ItemBuilder]:
        """Access root builder list."""
        return self._root

    @root.setter
    def root(self, value: List[Compliance1ItemBuilder]) -> None:
        """Set root builder list."""
        self._root = value

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

class ComplianceDeclarationsBuilder(BaseModel):
    """Statements on compliance of several data set aspects with compliance requirements as defined by the referenced compliance system (e.g. an EPD scheme, handbook of a national or international data network such as the ILCD, etc.). (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = ComplianceDeclarationsBuilder()
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
    _compliance: Optional[ComplianceBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
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

class ValidationBuilder(BaseModel):
    """Review information on LCIA method. (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = ValidationBuilder()
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
    _review: Optional[ReviewBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
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

class ModellingAndValidationBuilder(BaseModel):
    """Builder for ModellingAndValidation.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = ModellingAndValidationBuilder()
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
    _LCIMethodAndAllocation_1: Optional[LCIMethodAndAllocationBuilder] = None
    _dataSourcesTreatmentAndRepresentativeness: Optional[DataSourcesTreatmentAndRepresentativenessBuilder] = None
    _completeness: Optional[CompletenessBuilder] = None
    _validation: Optional[ValidationBuilder] = None
    _complianceDeclarations: Optional[ComplianceDeclarationsBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def LCIMethodAndAllocation_1(self) -> LCIMethodAndAllocationBuilder:
        """Access LCIMethodAndAllocation_1 builder (auto-initialized)."""
        if self._LCIMethodAndAllocation_1 is None:
            self._LCIMethodAndAllocation_1 = LCIMethodAndAllocationBuilder()
        return self._LCIMethodAndAllocation_1

    @property
    def dataSourcesTreatmentAndRepresentativeness(self) -> DataSourcesTreatmentAndRepresentativenessBuilder:
        """Access dataSourcesTreatmentAndRepresentativeness builder (auto-initialized)."""
        if self._dataSourcesTreatmentAndRepresentativeness is None:
            self._dataSourcesTreatmentAndRepresentativeness = DataSourcesTreatmentAndRepresentativenessBuilder()
        return self._dataSourcesTreatmentAndRepresentativeness

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

    def build(self) -> ModellingAndValidation:
        """Build the final ModellingAndValidation instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_LCIMethodAndAllocation_1', None)
        data.pop('_dataSourcesTreatmentAndRepresentativeness', None)
        data.pop('_completeness', None)
        data.pop('_validation', None)
        data.pop('_complianceDeclarations', None)

        # Build nested objects
        if self._LCIMethodAndAllocation_1 is not None:
            data['LCIMethodAndAllocation'] = self._LCIMethodAndAllocation_1.build()
        if self._dataSourcesTreatmentAndRepresentativeness is not None:
            data['dataSourcesTreatmentAndRepresentativeness'] = self._dataSourcesTreatmentAndRepresentativeness.build()
        if self._completeness is not None:
            data['completeness'] = self._completeness.build()
        if self._validation is not None:
            data['validation'] = self._validation.build()
        if self._complianceDeclarations is not None:
            data['complianceDeclarations'] = self._complianceDeclarations.build()

        return ModellingAndValidation.model_validate(data)

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

class AllocationsBuilder(BaseModel):
    """container tag for the specification of allocations if process has more than one reference product. Use only for multifunctional processes. (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = AllocationsBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    _allocation: Optional[AllocationBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def allocation(self) -> AllocationBuilder:
        """Access allocation builder (auto-initialized)."""
        if self._allocation is None:
            self._allocation = AllocationBuilder()
        return self._allocation

    def build(self) -> Allocations:
        """Build the final Allocations instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_allocation', None)

        # Build nested objects
        if self._allocation is not None:
            data['allocation'] = self._allocation.build()

        return Allocations.model_validate(data)

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

class ReferencesToDataSourceBuilder(BaseModel):
    """"Source data set" of data source(s) used for the value of this specific Input or Output, especially if differing from the general data source used for this data set. (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = ReferencesToDataSourceBuilder()
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
    _referenceToDataSource: Optional[GlobalReferenceTypeBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def referenceToDataSource(self) -> GlobalReferenceTypeBuilder:
        """Access referenceToDataSource builder (auto-initialized)."""
        if self._referenceToDataSource is None:
            self._referenceToDataSource = GlobalReferenceTypeBuilder()
        return self._referenceToDataSource

    def build(self) -> ReferencesToDataSource:
        """Build the final ReferencesToDataSource instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_referenceToDataSource', None)

        # Build nested objects
        if self._referenceToDataSource is not None:
            data['referenceToDataSource'] = self._referenceToDataSource.build()

        return ReferencesToDataSource.model_validate(data)

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

class ExchangeItemBuilder(BaseModel):
    """Builder for ExchangeItem.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = ExchangeItemBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    field_dataSetInternalID: Optional[str] = Field(None, alias='@dataSetInternalID')
    location: Optional[str] = None
    functionType: Optional[FunctionType] = None
    exchangeDirection: Optional[ExchangeDirection] = None
    referenceToVariable: Optional[str] = None
    meanAmount: Optional[str] = None
    resultingAmount: Optional[str] = None
    minimumAmount: Optional[str] = None
    maximumAmount: Optional[str] = None
    uncertaintyDistributionType: Optional[UncertaintyDistributionType1] = None
    relativeStandardDeviation95In: Optional[str] = None
    dataSourceType: Optional[DataSourceType] = None
    dataDerivationTypeStatus: Optional[DataDerivationTypeStatus] = None
    generalComment: Optional[StringMultiLang] = None
    common_other: Optional[str] = Field(None, alias='common:other')
    _referenceToFlowDataSet: Optional[GlobalReferenceTypeBuilder] = None
    _allocations: Optional[AllocationsBuilder] = None
    _referencesToDataSource: Optional[ReferencesToDataSourceBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def referenceToFlowDataSet(self) -> GlobalReferenceTypeBuilder:
        """Access referenceToFlowDataSet builder (auto-initialized)."""
        if self._referenceToFlowDataSet is None:
            self._referenceToFlowDataSet = GlobalReferenceTypeBuilder()
        return self._referenceToFlowDataSet

    @property
    def allocations(self) -> AllocationsBuilder:
        """Access allocations builder (auto-initialized)."""
        if self._allocations is None:
            self._allocations = AllocationsBuilder()
        return self._allocations

    @property
    def referencesToDataSource(self) -> ReferencesToDataSourceBuilder:
        """Access referencesToDataSource builder (auto-initialized)."""
        if self._referencesToDataSource is None:
            self._referencesToDataSource = ReferencesToDataSourceBuilder()
        return self._referencesToDataSource

    @field_validator('generalComment', mode='before')
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

    def set_generalComment(self, text: str, lang: str = 'en') -> 'ExchangeItemBuilder':
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

    def build(self) -> ExchangeItem:
        """Build the final ExchangeItem instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_referenceToFlowDataSet', None)
        data.pop('_allocations', None)
        data.pop('_referencesToDataSource', None)

        # Build nested objects
        if self._referenceToFlowDataSet is not None:
            data['referenceToFlowDataSet'] = self._referenceToFlowDataSet.build()
        if self._allocations is not None:
            data['allocations'] = self._allocations.build()
        if self._referencesToDataSource is not None:
            data['referencesToDataSource'] = self._referencesToDataSource.build()

        return ExchangeItem.model_validate(data)

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

class ExchangesBuilder(BaseModel):
    """Builder for Exchanges.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = ExchangesBuilder()
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
    _exchange: List[ExchangeItemBuilder] = []

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def exchange(self) -> List[ExchangeItemBuilder]:
        """Access exchange builder list."""
        return self._exchange

    @exchange.setter
    def exchange(self, value: List[ExchangeItemBuilder]) -> None:
        """Set exchange builder list."""
        self._exchange = value

    def add_exchange(self) -> ExchangeItemBuilder:
        """Add and return a new ExchangeItem builder."""
        builder = ExchangeItemBuilder()
        self._exchange.append(builder)
        return builder

    def build(self) -> Exchanges:
        """Build the final Exchanges instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_exchange', None)

        # Build array fields
        if self._exchange:
            data['exchange'] = [item.build() for item in self._exchange]

        return Exchanges.model_validate(data)

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

class CommonCommissionerAndGoalBuilder(BaseModel):
    """Basic information about goal and scope of the data set. (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = CommonCommissionerAndGoalBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    common_project: Optional[StringMultiLang] = Field(None, alias='common:project')
    common_intendedApplications: Optional[FTMultiLang] = Field(None, alias='common:intendedApplications')
    common_other: Optional[str] = Field(None, alias='common:other')
    _common_referenceToCommissioner: Optional[GlobalReferenceTypeBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def common_referenceToCommissioner(self) -> GlobalReferenceTypeBuilder:
        """Access common_referenceToCommissioner builder (auto-initialized)."""
        if self._common_referenceToCommissioner is None:
            self._common_referenceToCommissioner = GlobalReferenceTypeBuilder()
        return self._common_referenceToCommissioner

    @field_validator('common_project', mode='before')
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

    @field_validator('common_intendedApplications', mode='before')
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

        self.common_intendedApplications.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
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

        # Remove private builder fields
        data.pop('_common_referenceToCommissioner', None)

        # Build nested objects
        if self._common_referenceToCommissioner is not None:
            data['common:referenceToCommissioner'] = self._common_referenceToCommissioner.build()

        return CommonCommissionerAndGoal.model_validate(data)

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

class DataGeneratorBuilder(BaseModel):
    """Expert(s), that compiled and modelled the data set as well as internal administrative information linked to the data generation activity. (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = DataGeneratorBuilder()
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
    _common_referenceToPersonOrEntityGeneratingTheDataSet: Optional[GlobalReferenceTypeBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def common_referenceToPersonOrEntityGeneratingTheDataSet(self) -> GlobalReferenceTypeBuilder:
        """Access common_referenceToPersonOrEntityGeneratingTheDataSet builder (auto-initialized)."""
        if self._common_referenceToPersonOrEntityGeneratingTheDataSet is None:
            self._common_referenceToPersonOrEntityGeneratingTheDataSet = GlobalReferenceTypeBuilder()
        return self._common_referenceToPersonOrEntityGeneratingTheDataSet

    def build(self) -> DataGenerator:
        """Build the final DataGenerator instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_common_referenceToPersonOrEntityGeneratingTheDataSet', None)

        # Build nested objects
        if self._common_referenceToPersonOrEntityGeneratingTheDataSet is not None:
            data['common:referenceToPersonOrEntityGeneratingTheDataSet'] = self._common_referenceToPersonOrEntityGeneratingTheDataSet.build()

        return DataGenerator.model_validate(data)

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
    """Staff or entity, that documented the generated data set, entering the information into the database; plus administrative information linked to the data entry activity. (Builder)
    
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
    common_other: Optional[str] = Field(None, alias='common:other')
    _common_referenceToDataSetFormat: Optional[GlobalReferenceTypeBuilder] = None
    _common_referenceToConvertedOriginalDataSetFrom: Optional[GlobalReferenceTypeBuilder] = None
    _common_referenceToPersonOrEntityEnteringTheData: Optional[GlobalReferenceTypeBuilder] = None
    _common_referenceToDataSetUseApproval: Optional[GlobalReferenceTypeBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def common_referenceToDataSetFormat(self) -> GlobalReferenceTypeBuilder:
        """Access common_referenceToDataSetFormat builder (auto-initialized)."""
        if self._common_referenceToDataSetFormat is None:
            self._common_referenceToDataSetFormat = GlobalReferenceTypeBuilder()
        return self._common_referenceToDataSetFormat

    @property
    def common_referenceToConvertedOriginalDataSetFrom(self) -> GlobalReferenceTypeBuilder:
        """Access common_referenceToConvertedOriginalDataSetFrom builder (auto-initialized)."""
        if self._common_referenceToConvertedOriginalDataSetFrom is None:
            self._common_referenceToConvertedOriginalDataSetFrom = GlobalReferenceTypeBuilder()
        return self._common_referenceToConvertedOriginalDataSetFrom

    @property
    def common_referenceToPersonOrEntityEnteringTheData(self) -> GlobalReferenceTypeBuilder:
        """Access common_referenceToPersonOrEntityEnteringTheData builder (auto-initialized)."""
        if self._common_referenceToPersonOrEntityEnteringTheData is None:
            self._common_referenceToPersonOrEntityEnteringTheData = GlobalReferenceTypeBuilder()
        return self._common_referenceToPersonOrEntityEnteringTheData

    @property
    def common_referenceToDataSetUseApproval(self) -> GlobalReferenceTypeBuilder:
        """Access common_referenceToDataSetUseApproval builder (auto-initialized)."""
        if self._common_referenceToDataSetUseApproval is None:
            self._common_referenceToDataSetUseApproval = GlobalReferenceTypeBuilder()
        return self._common_referenceToDataSetUseApproval

    def build(self) -> DataEntryBy:
        """Build the final DataEntryBy instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_common_referenceToDataSetFormat', None)
        data.pop('_common_referenceToConvertedOriginalDataSetFrom', None)
        data.pop('_common_referenceToPersonOrEntityEnteringTheData', None)
        data.pop('_common_referenceToDataSetUseApproval', None)

        # Build nested objects
        if self._common_referenceToDataSetFormat is not None:
            data['common:referenceToDataSetFormat'] = self._common_referenceToDataSetFormat.build()
        if self._common_referenceToConvertedOriginalDataSetFrom is not None:
            data['common:referenceToConvertedOriginalDataSetFrom'] = self._common_referenceToConvertedOriginalDataSetFrom.build()
        if self._common_referenceToPersonOrEntityEnteringTheData is not None:
            data['common:referenceToPersonOrEntityEnteringTheData'] = self._common_referenceToPersonOrEntityEnteringTheData.build()
        if self._common_referenceToDataSetUseApproval is not None:
            data['common:referenceToDataSetUseApproval'] = self._common_referenceToDataSetUseApproval.build()

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

    common_dateOfLastRevision: Optional[AwareDatetime] = Field(None, alias='common:dateOfLastRevision')
    common_dataSetVersion: Optional[str] = Field(None, alias='common:dataSetVersion')
    common_permanentDataSetURI: Optional[AnyUrl] = Field(None, alias='common:permanentDataSetURI')
    common_workflowAndPublicationStatus: Optional[CommonWorkflowAndPublicationStatus] = Field(None, alias='common:workflowAndPublicationStatus')
    common_registrationNumber: Optional[str] = Field(None, alias='common:registrationNumber')
    common_copyright: Optional[CommonCopyright] = Field(None, alias='common:copyright')
    common_licenseType: Optional[CommonLicenseType] = Field(None, alias='common:licenseType')
    common_accessRestrictions: Optional[FTMultiLang] = Field(None, alias='common:accessRestrictions')
    common_other: Optional[str] = Field(None, alias='common:other')
    _common_referenceToPrecedingDataSetVersion: Optional[GlobalReferenceTypeBuilder] = None
    _common_referenceToUnchangedRepublication: Optional[GlobalReferenceTypeBuilder] = None
    _common_referenceToRegistrationAuthority: Optional[GlobalReferenceTypeBuilder] = None
    _common_referenceToOwnershipOfDataSet: Optional[GlobalReferenceTypeBuilder] = None
    _common_referenceToEntitiesWithExclusiveAccess: Optional[GlobalReferenceTypeBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def common_referenceToPrecedingDataSetVersion(self) -> GlobalReferenceTypeBuilder:
        """Access common_referenceToPrecedingDataSetVersion builder (auto-initialized)."""
        if self._common_referenceToPrecedingDataSetVersion is None:
            self._common_referenceToPrecedingDataSetVersion = GlobalReferenceTypeBuilder()
        return self._common_referenceToPrecedingDataSetVersion

    @property
    def common_referenceToUnchangedRepublication(self) -> GlobalReferenceTypeBuilder:
        """Access common_referenceToUnchangedRepublication builder (auto-initialized)."""
        if self._common_referenceToUnchangedRepublication is None:
            self._common_referenceToUnchangedRepublication = GlobalReferenceTypeBuilder()
        return self._common_referenceToUnchangedRepublication

    @property
    def common_referenceToRegistrationAuthority(self) -> GlobalReferenceTypeBuilder:
        """Access common_referenceToRegistrationAuthority builder (auto-initialized)."""
        if self._common_referenceToRegistrationAuthority is None:
            self._common_referenceToRegistrationAuthority = GlobalReferenceTypeBuilder()
        return self._common_referenceToRegistrationAuthority

    @property
    def common_referenceToOwnershipOfDataSet(self) -> GlobalReferenceTypeBuilder:
        """Access common_referenceToOwnershipOfDataSet builder (auto-initialized)."""
        if self._common_referenceToOwnershipOfDataSet is None:
            self._common_referenceToOwnershipOfDataSet = GlobalReferenceTypeBuilder()
        return self._common_referenceToOwnershipOfDataSet

    @property
    def common_referenceToEntitiesWithExclusiveAccess(self) -> GlobalReferenceTypeBuilder:
        """Access common_referenceToEntitiesWithExclusiveAccess builder (auto-initialized)."""
        if self._common_referenceToEntitiesWithExclusiveAccess is None:
            self._common_referenceToEntitiesWithExclusiveAccess = GlobalReferenceTypeBuilder()
        return self._common_referenceToEntitiesWithExclusiveAccess

    @field_validator('common_accessRestrictions', mode='before')
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

    def set_accessRestrictions(self, text: str, lang: str = 'en') -> 'PublicationAndOwnershipBuilder':
        """Set common_accessRestrictions text for a specific language."""
        if self.common_accessRestrictions is None:
            self.common_accessRestrictions = FTMultiLang()

        # Update existing or add new
        for item in self.common_accessRestrictions.items:
            if item.lang == lang:
                item.text = text
                return self

        self.common_accessRestrictions.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
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

        # Remove private builder fields
        data.pop('_common_referenceToPrecedingDataSetVersion', None)
        data.pop('_common_referenceToUnchangedRepublication', None)
        data.pop('_common_referenceToRegistrationAuthority', None)
        data.pop('_common_referenceToOwnershipOfDataSet', None)
        data.pop('_common_referenceToEntitiesWithExclusiveAccess', None)

        # Build nested objects
        if self._common_referenceToPrecedingDataSetVersion is not None:
            data['common:referenceToPrecedingDataSetVersion'] = self._common_referenceToPrecedingDataSetVersion.build()
        if self._common_referenceToUnchangedRepublication is not None:
            data['common:referenceToUnchangedRepublication'] = self._common_referenceToUnchangedRepublication.build()
        if self._common_referenceToRegistrationAuthority is not None:
            data['common:referenceToRegistrationAuthority'] = self._common_referenceToRegistrationAuthority.build()
        if self._common_referenceToOwnershipOfDataSet is not None:
            data['common:referenceToOwnershipOfDataSet'] = self._common_referenceToOwnershipOfDataSet.build()
        if self._common_referenceToEntitiesWithExclusiveAccess is not None:
            data['common:referenceToEntitiesWithExclusiveAccess'] = self._common_referenceToEntitiesWithExclusiveAccess.build()

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
    _common_commissionerAndGoal: Optional[CommonCommissionerAndGoalBuilder] = None
    _dataGenerator: Optional[DataGeneratorBuilder] = None
    _dataEntryBy: Optional[DataEntryByBuilder] = None
    _publicationAndOwnership: Optional[PublicationAndOwnershipBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
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

class LCIAResult1Builder(BaseModel):
    """Builder for LCIAResult1.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = LCIAResult1Builder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    root: Optional[list[LCIAResult1Item]] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> LCIAResult1:
        """Build the final LCIAResult1 instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return LCIAResult1.model_validate(data)

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

class LCIAResultsBuilder(BaseModel):
    """Builder for LCIAResults.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = LCIAResultsBuilder()
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
    _LCIAResult_1: Optional[LCIAResultBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def LCIAResult_1(self) -> LCIAResultBuilder:
        """Access LCIAResult_1 builder (auto-initialized)."""
        if self._LCIAResult_1 is None:
            self._LCIAResult_1 = LCIAResultBuilder()
        return self._LCIAResult_1

    def build(self) -> LCIAResults:
        """Build the final LCIAResults instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_LCIAResult_1', None)

        # Build nested objects
        if self._LCIAResult_1 is not None:
            data['LCIAResult'] = self._LCIAResult_1.build()

        return LCIAResults.model_validate(data)

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

class ProcessDataSetBuilder(BaseModel):
    """Builder for ProcessDataSet.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = ProcessDataSetBuilder()
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
    field_xmlns: Optional[Literal['http://lca.jrc.it/ILCD/Process']] = Field(None, alias='@xmlns')
    field_xmlns_xsi: Optional[Literal['http://www.w3.org/2001/XMLSchema-instance']] = Field(None, alias='@xmlns:xsi')
    field_version: Optional[Literal['1.1']] = Field(None, alias='@version')
    field_locations: Optional[Literal['../ILCDLocations.xml']] = Field(None, alias='@locations')
    field_xsi_schemaLocation: Optional[str] = Field(None, alias='@xsi:schemaLocation')
    common_other: Optional[str] = Field(None, alias='common:other')
    _processInformation: Optional[ProcessInformationBuilder] = None
    _modellingAndValidation: Optional[ModellingAndValidationBuilder] = None
    _administrativeInformation: Optional[AdministrativeInformationBuilder] = None
    _exchanges: Optional[ExchangesBuilder] = None
    _LCIAResults_1: Optional[LCIAResultsBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def processInformation(self) -> ProcessInformationBuilder:
        """Access processInformation builder (auto-initialized)."""
        if self._processInformation is None:
            self._processInformation = ProcessInformationBuilder()
        return self._processInformation

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
    def exchanges(self) -> ExchangesBuilder:
        """Access exchanges builder (auto-initialized)."""
        if self._exchanges is None:
            self._exchanges = ExchangesBuilder()
        return self._exchanges

    @property
    def LCIAResults_1(self) -> LCIAResultsBuilder:
        """Access LCIAResults_1 builder (auto-initialized)."""
        if self._LCIAResults_1 is None:
            self._LCIAResults_1 = LCIAResultsBuilder()
        return self._LCIAResults_1

    def build(self) -> ProcessDataSet:
        """Build the final ProcessDataSet instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_processInformation', None)
        data.pop('_modellingAndValidation', None)
        data.pop('_administrativeInformation', None)
        data.pop('_exchanges', None)
        data.pop('_LCIAResults_1', None)

        # Build nested objects
        if self._processInformation is not None:
            data['processInformation'] = self._processInformation.build()
        if self._modellingAndValidation is not None:
            data['modellingAndValidation'] = self._modellingAndValidation.build()
        if self._administrativeInformation is not None:
            data['administrativeInformation'] = self._administrativeInformation.build()
        if self._exchanges is not None:
            data['exchanges'] = self._exchanges.build()
        if self._LCIAResults_1 is not None:
            data['LCIAResults'] = self._LCIAResults_1.build()

        return ProcessDataSet.model_validate(data)

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

    _processDataSet: Optional[ProcessDataSetBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def processDataSet(self) -> ProcessDataSetBuilder:
        """Access processDataSet builder (auto-initialized)."""
        if self._processDataSet is None:
            self._processDataSet = ProcessDataSetBuilder()
        return self._processDataSet

    def build(self) -> Model:
        """Build the final Model instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_processDataSet', None)

        # Build nested objects
        if self._processDataSet is not None:
            data['processDataSet'] = self._processDataSet.build()

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

class CompletenessBuilder(BaseModel):
    """Builder for Completeness.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = CompletenessBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    completenessProductModel: Optional[CompletenessProductModel] = None
    completenessOtherProblemField: Optional[FTMultiLang] = None
    common_other: Optional[str] = Field(None, alias='common:other')
    _referenceToSupportedImpactAssessmentMethods: Optional[GlobalReferenceTypeBuilder] = None
    _completenessElementaryFlows: Optional[CompletenessElementaryFlowsBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def referenceToSupportedImpactAssessmentMethods(self) -> GlobalReferenceTypeBuilder:
        """Access referenceToSupportedImpactAssessmentMethods builder (auto-initialized)."""
        if self._referenceToSupportedImpactAssessmentMethods is None:
            self._referenceToSupportedImpactAssessmentMethods = GlobalReferenceTypeBuilder()
        return self._referenceToSupportedImpactAssessmentMethods

    @property
    def completenessElementaryFlows(self) -> CompletenessElementaryFlowsBuilder:
        """Access completenessElementaryFlows builder (auto-initialized)."""
        if self._completenessElementaryFlows is None:
            self._completenessElementaryFlows = CompletenessElementaryFlowsBuilder()
        return self._completenessElementaryFlows

    @field_validator('completenessOtherProblemField', mode='before')
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

    def set_completenessOtherProblemField(self, text: str, lang: str = 'en') -> 'CompletenessBuilder':
        """Set completenessOtherProblemField text for a specific language."""
        if self.completenessOtherProblemField is None:
            self.completenessOtherProblemField = FTMultiLang()

        # Update existing or add new
        for item in self.completenessOtherProblemField.items:
            if item.lang == lang:
                item.text = text
                return self

        self.completenessOtherProblemField.items.append(MultiLangItem(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_completenessOtherProblemField(self, lang: str = 'en') -> Optional[str]:
        """Get completenessOtherProblemField text for a specific language."""
        if not self.completenessOtherProblemField:
            return None
        for item in self.completenessOtherProblemField.items:
            if item.lang == lang:
                return item.text
        return None

    def build(self) -> Completeness:
        """Build the final Completeness instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_referenceToSupportedImpactAssessmentMethods', None)
        data.pop('_completenessElementaryFlows', None)

        # Build nested objects
        if self._referenceToSupportedImpactAssessmentMethods is not None:
            data['referenceToSupportedImpactAssessmentMethods'] = self._referenceToSupportedImpactAssessmentMethods.build()
        if self._completenessElementaryFlows is not None:
            data['completenessElementaryFlows'] = self._completenessElementaryFlows.build()

        return Completeness.model_validate(data)

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
CommonClasBuilder.model_rebuild()
CommonClas1Builder.model_rebuild()
CommonClas2Builder.model_rebuild()
CommonClas3Builder.model_rebuild()
CommonClassificationBuilder.model_rebuild()
ClassificationInformationBuilder.model_rebuild()
CompletenessElementaryFlowsBuilder.model_rebuild()
NameBuilder.model_rebuild()
CommonMethodBuilder.model_rebuild()
CommonMethodItemBuilder.model_rebuild()
CommonScopeBuilder.model_rebuild()
CommonScopeItemBuilder.model_rebuild()
CommonDataQualityIndicatorBuilder.model_rebuild()
CommonDataQualityIndicatorItemBuilder.model_rebuild()
CommonDataQualityIndicatorsBuilder.model_rebuild()
GlobalReferenceTypeBuilder.model_rebuild()
ComplementingProcessesBuilder.model_rebuild()
DataSetInformationBuilder.model_rebuild()
QuantitativeReferenceBuilder.model_rebuild()
TimeBuilder.model_rebuild()
LocationOfOperationSupplyOrProductionBuilder.model_rebuild()
SubLocationOfOperationSupplyOrProductionBuilder.model_rebuild()
GeographyBuilder.model_rebuild()
TechnologyBuilder.model_rebuild()
VariableParameterBuilder.model_rebuild()
MathematicalRelationsBuilder.model_rebuild()
ProcessInformationBuilder.model_rebuild()
LCIMethodAndAllocationBuilder.model_rebuild()
DataSourcesTreatmentAndRepresentativenessBuilder.model_rebuild()
LCIAResultBuilder.model_rebuild()
AllocationBuilder.model_rebuild()
ReviewBuilder.model_rebuild()
ComplianceBuilder.model_rebuild()
Compliance1ItemBuilder.model_rebuild()
Compliance1Builder.model_rebuild()
ComplianceDeclarationsBuilder.model_rebuild()
ValidationBuilder.model_rebuild()
ModellingAndValidationBuilder.model_rebuild()
AllocationsBuilder.model_rebuild()
ReferencesToDataSourceBuilder.model_rebuild()
ExchangeItemBuilder.model_rebuild()
ExchangesBuilder.model_rebuild()
CommonCommissionerAndGoalBuilder.model_rebuild()
DataGeneratorBuilder.model_rebuild()
DataEntryByBuilder.model_rebuild()
PublicationAndOwnershipBuilder.model_rebuild()
AdministrativeInformationBuilder.model_rebuild()
LCIAResult1Builder.model_rebuild()
LCIAResultsBuilder.model_rebuild()
ProcessDataSetBuilder.model_rebuild()
ModelBuilder.model_rebuild()
CompletenessBuilder.model_rebuild()
