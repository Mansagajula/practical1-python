fh=open('output1.txt','w')

temp=int(input("""Select your choice to enter the temperature   in respected degree 1.Farhenheit
                                   2.Celsius  : """))

if temp  == 1  :
    ce=int(input("Enter the temp in Fahrenheit:"))
    C=(ce-32)*5/9
    print(C, "Degrees  celsius") 
    fh.write(f'{str(C)} degree farenheit')
elif temp == 2 :
    fa=int(input("Enter the temp in Celsius : "))
    F=(9/5)*fa+32
    print(F," DEGREES  FARENHEIT")
    fh.write(f'{str(F)} degree celcius')
else :
    print( )


fh.close()

