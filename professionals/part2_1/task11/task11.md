В различных социальных сетях существуют системы лайков, которые в зависимости от количества людей, оценивших запись, показывают соответствующую информацию.

Реализуйте функцию likes(), которая принимает один аргумент:

names — список имён
Функция должна возвращать строку в соответствии с примерами ниже, содержание которой зависит от количества имён в списке names.

Приведенный ниже код:

print(likes([]))
print(likes(['Тимур']))
print(likes(['Тимур', 'Артур']))
print(likes(['Тимур', 'Артур', 'Руслан']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))
должен выводить:

Никто не оценил данную запись
Тимур оценил(а) данную запись
Тимур и Артур оценили данную запись
Тимур, Артур и Руслан оценили данную запись
Тимур, Артур и 2 других оценили данную запись
Тимур, Артур и 3 других оценили данную запись
Тимур, Артур и 6 других оценили данную запись
