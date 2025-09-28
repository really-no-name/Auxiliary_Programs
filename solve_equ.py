#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: Auxiliary_Programs solve_equ.py
作者: Bolun Xu
创建日期: 2025/9/27
版本: 1.0
描述: 宝洁在线测评题型2——数字运算题
    X表示数字1-9的9个数，例如输入为（X*X*X）-X=498,请输出4个 X依次是7，8，9，6
    注意：只会涉及四则运算及括号
"""
from itertools import permutations


def solve_simple():
    """简洁版本，只输出结果"""
    print("请输入等式（如：(X*X*X)-X=502）:")
    user_input = input().strip()

    if '=' not in user_input:
        print("输入格式错误")
        return

    equation_part, result_part = user_input.split('=', 1)
    equation_pattern = equation_part.strip()

    try:
        target_result = int(result_part.strip())
    except:
        print("结果必须是整数")
        return

    x_count = equation_pattern.count('X')

    for nums in permutations(range(1, 10), x_count):
        equation = equation_pattern
        for num in nums:
            equation = equation.replace('X', str(num), 1)

        try:
            if eval(equation) == target_result:
                print('；'.join(map(str, nums)))
                return
        except:
            continue

    print("未找到解")


if __name__ == "__main__":
    solve_simple()