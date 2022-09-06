class Calc:
 # инициализация класса
 def __init__(self):
   # результат
   self.result = 0

 # метод для добавления числа
 def add(self, n):
   self.result += n
   # возвращаем экземпляр, чтобы иметь возможность выполнять операции в цепочке
   return self

 # для вычитания
 def sub(self, n):
   self.result -= n
   return self

 # для умножения
 def mult(self, n):
   self.result *= n
   return self

 # для деления
 def div(self, n):
   self.result /= n
   return self

# создаем экземпляр
calc = Calc()

# выполняем операции
calc.add(5).sub(3).mult(4).div(2)

# выводим результат
print(int(calc.result)) # 4