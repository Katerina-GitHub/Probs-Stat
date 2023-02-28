import numpy as np
import scipy.stats as stats

# 1

x1 = np.array([380, 420, 290])
y1 = np.array([140, 360, 200, 900])

print(f'1) {stats.mannwhitneyu(x1, y1)} pvalue>alpha(0.05), статистически значимых различий нет')

# 2

before = np.array([150, 160, 165, 145, 155])
minutes_10 = np.array([140, 155, 150, 130, 135])
minutes_30 = np.array([130, 130, 120, 130, 125])

print(f'2) {stats.friedmanchisquare(before, minutes_10, minutes_30)} pvalue < alpha(0.05), статистически значимые различия есть')

# 3

before = np.array([150, 160, 165, 145, 155])
minutes_10 = np.array([140, 155, 150, 130, 135])

print(f'3) {stats.wilcoxon(before, minutes_10)} pvalue > alpha(0.05), статистически значимых различий нет')

# 4

group1 = np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
group2 = np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
group3 = np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])

print(f'4) {stats.kruskal(group1, group2, group3)} pvalue > alpha(0.05), статистически значимых различий нет')
