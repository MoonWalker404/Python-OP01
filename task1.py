# Создать калькулятор — программу, в которой мы вводим 2 числа,
# и с ними производятся сразу все математические действия


# Приветствие и объяснение работы программы
print("Привет! Это простой калькулятор.")
print("Введите два числа, и я выполню с ними основные математические операции.")

# Ввод чисел от пользователя
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Вычисление результатов операций
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Вывод результатов
print("Результаты:")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")