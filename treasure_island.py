print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print('''
________________________________________________________________________
|: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : |
|__________ : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :|
|__]\% % % | : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : |
|___]\% % %|: :______ : : : : : : : : : : : : : : : : : : : : :___: : : :|
|____]\% % | :|======| :_: : : : : : . : : : : : :_: : : : : :/   \: : : |
|_____]\% %|: ||\|||||:/_\: :,: : :.'o'.: : :,: :/_\: : : : :|//   |: : :|
|______]\% | :|======| =|= __#_____|___|_____#__ =|= : : : : | ,*, | : : |
|_______]\%|: |______|: ^ :[___]           [___]: ^ : : : : : \*;*/ : : :|
|________]\| :|__  __| : : [_|_] o  `(,  o [_|_] : : : : :_____(_)_____: |
|_________]\: | .||. |: : :[___] |  ( )  | [___]: : :_!_: ||   .|.   || :|
|__________]==|__||__|====_[_|_]/!\_@@@_/!\[_|_]_===/___\=||____|____||==|
     _                    '====================='     | _                |
    |_)         __.;;.__      _______________         |( |               |
    /_\__      / ;(;;); \    (               )       _|_)|               |
  ~=_|_ _)====/__________\==(\               /)=====(____|========~      |
 ~=|___|LL====|==========|===|               |======LLLLLL=========~     |
~============================|_______________|======================~    |
=============================LLLLLLLLLLLLLLLLL=======================~   |
lc====================================================================~  '
 ''')
print('''You wake up in a dark room.\n"Ah, where am I?" you whisper to yourself, your voice echoing in the emptiness. Your hands brush against a light switch, and with a flick, the room is bathed in soft illumination. In the center of the room, you spot a wooden table with three cards placed neatly.\n
There are three cards - "Lucia", "The Color Purple", "The Story of an Hour".
Choose one card!''')
lr = input()
print('''
          ______________________________________
                               |                                      |
                    _.---------|.--.                                  |
                 .-'  `       .'/  ``                                 |
              .-'           .' |    /|                                |
           .-'         |   /   `.__//                                 |
        .-'           _.--/        /                                  |
       |        _  .-'   /        /                                   |
       |     ._  \      /     `  /                                    |
       |        ` .    /     `  /                                     |
       |         \ \ '/        /                                      |
       |        - \  /        /|                                      |
       |        '  .'        / |                                      |
       |          '         |.'|                                      |
       |                    |  |                                      |
       |                    |  |______________________________________|
       |                    |.'
       |                    /
       |                   /
       |                  /
       )                 /|
    .A/`-.              / |
   AMMMA. `-._         / /
  AMMMMMMMMA. `-.     / /
 AMMMMMMMMMMMMA. `.    /
AMMMMMMMMMMMMMMMMA.`. /
MMMMMMMMMMMMMMMMMMMA.`.
MMMMMMMMMMMMMMMMMMMMMA.`.
MMMMMMMMMMMMMMMMMMMMMMMA.
MMMMMMMMMMMMMMMMMMMMMMMMMA.
MMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMV'
''')
str="Your answer is correct! Now you have unlocked the hidden door to the Room of Freedom"
if lr.lower() == "lucia":
  print("In recent years, we've seen significant advancements in women's rights and gender equality. What are some key achievements and milestones in the journey toward women's progress, and what challenges and areas of improvement still remain?")
  print('''A) Increased representation of women in political leadership roles and decision-making positions.
B) The #MeToo movement and increased awareness of issues related to sexual harassment and assault.
C) Achievements in closing the gender pay gap and promoting workplace equality.
D) Progress in expanding access to education and healthcare for women and girls.
E) All of the above.
Choose one option\n''')
  ans1 = input()
  if ans1=='E':
    print(str+"\n")
    print("You entered the room. There are two persons in the room looking at you. You ask them for the way out. They remain silent. \nOne of them tells you to enter the card name in this lock. The other person puts a box on the table with a lock.")
    input("Press any button to open the box")
    print("You enter - 'LUCIA'. The box opens and you find a note!\n")
    print("In the grand narrative of progress, you shine as the enlightened one. Your response to the question about women's progress is a brilliant chapter, showcasing your deep understanding of a fairer world's journey.\nYour knowledge is a guiding light, illuminating the path to a more just future. Congratulations on your wisdom and dedication to this brighter tomorrow! 🌟🌍📖\nYou are worthy of this treasure.\nYou recieve the treasure! You won.")
    print('''    __ .-~-.   .~``~,._
              .~  `     \ /     .  `\
              |     \    |   .'     |
        _      \     `.  |  /    __/
     .~` `'. .--;.       ,.O  -~`   `\
     \  '-. |     `-  o.O/o, __       |
      '-.,__ \    .-~' `\|o `  ~.    /_
        _.--'/   `    ,  /  \        | `~-.,
       /     |       /  :    '._    / -.    `\
      /   .-' '.___.;   `      \`--'\    `    |
     |          /    \         /     '.__,.--,/
     '--..,___.'      `~--'--~'
''')
  else:
    print("You lose! Is this all you've got?...")
