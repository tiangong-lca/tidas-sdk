"""
Auto generated file. DO NOT EDIT.
Source: tidas_unitgroups.json
"""
from __future__ import annotations

from typing import Literal

from pydantic import Field
from tidas_sdk.core.base import TidasBaseModel
from tidas_sdk.core.multilang import MultiLangList

from datetime import datetime

class CommonClassificationCommonClass(TidasBaseModel):
    level: str = Field(default=..., alias='@level', description='If more than one class is specified in a hierachical classification system, the hierarchy level (1,2,...) could be specified with this attribute of class.')
    class_id: str = Field(default=..., alias='@classId', description="Unique identifier for the class. [Notes: If such identifiers are also defined in the referenced category file, they should be identical. Identifiers can be UUID's, but also other forms are allowed.]")
    text: str = Field(default=..., alias='#text')

class DatasetinformationClassificationinformationCommonClassification(TidasBaseModel):
    """Optional statistical or other classification of the data set. Typically also used for structuring LCA databases."""
    common_class: CommonClassificationCommonClass = Field(default=..., alias='common:class')
    common_other: str | None = Field(default=None, alias='common:other')

class UnitgroupinformationDatasetinformationClassificationinformation(TidasBaseModel):
    """Hierachical classification of the Unit groups; foreseen to be used to structure the Unit group content of the database. (Note: This entry is NOT required for the identification of the Unit group data set. It should nevertheless be avoided to use identical names for Unit groups in the same class."""
    common_classification: DatasetinformationClassificationinformationCommonClassification = Field(default=..., alias='common:classification', description='Optional statistical or other classification of the data set. Typically also used for structuring LCA databases.')

class UnitgroupdatasetUnitgroupinformationDatasetinformation(TidasBaseModel):
    common_u_u_i_d: str = Field(default=..., alias='common:UUID', description='Automatically generated Universally Unique Identifier of this data set. Together with the "Data set version", the UUID uniquely identifies each data set.')
    common_name: MultiLangList = Field(default_factory=MultiLangList, alias='common:name', description='Name of the unit group, typically indicating for which flow property or group of flow properties it is used. The individual units are named in the "Units" section of the "Unit group data set"')
    classification_information: UnitgroupinformationDatasetinformationClassificationinformation = Field(default=..., alias='classificationInformation', description='Hierachical classification of the Unit groups; foreseen to be used to structure the Unit group content of the database. (Note: This entry is NOT required for the identification of the Unit group data set. It should nevertheless be avoided to use identical names for Unit groups in the same class.')
    common_general_comment: MultiLangList = Field(default_factory=MultiLangList, alias='common:generalComment', description='Free text for general information about the data set. E.g. coverage of different unit systems, information sources used, etc.')
    common_other: str | None = Field(default=None, alias='common:other')

class UnitgroupdatasetUnitgroupinformationQuantitativereference(TidasBaseModel):
    reference_to_reference_unit: str = Field(default=..., alias='referenceToReferenceUnit')
    common_other: str | None = Field(default=None, alias='common:other')

class UnitgroupsUnitgroupdatasetUnitgroupinformation(TidasBaseModel):
    data_set_information: UnitgroupdatasetUnitgroupinformationDatasetinformation = Field(default=..., alias='dataSetInformation')
    quantitative_reference: UnitgroupdatasetUnitgroupinformationQuantitativereference = Field(default=..., alias='quantitativeReference')
    common_other: str | None = Field(default=None, alias='common:other')

class ModellingandvalidationCompliancedeclarationsComplianceoption0(TidasBaseModel):
    common_reference_to_compliance_system: Globalreferencetype = Field(default=..., alias='common:referenceToComplianceSystem')
    common_approval_of_overall_compliance: Literal['Fully compliant', 'Not compliant', 'Not defined'] = Field(default=..., alias='common:approvalOfOverallCompliance')
    common_other: str | None = Field(default=None, alias='common:other')

class ModellingandvalidationCompliancedeclarationsComplianceoption1item(TidasBaseModel):
    common_reference_to_compliance_system: Globalreferencetype = Field(default=..., alias='common:referenceToComplianceSystem')
    common_approval_of_overall_compliance: Literal['Fully compliant', 'Not compliant', 'Not defined'] = Field(default=..., alias='common:approvalOfOverallCompliance')
    common_other: str | None = Field(default=None, alias='common:other')

class UnitgroupdatasetModellingandvalidationCompliancedeclarations(TidasBaseModel):
    compliance: ModellingandvalidationCompliancedeclarationsComplianceoption0 | list[ModellingandvalidationCompliancedeclarationsComplianceoption1item] = Field(default=..., alias='compliance', description='One compliance declaration. Multiple declarations may be provided.')
    common_other: str | None = Field(default=None, alias='common:other')

class UnitgroupsUnitgroupdatasetModellingandvalidation(TidasBaseModel):
    compliance_declarations: UnitgroupdatasetModellingandvalidationCompliancedeclarations = Field(default=..., alias='complianceDeclarations')
    common_other: str | None = Field(default=None, alias='common:other')

