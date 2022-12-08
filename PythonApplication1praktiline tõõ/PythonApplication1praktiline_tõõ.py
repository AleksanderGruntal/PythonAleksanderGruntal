#10------------
from math import *
from random import *
print()



#9-------------
from math import *
from random import *
print("Rulluisutaja keskmine kiirus on 29,9 km/h.") 
a=29.9
b=24
pu=a/b 
print(f"vastus:/n{round(b,2)} km {b} min")
print()



#8--------------
from math import *
from random import *
a=randint(1,100)
b=randint(1,100)
c=randint(1,50)
print(f"Vastus:/nkülg a={a} /nkülg b={b} /nkülg c={c}")
r=(c/b)*100
print(f"kutsekulu, {round(r,2)}")
print()



#7--------------
from math import *
p=float(input("pitsa => "))
n=float(input("näpunäiteid =>"))
s=(p+n)/3



print(f"vastus:/nSuma", round(p,2))
#6--------------
from math import *
from random import *
a=randint (1,100)
b=randint (1,100)
c=randint (1,100)
print(f"külg a={a}/nKülg b={b}/ nkülg c={c}")
print(f"kolmnurga ümbermõõt = {a+b+c}")
print()



#5---------------
print("   @..@")
print("  (----)")
print(" ( \__/ )")
print("  ^^ "" ^^ ")
print()



#4----------------
from math import *
from re import I
print("keskmine")
a=float(input("1 number =>"))
b=float(input("2 number =>"))
v=float(input("3 number =>"))
h=float(input("4 number =>"))
d=float(input("5 number =>"))
m=(a+b+v+h+d)/5
print(f"keskmine on {m}")



#3-----------------
print("harjutus")
aeg = float(input("mitu tundi kulus sõidub ? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = aeg / teepikkus
print()
print("sinu kirus oli " + str(round(kiirus,2)) + " km/h")



#2-----------------
from math import *
print("Ristkülikukujulise maatküki diagonaal")
N=float(input("Sisesta ristküliku 1. külje pikkus => "))
M=float(input("Sisesta ristküliku 2. külje pikkus => "))
d=sqrt(N**2+M**2)
print(f"Maatüki diagonaal on {d} m**2")



#1-----------------
from math import *
print("Puu läbimõõdu arvutamine")
C=float(input("puu ümbermõõt: "))
r=C/(2*pi)
print()
print("Puu radius", round(r,2))
d=2*r
print("Puu diagonal", round(d,2))
print(f"Vastus:/nPuu läbimõõduga {C} ümbermõõt võrdub {d}")

