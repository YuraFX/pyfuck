<p align="center"><img src="https://raw.githubusercontent.com/YuraFX/pyfuck/main/images/logo.png" width="360"></p>
<h1 align="center">Интерпретатор языка Brainfuck</h1>

![donate](images/donation_alerts.png) [Финансовая поддержка](https://www.donationalerts.com/r/yura_fx) 

## Вступление

Сидел я тут как-то вечером и думал, что можно такое интересное написать на Python’е и тут я вспомнил, что когда-то давно, ещё на C#, 
пытался написать интерпретатор какого-нибудь простого языка, того же BASIC например, но особо ничего не получалось. В момент этих попыток 
я наткнулся на такой язык, как [Brainfuck](https://ru.wikipedia.org/wiki/Brainfuck) – по истине мозговыносящий эзотерический язык программирования (нестандартный язык, который 
создаётся с целью развлечения или исследования особенностей программирования. Он обычно имеет необычный синтаксис и принципы работы, 
что делает его сложным для понимания и использования в реальных проектах). Я начал смотреть видеоролики, просматривал статью на Википедии, 
чтобы понять, что это за язык и с чем его едят)) Итогом этого стало написание интерпретатора, который я назвал Pyfuck. Как-то так)

## О самом интерпретаторе

Интерпретатор имеет память под 30.000 однобайтовых ячеек с нулевыми начальными значениями (всё, как в оригинальном Brainfuck).

Имеется указатель текущей ячейки памяти и результирующая строка.

Интерпретатор также имеет функцию сохранения и загрузки написанной программы в формате `.bf`.

Важное примечание: Путём сохранения и открытия написанных программ является папка с exe-шником интерпретатора.

Он имеет все 8 команд Brainfuck:

|Команда |Описание                                           |
|--------|---------------------------------------------------|
|`>`     |Следующая ячейка                                   |
|`<`     |Предыдущая ячейка                                  |
|`+`     |Значение текущей ячейки увеличивает на 1           |
|`-`     |Значение текущей ячейки уменьшают на 1             |
|`.`     |Напечатать значение из текущей ячейки              |
|`,`     |Ввести извне значение и сохранить в текущей ячейке |
|`[`     |Начало цикла                                       |
|`]`     |Конец цикла                                        |

### Как составляется программа?

Тут всё довольно интересно) Для составления программ удобно использовать таблицу символов ASCII:

![ASCII](images/ASCII_table.jpg)

Мы должны обратить внимание на Decimal (это число, которое соответствует определённому символу. Это десятичное 
представление числа символа в таблице ASCII. Например, символ «A» имеет значение 65 в ASCII). В Brainfuck это 
будет выглядеть, как 65 команд «+».

Вот пример программы, печатающая «Hello World!»:
```++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++.+++++++..+++.>++++++++++++++++++++++++++++++++.<------------------------.++++++++++++++++++++++++.+++.------.--------.>+.```

![hello](images/program_result.png)

## Ссылки

* [Скачать](https://github.com/YuraFX/pyfuck/releases/tag/1.0) ![windows](images/windows.png)Windows-версию в релизах.

## О лицензии

<img src="https://www.gnu.org/graphics/gplv3-with-text-136x68.png" width="160" align="right">

Это [свободная программа](https://www.gnu.org/philosophy/free-sw.html): вы можете перераспространять ее и/или изменять ее на 
условиях [Стандартной общественной лицензии GNU](https://www.gnu.org/licenses/gpl-3.0.html) в том виде, 
в каком она была опубликована [Фондом свободного программного обеспечения](https://www.fsf.org/); либо версии 3 лицензии, либо (по вашему выбору) любой более поздней версии.

Эта программа распространяется в надежде, что она будет полезной, но БЕЗО ВСЯКИХ ГАРАНТИЙ; даже без неявной гарантии 
ТОВАРНОГО ВИДА или ПРИГОДНОСТИ ДЛЯ ОПРЕДЕЛЕННЫХ ЦЕЛЕЙ. Подробнее см. в Стандартной общественной лицензии GNU.

Вы должны были получить [копию](https://github.com/YuraFX/pyfuck/blob/main/LICENSE) Стандартной общественной лицензии GNU вместе с этой программой. Если это не так, см. <https://www.gnu.org/licenses/>.
