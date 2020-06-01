from sympy import *

init_printing()

var("x, y")
# 定義函數
fn = cos(x*y) + sin(y)



for v1 in [x , y] :
    for v2 in [x , y] :        
        for v3 in [x, y] :
            for v4 in [x, y] :
                
                if v1+v2+v3+v4 != 2*x+2*y: # 並不是剛好微各2次
                    continue;
                    
                dfn = Derivative(fn, v1, v2, v3, v4) # 微分, 共4次     
                pprint( dfn ) # 漂亮列印 fn 的微分式子
        
                print("\n")
                print( "= " , dfn.doit() ) 
                print("\n\n")