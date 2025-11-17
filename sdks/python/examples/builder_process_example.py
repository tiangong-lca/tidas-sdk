#!/usr/bin/env python3
"""
示例：使用Builder模式创建TIDAS Process实体

本示例展示如何使用自动生成的Builder类来逐步构建一个完整的Process数据集。
Builder模式特别适合处理像TIDAS Process这样具有深层嵌套结构和众多必填字段的复杂实体。

Example: Using Builder Pattern to Create a TIDAS Process Entity

This example demonstrates how to use auto-generated Builder classes to incrementally
construct a complete Process dataset. The Builder pattern is especially useful for
handling complex entities like TIDAS Process with deep nesting and many required fields.
"""

import uuid
from datetime import datetime, timezone

from tidas_sdk.builders.tidas_processes_builders import (
    ModelBuilder,
)
from tidas_sdk.types.tidas_data_types import (
    StringMultiLang,
    MultiLangItemString,
    FTMultiLang,
    MultiLangItemST,
)


def create_simple_process():
    """
    创建一个简单的process示例 (Simple process example)

    演示Builder的基本用法：
    - 设置必填字段
    - 使用多语言helper方法
    - 增量构建复杂嵌套结构
    """
    print("=" * 60)
    print("示例 1: 创建简单的Process")
    print("Example 1: Create Simple Process")
    print("=" * 60)

    # 1. 创建builder实例
    builder = ModelBuilder()

    # 2. 设置命名空间属性 (Set namespace attributes)
    builder.processDataSet.field_xmlns = "http://lca.jrc.it/ILCD/Process"
    builder.processDataSet.field_xmlns_common = "http://lca.jrc.it/ILCD/Common"
    builder.processDataSet.field_xmlns_xsi = "http://www.w3.org/2001/XMLSchema-instance"
    builder.processDataSet.field_xsi_schemaLocation = (
        "http://lca.jrc.it/ILCD/Process ../../schemas/ILCD_ProcessDataSet.xsd"
    )
    builder.processDataSet.field_version = "1.1"
    builder.processDataSet.field_locations = "../ILCDLocations.xml"

    # 3. 设置基本信息 (Set basic information)
    process_uuid = str(uuid.uuid4())
    # 使用UUID
    builder.processDataSet.processInformation.dataSetInformation.common_UUID = (
        process_uuid
    )

    builder.processDataSet.processInformation.dataSetInformation.name.set_baseName(
        "Electricity production, photovoltaic", "en"
    )
    builder.processDataSet.processInformation.dataSetInformation.name.set_baseName(
        "光伏发电", "zh"
    )

    # 注意：builder 在构建过程中，嵌套数据存储在私有字段中
    # model_dump_json() 不会显示嵌套 builder 状态（输出为空或不完整）
    # 使用 build_dump() 可以查看完整的 builder 状态（用于调试）
    print("\n=== Builder 状态（调试用）===")
    print(builder.build_dump(indent=2))
    print("\n注意：以上是 builder 的调试输出，与最终模型结构不同")

    # 使用新的直接赋值功能
    builder.processDataSet.processInformation.dataSetInformation.name.treatmentStandardsRoutes = [
        {"@xml:lang": "en", "#text": "Photovoltaic"},
        {"@xml:lang": "zh", "#text": "光伏发电"},
    ]

    # 使用 assign-then-append 模式
    builder.processDataSet.processInformation.dataSetInformation.name.mixAndLocationTypes = {
        "@xml:lang": "en",
        "#text": "Production mix",
    }
    builder.processDataSet.processInformation.dataSetInformation.name.mixAndLocationTypes.append(
        {"@xml:lang": "zh", "#text": "生产混合"}
    )

    # 设置functionalUnitFlowProperties - 使用 helper 方法
    builder.processDataSet.processInformation.dataSetInformation.name.set_functionalUnitFlowProperties(
        "3kWp", "en"
    )
    builder.processDataSet.processInformation.dataSetInformation.name.set_functionalUnitFlowProperties(
        "3kWp", "zh"
    )

    # 设置classificationInformation（必填字段，需要提供分类数据）
    # 使用直接赋值设置 common_class
    builder.processDataSet.processInformation.dataSetInformation.classificationInformation.common_classification.common_class = [
        {
            "@level": "1",
            "@classId": "36",
            "#text": "Electricity",
        }
    ]

    # 设置generalComment - 使用 helper 方法
    builder.processDataSet.processInformation.dataSetInformation.set_generalComment(
        "Example process for photovoltaic electricity production", "en"
    )
    builder.processDataSet.processInformation.dataSetInformation.set_generalComment(
        "光伏发电示例流程", "zh"
    )

    # 4. 设置定量参考信息 (Set quantitative reference)

    builder.processDataSet.processInformation.quantitativeReference.field_type = (
        "Reference flow(s)"
    )
    builder.processDataSet.processInformation.quantitativeReference.referenceToReferenceFlow = (
        "1"
    )
    # 使用 helper 方法设置 functionalUnitOrOther
    builder.processDataSet.processInformation.quantitativeReference.set_functionalUnitOrOther(
        "1 kWh of electricity", "en"
    )
    builder.processDataSet.processInformation.quantitativeReference.set_functionalUnitOrOther(
        "1千瓦时电力", "zh"
    )

    # 5. 设置时间信息 (Set time information)
    builder.processDataSet.processInformation.time.common_referenceYear = 2024
    builder.processDataSet.processInformation.time.common_dataSetValidUntil = 2030

    # 6. 设置地理信息 (Set geography information)
    builder.processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction.field_location = (
        "GLO"
    )
    # 使用 helper 方法设置 descriptionOfRestrictions
    builder.processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction.set_descriptionOfRestrictions(
        "Global average data for photovoltaic electricity production", "en"
    )
    builder.processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction.set_descriptionOfRestrictions(
        "光伏发电的全球平均数据", "zh"
    )

    # 7. 设置行政信息 (Set administrative information)
    # 设置commissioner和goal
    builder.processDataSet.administrativeInformation.common_commissionerAndGoal.common_referenceToCommissioner.field_type = (
        "contact data set"
    )
    builder.processDataSet.administrativeInformation.common_commissionerAndGoal.common_referenceToCommissioner.uri = (
        "../contacts/00000000-0000-0000-0000-000000000000"
    )
    # shortDescription 是 GlobalReferenceType 的字段，使用直接赋值
    builder.processDataSet.administrativeInformation.common_commissionerAndGoal.common_referenceToCommissioner.shortDescription = [
        {"@xml:lang": "en", "#text": "Example organization"}
    ]

    # 使用 helper 方法设置 common_intendedApplications
    builder.processDataSet.administrativeInformation.common_commissionerAndGoal.set_intendedApplications(
        "Life cycle assessment", "en"
    )
    builder.processDataSet.administrativeInformation.common_commissionerAndGoal.set_intendedApplications(
        "生命周期评价", "zh"
    )

    # 设置data entry信息
    builder.processDataSet.administrativeInformation.dataEntryBy.common_timeStamp = (
        datetime.now(timezone.utc)
    )

    # 使用builder模式设置referenceToDataSetFormat
    builder.processDataSet.administrativeInformation.dataEntryBy.common_referenceToDataSetFormat.field_type = (
        "source data set"
    )
    builder.processDataSet.administrativeInformation.dataEntryBy.common_referenceToDataSetFormat.uri = (
        "../ILCD_Format/ILCD_1.1_Format"
    )
    # shortDescription 使用直接赋值
    builder.processDataSet.administrativeInformation.dataEntryBy.common_referenceToDataSetFormat.shortDescription = [
        {"@xml:lang": "en", "#text": "ILCD format 1.1"}
    ]

    # 使用builder模式设置referenceToConvertedOriginalDataSetFrom
    builder.processDataSet.administrativeInformation.dataEntryBy.common_referenceToConvertedOriginalDataSetFrom.field_type = (
        "source data set"
    )
    builder.processDataSet.administrativeInformation.dataEntryBy.common_referenceToConvertedOriginalDataSetFrom.uri = (
        "../sources/00000000-0000-0000-0000-000000000000"
    )
    # shortDescription 使用直接赋值
    builder.processDataSet.administrativeInformation.dataEntryBy.common_referenceToConvertedOriginalDataSetFrom.shortDescription = [
        {"@xml:lang": "en", "#text": "Original data source"}
    ]

    # 8. 构建最终的Process模型
    try:
        process = builder.build()
        print("\n✅ Process创建成功! (Process created successfully!)")
        print(f"   UUID: {process_uuid}")
        print(
            f"   Name (EN): {process.processDataSet.processInformation.dataSetInformation.name.baseName.get_text('en')}"
        )
        print(
            f"   Name (ZH): {process.processDataSet.processInformation.dataSetInformation.name.baseName.get_text('zh')}"
        )
        print(f"   Reference Year: 2024")

        return process

    except Exception as e:
        print(f"\n❌ 创建失败 (Creation failed): {e}")
        return None


