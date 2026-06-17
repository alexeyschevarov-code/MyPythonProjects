import random
import string

print("=== Генератор паролей ===\n")

# Спрашиваем настройки
length = int(input("Длина пароля (рекомендую 12-16): "))

use_letters = input("Использовать буквы? (да/нет): ").lower() == "да"
use_numbers = input("Использовать цифры? (да/нет): ").lower() == "да"
use_symbols = input("Использовать специальные символы (!@#$ и т.д.)? (да/нет): ").lower() == "да"

# Формируем набор символов
characters = ""
if use_letters:
    characters += string.ascii_letters  # a-z и A-Z
if use_numbers:
    characters += string.digits         # 0-9
if use_symbols:
    characters += "!@#$%^&*()_+-=[]{}|;:,.<>/?"

if not characters:
    print("Ошибка! Нужно выбрать хотя бы один тип символов.")
else:
    # Генерируем пароль
    password = ''.join(random.choice(characters) for _ in range(length))
    print("\n🎉 Твой сгенерированный пароль:")
    print(password)
    print(f"\nДлина: {length} символов")
    