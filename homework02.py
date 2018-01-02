# coding=utf-8
# Python 2 and 3 compatibility
# pip install future
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
# from builtins import *
from math import factorial, sqrt

__author__ = 'dobrogodin'

# This is homework for python ml class lesson 03

# Test
print('Test:')
print(2+3)

# 01 Даны два целых числа A и B (при этом A  ≤ B). Выведите все числа от A до B включительно.
print("Вывести числа от А до B:")
A, B = int(input("A: ")), int(input("B: "))
if B > A:
    for i in range(A, B+1):
        print(i)
else:
    print("A > B")

# 02 о данному натуральном n вычислите сумму  1**2 + 2**2 + 3**2 +
print("n: 1**2 + 2**2 + ... + n**2:")
n = int(input("n: "))
res = 0
for i in range(1, n+1):
    res += i**2
print(res)

# 03 По данному целому неотрицательному n вычислите значение n!.
print("n!:")
n = int(input("n: "))
res = 1
for i in range(n):
    res *= (i+1)
print(res)

# 04 По данным целым неотрицательным n и k вычислите значение числа сочетаний из n элементов по k
print('число сочитаний из n по k:')
n, k = [int(i) for i in input().split(',')]

def my_factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

print(my_factorial(n) / my_factorial(k) / my_factorial(n-k))

# 05 Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n пингвинов.
# Изображение одного пингвина имеет размер 5×9 символов, между двумя соседними пингвинами
# также имеется пустой (из пробелов) столбец. Разрешается вывести пустой столбец после последнего
# пингвина. Для упрощения рисования скопируйте пингвина из примера в среду разработки.
penguine = ["   _~_    ",
            "  (o o)   ",
            " /  V  \ ",
            "/(  _  )\ ",
            "  ^^ ^^   "]

n = int(input("Число пингвинов: "))
for i in range(len(penguine)):
    print(penguine[i] * n)

# 06 Шоколадка имеет вид прямоугольника, разделенного на n×m долек.
# Шоколадку можно один раз разломить по прямой на две части.
# Определите, можно ли таким образом отломить от шоколадки ровно k долек
print("деление шоколадки:")
print("размер шоколадки")
n, m = [int(i) for i in input().split(',')]
k = int(input("колчество долек k:"))
print("YES" if (k < n*m) and ((k % m == 0) or (k % n == 0)) else "NO")

# 07 Дано линейное уравнение  ax+b=0
# Решите уравнение, напечатайте ответ. Если ответов бесконечно много, выведите "INF", если их нет - "NO".
print("линейной уравнение:")
print("коэффициенты a, b:")
a, b = [int(i) for i in input().split(',')]
if (a == 0) and (b == 0):
    print("INF")
elif (a != 0) and (b % a == 0):
    print(-b/a)
else:
    print("NO")

# 08 Для данного числа n < 100 закончите фразу “На лугу пасется...”
# одним из возможных продолжений: “n коров”, “n корова”, “n коровы”, правильно склоняя слово “корова”
print("склонения сущ с числитиельными:")
n = int(input("n: "))
r = n % 10
if n > 100:
    print("Много коров")
elif r == 1 and (n not in range(11, 15)):
    print(n, "корова")
elif n not in range(11, 15) and r in (2, 3, 4):
    print(n, "коровы")
else:
    print(n, "коров")

# 09 Даны числа a, b, c, d. Выведите в порядке возрастания все целые числа от 0 до 1000,
# которые являются корнями уравнения  ax3+bx2+cx+d=0
print("корни кубического ур-я с коэф а б ц д:")
a, b, c, d = [int(i) for i in input().split(',')]
for i in range(1001):
    if a*i**3 + b*i**2 + c*i + d == 0:
        print(i)

# 10 Квадрат трехзначного числа оканчивается тремя цифрами, равными этому числу. Найдите и выведите все такие числа.
print("квадрат трехзначного оканчивается тремя цифрами:")
for i in range(100,1000):
    if i**2 % 1000 == i:
        print(i)


# 11 По данному натуральному  n≤9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.
print("ступеньки:")
n = int(input("n:"))
for i in range(n+1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

# 12 Дано три числа. Упорядочите их в порядке неубывания.
# Программа должна считывать три числа a, b, c, затем программа должна менять их значения так, чтобы стали
# выполнены условия  a≤b≤c затем программа выводит тройку a, b, c.
print("неубывание чисел a,b,c:")
a,b,c = [int(i) for i in input().split(',')]

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a, b, c, sep = ' ')

# 13 Давным-давно билет на одну поездку в метро стоил 15 рублей, билет на 10 поездок стоил 125 рублей,
# билет на 60 поездок стоил 440 рублей. Пассажир планирует совершить n поездок. Определите, сколько
# билетов каждого вида он должен приобрести, чтобы суммарное количество оплаченных поездок было не меньше n,
# а общая стоимость приобретенных билетов — минимальна.
print("число билетов и минимальная стоимость:")
n = int(input("n:"))

# стоимости проездных
C1, C2, C3 = 15, 125, 440
N1, N2, N3 = 1, 10, 60

def cost(n1, n2, n3):
    return C1 * n1 + C2 * n2 + C3 * n3

def rides(n1, n2, n3):
    return N1 * n1 + N2 * n2 + N3 * n3

# init for optimal numbers of tickets
opt_n = (0, 0, 0)

# initialize min_cost to some large number
min_cost = pow(10, 20)

for n1 in range(N3 + 1):
    for n2 in range(int(N3 / N2) + 1):
        for n3 in range(n // N3 + 2):
            if ((rides(n1, n2, n3) >= n) & (cost(n1, n2, n3) < min_cost)) :
                min_cost = cost(n1, n2, n3)
                opt_n = (n1, n2, n3)

print(opt_n[0], opt_n[1], opt_n[2], sep=' ')

# дрцго  вариант
print("билеты но другой варинат решения:")
from scipy.optimize import linprog

n = int(input())

C1, C2, C3 = 15, 125, 440
N1, N2, N3 = 1, 10, 60


c = [C1, C2, C3]
A = [[-N1,- N2, -N3]]
b = [-n]
n1_bounds, n2_bounds, n3_bounds = (0, None), (0, None), (0, None)
res = linprog(c, A_ub=A, b_ub=b, bounds=(n1_bounds, n2_bounds, n3_bounds),
              options={"disp": True})
print(res)

n1, n2, n3 = res.x
print(n1, n2, n3, sep=' ')

#14 по данному натуральном n вычислите сумму 1! + 2! + 3! + ... +n!.
# В решении этой задачи можно использовать только один цикл.
n = int(input())

def sum_factorials(n):
    """
    :param n - integer
    Calculates sum of factorials 1! + ... + n!
    Example: 1! + 2! + 3! + 4! = 33
    1! + 2! + 3! + 4! + 5! + 6! = 873
    """
    run_sum, total_sum = 1, 0
    for i in range(n):
        run_sum *= (i + 1)
        total_sum += run_sum
    return total_sum

print(sum_factorials(n))