def create_process_with_exchanges():
    """
    创建包含交换数据的Process (Create process with exchanges)

    演示如何添加输入输出交换：
    - 输入流（原材料、能源）
    - 输出流（产品、排放）
    - 设置交换的量和单位
    """
    print("\n" + "=" * 60)
    print("示例 2: 创建包含交换数据的Process")
    print("Example 2: Create Process with Exchanges")
    print("=" * 60)

    # 创建builder
    builder = ModelBuilder()

    # 设置基本信息 (类似示例1)
    process_uuid = str(uuid.uuid4())
    builder.processDataSet.field_xmlns = "http://lca.jrc.it/ILCD/Process"
    builder.processDataSet.field_version = "1.1"

    process_info = builder.processDataSet.processInformation.dataSetInformation
    process_info.common_UUID = process_uuid
    process_info.name.set_baseName("Steel production from iron ore", "en")
    process_info.name.set_baseName("铁矿石炼钢", "zh")

    # 设置时间信息
    builder.processDataSet.processInformation.time.referenceYear = 2024

    # 设置行政信息
    builder.processDataSet.administrativeInformation.dataEntryBy.common_timeStamp = (
        datetime.now(timezone.utc)
    )

    # TODO: 添加交换数据
    # 注意：当前生成的builder对于复杂的数组类型（如exchanges）可能需要进一步优化
    # 这里展示概念性的用法
    """
    # 添加输入交换 - 铁矿石
    input_exchange = builder.processDataSet.exchanges.add_exchange()
    input_exchange.dataSetInternalID = 1
    input_exchange.meanAmount = 1600.0  # kg iron ore per ton of steel
    input_exchange.set_generalComment("Iron ore input", "en")

    # 添加输出交换 - 钢材
    output_exchange = builder.processDataSet.exchanges.add_exchange()
    output_exchange.dataSetInternalID = 2
    output_exchange.meanAmount = 1000.0  # kg steel
    output_exchange.set_generalComment("Steel output", "en")

    # 添加排放交换 - CO2
    emission_exchange = builder.processDataSet.exchanges.add_exchange()
    emission_exchange.dataSetInternalID = 3
    emission_exchange.meanAmount = 1850.0  # kg CO2 per ton of steel
    emission_exchange.set_generalComment("CO2 emissions", "en")
    """

    print("\n⚠️  注意：Exchange添加功能需要进一步的builder增强")
    print("   Note: Exchange addition needs further builder enhancements")
    print(f"   Process UUID: {process_uuid}")
    print(f"   基本信息已设置完成 (Basic information set)")

    try:
        process = builder.build()
        print("\n✅ Process骨架创建成功! (Process skeleton created successfully!)")
        return process
    except Exception as e:
        print(f"\n❌ 创建失败 (Creation failed): {e}")
        return None


