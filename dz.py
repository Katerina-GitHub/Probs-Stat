import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# 1

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

plt.scatter(zp, ks)
plt.xlabel('zp')
plt.ylabel('ks', rotation=90)
plt.show()


def covar(array1, array2):
    MXY = sum(array1*array2)/len(array1)
    MX = sum(array1)/len(array1)
    MY = sum(array2)/len(array2)
    return MXY-MX*MY


print(covar(zp, ks))
print(np.cov(zp, ks, ddof=0))


def coef_pirson(array, offset=True):
    mean_array = sum(array)/len(array)
    square_dev = (array-mean_array)**2
    variance = sum(square_dev) / \
        len(array) if offset else sum(square_dev)/(len(array)-1)
    return variance**0.5


r = covar(zp, ks)/(coef_pirson(zp)*coef_pirson(ks))
print(f'Коэффициент корреляции r = {r: .4f}')
r1 = np.cov(zp, ks, ddof=1)/(coef_pirson(zp, offset=False)
                             * coef_pirson(ks, offset=False))
print(f'Коэффициент корреляции r = {r1}')
print(np.corrcoef(zp, ks))
df = pd.DataFrame(data={'zp': zp, 'ks': ks})
print(
    f'Присутствует линейная взаимосвязь между исходными данными.{df.corr()}')
# 2

arr = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
print(f'Среднее квадратическое отклонение по выборке(несмещенное): {np.std(arr, ddof=1): .2f}.'
      )


def t_crit(confidens, len_array):
    alpha = (1-confidens)
    return stats.t.ppf(1-alpha/2, len_array-1)


print(
    f'Из таблицы t-критерия для 95% доверительного интервала данной выборки: {t_crit(0.95, len(arr)): .2f}')


def confidens_int(arr, confidens):
    return round(np.mean(arr)-t_crit(confidens, len(arr))*np.std(arr, ddof=1)/len(arr)**0.5, 3), \
        round(np.mean(arr)+t_crit(confidens, len(arr))
              * np.std(arr, ddof=1)/len(arr)**0.5, 3)


print(
    f'95% доверительный интервал для истинного значения IQ : {confidens_int(arr, 0.95)}')
# 3

left = 174.2-(1.96*25**0.5)/27**0.5
right = 174.2+(1.96*25**0.5)/27**0.5
print(
    f'Доверительный интервал для мат. ожидания с надежностью 0.95: [{left: .4f};{right: .4f}].')
