for i in range(30):
    print("\n")
print("Welcome to Paulos' text adventures!\n\nYou need about 5 minutes to complete this game story.\n\nAll you have to do is answer to the questions\nby choosing the number next to every answer.\n\nAt the end of the game there will be some comments about your decisions.\n\nGOOD LUCK!!!  (press ENTER to start)")
input()
for i in range(30):
    print("\n")
print("\n\nA DAY WITHOUT MY WIFE\n\n")
print("\nThe phone rings. It's 08:30 and you see the name\nof your boss on the screen. You realise that you are very late.\nWhat do you do?\n")
print("1. Answer.\n2. Ignore the call.")
answer = int(input())
for i in range(30):
    print("\n")
call_answer = 0
truth = 0
if(answer == 1):
    call_answer = 1
    print("You pick up the phone. Your boss seems angry and asks for\na reason why you are not at work. What do you say?\n")
    print("1. Find an excuse.\n2. Tell the truth.")
    answer = int(input())
    for i in range(30):
        print("\n")
    if(answer == 1):
        print("You tell him that you got ill and couldn't go to the office.\nYou apologize and the call ends.")
    else:
        truth = 1
        print("You tell him that you slept more than usual and try to convince\nhim that it won't happen again. He tells you that he doesn't\nneed you today and the call ends.")
else:
    print("You don't answer the call.")
print("Now you feel bad for not going to work and wake up. You decide to stay home.\nWhat do you do?\n")
print("1. Wake up.\n2. Watch TV.\n3. Do some housework.")
answer = 1
silliness = 0
sedulity = 0
while(answer == 1):
    answer = int(input())
    if(answer == 1):
        silliness = 1
        print("\n\nYou already woke up, idiot!!! Mind your decisions!\n")
    elif(answer == 2):
        for i in range(30):
            print("\n")
        print("You sit on the couch and watch TV.")
    else:
        for i in range(30):
            print("\n")
        sedulity = 1
        print("You decide to spend your day cleaning the house, doing the\nlaundry and cooking.")
print("A few moments later, you remember that you have to pay some\nbills. Also, your nephew has his birthday today and you haven'n\nbought a gift for him. However, there is a very special offer\nfor a videogame you really love and you don't want to miss it.\nWhat do you do?\n")
print("1. Spend money on bills and gift.\n2. Spend money on videogame.")
answer = int(input())
for i in range(30):
    print("\n")
money_waste = 0
if(answer == 2):
    money_waste = 1
print("You get ready and go outside. You live many blocks away from\nthe city centre so you have to catch the bus! When you arrive\nat the bus stop, you see your bus leaving and realise that you\ncan't wait 3 hours for the next one. What do you do?\n")
print("1. Get back home.\n2. Go on foot.")
answer = int(input())
for i in range(30):
    print("\n")
giving_up = 0
if(answer == 1):
    giving_up = 1
    print("You are unlucky this time but don't worry. You can finish these\nobligations tomorrow. Anyway, your wife isn't home so no one\nknows what you 've been doing all day. If they ask you, you\ncan say that you were tired from work. Hehe!")
else:
    print("You start walking to the city centre. The distance is long but\nthis is the best you can do to proof to yourself that you are\na responsible person. Especially after the morning event!\n\nHalf an hour later, you arrive at the bank.")
    if(money_waste == 0):
        print("You make some payments and find a clothes store for your\nnephew's gift. After that, you bump into one of your friends,\nChris. You have a small talk and he offers to drive you home.")
    else:
        print("You supply your pockets with cash and run to the videogame shop\nto obtain the offer! On your way home, you bump into one of your friends,\nChris. You have a small talk and he offers to drive you home.")
print("\n\nTime is almost 19:30 and you have nothing to do. How are you\ngoing to spend the rest of your day?\n")
print("1. Go to the gym.\n2. Visit the girl next door and...ask for sugar!")
answer = int(input())
for i in range(30):
    print("\n")
cheating = 0
if(answer == 1):
    print("You finally do something good for yourself! Last time you went\nto the gym was ages ago and you must excersise more if you want\nto lose weight. Your time at the gym has finished and you get\nback home tired. You drink a glass of milk and go to bed early\nto avoid sleeping until late again!")
else:
    cheating = 1
    print("You take advantage of the fact that your wife isn't home and\ncan't imagine something better than visiting your neighbour.\nShe's a 25-year-old woman (9 years younger than you) and she's\nsingle this period. You knock on her door and she opens it wide\nopen, as she always does! (hehe)\n\nYou get inside with the excuse of needing sugar for the cake\nyou are making. She laughs jokingly and then she asks you to\ntake a look at her bedroom television because 'it broke down'...\nYou find out that the antenna wire wasn't connected and you fix\nit easily and in no time! She says 'Thank you' and rewards you\nwith a soft duration kiss. You respond and you end up sleeping\ntogether. Let's hope you will get up early the next morning!!!")
print("\n\nEND OF THE STORY. Press ENTER to continue\n\n")
input()
print("Results and comments:\n\n")
if(call_answer == 0):
    print("Well... You didn't answer to the phone call from your boss and it\nmeans that you are scared to face the responsibility of your\nactions.")
else:
    print("First of, the fact that you answered the phone call from your\nboss means you were sure that your boss wouldn't just overlook\nthe morning event.")
    if(truth == 0):
        print("However, you are a liar because you told him that you got ill.\nIt was easy to tell the truth and he could forgive you if you\nnever did that again.")
    else:
        print("At least you told him the truth! He seemed angry with you, though.\nGood luck with that, bro!!!")
if(silliness == 1):
    print("The funny moment was that, when you chose to wake up while you\nwere already awake! Good one, bro... Gongratulations! Next time\nmake sure you read more carefully!")
if(sedulity == 0):
    print("Also, it's not enough that you didn't wake up for work... You\ndecide to spend all day sitting on the couch and watch TV! Don't\nyou have to do anything better with your life?")
else:
    print("Although you didn't wake up for work, you made a good decision\nand dealt with the housework. This would make your wife proud\nof you! (hehe)")
if(giving_up == 0):
    print("Surprisingly you wasn't terrified when you missed the bus and\nyou considered as a wrong move to give up and return home.")
else:
    print("Dude! Are you bored with your life? Why didn't you walk to the\ncity centre and get some fresh air? Missed the bus and gave up?\nYou need to excersise, man! Pull yourself together!")
if(money_waste == 0):
    print("I couldn't believe the fact that you chose to do your obligations!\nWas it really your option???")
else:
    print("What about the videogame? Was it in your basic needs? Your wife\nwill get upset if she finds out! Better hide it under your pillow!")
if(cheating == 0):
    print("Finally, you went to the gym! You have been avoiding it for 2 weeks!\nJust be careful with your diet. Can you imagine yourself as a\nbodybuilder?")
else:
    print("I was sure about your last answer! Your wife left you for the\nweekend, so LET'S PARTY!!! Bullshit! I'm gonna tell her the truth!\nNo more lies! You should have been more careful.")
print("\n\nOne last critical question... Is it 'SOUVLAKI' or 'KALAMAKI'?")
print("1. 'SOUVLAKI'\n2. 'KALAMAKI'\n")
answer = int(input())
if(answer == 1):
    print("Thank God!")
else:
    silliness = 999999
    print("\n\nGET OUTTA HERE YOU STUPID POT!!!!!!!")
print("\n\n(program finished)")
