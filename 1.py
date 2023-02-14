import numpy as np
import pandas as pd
from math import factorial


def combinations(n, k):
    return (factorial(n)/(factorial(k)*factorial(n-k)))

# 1


salaries = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17,
                     30, 24, 57, 55, 70, 75, 65, 84, 90, 150])

am = salaries.sum()/salaries.size
#amean = salaries.mean()


saq = (salaries-am)**2

std = (saq.sum()/salaries.size)**.5
#stdd = (saq.sum()/(salaries.size-1))**.5

std_ = salaries.std()
#stdd_ = salaries.std(ddof=1)


var = saq.sum()/salaries.size
#var_ = salaries.var()


vard = saq.sum()/(salaries.size-1)
#vard_ = salaries.var(ddof=1)

print("Задание 1: Среднее арифметическое: ", am)
print("СКО: ", std)
print("Дисперсия смещенная оценка: ", var)
print("Дисперсия несмещенная оценка: ", vard)

# 2

t1 = combinations(8, 2)
t2 = combinations(12, 4)

# a)
a1 = combinations(5, 2)
a2 = combinations(5, 1)
b2 = combinations(7, 3)
p1 = a1/t1
p2 = (a2*b2)/t2
pa = p1*p2
#print(f"2 из 2 белые и 1 из 4 белый: {pa: .2f}")

# b)
a1 = combinations(5, 1)
b1 = combinations(3, 1)
a2 = combinations(5, 2)
b2 = combinations(7, 2)
p1 = (a1*b1)/t1
p2 = (a2*b2)/t2
pb = p1*p2
#print(f"1 из 2х белый и 2 из 4 белые: {pb: .2f}")

# c)
a1 = combinations(3, 2)
a2 = combinations(5, 3)
b2 = combinations(7, 1)
p1 = a1/t1
p2 = (a2*b2)/t2
pc = p1*p2
#print(f"0 из 2х белые и 3 из 4 белые: {pc: .2f}")

p = pa+pb+pc
print(f"Задание 2: вероятность того, что 3 мяча белые: {p: .2f}")

# 3
shoot1 = 0.9
shoot2 = 0.8
shoot3 = 0.6
q1 = 1-shoot1
q2 = 1-shoot2
q3 = 1-shoot3

# a)
p = shoot1*q2*q3
print("Задание 3: а) первым спортсменом:", p)
# b)
p = q1*shoot2*q3
print("б) вторым спортсменом:", p)
# c)
p = q1*q2*shoot3
print("в) третьим спортсменом:", p)

# 4

# вероятность случайного студента из факультета A
qa = 0.25
# вероятность случайного студента из факультета B
qb = 0.25
# вероятность случайного студента из факультета C
qc = 0.5

pa = 0.8
pb = 0.7
pc = 0.9

# доля сдавших студентов от общего количества поступивших
pt = qa*pa+qb*pb+qc*pc
print("Задание 4: доля сдавщих студентов от общего количества поступивших:", pt)

p = qa*pa/pt
print("a) из факультета A:", p)

p = qb*pb/pt
print("б) из факультета B:", p)

p = qc*pc/pt
print("в) из факультета C:", p)

# 5

d1 = 0.1
d2 = 0.2
d3 = 0.25
q1 = 1-d1
q2 = 1-d2
q3 = 1-d3

# a
p = d1*d2*d3
print("Задание 5: а) Вероятность выхода из строя всех деталей", p)

# b
p12 = d1*d2*d3
p13 = d1*d2*d3
p23 = d1*d2*d3
pt2 = p12+p13+p23
print("б) Вероятность выхода из строя 2х деталей", pt2)

# c
# ищем вероятность что не выйдет ни одна деталь
pn = q1*q2*q3
p = 1-pn
print("в) Вероятность выхода хотя бы одной детали", p)

# d
p1 = d1*q2*q3
p2 = q1*d2*q3
p3 = q1*q2*d3
p = p1+p2+p3+pt2
print("г) Вероятность выхода из строя 1-2х деталей", p)
