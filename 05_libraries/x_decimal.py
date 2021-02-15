реализует десятичную арифметику, подходящую для приложений бухгалтерского учета и высокоточных приложений.


from decimal import Decimal, ROUND_HALF_EVEN

# Decimal можно использовать в арифметических операциях:
number = Decimal("0.1")
number = number + number + number
print(number)                                # 0.3

# В операциях с Decimal можно использовать целые числа:
number = Decimal("0.1")
number = number + 2

# нельзя смешивать в операциях дробные числа float и Decimal:
number = Decimal("0.1")
number = number + 0.1                         # здесь возникнет ошибка

# С помощью дополнительных знаков мы можем определить, сколько будет символов в дробной части числа:
number = Decimal("0.10")
number = 3 * number                           # 0.30


# === Округление ==================================================

# ROUND_HALF_EVEN (по умолчанию) число округляется в большую сторону, если оно нечетное, а предыдущее перед ним больше 4
number = Decimal("0.444")
number = number.quantize(Decimal("1.00"))     # 0.44    Decimal("1.00") - формат округления до 2 знаков

number = Decimal("0.555678")
print(number.quantize(Decimal("1.00")))       # 0.56

number = Decimal("0.999")
print(number.quantize(Decimal("1.00")))       # 1.00


# ROUND_HALF_UP: округляет число в сторону повышения, если после него идет число 5 или выше
number = Decimal("10.025")
print(number.quantize(Decimal("1.00"), ROUND_HALF_EVEN))       # 10.02

number = Decimal("10.035")
print(number.quantize(Decimal("1.00"), ROUND_HALF_EVEN))       # 10.04


# ROUND_HALF_DOWN: округляет число в сторону повышения, если после него идет число больше 5
number = Decimal("10.026")
print(number.quantize(Decimal("1.00"), ROUND_HALF_DOWN))       # 10.03

number = Decimal("10.025")
print(number.quantize(Decimal("1.00"), ROUND_HALF_DOWN))       # 10.02


# ROUND_05UP: округляет только 0 до единицы, если после него идет 5
number = Decimal("10.005")
print(number.quantize(Decimal("1.00"), ROUND_05UP))            # 10.01

number = Decimal("10.025")
print(number.quantize(Decimal("1.00"), ROUND_05UP))            # 10.02


# ROUND_CEILING: округляет число в большую сторону вне зависимости от того, какое число идет после него
number = Decimal("10.021")
print(number.quantize(Decimal("1.00"), ROUND_CEILING))         # 10.03

number = Decimal("10.025")
print(number.quantize(Decimal("1.00"), ROUND_CEILING))         # 10.03


# ROUND_FLOOR: не округляет число вне зависимости от того, какое число идет после него
number = Decimal("10.021")
print(number.quantize(Decimal("1.00"), ROUND_FLOOR))           # 10.02

number = Decimal("10.025")
print(number.quantize(Decimal("1.00"), ROUND_FLOOR))           # 10.02
