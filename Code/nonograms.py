from itertools import combinations

def generate_sequences(n, blocks, certain_zeros, certain_ones):
    positions = list(range(n))
    valid_sequences = []

    for start_positions in combinations(positions, len(blocks)):
        sequence = [0] * n
        current_position = 0
        valid = True

        for i, start in enumerate(start_positions):
            block = blocks[i]
            if start + block > n or (i > 0 and start_positions[i] <= start_positions[i - 1] + blocks[i - 1]):
                valid = False
                break

            for j in range(start, start + block):
                sequence[j] = 1

        for index in certain_zeros:
            if sequence[index] == 1:
                valid = False
                break

        for index in certain_ones:
            if sequence[index] == 0:
                valid = False
                break

        if valid:
            valid_sequences.append(sequence)

    return valid_sequences

def find_certain_ones_and_zeros(n, blocks, certain_zeros, certain_ones):
    all_sequences = generate_sequences(n, blocks, certain_zeros, certain_ones)

    if not all_sequences:
        return "不符合"

    certain_ones_result = [1] * n
    certain_zeros_result = [1] * n
    for sequence in all_sequences:
        for i in range(n):
            if sequence[i] == 0:
                certain_ones_result[i] = 0
            else:
                certain_zeros_result[i] = 0

    result_ones = [i + 1 for i, val in enumerate(certain_ones_result) if val == 1]
    result_zeros = [i + 1 for i, val in enumerate(certain_zeros_result) if val == 1]
    return result_ones if result_ones else "不符合", result_zeros if result_zeros else "不符合"

while True:
    # 获取用户输入
    n = int(input("请输入数列的长度: "))
    certain_zeros = list(map(lambda x: int(x) - 1, input("请输入肯定为0的位置（用空格分隔）: ").split()))
    certain_ones = list(map(lambda x: int(x) - 1, input("请输入肯定为1的位置（用空格分隔）: ").split()))
    blocks = list(map(int, input("请输入相邻1的长度（用空格分隔）: ").split()))

    # 获取结果
    result_ones, result_zeros = find_certain_ones_and_zeros(n, blocks, certain_zeros, certain_ones)

    if result_ones == "不符合":
        print(result_ones)
    else:
        result_ones_divmod = [(x, divmod(x, 5)) for x in result_ones]
        print("肯定为1的项的索引及其除以5的整倍数和余数:")
        for original, (quotient, remainder) in result_ones_divmod:
            print(f"索引: {original}, 第 {quotient + 1} 个格子, 第 {remainder} 个")

    if result_zeros == "不符合":
        print(result_zeros)
    else:
        result_zeros_divmod = [(x, divmod(x, 5)) for x in result_zeros]
        print("肯定为0的项的索引及其除以5的整倍数和余数:")
        for original, (quotient, remainder) in result_zeros_divmod:
            print(f"索引: {original}, 第 {quotient + 1} 个格子, 第 {remainder} 个")

    # 询问用户是否要重新运行
    # again = input("是否要重新运行程序？(是/否): ")
    # if again.lower() != 'y':
    #     break
