import numpy as np
import matplotlib.pyplot as plt

# 1

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

plt.scatter(zp, ks)
plt.xlabel('Зарплата')
plt.ylabel('Скоринг', rotation=90)
plt.show()

b = (np.mean(zp * ks) - np.mean(zp) * np.mean(ks)) / \
    (np.mean(zp**2) - np.mean(zp) ** 2)
print(b)

a = np.mean(ks)-b*np.mean(zp)
print(a)

plt.scatter(zp, ks)
plt.plot(zp, 444.18+2.62*zp, c='r', label=r'$ks=444.18+2.62\cdot zp$')
plt.legend()
plt.xlabel('Зарплата')
plt.ylabel('Скоринг', rotation=90)
plt.show()

ks = ks.reshape((-1, 1))

zp = zp.reshape((-1, 1))
zp = np.hstack([np.ones((len(zp), 1)), zp])

B = np.dot(np.linalg.inv(np.dot(zp.T, zp)), np.dot(zp.T, ks))
print(B)

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

ks = ks.reshape((-1, 1))

zp = zp.reshape((-1, 1))


B = np.dot(np.linalg.inv(np.dot(zp.T, zp)), np.dot(zp.T, ks))
print(B)

plt.scatter(zp, ks)
plt.plot(zp, 444.18+2.62*zp, c='r', label=r'$ks=444.18+2.62\cdot zp$')
plt.plot(zp, B*zp, c='g', label=r'$ks=5.89\cdot zp$')
plt.legend()
plt.xlabel('Зарплата')
plt.ylabel('Скоринг', rotation=90)
plt.show()

# 2


def _mse(b, x, y):
    return np.sum((b*x-y)**2)/len(x)


zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
print(_mse(2.62, zp, ks))


def _mse_p(b, x, y):
    return (2/len(x))*np.sum((b*x-y)*x)


alpha = 1e-06

b = 0.1
mse_min = _mse(b, zp, ks)
i_min = 1
b_min = b
for i in range(10000):
    b -= alpha*_mse_p(b, zp, ks)
    if i % 100 == 0:
        print(f'Итерация #{i}, b={b}, mse={_mse(b, zp,ks)}')
    if _mse(b, zp, ks) > mse_min:
        print(
            f'Итерация #{i_min}, b={b_min}, mse={mse_min},\nМинимум')
        break
    else:
        mse_min = _mse(b, zp, ks)
        i_min = i
        b_min = b

# 3


def _mse_ab(a, b, x, y):
    return np.sum(((a+b*x)-y)**2)/len(x)


def _mse_pa(a, b, x, y):
    return 2*np.sum((a+b*x)-y)/len(x)


def _mse_pb(a, b, x, y):
    return 2*np.sum(((a+b*x)-y)*x)/len(x)


alpha = 5e-05
b = 0.1
a = 0.1
mseab_min = _mse_ab(a, b, zp, ks)
i_min = 1
b_min = b
a_min = a

for i in range(1000000):
    a -= alpha*_mse_pa(a, b, zp, ks)
    b -= alpha*_mse_pb(a, b, zp, ks)
    if i % 50000 == 0:
        print(f'Итерация #{i}, a={a}, b={b}, mse={_mse_ab(a, b, zp,ks)}')
    if _mse_ab(a, b, zp, ks) > mseab_min:
        print(
            f'Итерация #{i_min}, a={a_min}, b={b_min}, mse={mseab_min},\nМинимум')
        break
    else:
        mseab_min = _mse_ab(a, b, zp, ks)
        i_min = i
        b_min = b
        a_min = a
print(f'a={a_min}\nb={b_min}')
