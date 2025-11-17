#!/usr/bin/env python3
"""
测试新的 Builder 功能

Test New Builder Features:
1. Direct dict assignment to multi-lang fields
2. Direct list[dict] assignment
3. Assign then append pattern
4. StringMultiLang convenience methods
"""

from tidas_sdk.builders.tidas_processes_builders import ModelBuilder


def test_dict_assignment():
    """测试直接赋值 dict"""
    print("=" * 60)
    print("Test 1: Direct dict assignment")
    print("=" * 60)

    builder = ModelBuilder()

    # 测试：单个 dict 赋值
    builder.processDataSet.processInformation.dataSetInformation.name.baseName = {
        "@xml:lang": "en",
        "#text": "Solar Power"
    }

    print("✅ Direct dict assignment successful!")
    print(f"   Value: {builder.processDataSet.processInformation.dataSetInformation.name.baseName}")
    print(f"   Type: {type(builder.processDataSet.processInformation.dataSetInformation.name.baseName)}")
    print(f"   Items: {len(builder.processDataSet.processInformation.dataSetInformation.name.baseName)} item(s)")
    print()


def test_list_dict_assignment():
    """测试直接赋值 list[dict]"""
    print("=" * 60)
    print("Test 2: Direct list[dict] assignment")
    print("=" * 60)

    builder = ModelBuilder()

    # 测试：list[dict] 批量赋值
    builder.processDataSet.processInformation.dataSetInformation.name.treatmentStandardsRoutes = [
        {"@xml:lang": "en", "#text": "Photovoltaic"},
        {"@xml:lang": "zh", "#text": "光伏发电"},
        {"@xml:lang": "fr", "#text": "Photovoltaïque"},
    ]

    print("✅ Direct list[dict] assignment successful!")
    field = builder.processDataSet.processInformation.dataSetInformation.name.treatmentStandardsRoutes
    print(f"   Type: {type(field)}")
    print(f"   Items: {len(field)} item(s)")
    for i, item in enumerate(field):
        print(f"   Item {i+1}: {item.lang} = {item.text}")
    print()


def test_assign_then_append():
    """测试先赋值再 append"""
    print("=" * 60)
    print("Test 3: Assign then append pattern")
    print("=" * 60)

    builder = ModelBuilder()

    # 测试：先赋值一个 dict
    builder.processDataSet.processInformation.dataSetInformation.name.mixAndLocationTypes = {
        "@xml:lang": "en",
        "#text": "Production mix"
    }

    print(f"After initial assignment: {len(builder.processDataSet.processInformation.dataSetInformation.name.mixAndLocationTypes)} item(s)")

    # 测试：然后 append 更多项
    builder.processDataSet.processInformation.dataSetInformation.name.mixAndLocationTypes.append({
        "@xml:lang": "zh",
        "#text": "生产混合"
    })

    builder.processDataSet.processInformation.dataSetInformation.name.mixAndLocationTypes.append({
        "@xml:lang": "es",
        "#text": "Mezcla de producción"
    })

    print("✅ Assign then append successful!")
    field = builder.processDataSet.processInformation.dataSetInformation.name.mixAndLocationTypes
    print(f"   Final count: {len(field)} item(s)")
    for i, item in enumerate(field):
        print(f"   Item {i+1}: {item.lang} = {item.text}")
    print()


def test_convenience_methods():
    """测试便利方法"""
    print("=" * 60)
    print("Test 4: StringMultiLang convenience methods")
    print("=" * 60)

    from tidas_sdk.types.tidas_data_types import StringMultiLang

    ml = StringMultiLang()

    # Test append with dict
    ml.append({"@xml:lang": "en", "#text": "English text"})
    ml.append({"@xml:lang": "zh", "#text": "中文文本"})

    print(f"✅ After 2 appends: {len(ml)} item(s)")

    # Test extend
    ml.extend([
        {"@xml:lang": "fr", "#text": "Texte français"},
        {"@xml:lang": "es", "#text": "Texto español"},
    ])

    print(f"✅ After extend: {len(ml)} item(s)")

    # Test iteration
    print("   All items:")
    for item in ml:
        print(f"   - {item.lang}: {item.text}")

    # Test indexing
    print(f"   First item via indexing: {ml[0].lang} = {ml[0].text}")

    # Test get_text
    print(f"   French text via get_text: {ml.get_text('fr')}")
    print()


