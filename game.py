import random

print("=== Игра 'Угадай число' ===")
print("Я загадал число от 1 до 20.")
print("У тебя есть 7 попыток.\n")

while True:                           # главный цикл (для игры заново)
    secret = random.randint(1, 20)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        attempts += 1
        guess = int(input(f"Попытка {attempts} из {max_attempts}. Твой вариант: "))

        if guess == secret:
            print(f"🎉 Правильно! Ты угадал за {attempts} попыток!")
            break
        elif guess < secret:
            print("Слишком мало.")
        else:
            print("Слишком много.")

    if guess != secret:
        print(f"😢 Ты проиграл. Загаданное число было: {secret}")

    # Спрашиваем, хочет ли играть ещё раз
    again = input("\nХочешь сыграть ещё раз? (да/нет): ").lower()
    if again != "да":
        print("Спасибо за игру! До встречи 👋")
        break