"""
Auto generated file. DO NOT EDIT.
Source: tidas_flows.json
"""
from __future__ import annotations

from typing import Any, Literal

from pydantic import Field
from tidas_sdk.core.base import TidasBaseModel
from tidas_sdk.core.multilang import MultiLangList

from datetime import datetime

class FlowinformationDatasetinformationName(TidasBaseModel):
    base_name: MultiLangList = Field(default_factory=MultiLangList, alias='baseName')
    treatment_standards_routes: MultiLangList = Field(default_factory=MultiLangList, alias='treatmentStandardsRoutes')
    mix_and_location_types: MultiLangList = Field(default_factory=MultiLangList, alias='mixAndLocationTypes')
    flow_properties: MultiLangList = Field(default_factory=MultiLangList, alias='flowProperties')
    common_other: str | None = Field(default=None, alias='common:other')

class FlowdatasetFlowinformationDatasetinformation(TidasBaseModel):
    common_u_u_i_d: str = Field(default=..., alias='common:UUID', description='Automatically generated Universally Unique Identifier of this data set. Together with the "Data set version", the UUID uniquely identifies each data set.')
    name: FlowinformationDatasetinformationName = Field(default=..., alias='name')
    common_synonyms: MultiLangList = Field(default_factory=MultiLangList, alias='common:synonyms', description='Synonyms / alternative names / brands of the good, service, or process. Separated by semicolon.')
    classification_information: Any = Field(default=..., alias='classificationInformation', description='Hierachical classification of the Flow property foreseen to be used to structure the Flow property content of the database. (Note: This entry is NOT required for the identification of the Flow property data set. It should nevertheless be avoided to use identical names for Flow properties in the same class.')
    c_a_s_number: str | None = Field(default=None, alias='CASNumber', description='Chemical Abstract Systems Number of the substance. [Note: Should only be given for (virtually) pure substances, but NOT also for the main constituent of a material or product etc.]')
    sum_formula: str | None = Field(default=None, alias='sumFormula', description='Chemical sum formula of the substance.')
    common_general_comment: MultiLangList = Field(default_factory=MultiLangList, alias='common:generalComment', description='Free text for general information about the Flow data set. It may contain information about e.g. the use of the substance, good, service or process in a specific technology or industry-context, information sources used, data selection principles etc.')
    common_other: str | None = Field(default=None, alias='common:other')

class FlowdatasetFlowinformationQuantitativereference(TidasBaseModel):
    reference_to_reference_flow_property: str = Field(default=..., alias='referenceToReferenceFlowProperty')
    common_other: str | None = Field(default=None, alias='common:other')

class FlowdatasetFlowinformationGeography(TidasBaseModel):
    location_of_supply: TidasLocationsCategoryJson | None = Field(default=None, alias='locationOfSupply')
    common_other: str | None = Field(default=None, alias='common:other')

class FlowdatasetFlowinformationTechnology(TidasBaseModel):
    technological_applicability: MultiLangList = Field(default_factory=MultiLangList, alias='technologicalApplicability', description='Description of the intended / possible applications of the good or service, or waste. E.g. for which type of products the material, represented by this data set, is used. Examples: "This high purity chemical is used for analytical laboratories only." or "This technical quality bulk chemical is used for large scale synthesis in chemical industry.". Or: "This type of biowaste is typically composted or biodigested as the water content is too high for efficient combustion".')
    reference_to_technical_specification: Globalreferencetype | None = Field(default=None, alias='referenceToTechnicalSpecification', description='"Source data set(s)" of the product\'s or waste\'s technical specification, waste data sheet, safety data sheet, etc.')
    common_other: str | None = Field(default=None, alias='common:other')

class FlowsFlowdatasetFlowinformation(TidasBaseModel):
    data_set_information: FlowdatasetFlowinformationDatasetinformation = Field(default=..., alias='dataSetInformation')
    quantitative_reference: FlowdatasetFlowinformationQuantitativereference = Field(default=..., alias='quantitativeReference')
    geography: FlowdatasetFlowinformationGeography | None = Field(default=None, alias='geography')
    technology: FlowdatasetFlowinformationTechnology | None = Field(default=None, alias='technology')
    common_other: str | None = Field(default=None, alias='common:other')

