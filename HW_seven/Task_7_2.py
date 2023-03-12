# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны.

def print_operation_table(operation, num_rows = 6, num_columns = 6): #функция создает таблицу, используя переданную функцию для вычисления значений элементов
     for x in range(1, num_rows+1): # перебираем строки
        row = [] # задаем пустую строку
        for y in range(1, num_columns+1): 
            row.append(str(operation(x, y))) # записываем елемент функции lambda в строку
        print(row) 
    
print_operation_table(lambda x, y: x * y) # функция вычислений значений елементов таблицы
