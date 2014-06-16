isbn =" "

while (len(isbn)!=10):
    isbn=raw_input("please enter 10 digit number")
  

Digit1=int(isbn[0])*11
Digit2=int(isbn[1])*10
Digit3=int(isbn[2])*9
Digit4=int(isbn[3])*8
Digit5=int(isbn[4])*7
Digit6=int(isbn[5])*6
Digit7=int(isbn[6])*5
Digit8=int(isbn[7])*4
Digit9=int(isbn[8])*3
Digit10=int(isbn[9])*2
Result=(Digit1+Digit2+Digit3+Digit4+Digit5+Digit6+Digit7+Digit8+Digit9+Digit10)
Remainder=Result%11
Digit11=11-Remainder
if Digit11==10:
   Digit11='X'
isbnNumber=str(isbn)+str(Digit11)
print('Your 11 digit isbn Number is ' + isbnNumber)
