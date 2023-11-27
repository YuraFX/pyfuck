# Foobar is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

print("  ____         __            _     ")
print(" |  _ \ _   _ / _|_   _  ___| | __ ")
print(" | |_) | | | | |_| | | |/ __| |/ / ")
print(" |  __/| |_| |  _| |_| | (__|   <  ")
print(" |_|    \__, |_|  \__,_|\___|_|\_\ ")
print("        |___/                      ")
print("   Интерпретатор языка Brainfuck   ")
print("             Версия 1.0            ")
print("  Автор: Конышев Юрий aka Yura_FX  ")
print("")

import os
from interpreter import Pyfuck

interpreter = Pyfuck()

def input_output(): # Функция ввода-вывода
    while True:
        keyboard = input("# ")

        # Сбрасываем значения памяти и указателя текущей ячейки перед каждой интерпретацией
        interpreter.memory = [0] * 30000
        interpreter.pointer = 0

        if keyboard == "save": # Сохранение написанной программы
            filename = input("Введите имя файла для сохранения: ") # Получение имени файла от пользователя

            if filename == "":
                print("Ошибка: Вы не указали название файла!")
                continue
            else:
                filename += ".bf" # Добавление расширения файла
                with open(filename, "w") as file: # Открытие файла для записи
                    file.write(program) # Запись содержимого переменной «program» в файл

                    print("Программа успешно сохранена!")
                    continue

        elif keyboard == "load": # Открытие написанной программы
            filename = input("Введите имя файла для загрузки: ") # Получение имени файла от пользователя

            if filename == "":
                print("Ошибка: Вы не указали название файла!")
                continue
            else:
                filename += ".bf" # Добавление расширения файла

                if os.path.exists(filename):
                    with open(filename, "r") as file: # Открытие файла для загрузки
                        program = file.read() # Загрузка содержимого файла в переменную «program»

                        print("Программа успешно загружена!")
                        print(f"Код программы: {program}")

                        output = interpreter.interpret(program)
                        print(f"Результат программы: {output}")
                        continue

        elif keyboard == "exit":
            break

        program = keyboard # Присваивание значения переменной «keyboard» переменной «program»

        output = interpreter.interpret(program) # Производим интерпретацию

        print(f"Результат программы: {output}") # Выводим результат в консоль

input_output()