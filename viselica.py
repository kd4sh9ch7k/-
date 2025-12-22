from random import choice

HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |    |
     | 
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   
     |   
     |     
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
     |   
    ----------
    """
)

def load_words_from_file(filename="words.txt"):
    """
    Загружает слова из текстового файла.
    Каждое слово должно быть на новой строке.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # читаем все строки убираем проблема и пустые строки
            words = []
            for line in file:
                word = line.strip() 
                if word:  # пустые строки
                    words.append(word.lower())  
        
        if not words:
            print(f"Файл {filename} пуст! Используются слова по умолчанию.")
            return ["python", "игра", "программирование"]
        
        return words
    
    except FileNotFoundError:
        print(f"Файл {filename} не найден! Создайте файл words.txt со словами.")
        print("Используются слова по умолчанию.")
        return ["умный", "человек", "обои"]

# слова из файла
WORDS = load_words_from_file("words.txt")

max_wrong = len(HANGMAN) - 1

word = choice(WORDS)  # случайное слово
so_far = "_" * len(word)
wrong = 0  # количество неверных ответов
used = []  # буквы угаданы

print(f"Добро пожаловать в игру 'Виселица'!")
print(f"В слове {len(word)} букв. У вас есть {max_wrong} попыток.")

while wrong < max_wrong and so_far != word:
    print(HANGMAN[wrong])  # вывод виселицы
    print("\nИспользованные буквы:", ', '.join(used) if used else "пока нет")
    print("\nСлово:", ' '.join(so_far))

    guess = input("\n\nВведите букву: ").lower()  # нижний регистр

    if len(guess) != 1 or not guess.isalpha():
        print("Пожалуйста, введите одну букву!")
        continue

    if guess in used:
        print(f"Вы уже вводили букву '{guess}'!")
        continue

    used.append(guess)

    if guess in word:
        print(f"\n Правильно! Буква '{guess}' есть в слове!")
        # отображение слова
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print(f"\n Нет, буквы '{guess}' нет в слове.")
        wrong += 1
        print(f"Ошибок: {wrong} из {max_wrong}")

# вывод финала
print("\n" + "="*40)
print(HANGMAN[wrong])  

if wrong == max_wrong:
    print("ТЕБЯ ПОВЕСИЛИ! ТЫ ПРОИГРАЛ!")
else:
    print("ПОЗДРАВЛЯЮ! ТЫ ВЫИГРАЛ!")

print(f"\nЗагаданное слово было: '{word}'")
print("="*40)
