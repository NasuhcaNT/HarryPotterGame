
F="yes"
while F=="yes" or F=="y" or F=="Y":
     
     U=W=N=raw_input("what is your name?:")
     S=Y=":"

     print N,"you have to answer the Q. only yes(y) or no(n)"
     if N=="nasuhcan" or N=="Nasuhcan" or N=="NASUHCAN" or N=="NasuhcaN" or N=="nasuh" or N=="Nasuh":
         print "You are my originator Welcome to back",N
         N="my originator"

     A=raw_input("do you have a nose? "+ N)
     if A=="yes" or A=="y" or A=="of course" or A=="why not" or A=="Y" :
              B=raw_input("do you have a beard? "+W)
              if B=="yes" or B=="y" or B=="Y":
                 C=raw_input("are you fat? "+U)
                 if C=="yes" or C=="y" or C=="Y":
                     print"you are hagrid"
                     F=raw_input("devam mi yes or no:")
                 else:
                     print"hello prof.dumbledore"
                     F=raw_input("devam mi yes or no:")
              else:
                 D=raw_input(N+" do you have frends?:")
        
                 if D=="yes" or D=="y" or D=="Y":
                     E=raw_input("can you do magic?"+Y)
                     if E=="yes" or E=="Y" or E=="y":
                         F=raw_input("really?:")
                         if F=="yes"or F=="y" or F=="Y":
                             H=raw_input("What is the hair color?:(red/blond/black)"+S)
                             if H=="black"or H=="bla":
                                  
                                 K=raw_input("Are u student?:")
                                 if K=="yes" or K=="y":
                                     print"you are harry potter and this great :D"
                                     F=raw_input("play again? yes or no:")
                                 else:
                                     print N,"you are not",N,"you are prof.Snape"
                                     F=raw_input("play again? yes or no:")
                             elif H=="red" or H=="orange" or H=="r":
                                 print"you are ron weasley"
                                 F=raw_input("play again? yes or no:")
                             elif H=="yellow" or H=="blond" or H=="blo":
                                  L=raw_input("What is Your sex? Female(f) or Male(m):")
                                  if L=="male" or L=="m":
                                      O=raw_input("Are you father(f)?:")
                                      if O=="father" or O=="f":
                                          print "you are Lucius Malfoy"
                                          F=raw_input("play again? yes or no:")
                                      else:
                                          print"you are Draco Malfoy"
                                          F=raw_input("play again? yes or no:")
                                  else:
                                      print "Hello luna. You are luna Lovegood"
                                      F=raw_input("play again? yes or no:")
                             else:
                                 print"you are Prof. Quirrell"
                                 F=raw_input("play again? yes or no:")
                         else:
                             print"damit you are a muggle"
                             F=raw_input("play again? yes or no:")
                     else:
                        print"damit",N,"are a muggle"
                        F=raw_input("play again? yes or no:")
                 else:
                     print "oh my sweety you are hermione"
                     F=raw_input("play again? yes or no:")
     else:
        print str(N),"are voldemort o.o",N
        F=raw_input("play again? yes or no:")
print "BYE BYE"*30
