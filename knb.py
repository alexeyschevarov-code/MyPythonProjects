import random

print("=== Камень — Ножницы — Бумага ===")
print("Для выхода напиши 'выход'\n")

choices = ["камень", "ножницы", "бумага"]

while True:
    player = input("Твой выбор (камень, ножницы, бумага): ").lower().strip()
    
    if player == "выход":
        print("Спасибо за игру! До встречи 👋")
        break
    
    if player not in choices:
        print("❌ Неправильный выбор! Пиши только: камень, ножницы или бумага")
        continue
    
    computer = random.choice(choices)
    print(f"Компьютер выбрал: {computer}")
    
    # Определяем победителя
    if player == computer:
        print("🤝 Ничья!")
    elif (
        (player == "камень" and computer == "ножницы") or
        (player == "ножницы" and computer == "бумага") or
        (player == "бумага" and computer == "камень")
    ):
        print("🎉 Ты выиграл!")
    else:
        print("😢 Компьютер выиграл!")
    
    print("-" * 40)