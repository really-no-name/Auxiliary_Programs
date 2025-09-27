#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: Auxiliary_Programs puzzle_words.py
作者: Bolun Xu
创建日期: 2025/5/23
版本: 1.0
描述: 。
时间复杂度：
空间复杂度：
"""
import json
import requests
from collections import defaultdict
from itertools import product
import multiprocessing as mp
from functools import partial


class TrieNode:
    __slots__ = ['children', 'is_word']  # 优化内存使用

    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Dictionary:
    def __init__(self):
        self.trie = TrieNode()
        self.min_length = 3  # 默认最小单词长度
        self.loaded = False

    def load_from_file(self, file_path):
        try:
            with open(file_path, 'r') as f:
                words = json.load(f).keys()
                for word in words:
                    if len(word) >= self.min_length:
                        self._insert_word(word.lower())
            self.loaded = True
            print(f"已加载本地词典，包含{len(words)}个单词")
        except Exception as e:
            print(f"加载词典失败: {e}")

    def _insert_word(self, word):
        node = self.trie
        for char in word:
            node = node.children[char]
        node.is_word = True

    def has_prefix(self, prefix):
        node = self.trie
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def is_word(self, word):
        node = self.trie
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word


def check_word_online(word):
    """使用Free Dictionary API检查单词是否存在"""
    try:
        response = requests.get(
            f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}",
            timeout=3
        )
        return response.status_code == 200
    except requests.RequestException:
        return False


def get_adjacent_positions(matrix, position, visited):
    """获取所有有效相邻位置，优化版"""
    rows, cols = len(matrix), len(matrix[0])
    x, y = position
    adjacent = []

    # 预计算边界
    min_x, max_x = max(0, x - 1), min(rows - 1, x + 1)
    min_y, max_y = max(0, y - 1), min(cols - 1, y + 1)

    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            if (i, j) != position and (i, j) not in visited:
                adjacent.append((i, j))
    return adjacent


def dfs_search(matrix, dictionary, position, visited, current_word, results, online_check=False):
    """深度优先搜索优化版"""
    x, y = position
    cell = matrix[x][y].lower()

    # 处理qu组合
    if cell == 'u' and len(current_word) > 0 and current_word[-1] == 'q':
        new_word = current_word + cell
        if len(new_word) >= dictionary.min_length and dictionary.is_word(new_word):
            results.add(new_word)
        return  # qu组合后不能继续延伸

    new_word = current_word + cell

    # 检查是否值得继续搜索
    if len(new_word) >= dictionary.min_length:
        if dictionary.is_word(new_word):
            results.add(new_word)

    if not dictionary.has_prefix(new_word):
        return

    # 获取相邻位置
    neighbors = get_adjacent_positions(matrix, position, visited)

    for neighbor in neighbors:
        nx, ny = neighbor
        # 跳过会导致qu拆分的u
        if matrix[nx][ny].lower() == 'u' and len(new_word) > 0 and new_word[-1] == 'q':
            continue

        dfs_search(
            matrix, dictionary,
            (nx, ny),
            visited | {neighbor},
            new_word,
            results,
            online_check
        )


def parallel_search(matrix, dictionary, start_positions, online_check=False):
    """并行搜索实现"""
    with mp.Manager() as manager:
        shared_results = manager.list()  # 使用list代替set

        with mp.Pool(mp.cpu_count()) as pool:
            search_func = partial(
                _parallel_search_task,
                matrix=matrix,
                dictionary=dictionary,
                results=shared_results,
                online_check=online_check
            )
            pool.map(search_func, start_positions)

        # 转换为普通set去重
        return set(shared_results)


def _parallel_search_task(position, matrix, dictionary, results, online_check):
    """并行搜索任务"""
    local_results = set()
    dfs_search(
        matrix, dictionary,
        position, {position},
        "", local_results,
        online_check
    )
    results.extend(local_results)  # 使用extend添加到list


def parse_matrix_input(input_str):
    """安全解析矩阵输入"""
    try:
        matrix = json.loads(input_str.replace("'", '"'))
        if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
            raise ValueError("输入格式不正确")

        row_lengths = {len(row) for row in matrix}
        if len(row_lengths) != 1:
            raise ValueError("矩阵每行长度必须相同")

        for row in matrix:
            for elem in row:
                if not isinstance(elem, str) or not elem.isalpha():
                    raise ValueError("矩阵元素必须为字母")

        return matrix
    except Exception as e:
        print(f"输入错误: {e}")
        return None


def main():
    print("优化版英语单词矩阵拼图游戏")
    print("输入格式示例: [['u','p','qu'],['m','a','e'],['l','i','d']]")
    print("注意: 'qu'被视为一个不可拆分的字母组合\n")

    # 初始化词典
    dictionary = Dictionary()
    dictionary.load_from_file("words_dictionary.json")  # 替换为你的词典路径

    # 获取矩阵输入
    while True:
        input_str = input("请输入字母矩阵: ").strip()
        matrix = parse_matrix_input(input_str)
        if matrix is not None:
            break

    # 设置最小长度
    min_len = int(input("设置最小单词长度(默认3): ") or 3)
    dictionary.min_length = min_len

    # 选择搜索模式
    use_parallel = input("启用并行搜索(y/n, 默认y)? ").lower() != 'n'
    online_check = input("启用在线验证(y/n, 默认n)? ").lower() == 'y'

    print("\n开始搜索...")

    # 准备搜索
    rows, cols = len(matrix), len(matrix[0])
    start_positions = [(i, j) for i in range(rows) for j in range(cols)]

    # 过滤掉会导致qu拆分的u
    start_positions = [
        pos for pos in start_positions
        if not (matrix[pos[0]][pos[1]].lower() == 'u' and
                any(matrix[nx][ny].lower() == 'q'
                    for nx, ny in get_adjacent_positions(matrix, pos, set())))
    ]

    found_words = set()

    if use_parallel and len(matrix) >= 3:  # 小矩阵并行开销大
        found_words = parallel_search(matrix, dictionary, start_positions, online_check)
    else:
        for position in start_positions:
            dfs_search(matrix, dictionary, position, {position}, "", found_words, online_check)

    # 输出结果
    print(f"\n找到{len(found_words)}个有效单词(长度>={min_len}):")
    for word in sorted(found_words, key=lambda x: (len(x), x)):
        print(word, end=' ')

    print("\n\n按长度分组统计:")
    length_groups = defaultdict(list)
    for word in found_words:
        length_groups[len(word)].append(word)

    for length in sorted(length_groups.keys()):
        print(f"{length}字母单词({len(length_groups[length])}个): {', '.join(sorted(length_groups[length]))}")


if __name__ == "__main__":
    mp.freeze_support()  # 对于Windows系统可能需要
    main()