class FlowdatasetModellingandvalidationLcimethod(TidasBaseModel):
    type_of_data_set: Literal['Elementary flow', 'Product flow', 'Waste flow'] = Field(default=..., alias='typeOfDataSet')
    common_other: str | None = Field(default=None, alias='common:other')

class ModellingandvalidationCompliancedeclarationsComplianceoption0(TidasBaseModel):
    common_reference_to_compliance_system: Globalreferencetype = Field(default=..., alias='common:referenceToComplianceSystem')
    common_approval_of_overall_compliance: Literal['Fully compliant', 'Not compliant', 'Not defined'] = Field(default=..., alias='common:approvalOfOverallCompliance')
    common_other: str | None = Field(default=None, alias='common:other')

class ModellingandvalidationCompliancedeclarationsComplianceoption1item(TidasBaseModel):
    common_reference_to_compliance_system: Globalreferencetype = Field(default=..., alias='common:referenceToComplianceSystem')
    common_approval_of_overall_compliance: Literal['Fully compliant', 'Not compliant', 'Not defined'] = Field(default=..., alias='common:approvalOfOverallCompliance')
    common_other: str | None = Field(default=None, alias='common:other')

class FlowdatasetModellingandvalidationCompliancedeclarations(TidasBaseModel):
    compliance: ModellingandvalidationCompliancedeclarationsComplianceoption0 | list[ModellingandvalidationCompliancedeclarationsComplianceoption1item] = Field(default=..., alias='compliance', description='One compliance declaration. Multiple declarations may be provided.')
    common_other: str | None = Field(default=None, alias='common:other')

class FlowsFlowdatasetModellingandvalidation(TidasBaseModel):
    l_c_i_method: FlowdatasetModellingandvalidationLcimethod = Field(default=..., alias='LCIMethod')
    compliance_declarations: FlowdatasetModellingandvalidationCompliancedeclarations = Field(default=..., alias='complianceDeclarations')
    common_other: str | None = Field(default=None, alias='common:other')

class FlowdatasetAdministrativeinformationDataentryby(TidasBaseModel):
    common_time_stamp: datetime = Field(default=..., alias='common:timeStamp', description='Date and time stamp of data set generation, typically an automated entry ("last saved").')
    common_reference_to_data_set_format: Globalreferencetype = Field(default=..., alias='common:referenceToDataSetFormat', description='"Source data set" of the used version of the ILCD format. If additional data format fields have been integrated into the data set file, using the "namespace" option, the used format namespace(s) are to be given. This is the case if the data sets carries additional information as specified by other, particular LCA formats, e.g. of other database networks or LCA softwares.')
    common_reference_to_person_or_entity_entering_the_data: Globalreferencetype | None = Field(default=None, alias='common:referenceToPersonOrEntityEnteringTheData', description='"Contact data set" of the responsible person or entity that has documented this data set, i.e. entered the data and the descriptive information.')
    common_other: str | None = Field(default=None, alias='common:other')

class FlowdatasetAdministrativeinformationPublicationandownership(TidasBaseModel):
    common_data_set_version: str = Field(default=..., alias='common:dataSetVersion', description='Version number of data set. First two digits refer to major updates, the second two digits to minor revisions and error corrections etc. The third three digits are intended for automatic and internal counting of versions during data set development. Together with the data set\'s UUID, the "Data set version" uniquely identifies each data set.')
    common_reference_to_preceding_data_set_version: Globalreferencetype | None = Field(default=None, alias='common:referenceToPrecedingDataSetVersion', description='Last preceding data set, which was replaced by this version. Either a URI of that data set (i.e. an internet address) or its UUID plus version number is given (or both).')
    common_permanent_data_set_u_r_i: str | None = Field(default=None, alias='common:permanentDataSetURI', description="URI (i.e. an internet address) of the original of this data set. [Note: This equally globally unique identifier supports users and software tools to identify and retrieve the original version of a data set via the internet or to check for available updates. The URI must not represent an existing WWW address, but it should be unique and point to the data access point, e.g. by combining the data owner's www path with the data set's UUID, e.g. http://www.mycompany.com/lca/processes/50f12420-8855-12db-b606-0900210c9a66.]")
    common_reference_to_ownership_of_data_set: Globalreferencetype = Field(default=..., alias='common:referenceToOwnershipOfDataSet', description='"Contact data set" of the person or entity who owns this data set. (Note: this is not necessarily the publisher of the data set.)')
    common_other: str | None = Field(default=None, alias='common:other')

