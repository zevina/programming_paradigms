import random

def binarySearch(arr, l, r, x):
  while l <= r:
    mid = l + (r - l) // 2

    if arr[mid] == x:
        return mid

    elif arr[mid] < x:
        l = mid + 1

    else:
        r = mid - 1
  return -1

arr = random.sample(range(1, 50), 10) #список неповторяющихся значений
arr.sort()
print(f"Исходный массив: {arr}")
x = random.randrange(1, 50)
print(f"Искомое значение: {x}")

result = binarySearch(arr, 0, len(arr)-1, x)
if result != -1:
    print(f"Индекс элемента в списке: {result}")
else:
    print("Элемента нет в списке")