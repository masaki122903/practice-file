from . import gui, util
#. は必要，ディレクトリを参照するときの「自分自身のパッケージ」的なことを表す
# x = 1     package全体で使える変数となる
from .gui import App
#Appというguiで定義されたものを簡単に使えるようになる
#initpyでつくったものがパッケージのクラスaみたいな
