#!/usr/bin/env python3
"""
示例：使用Builder模式创建TIDAS Contact实体

本示例展示如何使用自动生成的Builder类来逐步构建一个完整的Contact数据集。
Builder模式特别适合处理像TIDAS Contact这样具有深层嵌套结构和众多必填字段的复杂实体。

Example: Using Builder Pattern to Create a TIDAS Contact Entity

This example demonstrates how to use auto-generated Builder classes to incrementally
construct a complete Contact dataset. The Builder pattern is especially useful for
handling complex entities like TIDAS Contact with deep nesting and many required fields.
"""

import uuid
from datetime import datetime, timezone

from tidas_sdk.builders.tidas_contacts_builders import (
    ModelBuilder as ContactBuilder,  # Root builder for Contact entity
)


def create_simple_contact():
    """
    创建一个简单的contact示例 (Simple contact example)

    演示Builder的基本用法：
    - 设置必填字段
    - 使用多语言helper方法
    - 增量构建复杂嵌套结构
    """
    print("=" * 60)
    print("示例 1: 创建简单的Contact")
    print("Example 1: Create Simple Contact")
    print("=" * 60)

    # 1. 创建builder实例
    builder = ContactBuilder()

    # 2. 设置基本信息 (Set basic information)
    contact_uuid = str(uuid.uuid4())
    contact_info = builder.contactDataSet.contactInformation.dataSetInformation

    # 使用UUID
    contact_info.common_UUID = contact_uuid

    # 使用多语言helper方法设置名称
    contact_info.set_name("Dr. Jane Smith", "en")
    contact_info.set_name("简·史密斯博士", "zh")

    contact_info.set_shortName("J. Smith", "en")
    contact_info.set_shortName("简·史", "zh")

    # 设置联系方式
    contact_info.email = "jane.smith@example.com"
    contact_info.telephone = "+1-555-0100"
    contact_info.WWWAddress = "https://example.com/jane"

    # 3. 设置行政信息 (Set administrative information)
    data_entry = builder.contactDataSet.administrativeInformation.dataEntryBy
    data_entry.common_timeStamp = datetime.now(timezone.utc)

    # 4. 构建最终的Contact模型
    try:
        contact = builder.build()
        print("\n✅ Contact创建成功! (Contact created successfully!)")
        print(f"   UUID: {contact_uuid}")
        print(f"   Name (EN): {contact_info.get_name('en')}")
        print(f"   Name (ZH): {contact_info.get_name('zh')}")
        print(f"   Email: {contact_info.email}")
        print(f"   Telephone: {contact_info.telephone}")

        return contact

    except Exception as e:
        print(f"\n❌ 创建失败 (Creation failed): {e}")
        import traceback
        traceback.print_exc()
        return None


def incremental_construction_example():
    """
    增量构建示例 (Incremental construction example)

    演示如何分多个步骤构建Contact：
    1. 先创建基本信息
    2. 然后添加联系细节
    3. 最后添加行政信息
    4. 在所有数据准备好后再build()
    """
    print("\n" + "=" * 60)
    print("示例 2: 增量构建Contact")
    print("Example 2: Incremental Contact Construction")
    print("=" * 60)

    builder = ContactBuilder()

    # 步骤1: 设置基本标识信息
    print("\n第1步: 设置基本标识信息 (Step 1: Set basic identification)")
    contact_uuid = str(uuid.uuid4())

    contact_info = builder.contactDataSet.contactInformation.dataSetInformation
    contact_info.common_UUID = contact_uuid
    contact_info.set_name("Incremental Contact", "en")
    contact_info.set_shortName("IC", "en")
    print("   ✓ 基本信息设置完成")

    # 步骤2: 添加多语言支持
    print("\n第2步: 添加多语言支持 (Step 2: Add multilingual support)")
    contact_info.set_name("增量构建联系人", "zh")
    contact_info.set_name("Contact Incrémental", "fr")
    contact_info.set_name("Contacto Incremental", "es")

    contact_info.set_shortName("增量", "zh")
    contact_info.set_shortName("CI", "fr")
    contact_info.set_shortName("CI", "es")
    print("   ✓ 已添加4种语言支持")

    # 步骤3: 添加联系方式
    print("\n第3步: 添加联系方式 (Step 3: Add contact details)")
    contact_info.email = "incremental@example.com"
    contact_info.telephone = "+1-555-0200"
    contact_info.WWWAddress = "https://example.com/incremental"
    print("   ✓ 联系方式已添加")

    # 步骤4: 添加行政信息
    print("\n第4步: 添加行政信息 (Step 4: Add administrative information)")
    builder.contactDataSet.administrativeInformation.dataEntryBy.common_timeStamp = (
        datetime.now(timezone.utc)
    )
    print("   ✓ 行政信息已添加")

    # 步骤5: 构建最终模型
    print("\n第5步: 构建最终模型 (Step 5: Build final model)")
    try:
        contact = builder.build()
        print(
            "\n✅ 增量构建成功完成! (Incremental construction completed successfully!)"
        )
        print(f"   UUID: {contact_uuid}")
        print(f"   支持语言数: 4 (English, 中文, Français, Español)")
        print(f"   Email: {contact_info.email}")

        # 验证多语言
        print("\n   多语言名称验证:")
        for lang in ["en", "zh", "fr", "es"]:
            name = contact_info.get_name(lang)
            short_name = contact_info.get_shortName(lang)
            print(f"   - {lang}: {name} ({short_name})")

        return contact

    except Exception as e:
        print(f"\n❌ 构建失败 (Build failed): {e}")
        import traceback
        traceback.print_exc()
        return None


def export_contact_example(contact):
    """
    导出Contact为JSON (Export contact to JSON)

    演示如何将构建好的Contact导出为JSON格式
    """
    if not contact:
        print("\n⚠️  没有可用的contact进行导出")
        return

    print("\n" + "=" * 60)
    print("示例 3: 导出Contact为JSON")
    print("Example 3: Export Contact to JSON")
    print("=" * 60)

    try:
        # 导出为JSON字符串
        json_output = contact.model_dump_json(
            indent=2, by_alias=True, exclude_none=True
        )

        # 显示前500个字符
        print("\nJSON输出预览 (前500字符):")
        print("-" * 60)
        print(json_output[:500] + "...")
        print("-" * 60)

        # 保存到文件
        output_file = "/tmp/tidas_contact_example.json"
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
    print("║  TIDAS SDK Builder Pattern - Contact Creation Examples  ║")
    print("║  TIDAS SDK Builder模式 - Contact创建示例                ║")
    print("╚" + "=" * 58 + "╝")

    # 示例1: 创建简单contact
    contact1 = create_simple_contact()

    # 示例2: 增量构建
    contact2 = incremental_construction_example()

    # 示例3: 导出JSON
    export_contact_example(contact2)

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