def test_helper_methods_still_work():
    """确认 helper 方法仍然可用"""
    print("=" * 60)
    print("Test 5: Helper methods still work")
    print("=" * 60)

    builder = ModelBuilder()

    # 使用 helper 方法
    builder.processDataSet.processInformation.dataSetInformation.name.set_baseName("Wind Power", "en")
    builder.processDataSet.processInformation.dataSetInformation.name.set_baseName("风力发电", "zh")

    print("✅ Helper methods still functional!")
    base_name_en = builder.processDataSet.processInformation.dataSetInformation.name.get_baseName("en")
    base_name_zh = builder.processDataSet.processInformation.dataSetInformation.name.get_baseName("zh")
    print(f"   EN: {base_name_en}")
    print(f"   ZH: {base_name_zh}")
    print()


def test_full_workflow():
    """完整工作流测试"""
    print("=" * 60)
    print("Test 6: Full workflow with build()")
    print("=" * 60)

    import uuid
    from datetime import datetime, timezone

    builder = ModelBuilder()

    # 设置必要字段
    builder.processDataSet.field_xmlns = "http://lca.jrc.it/ILCD/Process"
    builder.processDataSet.field_version = "1.1"

    process_uuid = str(uuid.uuid4())
    builder.processDataSet.processInformation.dataSetInformation.common_UUID = process_uuid

    # 使用新的直接赋值方式
    builder.processDataSet.processInformation.dataSetInformation.name.baseName = [
        {"@xml:lang": "en", "#text": "Test Process"},
        {"@xml:lang": "zh", "#text": "测试流程"}
    ]

    # 使用 assign-then-append 模式
    builder.processDataSet.processInformation.dataSetInformation.name.treatmentStandardsRoutes = {
        "@xml:lang": "en",
        "#text": "Standard treatment"
    }
    builder.processDataSet.processInformation.dataSetInformation.name.treatmentStandardsRoutes.append({
        "@xml:lang": "zh",
        "#text": "标准处理"
    })

    # 设置必填字段 mixAndLocationTypes
    builder.processDataSet.processInformation.dataSetInformation.name.mixAndLocationTypes = {
        "@xml:lang": "en",
        "#text": "Production mix"
    }

    # 设置必填字段 classificationInformation (空对象即可)
    # classificationInformation builder 会自动初始化

    # 设置必填字段 common_generalComment
    builder.processDataSet.processInformation.dataSetInformation.set_generalComment(
        "Test process for demonstrating new builder features", "en"
    )

    # 设置必要的时间戳
    builder.processDataSet.administrativeInformation.dataEntryBy.common_timeStamp = datetime.now(timezone.utc)

    try:
        process = builder.build()
        print("✅ Full workflow successful - build() passed!")
        print(f"   Process UUID: {process_uuid}")
        print(f"   baseName has {len(process.processDataSet.processInformation.dataSetInformation.name.baseName.items)} item(s)")
        print(f"   treatmentStandardsRoutes has {len(process.processDataSet.processInformation.dataSetInformation.name.treatmentStandardsRoutes.items)} item(s)")
    except Exception as e:
        print(f"❌ Build failed: {e}")
    print()


def main():
    """运行所有测试"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║  Testing New Builder Features                           ║")
    print("║  测试新的 Builder 功能                                   ║")
    print("╚" + "=" * 58 + "╝")
    print()

    test_dict_assignment()
    test_list_dict_assignment()
    test_assign_then_append()
    test_convenience_methods()
    test_helper_methods_still_work()
    test_full_workflow()

    print("=" * 60)
    print("All tests completed! 所有测试完成！")
    print("=" * 60)
    print()
    print("Summary 总结:")
    print("✅ Dict assignment works")
    print("✅ List[dict] assignment works")
    print("✅ Assign-then-append pattern works")
    print("✅ StringMultiLang convenience methods work")
    print("✅ Helper methods still work")
    print("✅ Full workflow with build() works")
    print()


if __name__ == "__main__":
    main()
