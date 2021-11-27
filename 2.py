def countMoves(numbers):
    array = numbers
    length = len(numbers)

    # 配列の動きをシミュレーションする
    while True:
        array = numbers
        for i in range (100):
            array = numbers
            count = 0

            for j in range(length):
                # j -> 増加させないインデックス番号
                same_number_count = 0 # 配列の全要素が等しいか判定するための変数を初期化
                for k in range(length):
                    # k -> 配列arrayの[j]以外の要素を1ずつ増加させるためのループ
                    if j == k:
                        continue
                    array[k] += 1
                
                count += 1

                # 以下で配列の要素がすべて等しいか判定
                for index in range(1, length):
                    if array[0] == array[index]:
                        same_number_count += 1

                # すべて等しかったらシミュレーション終了
                if same_number_count == length:
                    break
            else:
                continue
            break
        else:
            continue
        break

    return count