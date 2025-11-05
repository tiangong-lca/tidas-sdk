#!/bin/bash
set -e

echo "准备发布TIDAS Python SDK..."

# 检查工作目录是否干净
if [ -n "$(git status --porcelain)" ]; then
    echo "错误：工作目录不干净，请先提交所有更改"
    exit 1
fi

# 获取当前版本
CURRENT_VERSION=$(grep -o 'version = "[^"]*"' pyproject.toml | cut -d'"' -f2)
echo "当前版本: $CURRENT_VERSION"

# 询问是否要更新版本
read -p "是否要更新版本号? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    read -p "输入新版本号 (当前: $CURRENT_VERSION): " NEW_VERSION
    if [ -z "$NEW_VERSION" ]; then
        echo "版本号不能为空，使用当前版本"
        NEW_VERSION=$CURRENT_VERSION
    fi
    
    # 更新版本号
    sed -i.bak "s/version = \"$CURRENT_VERSION\"/version = \"$NEW_VERSION\"/" pyproject.toml
    echo "版本号已更新为: $NEW_VERSION"
    
    # 提交版本更新
    git add pyproject.toml
    git commit -m "chore: bump version to $NEW_VERSION"
    echo "版本更新已提交"
else
    NEW_VERSION=$CURRENT_VERSION
fi

# 运行测试
echo "运行测试..."
uv run pytest

# 代码检查
echo "运行代码检查..."
uv run ruff check .
uv run mypy .

# 构建包
echo "构建包..."
uv run python -m build

# 显示将要发布的文件
echo "将要发布的文件:"
ls -la dist/

# 确认发布
read -p "确认发布到PyPI? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    # 询问是否先发布到测试PyPI
    read -p "是否先发布到测试PyPI? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "上传到测试PyPI..."
        uv run twine upload --repository testpypi dist/*
        echo "测试PyPI发布成功!"
        
        read -p "测试PyPI发布成功，是否继续发布到正式PyPI? (y/n) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "发布已取消"
            exit 0
        fi
    fi
    
    echo "上传到正式PyPI..."
    uv run twine upload dist/*
    
    # 创建Git标签
    git tag -a "v$NEW_VERSION" -m "Release version $NEW_VERSION"
    echo "已创建Git标签: v$NEW_VERSION"
    
    # 推送标签
    read -p "是否推送Git标签到远程仓库? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git push origin "v$NEW_VERSION"
        echo "Git标签已推送"
    fi
    
    echo "发布成功! 版本 $NEW_VERSION 已发布到PyPI"
else
    echo "发布已取消"
fi
