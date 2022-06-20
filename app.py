
firstNum = 0
secondNum = 0

def calculate():

  firstNum = input('Enter first number: ')
  if(firstNum.endswith('$')):
    return
  elif(firstNum == '#'):
    print("Done. Terminating")
    exit()
  secondNum = input('Enter second number: ')
  if(secondNum.endswith('$')):
    return
  elif(secondNum == '#'):
    print("Done. Terminating")
    exit()

  try:
    firstNum = float(firstNum)
    secondNum = float(secondNum)
  except ValueError:
    print('Not a valid number,please enter again')
  except:
    print('Something Went Wrong')
  if(choice == '+'):
    result = firstNum + secondNum
  elif(choice == '-'):
    result = firstNum - secondNum
  elif(choice == '*'):
    result = firstNum * secondNum
  elif(choice == '/'):
    try:
        result = firstNum / secondNum
    except: 
        print('float division by zero')
        result = 'None'
  elif(choice == '^'):
    result = firstNum ** secondNum
  elif(choice == '%'):
    result = firstNum % secondNum
  
  print(str(firstNum) + ' ' + str(choice) + ' ' + str(secondNum) + ' = ' + str(result))


while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  if(choice == '#'):
    print("Done. Terminating")
    exit()
  elif(choice == '$'):
    continue
  elif(choice == '+' or choice == '-' or choice == '*' or choice == '/' or choice == '^' or choice == '%'):
    calculate()
  else:
    print('Unrecognized operation')
