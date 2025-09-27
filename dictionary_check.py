#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: Auxiliary_Programs dictionary_check.py
作者: Bolun Xu
创建日期: 2025/5/24
版本: 1.0
描述: 。
时间复杂度：
空间复杂度：
"""
import json
import os
from pathlib import Path


def load_dictionary(file_path):
    """加载词典JSON文件"""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"词典文件 {file_path} 不存在，将创建新文件")
        return {}
    except json.JSONDecodeError:
        print("词典文件格式错误，将创建新词典")
        return {}


def save_dictionary(dictionary, file_path):
    """保存词典到JSON文件"""
    with open(file_path, 'w') as f:
        json.dump(dictionary, f, indent=2)
    print(f"词典已保存到 {file_path}")


def check_and_add_word():
    # 设置词典文件路径
    dict_file = "words_dictionary.json"

    # 加载词典
    dictionary = load_dictionary(dict_file)

    while True:
        print("\n" + "=" * 40)
        word = input("请输入要查询的单词(输入q退出): ").strip().lower()

        if word == 'q':
            break

        if not word.isalpha():
            print("请输入有效的英语单词(只包含字母)")
            continue

        # 检查单词是否存在
        if word in dictionary:
            print(f"单词 '{word}' 已存在于词典中")
        else:
            print(f"单词 '{word}' 不在词典中")
            add = input("是否要将此单词添加到词典中?(y/n): ").lower()

            if add == 'y':
                # 添加单词到词典(值设为1，保持与其他单词一致)
                dictionary[word] = 1
                save_dictionary(dictionary, dict_file)
                print(f"单词 '{word}' 已添加到词典")
            else:
                print("未添加该单词")

    print("程序结束")


if __name__ == "__main__":
    print("英语词典查询与更新工具")
    print("=" * 40)
    print(f"将使用/创建词典文件: words_dictionary.json")
    check_and_add_word()