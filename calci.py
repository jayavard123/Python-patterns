select=int(input("select operation form :"))
number_1=int(input('Enter first number = '))
number_2=int(input('Enter second number = '))
if select == 1 :
     print(number_1 , "+" , number_2, "=", number_1+number_2)
elif select == 2 :
    print(number_1,"-",number_2, "=", number_1-number_2)
elif select == 3:
     print(number_1, "*",number_2, "=", number_1*number_2)
elif select == 4:
     print(number_1,"/",number_2, "=", number_1/number_2)
elif select==5:
     print(number_1,"%",number_2,"=",number_1%number_2)
else:
     print("Invalid input")
     
