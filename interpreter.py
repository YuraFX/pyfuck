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

class Pyfuck:
    def __init__(self):
        self.memory = [0] * 30000 # Память для хранения данных
        self.pointer = 0 # Указатель текущей ячейки памяти
        self.output = "" # Результирующая строка

    def interpret(self, program):
        self.output = ""

        for i in range(len(program)):
            command = program[i]

            if command == ">": # Следующая ячейка
                self.pointer += 1

            elif command == "<": # Предыдущая ячейка
                self.pointer -= 1

            elif command == "+": # Значение текущей ячейки увеличивает на 1
                self.memory[self.pointer] += 1

            elif command == "-": # Значение текущей ячейки уменьшают на 1
                self.memory[self.pointer] -= 1

            elif command == ".": # Напечатать значение из текущей ячейки
                self.output += chr(self.memory[self.pointer])

            elif command == ",": # Ввести извне значение и сохранить в текущей ячейке
                input_value = input("Введите значение: ")
                if len(input_value) <= 1:
                    self.memory[self.pointer] = ord(input_value)
                else:
                    return

            elif command == "[": # Начало цикла
                if self.memory[self.pointer] == 0:
                    nested = 1
                    while nested > 0:
                        i += 1
                        if program[i] == "[":
                            nested += 1
                        elif program[i] == "]":
                            nested -= 1

            elif command == "]": # Конец цикла
                if self.memory[self.pointer] != 0:
                    nested = 1
                    while nested > 0:
                        i -= 1
                        if program[i] == "]":
                            nested += 1
                        elif program[i] == "[":
                            nested -= 1

            else:
                print("Ошибка: неизвестная команда!")
        return self.output