def incremental_construction_example():
    """
    增量构建示例 (Incremental construction example)

    演示如何分多个步骤构建Process：
    1. 先创建基本信息
    2. 然后添加技术细节
    3. 最后添加行政信息
    4. 在所有数据准备好后再build()
    """
    print("\n" + "=" * 60)
    print("示例 3: 增量构建Process")
    print("Example 3: Incremental Process Construction")
    print("=" * 60)

    builder = ModelBuilder()

    # 步骤1: 设置基本标识信息
    print("\n第1步: 设置基本标识信息 (Step 1: Set basic identification)")
    process_uuid = str(uuid.uuid4())
    builder.processDataSet.field_xmlns = "http://lca.jrc.it/ILCD/Process"
    builder.processDataSet.field_version = "1.1"

    process_info = builder.processDataSet.processInformation.dataSetInformation
    process_info.common_UUID = process_uuid
    process_info.name.set_baseName("Incremental Process", "en")
    print("   ✓ 基本信息设置完成")

    # 步骤2: 添加多语言支持
    print("\n第2步: 添加多语言支持 (Step 2: Add multilingual support)")
    process_info.name.set_baseName("增量构建流程", "zh")
    process_info.name.set_baseName("Processus Incrémental", "fr")
    process_info.name.set_baseName("Proceso Incremental", "es")
    print("   ✓ 已添加4种语言支持")

    # 步骤3: 设置时间信息
    print("\n第3步: 设置时间信息 (Step 3: Set time information)")
    builder.processDataSet.processInformation.time.referenceYear = 2024
    builder.processDataSet.processInformation.time.dataSetValidUntil = 2030
    print("   ✓ 时间信息已设置")

    # 步骤4: 添加行政信息
    print("\n第4步: 添加行政信息 (Step 4: Add administrative information)")
    builder.processDataSet.administrativeInformation.dataEntryBy.common_timeStamp = (
        datetime.now(timezone.utc)
    )
    print("   ✓ 行政信息已添加")

    # 步骤5: 构建最终模型
    print("\n第5步: 构建最终模型 (Step 5: Build final model)")
    try:
        process = builder.build()
        print(
            "\n✅ 增量构建成功完成! (Incremental construction completed successfully!)"
        )
        print(f"   UUID: {process_uuid}")
        print(f"   支持语言数: 4 (English, 中文, Français, Español)")
        print(f"   参考年份: 2024")
        print(f"   有效期至: 2030")

        # 验证多语言
        print("\n   多语言名称验证:")
        for lang in ["en", "zh", "fr", "es"]:
            name = process_info.name.get_baseName(lang)
            print(f"   - {lang}: {name}")

        return process

    except Exception as e:
        print(f"\n❌ 构建失败 (Build failed): {e}")
        return None


