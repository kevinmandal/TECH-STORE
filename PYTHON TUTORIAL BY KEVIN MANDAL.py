

print(" ")
print("~-~"*45)
print("                              P Y T H O N   T U T O R I A L   B Y : M A N D A L  K E V I N  P E R E Z")
print("~-~"*45)
print(" ")

Strt = input("Enter the word [START] to proceed :").upper()
print(" ")
if Strt == "START" :
   print("Hello welcome! (˙ᗜ˙)/")
   print("I'm Verity, your guiding assistant in this website.")
   print("This website have some basics PYTHON TUTORIAL, where you can learn")
   print("(BASIC SYNTAX, VARIABLES, DATA TYPES, AND ETC.)")
   print("Let's start your journey and have fun, but you must Enter your name first.")
   print(" ")

else :
    print("PLEASE ENTER [START].")
print("_-"*68)
print(" ")
Fn1 =input("First Name : ")
Fn2 =input("Last  Name : ")
print(" ")
print("_-"*68)
print(" ")
print(f"Hi {Fn1}, down below there's lessons waiting for you. You can able to choose")
print("whatever you want to learn. I'll put the code, decide either PICK or "
      "learn from chapter 1 - 5. You can")
print("see it down below. Also after you finished, you'll get a little simple quiz.")
print("That's all. GOOD LUCK! (◠‿◠).")
print(" ")
print("_-"*68)
print(" ")
print(">>>>>>>>>>>>> P Y T H O N   L E S S O N S <<<<<<<<<<<<<")
print(" ")
print("CHAPTER 1 (INTRODUCTION TO PROGRAMMING         ) - [1]")
print("CHAPTER 2 (PYTHON BASIC SYNTAX                 ) - [2]")
print("CHAPTER 3 (ARITHMETIC OPERATORS AND EXPRESSIONS) - [3]")
print("CHAPTER 4 (CONDITIONAL STATEMENT IN PYTHON     ) - [4]")
print("CHAPTER 5 (INTRODUCTION TO ITERATIONS AND LOOP ) - [5]")
print("\n>>>>>>>>>>>>>>>>>> T U T O R I A L <<<<<<<<<<<<<<<<<<<")
print(" ")
print("_-"*68)
print(" ")
pick = input("You want to learn step by step? or pick a lesson? (PICK/LSBS) : ").upper()
if pick == "PICK" :
   print(" ")

   print("*"*62)
   print(" ")
   print("That's great! it means you have experience already. ꒰ঌ(˶ˆᗜˆ˵)໒꒱")
   print(" ")
   print("*"*62)

   print(" ")
   choice = input("Choose Chapter 1 to 5 :")
   print(" ")

   print("_-" * 68)
   print("GOOD LUCK AND HAVE FUN! ദ്ദി*ˊᗜˋ*)")
   print("_-" * 68)
   print(" ")

   if choice == "1" :
      print("__________________________________________________________________________________________")
      print("|                                                                                        |")
      print("|      C H A P T E R   1    I N T R O D U C T I O N    T O    P R O G R A M M I N G      |")
      print("|________________________________________________________________________________________|\n")


      print("Do you have any idea what's programming language is? if not, PROGRAMMING LANGUAGE is a special language")
      print("that computers understand and use to perform task.(。•̀ᴗ-)✧\n")
      print("Anyways PYTHON PROGRAMMING is widely used around the world because it was easy to learn, simple and readable.")
      print("It was created by Guido Van Rossum in 1991.\n")
      print("What do you need to start python?\n")
      print("_________________________________________________________________________")
      print("|`````P R O F E S S I O N A L   I D E S / C O D E S   E D I T O R S`````|")
      print("|_______________________________________________________________________|")
      print("| PYCHARM BY JET BRAINS.                                                |")
      print("| VS CODE  (VISUAL STUDIO CODE).                                        |")
      print("| JUPYTER NOTEBOOK/JUPYTER LAB.                                         |")
      print("|_______________________________________________________________________|\n")
      print("That's all for Chapter 1.")
      print("Easy Right? RIGHTTTTTTTTTTTTTTTT?. ＼(ˇ∇ˇ)／\n")
      print("_-" * 68)
      print("                                                         _________________________    ")
      print("                    /|      _____          _____       |   |     |     |    | |  |   ")
      print("     ,-----,       /  |____/__|__|_    ___/__|__|___   |___|_____|_____|____|_|___|  ")
      print("  ,--'---:---`--, /  |  _     |     `| |      |      `| |                    | |    | ")
      print(" ==(o)-----(o)==J    `(o)-------(o)=   `(o)------(o)'   `--(o)(o)--------------(o)--'  ")
      print("`````````````````````````````````````````````````````````````````````````````````````")
      print("_-" * 68)
      print("========== L O A D I N G   P L E A S E   W A I T ==========................................................")
      print("_-" * 68)
      print(" ")
      quizc1 = input("Would you like to take a quiz? (YES/NO) :").upper()


      pass_score = 3
      if quizc1 == "YES":

          score = 0
          print("[------------------------------------------------------------------------]")
          print("| This quiz has 5 items. Write T if True. F if False.                    |")
          print("|________________________________________________________________________|")

          answer = input("1. Python is not part of special language/programming language. Answer :\n").upper()
          if answer == "F" :
           score += 1
          answer = input("2.Guido van Created python in 1992. Answer :\n").upper()
          if answer == "F" :
           score += 1
          answer = input("3.Python is readable, easy to learn and simple. Answer :\n").upper()
          if answer == "T":
           score += 1
          answer = input("4.Pycharm is one of the ides and professional code editors.Answer :\n").upper()
          if answer == "T":
           score += 1
          answer = input("5.Computers don't understand programming language. Answer :\n").upper()
          if answer == "F":
           score += 1

          print(" ")
          print("_-" * 68)
          print(" ")
          print(" __________________________________________________")
          print(" |   *************************                    |")
          print(f" |   *  You got {score} / 5!       *                    |")
          print(" |   *************************                    |\n")
          print(" |________________________________________________|")


          if score >= pass_score :

              print(" | Congrats! You passed the quiz! d-(^_^)z        |")
              print(" |________________________________________________|")
              print(" ")
              print("_-" * 68)
          else :
           print(" | You Failed, Keep Going! (9'-')9                |")
           print(" |________________________________________________|")
           print(" ")
           print("_-" * 68)
   elif choice == "2" :
       print("__________________________________________________________________________________________")
       print("|                                                                                        |")
       print("|      C H A P T E R   2    P Y T H O N   B A S I C   S Y N T A X                        |")
       print("|________________________________________________________________________________________|\n")

       print("What is SYNTAX.\n")
       print("SYNTAX refers to the set of rules that tells us how correctly write a program in Python.\n")
       print("=--PYTHON SYNTAX--=")
       print("These things is really important to understand, remember this. Python is case sensitive ")
       print("because python treats upper and lower case differently.Also Python need Indentation or called")
       print("spaces to define blocks of code.  <(-^,^-)=b \n")
       print("For example....\n")
       print("__________________________________________________________________________________________")
       print("|  Python Case Sensitive.                                                                |")
       print("|                                                                                        |")
       print("|  (1). name = 'Kevin'               (2). name = 'Kevin'                                 |")
       print("|       print(Name)                       print(name)                                    |")
       print("|                                                                                        |")
       print("|    The number  1 is wrong. Number 2 is correct. Why?                                   |")
       print("|    because even though the word NAME is same.                                          |")
       print("|    You can see that, 1 has lowercase variable storage.                                 |")
       print("|    But has upper case with print(Name).                                                |")
       print("|                                                                                        |")
       print("|    Keyword : If it's lower. It's lower. If it's upper. It's upper.                     |")
       print("|                                                                                        |")
       print("|  Indentations(Spaces).                                                                 |")
       print("|                                                                                        |")
       print("|   (1). age = 18                    (2). age = 18                                       |")
       print("|        if age >= 18 :                   if age >= 18 :                                 |")
       print("|          print('Adult')                 print('Adult')                                 |")
       print("|                                                                                        |")
       print("|   Number 2 is incorrect because it is not intended or he doesn't have spaces           |")
       print("|   to get inside the block. While number 1 has spaces that's why it's intended.         |")
       print("|                                                                                        |")
       print("|    Keyword: Use spaces and make sure it is align perfectly in your coding              |")
       print("|             to get intended.                                                           |")
       print("|________________________________________________________________________________________|\n")

       print("_-" * 68)
       print("."*136)
       print("_-" * 68)





