import random
import math
from functools import reduce

arr1 = [random.randrange(1, 10) for i in range(10)]
arr2 = [random.randrange(1, 10) for i in range(10)]
print(f"Массив 1: {arr1}")
print(f"Массив 2: {arr2}")

def pearson_correlation(array_x, array_y):
  if len(array_x) != len(array_y):
    raise ValueError("Массивы должны быть одинаковой длины!")

  n = len(array_x)
  avg_x = sum(array_x) / n
  avg_y = sum(array_y) / n

  def deviation_mult(array_x, array_y):
    return list(map(lambda x, y: (x - avg_x) * (y - avg_y), array_x, array_y))

  numerator = reduce(lambda a, b: a + b, deviation_mult(array_x, array_y))
  if numerator == 0:
    return 0

  var_x = reduce(lambda a, b: a + b, list(map(lambda x: (x - avg_x) ** 2, array_x)))
  var_y = reduce(lambda a, b: a + b, list(map(lambda y: (y - avg_y) ** 2, array_y)))
  denominator = math.sqrt(var_x * var_y)
  
  correlation = numerator / denominator
  return correlation

correlation = round(pearson_correlation(arr1, arr2), 2)
print(f"Корреляция Пирсона: {correlation}")