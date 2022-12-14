#list型: 色々なデータを順番に並べて管理する
#アクセス: listの後ろに[index]を使う
fruits = ["apple", "orange", "banana", "grape"]
#fruits[2] -> "banana"

"""-------------------------------------------------------------------------------------------"""
#listの要素には全てのオブジェクトを格納できる(種類が統一されている必要はない)
integers = [1, 2, 3, 4]
integers.append(5)
messed_list = ["aaa", "bbb", 111, True, None]
#str型，:,int,bool,Nonetype型


"""-------------------------------------------------------------------------------------------"""
#listの(標準装備してる)メソッド:
    #append(element): listの一番最後にelementを追加する。
    #上に使い方あるよ
    #index(element): listに含まれるelementが何番目かを返す。elementが存在しない場合はエラー(通常はin演算子と組み合わせる)
    #pop(index): list[index]をlistから消して、その要素(list[index])を返す，indeXは順番．
    #reverse(): listの並び順を逆にする
    #remove(element): listからelementを消す。list.pop(list.index(element))と同じ？
    #sort(): listを昇順、降順で並び変える
"""-------------------------------------------------------------------------------------------"""
#スライス
#listの一部分を切り出して新しいリストを作る
#l[start:stop:step](start:開始位置(含まれる), stop:終了位置(含まれない), step:増分) -> list
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
teens = numbers[12:19]
#teensはリスト型
print(teens)
#numbersは変わらない
c_numbers = numbers.copy()
temp = c_numbers[1:10]
temp = [2,2]

#numbersが置き換わる
c_numbers[1:10] = [2,2]

#スライシングを利用したlistの逆順
reversed_ns = numbers[::-1] #numbers[-1::-1]と等価
#要素の数え方，-1はリストの最後の要素，-2はリストの最後から2番目の要素
#https://qiita.com/k-nakamura/items/49c393227d68bd10562b


"""-------------------------------------------------------------------------------------------"""
#二次元配列、多次元配列
matrix = [
    [0,  0,  0,  0,  0,  0],
    [0,  1,  2,  3,  4,  5],
    [0,  2,  4,  6,  8, 10],
    [0,  3,  6,  9, 12, 15],
    [0,  4,  8, 12, 16, 20],
    [0,  5, 10, 15, 20, 25]
]
print(matrix[3][4])

for row in matrix:
    for i in row:
        print(i)

for row in range(len(matrix)):
    for column in range(len(matrix[0])):
        print(matrix[row][column])
#ネストしたforループ
"""-------------------------------------------------------------------------------------------"""
#内包表記: 要素が一般項で表せる配列を簡単に作ることができる
#[要素を表す式 for 繰り返し変数 in iterableなオブジェクト]

#例(二乗した数の配列を作りたい場合)：
#1. 愚直に空リストにappendする方法，6回行うから，この場合6個の数字出る
sqrt = []
for i in range(6):
    sqrt.append(i**2)

#2. 内包表記を利用する方法←使えるようになれ
sqrt = [i**2 for i in range(6)]

#メリット：
    #コードがすっきりする!
    #実行速度が通常のfor文よりも早い(インタプリタがappend()の参照、呼び出しを行わないため。(専用の追加命令をおこなっている))
#デメリット：
    #ネストすると可読性が下がる可能性がある(ネストは二重まで)

#if文とも組み合わせることができる
odds = [i for i in range(10) if i%2 == 1]

#ネストの例
matrix = [[i*j for i in range(6)] for j in range(6)]

not_triples = [i for i in range(30) if not i%3 == 0]
print(not_triples)