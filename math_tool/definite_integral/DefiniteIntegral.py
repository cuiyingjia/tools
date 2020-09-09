
from sympy import  integrate ,cos,sin
from sympy.abc import  a,x,y

result = integrate(sin(x)/x,(x,-float("inf"),float("inf")))
print(result)