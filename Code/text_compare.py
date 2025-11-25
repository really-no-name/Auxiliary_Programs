#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: Auxiliary_Programs text_compare.py
作者: Bolun Xu
创建日期: 2025/11/25
版本: 1.0
描述: 。
时间复杂度：
空间复杂度：
"""
import re


def read_and_clean_file(filename):
    """读取文件并清理内容（移除空格、换行等）"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            # 移除非文字字符（空格、换行、标点等），只保留文字
            cleaned_content = re.sub(r'[^\w\u4e00-\u9fff]', '', content)
            return cleaned_content
    except FileNotFoundError:
        print(f"错误：找不到文件 '{filename}'")
        return None
    except Exception as e:
        print(f"读取文件 '{filename}' 时出错：{e}")
        return None


def compare_files(file1, file2):
    """比较两个文件的内容"""
    print(f"正在比较文件：'{file1}' 和 '{file2}'")
    print("-" * 50)

    # 读取并清理文件内容
    content1 = read_and_clean_file(file1)
    content2 = read_and_clean_file(file2)

    if content1 is None or content2 is None:
        return

    # 显示清理后的内容长度
    print(f"文件1清理后长度：{len(content1)} 字符")
    print(f"文件2清理后长度：{len(content2)} 字符")
    print()

    # 比较内容
    if content1 == content2:
        print("✅ 结果：两个文件的内容相同")
        return True
    else:
        print("❌ 结果：两个文件的内容不同")

        # 找出差异位置
        min_len = min(len(content1), len(content2))
        differences = []

        for i in range(min_len):
            if content1[i] != content2[i]:
                differences.append(i)
                if len(differences) >= 10:  # 最多显示10个差异
                    break

        if differences:
            print(f"\n前{len(differences)}个差异位置：")
            for pos in differences:
                print(f"  位置 {pos}: 文件1='{content1[pos]}' vs 文件2='{content2[pos]}'")

        # 如果长度不同也提示
        if len(content1) != len(content2):
            print(f"\n⚠️  文件长度不同：文件1有{len(content1)}字符，文件2有{len(content2)}字符")

        return False


def main():
    """主函数"""
    print("文本文件比较工具")
    print("=" * 30)

    # 获取用户输入
    file1 = 'compare_1.txt'
    file2 = 'compare_2.txt'

    print()
    compare_files(file1, file2)


# 如果需要直接测试，可以取消注释下面的代码
if __name__ == "__main__":
    main()