elif lr.lower() == "the color purple":
  print("What are some of the key factors that hinder women's career advancement in India?")
  print('''A) Gender bias and discrimination in hiring and promotions.
B) Limited access to mentorship and role models.
C) Favorable government policies and initiatives promoting gender equality.
Choose one option\n''')
  ans2 = input()
  if ans2=='A':
    print(str+"\n")
    print("You entered the room. There are two persons in the room looking at you. You ask them for the way out. They remain silent.\nOne of them tells you to enter the card name in this lock. The other person puts a box on the table with a lock.")
    input("Press any button to open the box")
    print("You enter - 'PURPLE'. The box opens and you find a note!")
    print('''You've shown a deep understanding of the challenges women face in their careers in India. By correctly identifying 'Gender bias and discrimination in hiring and promotions' as a key hindrance to women's career advancement, you've demonstrated your awareness of these critical issues. Your knowledge and recognition of these challenges are essential steps toward creating a more inclusive and equitable workplace. Keep championing the cause of gender equality, and your efforts will undoubtedly contribute to positive change. Well done, and thank you for your commitment to a brighter, fairer future for all! 🚀💪🙌
    You are worthy of this treasure.
    You recieve the treasure! You won.
    
       ___
     /  /|
    /__/-
    /     |\
   |      | \
    \      \ \
    /       | >  **@
    \       / \\*''*
     \     /     )|
      | | |     /  \
      | | |      ||
       - --'
''')
  else:
    print("You lose! Is this all you've got?...")
else:
  print("What is the true nature of freedom, and how does it manifest in individuals' lives?")
  print('''A) Freedom is the ability to make choices and decisions without external constraints, allowing individuals to pursue their desires and dreams.
B) Freedom can be both a source of empowerment and a burden, as it comes with the responsibility of making choices and facing consequences.
C) Freedom is a societal construct that varies across cultures and eras, shaping individuals' lives differently in different contexts.
D) Freedom is a fundamental human right that should be protected and promoted to ensure individual autonomy and well-being.
E) Freedom is a double-edged sword, as it can lead to both personal fulfillment and societal conflicts.
Choose one option\n''')
  ans3 = input()
  print(str+"\n")
  print("You entered the room. There are two persons in the room looking at you. You ask them for the way out. They remain silent.\nOne of them tells you to enter the card name in this lock. The other person puts a box on the table with a lock.")
  input("Press any button to open the box")
  print('''You enter - 'HOUR'. The box opens and you find a note!
  Your perspective on the nature of freedom is greatly appreciated. The concept of freedom is indeed multifaceted, and your response reflects a thoughtful understanding of its complexities.

Your willingness to contemplate and discuss this important topic adds to the rich tapestry of ideas and beliefs that shape our understanding of freedom. Keep exploring and sharing your insights, as they contribute to meaningful conversations and greater awareness.

Thank you for your thoughtful response and your engagement with this profound concept! 🌟🤔🗨️
You are worthy of this treasure.
You recieve the treasure! You won.''')
  print('''                                              
                                   :--:+*+*=                          
                          .-=-=*+*#=:-%=   *=                         
                         .#-.+#  :%-..#-...*+                         
                         :%. -#  .*+--====--*+                        
                         :%-.+#:.=##=:       *+                       
                         :%==-:==-.-==+**+-  :#.                      
                         :%.          +*-.    #=                      
                         :%.         -#       +*                      
                          #=                .+*.                      
                     +-   .#-              =*:   :+.                  
                     .=+.  .#*-           +=   .++.                   
                  -=:. :+. .#:-++        =*    +:  :=-                
                   .-+.    .%.           #-      .+-:                 
                           .#.          .%.                           
                   .=*+:   .#.          .%.   .+*=.                   
                  :#-:.    .#.          .%.    .:-#-                  
            .-+==:+##=:-++ .#:          .%. ++-:=##+:-==-.            
         :=+=::=*#=:=+=-.   +.           +    -=+=:=#*=::=+=:         
       -*-.  .-:=#.                                .#=:-.  .-*-       
       *+   .=*+-                                    -+*=:   =*       
       .+*+*=:                                          :=*+++.   ''')

