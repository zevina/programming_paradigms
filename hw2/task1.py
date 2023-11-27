n = int(input('Введите положительное число: '))

def multi_table(n):
  print('\nТаблица умножения от 1 до %d:' % n)
  for row in range(1, n + 1):
    for col in range(1, 10):
      print('%d * %d = %d' % (row, col, row * col))
    print('\n')
  

multi_table(n)