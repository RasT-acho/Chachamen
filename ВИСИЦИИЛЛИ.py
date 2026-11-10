word = input()

man_5 = " ○"

man_4 = " ○", " ъ|"
         
man_3 = " ○", "/|"
        
man_2 = " ○", "/|\\"
        
man_1 = " ○", "/|\\", "/"
        
man_0 = " ○", "/|\\", "/ \\"

def play_hangman():
    guessed_letters = set()
    attempts = 6 
    print("Начинаем.")
    while attempts > 0:
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
        print(f"\nСлово: {display_word}")
        print(f"Осталось попыток: {attempts}")
        if attempts == 5:
            print(man_5, sep="\n")
        elif attempts == 4:
            print(*man_4, sep="\n")
        elif attempts == 3:
            print(*man_3,sep="\n")
        elif attempts == 2:
            print(*man_2, sep="\n")
        elif attempts == 1:
            print(*man_1, sep="\n")

        if display_word == word:
            print("Угадал.")
            return

        guess = input("Введите букву: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Буква: ")
            continue

        if guess in guessed_letters:
            print("Вы уже называли эту букву.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Есть.")
        else:
            attempts -= 1
            print("Этой буквы нет в слове.")

    print(f"\nВы проиграли. Было загадано слово: {word}")
    print(*man_0, sep="\n")

if __name__ == "__main__":
    play_hangman()