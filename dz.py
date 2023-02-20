from statistics import NormalDist

# 1


def mean_and_variance(a, b):
    return f'1. Среднее значение:{(a+b)/2: .2f}, дисперсия:{((b-a)**2)/12: .2f}'


print(mean_and_variance(200, 800))

# 2

b = 0.5+2.4**(1/2)
print(f'2. Правая граница распределения величины В - b = {b: .2f}\n'
      f'Среднее значение В на промежутке (0.5; {b: .2f}) M(B) = {(b+0.5)/2: .2f}'
      )

# 4


def z_value(hgt):
    return (hgt-174)/8


P = 1-NormalDist().cdf(z_value(182))
print(f'4. a){P}')
P = 1-NormalDist().cdf(z_value(190))
print(f'б){P}')
z1 = z_value(166)
z2 = z_value(190)
P = NormalDist().cdf(z2)-NormalDist().cdf(z1)
print(f'в){P}')
z1 = z_value(166)
z2 = z_value(182)
P = NormalDist().cdf(z2)-NormalDist().cdf(z1)
print(f'г){P}')
z1 = z_value(158)
z2 = z_value(190)
P = NormalDist().cdf(z2)-NormalDist().cdf(z1)
print(f'д){P}')
z1 = z_value(150)
z2 = z_value(190)
P = NormalDist().cdf(z1)+(1-NormalDist().cdf(z2))
print(f'е){P}')
z1 = z_value(150)
z2 = z_value(198)
P = NormalDist().cdf(z1)+(1-NormalDist().cdf(z2))
print(f'ё){P}')
z = z_value(166)
P = NormalDist().cdf(z)
print(f'ж){P}')

# 5

Z = (190-178)/25**(1/2)
print(f'5. на: {Z} сигм.')
