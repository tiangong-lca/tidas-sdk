#!/usr/bin/env python3
"""
测试 Builder 修复

Test Builder Fixes:
1. 列表字段支持直接赋值（setter）
2. add_*() 方法正确实例化 union 类型
3. build_dump() 方法显示完整 builder 状态
"""

from tidas_sdk.builders.tidas_processes_builders import ModelBuilder
import uuid
from datetime import datetime, timezone


def test_list_field_setter():
    """测试列表字段 setter"""
    print("=" * 60)
    print("测试 1: 列表字段直接赋值 (common_class setter)")
    print("Test 1: List field direct assignment (common_class setter)")
    print("=" * 60)

    builder = ModelBuilder()

    # 测试：直接赋值列表字段
    try:
        builder.processDataSet.processInformation.dataSetInformation.classificationInformation.common_classification.common_class = [
            {"@level": "1", "@classId": "36", "#text": "Electricity"}
        ]
        print("✅ 列表字段 setter 工作正常！可以直接赋值")
        print(f"   设置的值: {builder.processDataSet.processInformation.dataSetInformation.classificationInformation.common_classification.common_class}")
    except AttributeError as e:
        print(f"❌ 列表字段 setter 失败: {e}")
        return False

    print()
    return True


def test_union_type_instantiation():
    """测试 union 类型实例化"""
    print("=" * 60)
    print("测试 2: add_*() 方法 union 类型实例化")
    print("Test 2: add_*() method union type instantiation")
    print("=" * 60)

    builder = ModelBuilder()

    # 测试：调用 add_common_cla() 方法
    try:
        item = builder.processDataSet.processInformation.dataSetInformation.classificationInformation.common_classification.add_common_cla()
        print("✅ add_common_cla() 方法工作正常！没有语法错误")
        print(f"   返回的对象类型: {type(item).__name__}")
    except (SyntaxError, TypeError, NameError) as e:
        print(f"❌ add_common_cla() 方法失败: {e}")
        return False

    print()
    return True


def test_build_dump():
    """测试 build_dump() 方法"""
    print("=" * 60)
    print("测试 3: build_dump() 显示完整 builder 状态")
    print("Test 3: build_dump() shows full builder state")
    print("=" * 60)

    builder = ModelBuilder()

    # 设置一些字段
    process_uuid = str(uuid.uuid4())
    builder.processDataSet.processInformation.dataSetInformation.common_UUID = process_uuid
    builder.processDataSet.processInformation.dataSetInformation.name.set_baseName(
        "Test Process", "en"
    )
    builder.processDataSet.processInformation.dataSetInformation.name.set_baseName(
        "测试流程", "zh"
    )

    # 测试：调用 build_dump()
    try:
        dump_output = builder.build_dump(indent=2)
        print("✅ build_dump() 方法工作正常！")
        print(f"\n前 300 个字符的输出:")
        print(dump_output[:300] + "...")

        # 验证输出包含我们设置的数据
        if process_uuid in dump_output and "Test Process" in dump_output:
            print("\n✅ 输出包含设置的数据（UUID 和 name）")
        else:
            print("\n❌ 输出不包含预期的数据")
            return False

    except Exception as e:
        print(f"❌ build_dump() 方法失败: {e}")
        return False

    print()
    return True


def test_model_dump_vs_build_dump():
    """对比 model_dump() 和 build_dump()"""
    print("=" * 60)
    print("测试 4: 对比 model_dump() 和 build_dump()")
    print("Test 4: Compare model_dump() vs build_dump()")
    print("=" * 60)

    builder = ModelBuilder()

    # 设置一些嵌套数据
    builder.processDataSet.processInformation.dataSetInformation.common_UUID = str(uuid.uuid4())
    builder.processDataSet.processInformation.dataSetInformation.name.set_baseName(
        "Solar Power", "en"
    )

    # model_dump_json() - 应该是空或很少数据
    model_dump_output = builder.model_dump_json(indent=2, by_alias=True)
    print(f"model_dump_json() 输出长度: {len(model_dump_output)} 字符")
    print(f"输出内容: {model_dump_output[:200]}...")

    # build_dump() - 应该包含完整数据
    build_dump_output = builder.build_dump(indent=2)
    print(f"\nbuild_dump() 输出长度: {len(build_dump_output)} 字符")
    print(f"输出内容: {build_dump_output[:200]}...")

    if len(build_dump_output) > len(model_dump_output):
        print("\n✅ build_dump() 输出更多数据（包含嵌套 builder 状态）")
        print(f"   build_dump 比 model_dump 多 {len(build_dump_output) - len(model_dump_output)} 字符")
    else:
        print("\n❌ build_dump() 输出不如预期")
        return False

    print()
    return True


def main():
    """运行所有测试"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║  测试 Builder 修复                                      ║")
    print("║  Testing Builder Fixes                                  ║")
    print("╚" + "=" * 58 + "╝")
    print()

    results = []
    results.append(("列表字段 setter", test_list_field_setter()))
    results.append(("Union 类型实例化", test_union_type_instantiation()))
    results.append(("build_dump() 方法", test_build_dump()))
    results.append(("model_dump vs build_dump", test_model_dump_vs_build_dump()))

    # 总结
    print("=" * 60)
    print("测试结果总结 (Test Results Summary)")
    print("=" * 60)
    for name, passed in results:
        status = "✅ 通过" if passed else "❌ 失败"
        print(f"{name}: {status}")

    all_passed = all(passed for _, passed in results)
    print()
    if all_passed:
        print("🎉 所有测试通过！All tests passed!")
    else:
        print("⚠️  部分测试失败 Some tests failed")
    print()

    return all_passed


if __name__ == "__main__":
    import sys
    success = main()
    sys.exit(0 if success else 1)
