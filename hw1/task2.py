numbers = [5, 8, 1, 3, 7]

def sort_list_declarative(numbers):
  numbers.sort(reverse=True)
  return numbers

sort_list_declarative(numbers)
print(numbers)