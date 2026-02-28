print("""
                         __,,,,_
          _ __..-;''`--/'/ /.',-`-.
      (`/' ` |  \ \ \\ / / / / .-'/`,_
     /'`\ \   |  \ | \| // // / -.,/_,'-,
    /<7' ;  \ \  | ; ||/ /| | \/    |`-/,/-.,_,/')
   /  _.-, `,-\,__|  _-| / \ \/|_/  |    '-/.;.\'
   `-`  f/ ;      / __/ \__ `/ |__/ |
        `-'      |  -| =|\_  \  |-' |
              __/   /_..-' `  ),'  //
          fL ((__.-'((___..-'' \__.'
""")

print("Welcome to Treasure Island.")
print("Your mission is to find treasure.")


first_step = input("left or right? ").lower()

if first_step == "left":
    second_step = input("swim or wait? ").lower()
    if second_step == "wait":
        third_step = input("red, yellow or blue? ").lower()
        if third_step == "red":
            print("You lost the game.")
        elif third_step == "yellow":
            print("You won the game.")
        elif third_step == "blue":
            print("You lost the game. ")
        else:
              print("You typed something incorrect.")  
    elif second_step == "swim":
        print("You lost the game.")
    else:
              print("You typed something incorrect.") 
elif first_step == "right":
    print("You lost the game.")
else:
    print("You typed something incorrect.")