def export_process_example(process):
    """
    导出Process为JSON (Export process to JSON)

    演示如何将构建好的Process导出为JSON格式
    """
    if not process:
        print("\n⚠️  没有可用的process进行导出")
        return

    print("\n" + "=" * 60)
    print("示例 4: 导出Process为JSON")
    print("Example 4: Export Process to JSON")
    print("=" * 60)

    try:
        # 导出为JSON字符串
        json_output = process.model_dump_json(
            indent=2, by_alias=True, exclude_none=True
        )

        # 显示前500个字符
        print("\nJSON输出预览 (前500字符):")
        print("-" * 60)
        print(json_output[:500] + "...")
        print("-" * 60)

        # 保存到文件
        output_file = "/tmp/tidas_process_example.json"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(json_output)

        print(f"\n✅ JSON已保存到: {output_file}")
        print(f"   文件大小: {len(json_output)} 字节")

    except Exception as e:
        print(f"\n❌ 导出失败 (Export failed): {e}")


def main():
    """主函数 - 运行所有示例 (Main function - run all examples)"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║  TIDAS SDK Builder Pattern - Process Creation Examples  ║")
    print("║  TIDAS SDK Builder模式 - Process创建示例                ║")
    print("╚" + "=" * 58 + "╝")

    # 示例1: 创建简单process
    process1 = create_simple_process()

    # 示例2: 创建包含交换的process
    # process2 = create_process_with_exchanges()

    # 示例3: 增量构建
    # process3 = incremental_construction_example()

    # 示例4: 导出JSON
    export_process_example(process1)

    # 总结
    print("\n" + "=" * 60)
    print("示例运行完成! (Examples completed!)")
    print("=" * 60)
    print("\n主要学习点 (Key takeaways):")
    print("1. ✅ Builder允许增量设置字段 (Incremental field setting)")
    print("2. ✅ 嵌套builder自动初始化 (Nested builders auto-initialize)")
    print("3. ✅ 多语言helper方法简化操作 (Multilingual helpers)")
    print("4. ✅ 验证在build()时进行 (Validation at build time)")
    print("5. ✅ 构建结果是标准Pydantic模型 (Result is standard Pydantic model)")

    print("\n更多文档:")
    print("- Builder Pattern Guide: sdks/python/docs/builder-pattern-guide.md")
    print("- Test Examples: sdks/python/tests/unit/test_builders.py")
    print("- README: sdks/python/README.md")


if __name__ == "__main__":
    main()
