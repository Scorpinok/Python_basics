# 4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего
# задания. Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов
# функции currency_rates(). Убедиться, что ничего лишнего не происходит.

import utils_not_console as unc

unc.currency_rates("USD")
unc.currency_rates("EUR")
unc.currency_rates("GBP")