class UnitgroupdatasetAdministrativeinformationDataentryby(TidasBaseModel):
    common_time_stamp: datetime = Field(default=..., alias='common:timeStamp', description='Date and time stamp of data set generation, typically an automated entry ("last saved").')
    common_reference_to_data_set_format: Globalreferencetype = Field(default=..., alias='common:referenceToDataSetFormat', description='"Source data set" of the used version of the ILCD format. If additional data format fields have been integrated into the data set file, using the "namespace" option, the used format namespace(s) are to be given. This is the case if the data sets carries additional information as specified by other, particular LCA formats, e.g. of other database networks or LCA softwares.')
    common_other: str | None = Field(default=None, alias='common:other')

class UnitgroupdatasetAdministrativeinformationPublicationandownership(TidasBaseModel):
    common_data_set_version: str = Field(default=..., alias='common:dataSetVersion', description='Version number of data set. First two digits refer to major updates, the second two digits to minor revisions and error corrections etc. The third three digits are intended for automatic and internal counting of versions during data set development. Together with the data set\'s UUID, the "Data set version" uniquely identifies each data set.')
    common_reference_to_preceding_data_set_version: Globalreferencetype | None = Field(default=None, alias='common:referenceToPrecedingDataSetVersion', description='Last preceding data set, which was replaced by this version. Either a URI of that data set (i.e. an internet address) or its UUID plus version number is given (or both).')
    common_permanent_data_set_u_r_i: str | None = Field(default=None, alias='common:permanentDataSetURI', description="URI (i.e. an internet address) of the original of this data set. [Note: This equally globally unique identifier supports users and software tools to identify and retrieve the original version of a data set via the internet or to check for available updates. The URI must not represent an existing WWW address, but it should be unique and point to the data access point, e.g. by combining the data owner's www path with the data set's UUID, e.g. http://www.mycompany.com/lca/processes/50f12420-8855-12db-b606-0900210c9a66.]")
    common_reference_to_ownership_of_data_set: Globalreferencetype = Field(default=..., alias='common:referenceToOwnershipOfDataSet', description='"Contact data set" of the person or entity who owns this data set. (Note: this is not necessarily the publisher of the data set.)')
    common_other: str | None = Field(default=None, alias='common:other')

class UnitgroupsUnitgroupdatasetAdministrativeinformation(TidasBaseModel):
    data_entry_by: UnitgroupdatasetAdministrativeinformationDataentryby = Field(default=..., alias='dataEntryBy')
    publication_and_ownership: UnitgroupdatasetAdministrativeinformationPublicationandownership = Field(default=..., alias='publicationAndOwnership')
    common_other: str | None = Field(default=None, alias='common:other')

class UnitgroupdatasetUnitsUnitoption0(TidasBaseModel):
    data_set_internal_i_d: str | None = Field(default=None, alias='@dataSetInternalID')
    name: str | None = Field(default=None, alias='name')
    mean_value: str | None = Field(default=None, alias='meanValue')
    general_comment: MultiLangList = Field(default_factory=MultiLangList, alias='generalComment', description='General comment on each single unit, typically giving the long name and unit system from which this unit stems, and (if necessary) referring to specifc data sources used, or for workflow purposes about status of "finalisation" of an entry etc.')
    common_other: str | None = Field(default=None, alias='common:other')

class UnitgroupdatasetUnitsUnitoption1item(TidasBaseModel):
    data_set_internal_i_d: str | None = Field(default=None, alias='@dataSetInternalID')
    name: str | None = Field(default=None, alias='name')
    mean_value: str | None = Field(default=None, alias='meanValue')
    general_comment: MultiLangList = Field(default_factory=MultiLangList, alias='generalComment', description='General comment on each single unit, typically giving the long name and unit system from which this unit stems, and (if necessary) referring to specifc data sources used, or for workflow purposes about status of "finalisation" of an entry etc.')

class UnitgroupsUnitgroupdatasetUnits(TidasBaseModel):
    unit: UnitgroupdatasetUnitsUnitoption0 | list[UnitgroupdatasetUnitsUnitoption1item] | None = Field(default=None, alias='unit')
    common_other: str | None = Field(default=None, alias='common:other')

class UnitgroupsUnitgroupdataset(TidasBaseModel):
    xmlns: Literal['http://lca.jrc.it/ILCD/UnitGroup'] = Field(default=..., alias='@xmlns')
    xmlns_common: Literal['http://lca.jrc.it/ILCD/Common'] = Field(default=..., alias='@xmlns:common')
    xmlns_xsi: Literal['http://www.w3.org/2001/XMLSchema-instance'] = Field(default=..., alias='@xmlns:xsi')
    version: Literal['1.1'] = Field(default=..., alias='@version')
    xsi_schema_location: Literal['http://lca.jrc.it/ILCD/UnitGroup ../../schemas/ILCD_UnitGroupDataSet.xsd'] = Field(default=..., alias='@xsi:schemaLocation')
    unit_group_information: UnitgroupsUnitgroupdatasetUnitgroupinformation = Field(default=..., alias='unitGroupInformation')
    modelling_and_validation: UnitgroupsUnitgroupdatasetModellingandvalidation = Field(default=..., alias='modellingAndValidation')
    administrative_information: UnitgroupsUnitgroupdatasetAdministrativeinformation = Field(default=..., alias='administrativeInformation')
    units: UnitgroupsUnitgroupdatasetUnits | None = Field(default=None, alias='units')
    common_other: str | None = Field(default=None, alias='common:other')

class Unitgroups(TidasBaseModel):
    unit_group_data_set: UnitgroupsUnitgroupdataset = Field(default=..., alias='unitGroupDataSet')
