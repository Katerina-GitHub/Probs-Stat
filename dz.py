import numpy as np
import scipy.stats as stats
# 1
# 80- среднее значение выборки, объем -256, с надежностью 0.95 z a/2 = 1,96, 16-среднее квадрат. отклонение

left_side = 80-1.96*16/256**(1/2)
right_side = 80+1.96*16/256**(1/2)
print(
    f'1) Доверительный интервал для оценки мат. ожидания с надежностью 0.95: {left_side}; {right_side}')
# 2

arr = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])


def t_table(confidens, len_array):
    alpha = (1-confidens)
    return stats.t.ppf(1-alpha/2, len_array-1)


def confidens_int(arr, confidens):
    return round(np.mean(arr)-t_table(confidens, len(arr))*np.std(arr, ddof=1)/len(arr)**0.5, 3), \
        round(np.mean(arr)+t_table(confidens, len(arr))
              * np.std(arr, ddof=1)/len(arr)**0.5, 3)


print(
    f'2) истинное значение Х с доверительной вероятностью 0.95: {confidens_int(arr, 0.95)}.')

# 3

daughters = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
mothers = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
x1 = np.mean(daughters)
x2 = np.mean(mothers)
delta = x1 - x2
n = len(daughters)
d1 = np.var(daughters, ddof=1)
d2 = np.var(mothers, ddof=1)

d = (d1 + d2) / 2
SE = np.sqrt(d/n + d/n)

t = stats.t.ppf(0.975, 2 * (n - 1))

result = (delta - t*SE, delta + t*SE)
print(
    f'3) 95% доверительный интервал для разности среднего роста родителей и детей: {result}')
