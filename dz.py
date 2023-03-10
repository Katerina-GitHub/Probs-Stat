import numpy as np
from scipy import stats

football = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weights = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

print(f'1.{stats.f_oneway(football, hockey, weights)} < alpha = 0.05, средний рост различен, зависит от вида спорта.')
