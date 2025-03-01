# QUESTION 4
# For n cities, create a randomized n × n matrix to represent the cost of traveling between
# the cities. Then find the cheapest route that starts from the first city, visits all other cities,
# and returns to the first city (a classic traveling salesman problem). Brute force is fine.
# Example Input:
# n = 4
# This will create a 4 × 4 matrix with random values, e.g.:
# '
# 0 0.914 0.136 0.507
# 0.118 0 0.259 0.389
# 0.876 0.664 0 0.734
# 0.097 0.475 0.310 0
# 2

# in which entry (i, j) is the cost of going from city i to city j (indices in our matrix start from
# the top-left).
# Output:
# The cheapest route is (1,3,2,4,1) which costs 1.286.

import random
import itertools
import sys

n = 4
matrix = [[random.random() for i in range(n)] for j in range(n)]

for i in range(n):
    matrix[i][i] = sys.maxsize
    