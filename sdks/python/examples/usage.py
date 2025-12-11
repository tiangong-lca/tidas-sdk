from pathlib import Path

from tidas_sdk import (
    TidasProcess,
    create_flow_from_json,
    create_process,
    create_process_from_json,
)


def creat_object_from_json():
    """
    特征1:
    从JSON数据创建对象.
    使用的JSON数据须符合对应的JSON Schema定义, 但是由于数据结构过于复杂, 允许传入不完整的JSON数据进行对象的初始化.
    """
    sample_path = Path(__file__).resolve().parents[3] / "test-data" / "tidas-example-process.json"
    process: TidasProcess = create_process_from_json(sample_path)

    print("✓ Created Process entity from JSON data")


def convert_object_to_json():
    """
    特征2:
    将对象转换为JSON数据.
    对象内部维护一个符合ILCD JSON格式的嵌套字典结构, 可以通过to_json()方法导出为JSON数据.
    """

    process: TidasProcess = create_process({})

    process.process_data_set.process_information.data_set_information.name.base_name.set_text("Updated Process Name", lang="en")
    json_data = process.to_json()
    print("✓ Converted Process entity to JSON data")
    print(json_data)

    pass


def properties_access():
    """
    特征3:
    通过属性访问对象的数据.
    对象的每个字段都可以通过属性进行访问和修改, 提供了更直观的操作方式.
    对于多语言字段, 也提供set_text(text: str, lang: str)和get_text(lang: str)方法进行操作.
    """
    sample_path = Path(__file__).resolve().parents[3] / "test-data" / "tidas-example-process.json"
    process: TidasProcess = create_process_from_json(sample_path)
    name_list = process.process_data_set.process_information.data_set_information.name.base_name
    name_list.set_text("Updated Process Name", lang="en")
    name_list.set_text("中文名称", lang="zh")
    print("✓ Updated localized names:", name_list.to_plain_list())


def type_hinting_and_autocompletion():
    """
    特征4:
    支持类型提示和自动补全.
    由于对象的属性和方法都有明确的类型定义, 因此在使用IDE时可以获得类型提示和自动补全功能, 提高开发效率.
    """

    pass


def validation_on_demand():
    """
    特征5:
    支持按需验证.
    对象可以在创建时跳过验证, 提供validate()可在对象数据完整后进行验证, 以确保数据符合JSON Schema定义.
    """

    sample_path = Path(__file__).resolve().parents[3] / "test-data" / "tidas-example-process.json"
    process: TidasProcess = create_process_from_json(sample_path)  # 创建时跳过验证
    # 在对象数据完整后进行验证
    is_valid = process.validate()
    if is_valid:
        print("✓ Process entity is valid")
    else:
        print("✗ Process entity is invalid")
        error = process.last_validation_error()
        if error:
            first_issue = error.errors()[0]
            print("  首个校验错误:", first_issue["loc"], "-", first_issue["msg"])

    pass


def convert_to_xml():
    """
    特征6:
    支持转换为XML格式.
    对象可以通过to_xml()方法将数据转换为符合ILCD XML格式的表示, 方便与其他系统进行数据交换.
    """
    sample_path = Path(__file__).resolve().parents[3] / "test-data" / "tidas-example-process.json"
    process: TidasProcess = create_process_from_json(sample_path)
    xml_data = process.to_xml()
    print(f"XML Data:{xml_data}")
    print("✓ Converted Process entity to XML format")

    pass


def create_object_from_xml():
    """
    特征7:
    直接从 ILCD XML 字符串创建对象.
    """
    process_xml = """<?xml version="1.0" encoding="UTF-8"?>
<processDataSet xmlns="http://lca.jrc.it/ILCD/Process"
                xmlns:common="http://lca.jrc.it/ILCD/Common"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                version="1.1"
                locations="../ILCDLocations.xml"
                xsi:schemaLocation="http://lca.jrc.it/ILCD/Process ../../schemas/ILCD_ProcessDataSet.xsd">
  <processInformation>
    <dataSetInformation>
      <common:UUID>123e4567-e89b-12d3-a456-426614174000</common:UUID>
      <name>
        <baseName xml:lang="en">XML Sample Process</baseName>
      </name>
    </dataSetInformation>
    <quantitativeReference type="Reference flow(s)">
      <referenceToReferenceFlow>1</referenceToReferenceFlow>
    </quantitativeReference>
  </processInformation>
  <administrativeInformation>
    <dataEntryBy>
      <common:timeStamp>2024-01-01T00:00:00Z</common:timeStamp>
    </dataEntryBy>
    <publicationAndOwnership/>
  </administrativeInformation>
</processDataSet>
"""
    process: TidasProcess = TidasProcess.from_xml(process_xml)
    print("✓ Created Process entity from XML data")
    print(process.to_json())

    pass


def convert_to_markdown():
    """
    特征6.1:
    使用示例 JSON 生成实体, 并导出为 Markdown 摘要.
    """
    base = Path(__file__).resolve().parents[3] / "test-data"

    # Process 示例
    process = create_process_from_json(base / "tidas-example-process.json")
    process_md = process.to_markdown(lang="en")
    print("✓ Process markdown preview:")
    print(process_md.split("\n")[0])

    # Flow 示例
    flow = create_flow_from_json(base / "tidas-example-flow.json")
    flow_md = flow.to_markdown(lang="en")
    print("✓ Flow markdown preview:")
    print(flow_md.split("\n")[0])

if __name__ == "__main__":
    creat_object_from_json()
    convert_object_to_json()
    properties_access()
    type_hinting_and_autocompletion()
    validation_on_demand()
    convert_to_xml()
    create_object_from_xml()
    convert_to_markdown()
