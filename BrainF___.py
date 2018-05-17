__author__ = 'Alejandro Rodriguez-Perez'
#BBrainF*** is an easy program design to test the limits ,it was not made with usefulness in mind
#it sole purpose id to challenge the person coding .BrainF*** has 7 commands an 8 characters
#imagine cells ,you have a "unlimited" amount of cells you start at cell#0 with a value of 0 .the
#">"character moves the "pointer" one cell to the right the"<" moves the "pointer" one cell to the
#leftthe "+" character adds one to the cell the pointer is pointing at .the"-" character
#subtracts 1 to the cell the pointer is pointing at.each cell represents a byte so the top number
#is 255 so if the cell is at 255 and you add one it will go back to 0 and if the cell is at 0 it
#will go to 255.the"."character prints out the character corresponding to that cells ascii
#value,so if the cell has a value of 104 it will print out an "h" .the "," character is for
#input ,it adds the input in the ascii value so if the user types an "h" it will count it as
#104.the "[" and"]" are a loop.they will continue the operation until a number is equal to 0
#example
# +++++ +++++                        set cell 0 =to 10
# [                                  start loop
# >+++++ ++                          move to cell#1 and add 7
# >+++++ +++++                       move to cell#2 and add 10
# >+++                               move to cell#3 and add 3
# >+                                 move to cell#4 and add 1
# <<<<-                              move to cell#0 and subtract 1 (this changes a variable and starts the loop again until cell#0 equals 0)
# ]                                  end loop
# >++.                               move to cell#1,add 2 and print the character with that ascii value "H"
# >+.                                move to cell#2,add 1 and print the character with that ascii value "e"
# +++++ ++.                          add 7 to cell#2 and print the character with that ascii value "l"
# .                                  print the character corresponding with the ascii value of cell#2 "l"
# +++.                               add 2 to cell#2 and print the character with that ascii value "o"
# >++.                               move to cell#3,add 2 and print the character with that ascii value " "
# <<+++++ +++++ +++++.               move to cell#1,add 15 and print the character with that ascii value "W"
# >.                                 move to cell#2 and print the character with that ascii value "o"
# +++.                               stay in cell#2,add 3 and print the character with that ascii value "r"
# ----- -.                           stay in cell#2,subtract 6 and print the character with that ascii value "l"
# ----- ---.                         stay in cell#2,subtract 8 and print the character with that ascii value "d"
# >+.                                move to cell#3,add 1 and print the character with that ascii value "!"

#actua code:
pointer=0                                               #the position of the pointer in the cells
cells=[0]                                               #the cells are individual components in a list
step=0                                                  #wich step of the code it is in
hold=0                                                  #just holds onto thins for single use
code=input("What would you like me to enterpret?")      #ya'know the ACTUAL code 'n stuff
clen=int(len(code))                                     #the lenght of the code (for loop reasons 'n stuff like that)
loop=0                                                  #this is to see of there are nested loops like:[[[]]]
while(step<clen):                                       #so you dont have more steps than you have instuctions
   if(code[step]=="<"):
      if(pointer==0):                                  #imagine going to one end of a room and someone telling you to go further , doesn't wotk righ?
          print("sorry, you cant go back any more")
          quit()
      else:
          pointer-=1
   elif(code[step]==">"):
       pointer+=1
       cells.append('0')                               #so you dont run out of cells , you're welcome
   elif(code[step]=="+"):
       if(cells[pointer]=="255"):                      #like i said , bytes can only go up to 255
           cells.pop(pointer)
           cells.insert(int(pointer),'0')
       else:
           hold=int(cells[pointer])+1                  #adds 1 to that cells spot
           cells.pop(pointer)
           cells.insert(pointer,int(hold))
           hold=0                                      #it's 1 am and im really tired so ya'll better apretiaate this
   elif(code[step]=="-"):
       if(cells[pointer]=="0"):                        #also like i explaned with all the byte stuff 0-1=255
           cells.pop(pointer)
           cells.insert(int(pointer),'255')
       else:
           hold=int(cells[pointer])-1
           cells.pop(pointer)
           cells.insert(pointer,int(hold))
           hold=0
   elif(code[step]=="."):
       print(chr(cells[pointer]), end='')
   elif(code[step]==","):
       hold=input('type EXACTLY ONE character')        #PLEASE only put one character , don't break my code
       cells.pop(pointer)
       cells.append(pointer,hold)
   elif(code[step]=="["):                              #oh boi loops, sum fun stuff
       if(cells[pointer]==0):                          #so the "loop"variable keeps count of the nested loops(see line 82)
           step+=1                                     #if you dont move one then the code will get mixed up becuse it will count the opening loop
           while(step<clen):                           #line 42
               if(code[step]==']'and loop==0):         #when the "loop" variable is 0 it means the it has found its matching loop symbol think of it like if opening loops are +1 and closing loops are -1 , if the sum of them equals 0 then there is an equal amout of each one
                   break
               elif(code[step]=='['):                  #it adds 1 when it sees another opening loop(see line 84)
                   loop+=1
               elif(code[step]==']'):                  #then it subtracts 1 when it sees a closing loop (see line 80)
                   loop-=1
               step+=1                                 #what would happen if pinocchio(yes i had to google his name)saind "my nose will grow"?
   elif(code[step]=="]"):                              #same stuff but in somewhat reverse
       if(cells[pointer]!=0):                          #'cuz if it IS 0 then you dont need to go trough this becuse you already found the pair
           step-=1                                     #pretty much the same as line 78
           while(step>=0):                             #so you dont do the wall metaphor(line 44)
               if(code[step]=='[' and loop==0):        #this means you have found the pair
                   break
               elif(code[step]==']'):                  #same thing as before exept flippy flopped
                   loop+=1
               elif(code[step]=='['):                  #this too , it flippy floped so now the opening brachets are -1 and the closing brachets are +1
                   loop-=1
               step-=1
   step+=1                                             #if you see any typos its becuse it now is 2 am soo yeah
