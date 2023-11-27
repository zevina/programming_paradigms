numbers = [5, 8, 1, 3, 7]

def sort_list_imperative(numbers):
  changed = True
  while changed:
    changed = False
    for i in range(len(numbers) - 1):
      if numbers[i] < numbers[i+1]:
        numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        changed = True
  return numbers

sort_list_imperative(numbers)
print(numbers)