import random 
print("                            Welcome To NumberScrabble                          ")
def computer():
      print("who will start first 1-you or 2-computer")
      mm=int(input())
      if mm==1 :
          name=input("Enter your name: ")
          kk=[1,2,3,4,5,6,7,8,9]
          print(kk)
          a1=int(input(name+" choose number from list: "))
          while a1>=10 or a1<=0 :
               print("please enter anothor num:")
               a1=int(input())
          kk.remove(a1)
          print(kk)
          b1=random.choice(kk)
          print("Computer Turn: ",b1)
          kk.remove(b1)
          print(kk)
          a2=int(input(name+" choose number from list: "))
          while a2==a1  or a2==b1 or a2>=10 or a2<=0 :
               print("please enter anothor num:")
               a2=int(input(name+" choose number from list: "))
          kk.remove(a2)
          print(kk)
          b2=random.choice(kk)
          print("Computer Turn: ",b2)
          kk.remove(b2)
          print(kk)
          a3=int(input(name+"choose number from list: "))
          while a3==a1 or a3==a2 or a3==b1 or a3==b2 or a3>=10 or a3<=0:
              print("please Enter another num:")
              a3=int(input())
          kk.remove(a3) 
          print(kk)
          if (a1+a2+a3) == 15 :
             print("winner is "+name)
          else : 
               b3=random.choice(kk)
               print("Computer Turn: ",b3)
               kk.remove(b3)
               print(kk)
               if (b1+b2+b3)==15:
                   print("Computer win")
               else:
                   a4=int(input(name+"choose number from list: "))
                   while a4==a1 or a4==a2 or a4==a3 or a4==b1 or a4==b2 or a4==b3  or a4>=10 or a4<=0:
                       print("please Enter another num:")
                       a4=int(input())
                   kk.remove(a4) 
                   print(kk)
                   if  (a1+a2+a4) == 15 or (a1+a2+a4)==15 or (a1+a3+a4)==15:
                       print("winner is "+name)
                   else:
                       b4=random.choice(kk)
                       print("Computer Turn: ",b4)
                       kk.remove(b4)
                       print(kk)
                       if (b1+b2+b4)==15 or (b2+b3+b4)==15 or (b1+b3+b4)==15 :
                         print("Computer win")
                       else:
                           a5=int(input(name+"choose number from list: "))
                           while a5==a1 or a5==a2 or a5==a3 or a5==a4 or a5==b1 or a5==b2 or a5==b3 or a5==b4 or a5>=10 or a5<=0:
                                print("please Enter another num:")
                                a5=int(input())
                           kk.remove(a5) 
                           print(kk)
                           if  (a1+a2+a5) == 15 or (a1+a3+a5)==15 or (a1+a4+a5)==15 or (a2+a3+a5)==15 or (a2+a4+a5)==15 or (a3+a4+a5)==15: 
                              print("winner is "+name)
                           else:
                                print("Draw")
#--------------------------------------------------------------------------------------------------------------------------------                              
      elif mm==2:
           name2=input("Enter your name: ")
           l2=[1,2,3,4,5,6,7,8,9]
           print(l2)
           q1=random.choice(l2)
           print("Computer Turn: ",q1)
           l2.remove(q1)
           print(l2)
           c1=int(input(name2+" choose number from list: "))
           while c1>=10 or c1<=0 or c1==q1 :
               print("please enter anothor num:")
               c1=int(input())
           l2.remove(c1)
           print(l2)

           q2=random.choice(l2)
           print("Computer Turn: ",q2)
           l2.remove(q2)
           print(l2)
           c2=int(input(name2+" choose number from list: "))
           while c2>=10 or c2<=0 or c2==q1 or c2==q2 or c2==c1:
               print("please enter anothor num:")
               c2=int(input())
           l2.remove(c2)
           print(l2)

           
           q3=random.choice(l2)
           print("Computer Turn: ",q3)
           l2.remove(q3)
           print(l2)
           if (q1+q2+q3)==15:
               print("Computer win")
           else:
              c3=int(input(name2+" choose number from list: "))
              while c3>=10 or c3<=0 or c3==c1 or c3==c2 or c3==q1 or c3==q2 or c3==q3 :
                  print("please enter anothor num:")
                  c3=int(input())
              l2.remove(c3)
              print(l2)
              if (c1+c2+c3)==15:
                 print("winner is "+name2)
              else:
                  q4=random.choice(l2)
                  print("Computer Turn: ",q4)
                  l2.remove(q4)
                  print(l2)
                  if (q1+q2+q4)==15 or (q1+q3+q4)==15 or (q2+q3+q4)==15:
                    print("Computer win")
                  else:
                       c4=int(input(name2+" choose number from list: "))
                       while c4>=10 or c4<=0 or c4==c1 or c4==c2 or c4==c3 or c4==q1 or c4==q2 or c4==q3 or c4==q4  :
                            print("please enter anothor num:")
                            c4=int(input())
                       l2.remove(c4)
                       print(l2)
                       if (c1+c2+c4)==15 or (c1+c3+c4)==15 or (c2+c3+c4)==15:
                            print("winner is "+name2)
                       else:
                           q5=random.choice(l2)
                           print("Computer Turn: ",q5)
                           if (q1+q2+q5)==15 or (q1+q3+q5)==15 or (q2+q3+q5)==15 or (q2+q4+q5)==15 or (q3+q4+q5)==15 or (q1+q4+q5)==15 :
                               print("Computer win")
                           else :
                               print("Draw")
                            
 #--------------------------------------------------------------------------------------------------------------------------                      
                    
