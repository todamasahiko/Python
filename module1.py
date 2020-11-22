# coding: utf-8
import math
print('円周率は{}です。'.format(math.pi))
print('小数点以下切り捨てをしたら{}です。'.format(math.floor(math.pi)))
print('小数点以下切り上げをしたら{}です。'.format(math.ceil(math.pi)))

from math import *
print('円周率は{}です。'.format(pi))
print('小数点以下切り捨てをしたら{}です。'.format(floor(pi)))
print('小数点以下切り上げをしたら{}です。'.format(ceil(pi)))

⭐︎import モジュール名　　　　　　　#import文
                             # 　　モジュールの取り込み
モジュール名.変数名             #モジュール内変数の参照
モジュール名.関数名(引数, ・・・)　　#モジュール内関数の呼び出し

import math　　　　　　　　　　　　　　　　　　--mathモジュールの取り込み
print('円周率は{}です。'.format(math.pi))　　--変数piの参照　
print('小数点以下切り捨てをしたら{}です。'.format(math.floor(math.pi)))　--floor関数の呼び出し
print('小数点以下切り上げをしたら{}です。'.format(math.ceil(math.pi)))   --ceil関数の呼び出し

*pi、floor、ceilはmathモジュールが提供する変数や関数



import math as m　　　　　　　　　　　　　　　　　　--mathモジュールを「m」として取り込む
print('円周率は{}です。'.format(m.pi))　　
print('小数点以下切り捨てをしたら{}です。'.format(m.floor(m.pi)))　
print('小数点以下切り上げをしたら{}です。'.format(m.ceil(m.pi)))



from math import pi                --mathモジュールから変数piを取り込む
from math import floor　　　　　　　　--mathモジュールからfloor関数を取り込む　　　
print('円周率は{}です。'.format(pi))　　
print('小数点以下切り捨てをしたら{}です。'.format(floor(pi)))

----
from モジュール名　import 変数名もしくは関数名 as 別名

from math import pi as ensyuritsu              
from math import floor as kirisute　　　　　　　　　　
print('円周率は{}です。'.format(ensyuritsu))　　
print('小数点以下切り捨てをしたら{}です。'.format(kirisute(ensyuritsu)))

from math import *　　
print('円周率は{}です。'.format(pi))　　
print('小数点以下切り捨てをしたら{}です。'.format(floor(pi)))
print('小数点以下切り上げをしたら{}です。'.format(ceil(pi)))

--matplotlibパッケージ--
import matplotlib.pyplot as plt　--matplotlibパッケージのpuplotモジュールをpltとして取り込む
weight = [45.0, 48.2, 54.5, 57.6, 64.5, 69.2]
plt.plot(weight)　--取り込んだpltのplot関数を呼び出す

--requestsパッケージ--
import requests
response = requests.get('https://python.org/downloads/')
text = response.text
print(text)