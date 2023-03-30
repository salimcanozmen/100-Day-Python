print('''
          ,ad88ba,
        ,dP'    `Yb,
        8"        "8
        8          8
        8          8
        Y,        ,P
        `b        d'
         8        8
         8        8
         8aaaaaaaa8
        ,8aaaaaaaa8,
       ,dP        Yb,
      ,8P          Y8,
     ,dP            Yb,
    ,8P              Y8,
   ,dP                Yb,
  ,8P                  Y8,
  dP                    Yb
  8I                    I8,
 I8'                    `8I
 I8                      8I
 I8                      8I
 `8                      8'
  Yb                    dP
  `8b                  d8'
   `8baaaaaaaaaaaaaaaad8'
    `8baaaaaaaaaaaaaad8'
     `8b,          ,d8'
      `8b,        ,d8'
       `Y8baaaaaad8P'

''')
print("Welcome to Big Lebowski Memorial Bowling Center.")
print("Your mission is to win the local tournament so you can go to regionals.")
start = input("Press enter to start")
print("While you approach to the bowling alley what do you do;")
print("1- Give your opponents a dirty look to intimitade them.")
print("2- Focus on your game.")
karar1 = input("Type '1' or '2' to determine your action ")
if karar1 == "1":
    print("Your opponents begin to sweat after seeing your confidence. Now you should follow that look up with your performance, what do you do?")
    print("1- Throw a curveball to show your skills")
    print("2- Roll the ball over in the karpuzlama style")
    print("3- Put on a blindfold and assert your dominance")
    karar2 = input("Type 1,2 or 3 to determine your action ")
    if karar2 == "1":
        print("You don't have any skills, sorry you lose.")
        quit()
    elif karar2 == "2":
        print("Your opponents gasped as you strike in an unseen fashion.")
        etc = input("Press enter to continue")
        print("Your opponents striked aswell. What do you do now?")
        print("1- Continue your game as usual")
        print("2- Plant drugs on them and call the police")
        print("3- Pull out your gun and shoot them")
        karar3 = input("Type 1,2 or 3 to determine your action ")
        if karar3 == "1":
            print("You gay fuck, go play fortnite.")
            quit()
        elif karar3 == "2":
            print("Plan goes succesfully but next day they find your fingerprints on the bags and you go jail. You Lose.")
            quit()
        elif karar3 == "3":
            print("They killed Donny. You win the game but at what cost..")
            quit()
    elif karar2 == "3":
        print("Your opponents are to scared to play with you anymore after you strike with blindfols on. You won by default. Congratz")
        quit()

else:
    print("What are you? 12? Go play mario kart, this game is not for you scrub")
    quit()
