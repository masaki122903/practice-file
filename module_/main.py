#モジュール(中身)とパッケージ（例，ジャンゴ　中身ありきのでっかいもの中身が高い）
#ライブラリは関数群，クラス群が集まったファイル
#モジュール：ファイル
#パッケージ：フォルダ(モジュール群)
#パッケージをimportするときは__init__.pyを使うことができる
#カプセル化と似てる

import module as m #as節で任意のモジュール名に，mathはmodule, moduleていう名前のmodule,packageを作ってある（使ってる
import math
a = math.cos(math.pi)  #使い方注意
print(a)

from math import pi
b = pi
print(b)
#packageからguiだけをimport
#パッケージの一部のみ（一個のモジュール）をimportするやり方
from package import gui
""""""
#from math import pi
#b = pi
#print(b)   piだけimportするとこんな感じ
""""""
#moduleのadd関数を呼び出し
x = m.add(3, 9)
app = gui.App()


"""-------------------------------------------------------------------------------------------"""
#__init__.py（というモジュール）がpackageには必要，packageというフォルダを動かしやすくみたいな， __init__.pyは参照される
