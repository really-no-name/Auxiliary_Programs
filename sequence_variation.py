#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: Auxiliary_Programs sequence_variation.py
作者: Bolun Xu
创建日期: 2025/9/27
版本: 1.0
描述: 宝洁在线测评题型1——水管翻转题

    定义规则：默认输入序列为 A B C D, 输入变化序列 1342后，新序列为 A C D B

    程序实现以下功能：默认输入序列为 A B C D；键盘输入新序列，以及3个变化序列；从3个变化序列中有顺序的挑选两个，使得默认输入序列变为新序列；输出有序的两个变化序列
"""


def apply_transformation(sequence, transformation):
    """
    应用变换序列到原序列上
    sequence: 原序列，如 ['A', 'B', 'C', 'D']
    transformation: 变换序列，如 '1342'
    返回: 新序列
    """
    # 将数字字符串转换为索引列表（注意：从1开始所以要减1）
    indices = [int(x) - 1 for x in transformation]

    # 根据索引重新排列序列
    new_sequence = [sequence[i] for i in indices]
    return new_sequence


def find_transformation_combination(default_seq, target_seq, transformations):
    """
    从3个变换序列中找到有序的两个变换序列组合
    default_seq: 默认序列
    target_seq: 目标序列
    transformations: 3个变换序列的列表
    """
    results = []

    # 尝试所有有序的组合（顺序重要）
    for i in range(len(transformations)):
        for j in range(len(transformations)):
            if i == j:  # 可以使用同一个变换序列两次
                continue

            # 应用第一个变换
            intermediate_seq = apply_transformation(default_seq, transformations[i])

            # 应用第二个变换
            final_seq = apply_transformation(intermediate_seq, transformations[j])

            # 检查是否等于目标序列
            if final_seq == target_seq:
                results.append((transformations[i], transformations[j]))

    return results


def main():
    # 默认序列
    default_sequence = ['A', 'B', 'C', 'D']
    print(f"默认序列: {default_sequence}")

    # 获取目标序列
    target_input = input("请输入新序列（用空格分隔，如 A C D B）: ")
    target_sequence = target_input.split()

    # 获取3个变换序列
    transformations = []
    for i in range(3):
        trans = input(f"请输入第{i + 1}个变化序列（如1342）: ")
        transformations.append(trans)

    print(f"\n默认序列: {default_sequence}")
    print(f"目标序列: {target_sequence}")
    print(f"可用的变换序列: {transformations}")
    print("\n正在寻找解决方案...")

    # 寻找解决方案
    solutions = find_transformation_combination(default_sequence, target_sequence, transformations)

    if solutions:
        print(f"\n找到 {len(solutions)} 个解决方案:")
        for idx, (trans1, trans2) in enumerate(solutions, 1):
            # 显示详细的变换过程
            intermediate = apply_transformation(default_sequence, trans1)
            final = apply_transformation(intermediate, trans2)

            print(f"\n解决方案 {idx}:")
            print(f"  第一步: 应用变换 {trans1}")
            print(f"     {default_sequence} → {intermediate}")
            print(f"  第二步: 应用变换 {trans2}")
            print(f"     {intermediate} → {final}")
            print(f"  组合: {trans1} + {trans2}")
    else:
        print("\n未找到解决方案，请检查输入是否正确。")

        # 显示调试信息
        print("\n调试信息:")
        print("每个变换序列单独应用的效果:")
        for i, trans in enumerate(transformations):
            result = apply_transformation(default_sequence, trans)
            print(f"  变换 {trans}: {default_sequence} → {result}")


# 测试示例
def test_example():
    """测试题目中的例子"""
    print("=== 测试示例 ===")
    default_sequence = ['A', 'B', 'C', 'D']
    target_sequence = ['A', 'C', 'D', 'B']
    transformations = ['1342']  # 示例中只给了一个，这里我们假设有多个

    print(f"默认序列: {default_sequence}")
    print(f"目标序列: {target_sequence}")

    # 测试单个变换
    result = apply_transformation(default_sequence, '1342')
    print(f"应用变换 '1342': {default_sequence} → {result}")


if __name__ == "__main__":
    # 运行测试示例
    test_example()
    print("\n" + "=" * 50 + "\n")

    # 运行主程序
    main()