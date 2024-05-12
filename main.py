print("Welcome Bro!")
name = input("Pls Can You Tpe Your Name?: ")
age = int(input("Now Age Pls: "))
tall = int(input("Now What's Your Tall: "))
print("Now Perfect!: ")
print(f"Name: {name}\nAge: {str(age)}\nTall: {str(tall)}")
print("Let's Play!")
ready = input("Are You Ready?: ")
if ready.lower() == "yes" or ready.lower() == "ready" :
    print("Good!")
    lev1 = input("""What's Oldest Country Ever
(A)-Egypt (B)-iraq (C)-USA (D)-Germany
                 """)
    if lev1.lower() == "iraq" or lev1.lower() == "b" :
        print("Correct! Next Question!")
    else : 
        print("Uncorrect! Your Score is 1!")
        lev2 = input("""Where Is BMW Made In?:
(A)-Egypt (B)-Germany (C)-USA (D)-Japen""")    
        if lev2.lower() == "germany" or lev2.lower() == "b" : 
            print("Correct! Next Question")
        else :
            print("Uncorrect! Your Score is 2!")
            lev3 = input("""What Is The Stronghest Country!: 
(A)-Egypt  (B)-Germany  (C)-USA (D)-Algria""")
            if lev3.lower() == "c" or lev3.lower() == "usa" or lev3.lower() == "united states from amarica" :
                print("Correct! Next Question")
            else :
                print("Uncorrect! Your Score is 3!")
                lev4 = input("""Witch Animal Is Forest King
(A)-Lion (B)-Elephant (C)-Rat (D)-Tiger """)
                if lev4.lower() == "a" or lev4.lower() == "lion" :
                    print("Correct! Next Question!")
                else:
                    print("Incorrect Your Score is 4!")
else :
    print("NP Just Come When You Are Ready!")