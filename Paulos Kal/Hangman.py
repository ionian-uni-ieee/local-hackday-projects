import random

invalid = "Invalid number."
low = "Too low number."
high = "Too high number."
word_category = [[23, 38, 90, 116, 121, 151, 175, 197, 209, 229, 258, 269, 293, 300, 386, 403, 417, 459, 471, 491, 501, 515, 528], ["Adjectives for people", "Adverbs of time", "Animals", "Bank", "Sports", "Body", "Buildings and places", "Car parts", "City", "Classroom", "Clothes", "Colours", "Cooking", "Days of the week", "Food", "Family", "Geography", "House", "Months", "Numbers", "Tools", "Transportation", "Weather"]]  # 0 - 22
standard_options = [True, False, 12]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def Main():
    stop = False
    while(not stop):
        ClearScreen()
        options = ["","",""]
        for i in range(len(standard_options)):
            options[i] = standard_options[i]
        print("Welcome to Hangman!\n\n\nMAIN MENU\n\n1. Play\n2. Options\n3. Exit")
        answer = CheckValues(1, 3, low, high)
        if(answer == 1):
            Game(options)
        elif(answer == 2):
            Options(standard_options)
        else:
            print("\nAre you sure?\n1. Yes\n2. No")
            answer = CheckValues(1, 2, invalid, invalid)
            if(answer == 1):
                stop = True

def Menu():
    print("\nPress ENTER to return to the menu")
    input()

def OptionChange(standard_options, number):
    print("Press [1] to change or [2] to reset\n")
    answer = CheckValues(1, 2, invalid, invalid)
    if(number == 1 or number == 2):
        if(answer == 1):
            standard_options[number - 1] = not standard_options[number - 1]
        else:
            standard_options[number - 1] = True
    else:
        if(answer == 1):
            print("Enter a number from 1 to 20:")
            standard_options[number - 1] = CheckValues(1, 20, low, high)
        else:
            standard_options[number - 1] = 12
    return standard_options

def Options(standard_options):
    stop = False
    while(not stop):
        ClearScreen()
        print("OPTIONS\n")
        print("\n1. First letter isible:", standard_options[0])
        print("\n2. Last letter visible:", standard_options[1])
        print("\n3. Max lives:", standard_options[2])
        print("\n4. Return to menu")
        answer = CheckValues(1, 4, low, high)
        if(answer != 4):
            OptionChange(standard_options, answer)
        else:
            stop = True

def ClearScreen():
    for i in range(30):
        print("\n")

def CheckType(answer, typ):
    if(typ == "int"):
        integer = False
        while(not integer):
            try:
                answer = int(answer)
                integer = True
            except ValueError:
                integer = False
                print("Answer must be an integer. Try again!")
                answer = input()
    else:
        string = False
        while(not string):
            string = True
            try:
                answer = int(answer)
                string = False
                print("Answer must be str. Try again!")
                answer = input()
            except ValueError:
                if(len(answer) > 1):
                    print("Only 1 letter is acceptable! Try again!")
                    answer = input()
                else:
                    string = True
        
    return answer

def CheckValues(low, high, message_low, message_high):
    answer = CheckType(input(), "int")
    if(high == -1):
        while(answer < low):
            if(answer < low):
                print(message_low, "Try again!")
                answer = CheckType(input(), "int")
    else:
        while(answer < low or answer > high):
            if(answer < low):
                print(message_low, "Try again!")
                answer = CheckType(input(), "int")
            elif(answer > high):
                print(message_high, "Try again!")
                answer = CheckType(input(), "int")
    return answer

def PickWord():
    with open("Word list.txt", "r") as file:
        number = random.randint(0, 528)
        word = file.readlines()[number].rstrip("\n").split(" ")
    positions1 = []
    for letter in alphabet:
        i = 0
        position = 0
        letter_position = []
        while(position != -1):
            position = word[0].find(letter, i)
            i = position + 1
            letter_position.append(position)
        positions1.append(letter_position)
    positions2 = []
    if(len(word) == 2):
        for letter in alphabet:
            i = 0
            position = 0
            letter_position = []
            while(position != -1):
                position = word[1].find(letter, i)
                i = position + 1
                letter_position.append(position)
            positions2.append(letter_position)
    word_data = [word, number, positions1, positions2]
    return word_data

def Appear(word, options):
    appear = ""
    for words in word:
        if(options[0] and options[1]):
            appear += words[0] + " " + "_ "*(len(words) - 2) + words[len(words) - 1]
        elif(options[1]):
            appear += "_ "*(len(words) - 1) + " " + words[len(words) - 1]
        elif(options[0]):
            appear += words[0] + " " + "_ "*(len(words) - 1)
        else:
            appear += "_ "*(len(words))
        appear += " "
    return appear

def Game(options):
    ClearScreen()
    word_data = PickWord()
    appear = Appear(word_data[0], options)
    print(word_data[0])  # temporary
    print("Your game has started!\n\nGOOD LUCK\n\n\n")
    while(options[2] > 0):
        print(appear, "\nlives:", options[2])
        print("\n\n1. Try a letter\n2. View hint (-3 lives)\n3. Skip word (-5 lives)")
        answer = CheckValues(1, 3, low, high)
        if(answer == 1):
            print("\nEnter 1 letter:")
            letter = CheckType(input(), "str")
            if(len(word_data[0]) == 2):
                if((letter in word_data[0][0]) or (letter in word_data[0][1])):
                    print("\nRight!")
                    index = alphabet.index(letter)
                    for c in range(2):
                        a = 0
                        for i in word_data[2 + c][index]:
                            if(word_data[2 + c][index][c] != -1):
                                appear = appear[:2*i + 2*c*len(word_data[0][0])] + appear[2*i + 2*c*len(word_data[0][0])].replace("_", letter) + appear[2*i  + 2*c*len(word_data[0][0]) + 1:]
                            a += 1
                else:
                    options[2] -= 1
                    print("\nThe word does not contain '{}'.".format(letter))
            else:
                if(letter in word_data[0][0]):
                    print("\nRight!")
                    index = alphabet.index(letter)
                    a = 0
                    for i in word_data[2][index]:
                        if(word_data[2][index] != -1):
                            appear = appear[:2*i] + appear[2*i].replace("_", letter) + appear[2*i + 1:]
                        a += 1
                else:
                    options[2] -= 1
                    print("\nThe word does not contain '{}'.".format(letter))
        elif(answer == 2):
            if(options[2] > 3):
                options[2] -= 3
                for i in range(len(word_category[0])):
                    if(word_data[1] <= word_category[0][i]):
                        category = word_category[1][i]
                        break
                print("\nThe word falls under the category '{}'".format(category))
            else:
                print("\nYou don't have enough lives!")
        else:
            if(options[2] > 5):
                options[2] -= 5
                if(len(word_data[0]) == 1):
                    print("\nThe word was '{}'".format(word_data[0][0]))
                else:
                    print("\nThe word was '{} {}'".format(word_data[0][0], word_data[0][1]))
                print("\n\nPress ENTER to continue")
                input()
                return Game(options)
            else:
                print("\nYou don't have enough lives!\n\n")
        if(not "_" in appear):
            print("\nYou found the word!\n\n", word_data[0][0] + word_data[0][1])
            return Game(options)
        print("\n\nPress ENTER to continue")
        input()
        ClearScreen()
    print("\nYou lost all of your lives.")
    return Menu()

Main()