class FlowsFlowdatasetAdministrativeinformation(TidasBaseModel):
    data_entry_by: FlowdatasetAdministrativeinformationDataentryby = Field(default=..., alias='dataEntryBy')
    publication_and_ownership: FlowdatasetAdministrativeinformationPublicationandownership = Field(default=..., alias='publicationAndOwnership')
    common_other: str | None = Field(default=None, alias='common:other')

class FlowdatasetFlowpropertiesFlowpropertyoption0(TidasBaseModel):
    data_set_internal_i_d: str = Field(default=..., alias='@dataSetInternalID', description='Automated entry: internal ID, used in the "Quantitative reference" section to identify the reference flow property.')
    reference_to_flow_property_data_set: Globalreferencetype = Field(default=..., alias='referenceToFlowPropertyDataSet')
    mean_value: str = Field(default=..., alias='meanValue', description='Value for the flow expressed in this flow property in relationship to the the value of the flow expressed in its reference flow property (see field "Reference to reference flow property" in the "Quantitative reference" section). [Notes and examples: If the product flow "Diesel" is expressed by default in "Mass" (= reference flow property) and "kg" (= corresponding reference unit), the value that would be stated here for an additional flow property e.g. "Net calorific value" would be "42.5", as this flow property has the reference unit "MJ" and Diesel has a net calorific value of 42.5 MJ per 1 kg. It is recommended to report only significant digits of the value.]')
    minimum_value: str | None = Field(default=None, alias='minimumValue', description='Minimum value of this flow property in case uncertainty distribution is uniform or triangular.')
    maximum_value: str | None = Field(default=None, alias='maximumValue', description='Maximum value of this flow property in case uncertainty distribution is uniform or triangular.')
    uncertainty_distribution_type: Literal['undefined', 'log-normal', 'normal', 'triangular', 'uniform'] | None = Field(default=None, alias='uncertaintyDistributionType')
    relative_standard_deviation95_in: str | None = Field(default=None, alias='relativeStandardDeviation95In', description='The resulting overall uncertainty of the calculated variable value considering uncertainty of measurements, modelling, appropriateness etc. [Notes: For log-normal distribution the square of the geometric standard deviation (SDg^2) is stated. Mean value times SDg^2 equals the 97.5% value (= Maximum value), Mean value divided by SDg^2 equals the 2.5% value (= Minimum value). For normal distribution the doubled standard deviation value (2*SD) is entered. Mean value plus 2*SD equals 97.5% value (= Maximum value), Mean value minus 2*SD equals 2.5% value (= Minimum value). This data field remains empty when uniform or triangular uncertainty distribution is applied.]')
    data_derivation_type_status: Literal['Measured', 'Calculated', 'Estimated', 'Unknown derivation'] | None = Field(default=None, alias='dataDerivationTypeStatus')
    general_comment: MultiLangList = Field(default_factory=MultiLangList, alias='generalComment')
    common_other: str | None = Field(default=None, alias='common:other')

