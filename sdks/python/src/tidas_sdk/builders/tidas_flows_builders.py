# Auto-generated builder classes for TIDAS entities
# DO NOT EDIT - Regenerate using scripts/generate_builders.py

from __future__ import annotations

from typing import List, Literal, Optional
from pydantic import AnyUrl, AwareDatetime, BaseModel, ConfigDict, Field, RootModel, field_validator
from enum import (
    Enum,
)
from tidas_sdk.types.tidas_flows_elementary_category import (
    FlowsElementary,
    TidasFlowsElementaryText,
)
from tidas_sdk.types.tidas_flows_product_category import (
    FlowsProduct,
    TidasFlowsProductText,
)
from tidas_sdk.types.tidas_locations_category import (
    Locations,
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

from tidas_sdk.types.tidas_flows import *


class CommonCategoryItemBuilder(BaseModel):
    """Builder for CommonCategoryItem.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = CommonCategoryItemBuilder()
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
    field_catId: Optional[FlowsElementary] = Field(None, alias='@catId')
    text: Optional[TidasFlowsElementaryText] = Field(None, alias='#text')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> CommonCategoryItem:
        """Build the final CommonCategoryItem instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonCategoryItem.model_validate(data)

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

class CommonCategoryItem1Builder(BaseModel):
    """Builder for CommonCategoryItem1.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = CommonCategoryItem1Builder()
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
    field_catId: Optional[FlowsElementary] = Field(None, alias='@catId')
    text: Optional[TidasFlowsElementaryText] = Field(None, alias='#text')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> CommonCategoryItem1:
        """Build the final CommonCategoryItem1 instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonCategoryItem1.model_validate(data)

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

class CommonCategoryItem2Builder(BaseModel):
    """Builder for CommonCategoryItem2.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = CommonCategoryItem2Builder()
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
    field_catId: Optional[FlowsElementary] = Field(None, alias='@catId')
    text: Optional[TidasFlowsElementaryText] = Field(None, alias='#text')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> CommonCategoryItem2:
        """Build the final CommonCategoryItem2 instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonCategoryItem2.model_validate(data)

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

class CommonElementaryFlowCategorizationBuilder(BaseModel):
    """Builder for CommonElementaryFlowCategorization.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = CommonElementaryFlowCategorizationBuilder()
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
    _common_category: List[CommonCategoryItem | CommonCategoryItem1 | CommonCategoryItem2Builder] = []

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def common_category(self) -> List[CommonCategoryItem | CommonCategoryItem1 | CommonCategoryItem2Builder]:
        """Access common_category builder list."""
        return self._common_category

    @common_category.setter
    def common_category(self, value: List[CommonCategoryItem | CommonCategoryItem1 | CommonCategoryItem2Builder]) -> None:
        """Set common_category builder list."""
        self._common_category = value

    def add_common_category(self) -> CommonCategoryItem | CommonCategoryItem1 | CommonCategoryItem2Builder:
        """Add and return a new CommonCategoryItem | CommonCategoryItem1 | CommonCategoryItem2 builder."""
        builder = CommonCategoryItemBuilder()
        self._common_category.append(builder)
        return builder

    def build(self) -> CommonElementaryFlowCategorization:
        """Build the final CommonElementaryFlowCategorization instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_common_category', None)

        # Build array fields
        if self._common_category:
            data['common:category'] = [item.build() for item in self._common_category]

        return CommonElementaryFlowCategorization.model_validate(data)

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
    field_classId: Optional[FlowsProduct] = Field(None, alias='@classId')
    text: Optional[TidasFlowsProductText] = Field(None, alias='#text')

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
    field_classId: Optional[FlowsProduct] = Field(None, alias='@classId')
    text: Optional[TidasFlowsProductText] = Field(None, alias='#text')

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
    field_classId: Optional[FlowsProduct] = Field(None, alias='@classId')
    text: Optional[TidasFlowsProductText] = Field(None, alias='#text')

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
    field_classId: Optional[FlowsProduct] = Field(None, alias='@classId')
    text: Optional[TidasFlowsProductText] = Field(None, alias='#text')

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

class CommonClas4Builder(BaseModel):
    """Builder for CommonClas4.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = CommonClas4Builder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    field_level: Optional[Literal['4']] = Field(None, alias='@level')
    field_classId: Optional[FlowsProduct] = Field(None, alias='@classId')
    text: Optional[TidasFlowsProductText] = Field(None, alias='#text')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> CommonClas4:
        """Build the final CommonClas4 instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonClas4.model_validate(data)

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
    _common_class: List[CommonClas | CommonClas1 | CommonClas2 | CommonClas3 | CommonClas4Builder] = []

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def common_class(self) -> List[CommonClas | CommonClas1 | CommonClas2 | CommonClas3 | CommonClas4Builder]:
        """Access common_class builder list."""
        return self._common_class

    @common_class.setter
    def common_class(self, value: List[CommonClas | CommonClas1 | CommonClas2 | CommonClas3 | CommonClas4Builder]) -> None:
        """Set common_class builder list."""
        self._common_class = value

    def add_common_cla(self) -> CommonClas | CommonClas1 | CommonClas2 | CommonClas3 | CommonClas4Builder:
        """Add and return a new CommonClas | CommonClas1 | CommonClas2 | CommonClas3 | CommonClas4 builder."""
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
    """Hierachical classification of the Flow property foreseen to be used to structure the Flow property content of the database. (Note: This entry is NOT required for the identification of the Flow property data set. It should nevertheless be avoided to use identical names for Flow properties in the same class. (Builder)
    
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

    _common_elementaryFlowCategorization: Optional[CommonElementaryFlowCategorizationBuilder] = None
    _common_classification: Optional[CommonClassificationBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def common_elementaryFlowCategorization(self) -> CommonElementaryFlowCategorizationBuilder:
        """Access common_elementaryFlowCategorization builder (auto-initialized)."""
        if self._common_elementaryFlowCategorization is None:
            self._common_elementaryFlowCategorization = CommonElementaryFlowCategorizationBuilder()
        return self._common_elementaryFlowCategorization

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
        data.pop('_common_elementaryFlowCategorization', None)
        data.pop('_common_classification', None)

        # Build nested objects
        if self._common_elementaryFlowCategorization is not None:
            data['common:elementaryFlowCategorization'] = self._common_elementaryFlowCategorization.build()
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

class CommonElementaryFlowCategorization1Builder(BaseModel):
    """Builder for CommonElementaryFlowCategorization1.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = CommonElementaryFlowCategorization1Builder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    common_category: Optional[list[CommonCategoryItem3 | CommonCategoryItem4 | CommonCategoryItem5] | CommonCategory] = Field(None, alias='common:category')
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> CommonElementaryFlowCategorization1:
        """Build the final CommonElementaryFlowCategorization1 instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonElementaryFlowCategorization1.model_validate(data)

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

class CommonClassification1Builder(BaseModel):
    """Builder for CommonClassification1.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = CommonClassification1Builder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    common_class: Optional[list[CommonClas5 | CommonClas6 | CommonClas7 | CommonClas8 | CommonClas9] | CommonClass] = Field(None, alias='common:class')
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> CommonClassification1:
        """Build the final CommonClassification1 instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return CommonClassification1.model_validate(data)

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

class ClassificationInformation1Builder(BaseModel):
    """Hierachical classification of the Flow property foreseen to be used to structure the Flow property content of the database. (Note: This entry is NOT required for the identification of the Flow property data set. It should nevertheless be avoided to use identical names for Flow properties in the same class. (Builder)
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = ClassificationInformation1Builder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    _common_elementaryFlowCategorization: Optional[CommonElementaryFlowCategorization1Builder] = None
    _common_classification: Optional[CommonClassification1Builder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def common_elementaryFlowCategorization(self) -> CommonElementaryFlowCategorization1Builder:
        """Access common_elementaryFlowCategorization builder (auto-initialized)."""
        if self._common_elementaryFlowCategorization is None:
            self._common_elementaryFlowCategorization = CommonElementaryFlowCategorization1Builder()
        return self._common_elementaryFlowCategorization

    @property
    def common_classification(self) -> CommonClassification1Builder:
        """Access common_classification builder (auto-initialized)."""
        if self._common_classification is None:
            self._common_classification = CommonClassification1Builder()
        return self._common_classification

    def build(self) -> ClassificationInformation1:
        """Build the final ClassificationInformation1 instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_common_elementaryFlowCategorization', None)
        data.pop('_common_classification', None)

        # Build nested objects
        if self._common_elementaryFlowCategorization is not None:
            data['common:elementaryFlowCategorization'] = self._common_elementaryFlowCategorization.build()
        if self._common_classification is not None:
            data['common:classification'] = self._common_classification.build()

        return ClassificationInformation1.model_validate(data)

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

class LCIMethodBuilder(BaseModel):
    """Builder for LCIMethod.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = LCIMethodBuilder()
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
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> LCIMethod:
        """Build the final LCIMethod instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        return LCIMethod.model_validate(data)

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

class NameBuilder(BaseModel):
    """Builder for Name.
    
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
    flowProperties: Optional[StringMultiLang] = None
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @field_validator('baseName', 'treatmentStandardsRoutes', 'mixAndLocationTypes', 'flowProperties', mode='before')
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

    def set_flowProperties(self, text: str, lang: str = 'en') -> 'NameBuilder':
        """Set flowProperties text for a specific language."""
        if self.flowProperties is None:
            self.flowProperties = StringMultiLang()

        # Update existing or add new
        for item in self.flowProperties.items:
            if item.lang == lang:
                item.text = text
                return self

        self.flowProperties.items.append(MultiLangItemString(**{'@xml:lang': lang, '#text': text}))
        return self

    def get_flowProperties(self, lang: str = 'en') -> Optional[str]:
        """Get flowProperties text for a specific language."""
        if not self.flowProperties:
            return None
        for item in self.flowProperties.items:
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
    common_synonyms: Optional[FTMultiLang] = Field(None, alias='common:synonyms')
    CASNumber: Optional[str] = None
    sumFormula: Optional[str] = None
    common_generalComment: Optional[FTMultiLang] = Field(None, alias='common:generalComment')
    common_other: Optional[str] = Field(None, alias='common:other')
    _name: Optional[NameBuilder] = None
    _classificationInformation: Optional[ClassificationInformationBuilder] = None

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
    def classificationInformation(self) -> ClassificationInformationBuilder:
        """Access classificationInformation builder (auto-initialized)."""
        if self._classificationInformation is None:
            self._classificationInformation = ClassificationInformationBuilder()
        return self._classificationInformation

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
        data.pop('_classificationInformation', None)

        # Build nested objects
        if self._name is not None:
            data['name'] = self._name.build()
        if self._classificationInformation is not None:
            data['classificationInformation'] = self._classificationInformation.build()

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
    """Builder for QuantitativeReference.
    
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

    referenceToReferenceFlowProperty: Optional[str] = None
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

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

    locationOfSupply: Optional[Locations] = None
    common_other: Optional[str] = Field(None, alias='common:other')

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    def build(self) -> Geography:
        """Build the final Geography instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

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

    technologicalApplicability: Optional[FTMultiLang] = None
    common_other: Optional[str] = Field(None, alias='common:other')
    _referenceToTechnicalSpecification: Optional[GlobalReferenceTypeBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def referenceToTechnicalSpecification(self) -> GlobalReferenceTypeBuilder:
        """Access referenceToTechnicalSpecification builder (auto-initialized)."""
        if self._referenceToTechnicalSpecification is None:
            self._referenceToTechnicalSpecification = GlobalReferenceTypeBuilder()
        return self._referenceToTechnicalSpecification

    @field_validator('technologicalApplicability', mode='before')
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
        data.pop('_referenceToTechnicalSpecification', None)

        # Build nested objects
        if self._referenceToTechnicalSpecification is not None:
            data['referenceToTechnicalSpecification'] = self._referenceToTechnicalSpecification.build()

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

class FlowInformationBuilder(BaseModel):
    """Builder for FlowInformation.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = FlowInformationBuilder()
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
    _geography: Optional[GeographyBuilder] = None
    _technology: Optional[TechnologyBuilder] = None

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

    def build(self) -> FlowInformation:
        """Build the final FlowInformation instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_dataSetInformation', None)
        data.pop('_quantitativeReference', None)
        data.pop('_geography', None)
        data.pop('_technology', None)

        # Build nested objects
        if self._dataSetInformation is not None:
            data['dataSetInformation'] = self._dataSetInformation.build()
        if self._quantitativeReference is not None:
            data['quantitativeReference'] = self._quantitativeReference.build()
        if self._geography is not None:
            data['geography'] = self._geography.build()
        if self._technology is not None:
            data['technology'] = self._technology.build()

        return FlowInformation.model_validate(data)

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
    """Builder for ComplianceDeclarations.
    
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
    _LCIMethod_1: Optional[LCIMethodBuilder] = None
    _complianceDeclarations: Optional[ComplianceDeclarationsBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def LCIMethod_1(self) -> LCIMethodBuilder:
        """Access LCIMethod_1 builder (auto-initialized)."""
        if self._LCIMethod_1 is None:
            self._LCIMethod_1 = LCIMethodBuilder()
        return self._LCIMethod_1

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
        data.pop('_LCIMethod_1', None)
        data.pop('_complianceDeclarations', None)

        # Build nested objects
        if self._LCIMethod_1 is not None:
            data['LCIMethod'] = self._LCIMethod_1.build()
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
    common_other: Optional[str] = Field(None, alias='common:other')
    _common_referenceToDataSetFormat: Optional[GlobalReferenceTypeBuilder] = None
    _common_referenceToPersonOrEntityEnteringTheData: Optional[GlobalReferenceTypeBuilder] = None

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
    def common_referenceToPersonOrEntityEnteringTheData(self) -> GlobalReferenceTypeBuilder:
        """Access common_referenceToPersonOrEntityEnteringTheData builder (auto-initialized)."""
        if self._common_referenceToPersonOrEntityEnteringTheData is None:
            self._common_referenceToPersonOrEntityEnteringTheData = GlobalReferenceTypeBuilder()
        return self._common_referenceToPersonOrEntityEnteringTheData

    def build(self) -> DataEntryBy:
        """Build the final DataEntryBy instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_common_referenceToDataSetFormat', None)
        data.pop('_common_referenceToPersonOrEntityEnteringTheData', None)

        # Build nested objects
        if self._common_referenceToDataSetFormat is not None:
            data['common:referenceToDataSetFormat'] = self._common_referenceToDataSetFormat.build()
        if self._common_referenceToPersonOrEntityEnteringTheData is not None:
            data['common:referenceToPersonOrEntityEnteringTheData'] = self._common_referenceToPersonOrEntityEnteringTheData.build()

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
    """Builder for PublicationAndOwnership.
    
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
    common_permanentDataSetURI: Optional[AnyUrl] = Field(None, alias='common:permanentDataSetURI')
    common_other: Optional[str] = Field(None, alias='common:other')
    _common_referenceToPrecedingDataSetVersion: Optional[GlobalReferenceTypeBuilder] = None
    _common_referenceToOwnershipOfDataSet: Optional[GlobalReferenceTypeBuilder] = None

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
    def common_referenceToOwnershipOfDataSet(self) -> GlobalReferenceTypeBuilder:
        """Access common_referenceToOwnershipOfDataSet builder (auto-initialized)."""
        if self._common_referenceToOwnershipOfDataSet is None:
            self._common_referenceToOwnershipOfDataSet = GlobalReferenceTypeBuilder()
        return self._common_referenceToOwnershipOfDataSet

    def build(self) -> PublicationAndOwnership:
        """Build the final PublicationAndOwnership instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_common_referenceToPrecedingDataSetVersion', None)
        data.pop('_common_referenceToOwnershipOfDataSet', None)

        # Build nested objects
        if self._common_referenceToPrecedingDataSetVersion is not None:
            data['common:referenceToPrecedingDataSetVersion'] = self._common_referenceToPrecedingDataSetVersion.build()
        if self._common_referenceToOwnershipOfDataSet is not None:
            data['common:referenceToOwnershipOfDataSet'] = self._common_referenceToOwnershipOfDataSet.build()

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
    """Builder for AdministrativeInformation.
    
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

class FlowPropertyBuilder(BaseModel):
    """Builder for FlowProperty.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = FlowPropertyBuilder()
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
    meanValue: Optional[str] = None
    minimumValue: Optional[str] = None
    maximumValue: Optional[str] = None
    uncertaintyDistributionType: Optional[UncertaintyDistributionType] = None
    relativeStandardDeviation95In: Optional[str] = None
    dataDerivationTypeStatus: Optional[DataDerivationTypeStatus] = None
    generalComment: Optional[StringMultiLang] = None
    common_other: Optional[str] = Field(None, alias='common:other')
    _referenceToFlowPropertyDataSet: Optional[GlobalReferenceTypeBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def referenceToFlowPropertyDataSet(self) -> GlobalReferenceTypeBuilder:
        """Access referenceToFlowPropertyDataSet builder (auto-initialized)."""
        if self._referenceToFlowPropertyDataSet is None:
            self._referenceToFlowPropertyDataSet = GlobalReferenceTypeBuilder()
        return self._referenceToFlowPropertyDataSet

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

    def set_generalComment(self, text: str, lang: str = 'en') -> 'FlowPropertyBuilder':
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

    def build(self) -> FlowProperty:
        """Build the final FlowProperty instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_referenceToFlowPropertyDataSet', None)

        # Build nested objects
        if self._referenceToFlowPropertyDataSet is not None:
            data['referenceToFlowPropertyDataSet'] = self._referenceToFlowPropertyDataSet.build()

        return FlowProperty.model_validate(data)

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

class FlowPropertiesBuilder(BaseModel):
    """Builder for FlowProperties.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = FlowPropertiesBuilder()
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
    _flowProperty: Optional[FlowPropertyBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def flowProperty(self) -> FlowPropertyBuilder:
        """Access flowProperty builder (auto-initialized)."""
        if self._flowProperty is None:
            self._flowProperty = FlowPropertyBuilder()
        return self._flowProperty

    def build(self) -> FlowProperties:
        """Build the final FlowProperties instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_flowProperty', None)

        # Build nested objects
        if self._flowProperty is not None:
            data['flowProperty'] = self._flowProperty.build()

        return FlowProperties.model_validate(data)

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

    _flowDataSet: Optional[FlowDataSetBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def flowDataSet(self) -> FlowDataSetBuilder:
        """Access flowDataSet builder (auto-initialized)."""
        if self._flowDataSet is None:
            self._flowDataSet = FlowDataSetBuilder()
        return self._flowDataSet

    def build(self) -> Model:
        """Build the final Model instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_flowDataSet', None)

        # Build nested objects
        if self._flowDataSet is not None:
            data['flowDataSet'] = self._flowDataSet.build()

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

class FlowDataSetBuilder(BaseModel):
    """Builder for FlowDataSet.
    
    Important:
        - During construction, nested data is stored in private fields
        - Calling model_dump() or model_dump_json() will NOT show nested builder state
        - Always call build() to create the final model before serialization
        - Use build_dump() for debugging to see full builder state during construction
    
    Example:
        builder = FlowDataSetBuilder()
        # Set fields...
        
        # WRONG - returns empty or incomplete:
        # json_str = builder.model_dump_json()
        
        # CORRECT - build first, then serialize:
        model = builder.build()
        json_str = model.model_dump_json()
        
        # For debugging during construction:
        debug_json = builder.build_dump()
    """

    field_xmlns: Optional[Literal['http://lca.jrc.it/ILCD/Flow']] = Field(None, alias='@xmlns')
    field_xmlns_common: Optional[Literal['http://lca.jrc.it/ILCD/Common']] = Field(None, alias='@xmlns:common')
    field_xmlns_ecn: Optional[Literal['http://eplca.jrc.ec.europa.eu/ILCD/Extensions/2018/ECNumber']] = Field(None, alias='@xmlns:ecn')
    field_xmlns_xsi: Optional[Literal['http://www.w3.org/2001/XMLSchema-instance']] = Field(None, alias='@xmlns:xsi')
    field_version: Optional[Literal['1.1']] = Field(None, alias='@version')
    field_locations: Optional[Literal['../ILCDLocations.xml']] = Field(None, alias='@locations')
    field_xsi_schemaLocation: Optional[Literal['http://lca.jrc.it/ILCD/Flow ../../schemas/ILCD_FlowDataSet.xsd']] = Field(None, alias='@xsi:schemaLocation')
    common_other: Optional[str] = Field(None, alias='common:other')
    _flowInformation: Optional[FlowInformationBuilder] = None
    _modellingAndValidation: Optional[ModellingAndValidationBuilder] = None
    _administrativeInformation: Optional[AdministrativeInformationBuilder] = None
    _flowProperties: Optional[FlowPropertiesBuilder] = None

    model_config = ConfigDict(
        extra='allow',
        validate_assignment=True,  # Enable validators on assignment
    )

    @property
    def flowInformation(self) -> FlowInformationBuilder:
        """Access flowInformation builder (auto-initialized)."""
        if self._flowInformation is None:
            self._flowInformation = FlowInformationBuilder()
        return self._flowInformation

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
    def flowProperties(self) -> FlowPropertiesBuilder:
        """Access flowProperties builder (auto-initialized)."""
        if self._flowProperties is None:
            self._flowProperties = FlowPropertiesBuilder()
        return self._flowProperties

    def build(self) -> FlowDataSet:
        """Build the final FlowDataSet instance."""
        data = self.model_dump(exclude_none=True, by_alias=True)

        # Remove private builder fields
        data.pop('_flowInformation', None)
        data.pop('_modellingAndValidation', None)
        data.pop('_administrativeInformation', None)
        data.pop('_flowProperties', None)

        # Build nested objects
        if self._flowInformation is not None:
            data['flowInformation'] = self._flowInformation.build()
        if self._modellingAndValidation is not None:
            data['modellingAndValidation'] = self._modellingAndValidation.build()
        if self._administrativeInformation is not None:
            data['administrativeInformation'] = self._administrativeInformation.build()
        if self._flowProperties is not None:
            data['flowProperties'] = self._flowProperties.build()

        return FlowDataSet.model_validate(data)

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
CommonCategoryItemBuilder.model_rebuild()
CommonCategoryItem1Builder.model_rebuild()
CommonCategoryItem2Builder.model_rebuild()
CommonElementaryFlowCategorizationBuilder.model_rebuild()
CommonClasBuilder.model_rebuild()
CommonClas1Builder.model_rebuild()
CommonClas2Builder.model_rebuild()
CommonClas3Builder.model_rebuild()
CommonClas4Builder.model_rebuild()
CommonClassificationBuilder.model_rebuild()
ClassificationInformationBuilder.model_rebuild()
CommonElementaryFlowCategorization1Builder.model_rebuild()
CommonClassification1Builder.model_rebuild()
ClassificationInformation1Builder.model_rebuild()
LCIMethodBuilder.model_rebuild()
GlobalReferenceTypeBuilder.model_rebuild()
NameBuilder.model_rebuild()
DataSetInformationBuilder.model_rebuild()
QuantitativeReferenceBuilder.model_rebuild()
GeographyBuilder.model_rebuild()
TechnologyBuilder.model_rebuild()
FlowInformationBuilder.model_rebuild()
ComplianceBuilder.model_rebuild()
Compliance1ItemBuilder.model_rebuild()
Compliance1Builder.model_rebuild()
ComplianceDeclarationsBuilder.model_rebuild()
ModellingAndValidationBuilder.model_rebuild()
DataEntryByBuilder.model_rebuild()
PublicationAndOwnershipBuilder.model_rebuild()
AdministrativeInformationBuilder.model_rebuild()
FlowPropertyBuilder.model_rebuild()
FlowPropertiesBuilder.model_rebuild()
ModelBuilder.model_rebuild()
FlowDataSetBuilder.model_rebuild()
