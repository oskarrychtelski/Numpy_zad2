import numpy as np
#zad,1
# a=np.array([10,9,8])
# b=np.array([1,2,3])
# print(a*b)

#zad.2
# x=np.arange(9).reshape(3,3)
# y=np.arange(16).reshape(4,4)
# print("min x kolumn: ",x.min(axis=0))
# print("min x wierszy: ",x.min(axis=1))
# print("min y kolumn: ",y.min(axis=0))
# print("min y wierszy: ",y.min(axis=1))

#zad.3
# print(np.dot(a,b))

#zad.4
# x=np.arange(1,2,0.4).reshape(1,3)
# y=np.arange(5,8).reshape(1,3)
# print(x*y)

#zad.5
# macierz1=np.arange(6).reshape(2,3)
# a=[np.sin(i) for i in macierz1]
# print(a)

#zad.6
# macierz2=np.arange(6).reshape(2,3)
# b=[np.cos(i) for i in macierz2]
# print(b)

#zad.7
# print(np.add(a,b))

#zad.8
# a=np.array([np.arange(3),np.arange(3),np.arange(3)])
# for x in a:
#     print(x)

#zad.9
# a=np.array([np.arange(3),np.arange(3),np.arange(3)]).flat
# for x in a:
#     print(x)

#zad.10
# a=np.array(9*[np.arange(9)]).reshape(3,27)
# for x in a:
#     print(x)
#
# licznik=0
# for x in range(1,82):
#     if 81%x==0:
#         licznik+=1
# licznik*=2
# print("Liczba możliwych macierzy to: ",licznik)
# Jest tak ponieważ macierz musi zawierać tyle samo elementów co poprzednia oraz jej wymiary muszą być liczbami naturalnymi, mniejszymi od 82. Każy z wymiarów musi więc być dzielnikiem 81.

#zad.11
# a=np.array([np.arange(12)]).reshape(3,4)
# b=np.array([np.arange(12)]).reshape(4,3)
# c=np.array([np.arange(12)]).reshape(2,6)
# print(a.flatten())
# print(b.flatten())
# print(c.flatten())