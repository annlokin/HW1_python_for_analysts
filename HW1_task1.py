# kwargs={'apple':5, 'lemon':3, 'plam': 2} 
def fruits_warehouse(**kwargs):
      {print(f'Количество {key} на складе {values} шт')
  for key, values in kwargs.items()}
      return print (f'Общее количество фруктов на складе:{sum(kwargs.values())}')

fruits_warehouse (яблок = 5, лемонов = 3, слив = 2)