def twoplayer() :
  q = input("Enter your name player1 : ")
  c = input("Enter your name player2 : ")
  x = [1,2,3,4,5,6,7,8,9]
  print(x)
  a1=int(input(q+" choose number from list: ")) 
  while a1>=10 or a1<=0 :
     print("please enter anothor num:")
     a1=int(input())
  x.remove(a1)
  print(x)

  b1=int(input(c+" choose number from list: "))
  while a1==b1 or b1>=10 or b1<=0:
        print("Please Enter anothor num : ")
        b1=int(input())
  x.remove(b1)
  print(x)

  a2=int(input(q+" choose number from list: "))
  while a2==a1 or a2==b1 or a2>=10 or a2<=0:
     print("Please Enter anothor num: ")
     a2=int(input())
  x.remove(a2)
  print(x)
  b2=int(input(c+"choose number from list: "))
  while b2==a1 or b2==a2 or b2==b1 or b2>=10 or b2<=0:
      print("please Enter another num:")
      b2=int(input())
  x.remove(b2)
  print(x)
  a3=int(input(q+"choose number from list: "))
  while a3==a1 or a3==a2 or a3==b1 or a3==b2 or a3>=10 or a3<=0: 
     print("please Enter another num:")
     a3=int(input())
  x.remove(a3) 
  print(x)
  if (a1+a2+a3) == 15 :
      print("winner is "+q)
  else :
    b3=int(input(c+"choose number from list: "))
    while b3==a1 or b3==a2 or b3==a3 or b3==b1 or b3==b2 or b3>=10 or b3<=0 :
           print("please Enter another num:")
           b3=int(input())
    x.remove(b3)
    print(x)
    if (b1+b2+b3) == 15 :
              print("winner is "+c)
    else :
            a4 =int(input(q+"choose number from list: "))
            while a4==a1 or a4==a2 or a4==a3 or a4==b1 or a4==b2 or a4==b3 or a4>=10 or a4<=0 :
                 print("please Enter another num:")
                 a4=int(input())
            x.remove(a4)
            print(x)
            if (a1+a2+a4) == 15 or (a1+a3+a4)==15 or (a2+a3+a4)==15:
                   print ("winner is "+q)
            else :
                  b4 = int(input(c+"choose number from list: "))
                  while  b4==a1 or b4==a2 or b4==a3 or b4==a4 or b4==b1 or b4==b2 or b4==b3 or b4>=10 or b4<=0:
                      print("please enter another num: ")
                      b4==int(input())
                  x.remove(b4)
                  print(x)
                  if (b1+b2+b4)== 15 or (b1+b3+b4)==15 or (b2+b3+b4)==15:
                      print ("winner is :"+c)
                  else :
                       a5 = int(input(q+" choose number from list: "))
                       while a5==a1 or a5==a2 or a5==a3 or a5==a4 or a5==b1 or a5==b2 or a5==b3 or a5==b4 or a5>=10 or a5<=0:
                            print("please enter another num: "
                                )
                            a5=int(input())
                       x.remove(a5)
                       if (a1+a2+a5) == 15 or (a1+a3+a5)==15 or (a1+a4+a5)==15 or (a2+a3+a5)==15 or (a2+a4+a5)==15 or (a3+a4+a5)==15 : 
                           print("winner is "+q)
                       else :
                           print("Draw")


#---------------------------------------------------------------------------------------------------------
print("Do you want to player with 1-computer or 2-with your friend ?")
ll=input()
if ll==("1") :
  computer()
elif ll==("2") :
    twoplayer()
          
