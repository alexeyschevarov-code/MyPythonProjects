import random

print("=== Простой симулятор боя Второй мировой ===\n")

def battle():
    print("Выбери сторону:")
    print("1. Красная Армия")
    print("2. Вермахт")
    side = input("Твой выбор (1 или 2): ")
    
    if side == "1":
        player = "Красная Армия"
        enemy = "Вермахт"
    else:
        player = "Вермахт"
        enemy = "Красная Армия"
    
    print(f"\nБитва началась! {player} против {enemy}\n")
    
    player_force = random.randint(50, 100)
    enemy_force = random.randint(50, 100)
    
    print(f"Силы {player}: {player_force}")
    print(f"Силы {enemy}: {enemy_force}\n")
    
    for round_num in range(1, 6):
        print(f"Раунд {round_num}:")
        damage = random.randint(10, 30)
        if random.random() > 0.5:
            enemy_force -= damage
            print(f"{player} нанёс урон {damage}!")
        else:
            player_force -= damage
            print(f"{enemy} нанёс урон {damage}!")
        
        print(f"Осталось: {player}: {player_force} | {enemy}: {enemy_force}\n")
        
        if player_force <= 0 or enemy_force <= 0:
            break
    
    if player_force > enemy_force:
        print(f"🎉 Победила {player}!")
    elif enemy_force > player_force:
        print(f"🎉 Победила {enemy}!")
    else:
        print("🤝 Ничья!")

# Главный цикл
while True:
    battle()
    again = input("\nЕщё одну битву? (да/нет): ").lower()
    if again != "да":
        print("До встречи на поле боя! 👋")
        break