class FlowdatasetFlowpropertiesFlowpropertyoption1item(TidasBaseModel):
    data_set_internal_i_d: str = Field(default=..., alias='@dataSetInternalID', description='Automated entry: internal ID, used in the "Quantitative reference" section to identify the reference flow property.')
    reference_to_flow_property_data_set: Globalreferencetype = Field(default=..., alias='referenceToFlowPropertyDataSet')
    mean_value: str = Field(default=..., alias='meanValue', description='Value for the flow expressed in this flow property in relationship to the the value of the flow expressed in its reference flow property (see field "Reference to reference flow property" in the "Quantitative reference" section). [Notes and examples: If the product flow "Diesel" is expressed by default in "Mass" (= reference flow property) and "kg" (= corresponding reference unit), the value that would be stated here for an additional flow property e.g. "Net calorific value" would be "42.5", as this flow property has the reference unit "MJ" and Diesel has a net calorific value of 42.5 MJ per 1 kg. It is recommended to report only significant digits of the value.]')
    minimum_value: str | None = Field(default=None, alias='minimumValue', description='Minimum value of this flow property in case uncertainty distribution is uniform or triangular.')
    maximum_value: str | None = Field(default=None, alias='maximumValue', description='Maximum value of this flow property in case uncertainty distribution is uniform or triangular.')
    uncertainty_distribution_type: Literal['undefined', 'log-normal', 'normal', 'triangular', 'uniform'] | None = Field(default=None, alias='uncertaintyDistributionType')
    relative_standard_deviation95_in: str | None = Field(default=None, alias='relativeStandardDeviation95In', description='The resulting overall uncertainty of the calculated variable value considering uncertainty of measurements, modelling, appropriateness etc. [Notes: For log-normal distribution the square of the geometric standard deviation (SDg^2) is stated. Mean value times SDg^2 equals the 97.5% value (= Maximum value), Mean value divided by SDg^2 equals the 2.5% value (= Minimum value). For normal distribution the doubled standard deviation value (2*SD) is entered. Mean value plus 2*SD equals 97.5% value (= Maximum value), Mean value minus 2*SD equals 2.5% value (= Minimum value). This data field remains empty when uniform or triangular uncertainty distribution is applied.]')
    data_derivation_type_status: Literal['Measured', 'Calculated', 'Estimated', 'Unknown derivation'] | None = Field(default=None, alias='dataDerivationTypeStatus')
    general_comment: MultiLangList = Field(default_factory=MultiLangList, alias='generalComment')
    common_other: str | None = Field(default=None, alias='common:other')

class FlowsFlowdatasetFlowproperties(TidasBaseModel):
    flow_property: FlowdatasetFlowpropertiesFlowpropertyoption0 | list[FlowdatasetFlowpropertiesFlowpropertyoption1item] = Field(default=..., alias='flowProperty')
    common_other: str | None = Field(default=None, alias='common:other')

class FlowsFlowdataset(TidasBaseModel):
    xmlns: Literal['http://lca.jrc.it/ILCD/Flow'] = Field(default=..., alias='@xmlns')
    xmlns_common: Literal['http://lca.jrc.it/ILCD/Common'] = Field(default=..., alias='@xmlns:common')
    xmlns_ecn: Literal['http://eplca.jrc.ec.europa.eu/ILCD/Extensions/2018/ECNumber'] = Field(default=..., alias='@xmlns:ecn')
    xmlns_xsi: Literal['http://www.w3.org/2001/XMLSchema-instance'] = Field(default=..., alias='@xmlns:xsi')
    version: Literal['1.1'] = Field(default=..., alias='@version')
    locations: Literal['../ILCDLocations.xml'] = Field(default=..., alias='@locations')
    xsi_schema_location: Literal['http://lca.jrc.it/ILCD/Flow ../../schemas/ILCD_FlowDataSet.xsd'] = Field(default=..., alias='@xsi:schemaLocation')
    flow_information: FlowsFlowdatasetFlowinformation = Field(default=..., alias='flowInformation')
    modelling_and_validation: FlowsFlowdatasetModellingandvalidation = Field(default=..., alias='modellingAndValidation')
    administrative_information: FlowsFlowdatasetAdministrativeinformation = Field(default=..., alias='administrativeInformation')
    flow_properties: FlowsFlowdatasetFlowproperties = Field(default=..., alias='flowProperties')
    common_other: str | None = Field(default=None, alias='common:other')

class Flows(TidasBaseModel):
    flow_data_set: FlowsFlowdataset = Field(default=..., alias='flowDataSet')
