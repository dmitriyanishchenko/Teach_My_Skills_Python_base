# Ввести строку. Вывести на экран букву, которая находится в середине этой строки.
# Также, если эта центральная буква равна первой букве в строке, то создать и вывести
# часть строки между первым и последним символами исходной строки.
# (подсказка: для получения центральной буквы, найдите длину строки и разделите ее пополам.
# Для создания результирующий строки используйте срез)

line = input('Enter some line --->')
middle_symbol = line[int(len(line) / 2)]
print(middle_symbol)
if middle_symbol == line[0]:
    new_line = line[1:-1]
    print(new_line)
