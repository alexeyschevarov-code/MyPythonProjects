print("=== Простой калькулятор ===")
print("Для выхода напиши 'выход' вместо операции\n")

while True:
    num1 = input("Введите первое число (или 'выход'): ")
    if num1.lower() == "выход":
        print("До свидания! 👋")
        break
    
    operation = input("Введите операцию (+, -, *, /): ")
    num2 = input("Введите второе число: ")

    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Ошибка! Делить на ноль нельзя."
        else:
            result = "Неизвестная операция!"

        print("Результат:", result)
        print("-" * 30)   # разделитель

    except:
        print("Ошибка! Введи числа правильно.")
        print("-" * 30)
        