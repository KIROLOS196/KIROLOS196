def kirchhoff_equation():
  while True:   
    def solve_equation(law, inputs):
        if law == 'KCL':
            Iin = inputs[0]
            Iout = inputs[1]
            if 'I1' in Iin:
                if 'I3' not in Iin and Iout:
                    print(Iin + '-' + Iout + '+0I3' + '=', 0)
                elif 'I3' in Iout:
                    print(Iin + '-' + Iout + '=', 0)
                elif 'I3' in Iin:
                    print(Iout + '-' + Iin + '=', 0)
            elif 'I1' in Iout:
                if 'I3' not in Iout and Iin:
                    print(Iout + '-' + Iin + '+0I3' + '=', 0)
                elif 'I3' in Iout:
                    print(Iout + '-' + Iin + '=', 0)
                elif 'I3' in Iin:
                    print(Iout + '-' + Iin + '=', 0)
        elif law == 'KVL':
            VB = inputs[0]
            IR = inputs[1]
            print(VB + ' = ' + IR)
        else:
            print('ERROR 404 NOT FOUND')

    Law = input('do you want KCL or KVL or KVL2 or KVL IR:')
    if Law == 'KCL':
        I = ['Iin', 'Iout']
        for i in range(2):
            I[i] = input('SEGMA ' + I[i] + ' = ')
        solve_equation(Law, I)
    elif Law == 'KVL':
        VB = input('SEGMA VB = ')
        IR = input('SEGMA IR = ')
        solve_equation(Law, [VB, IR])
    elif Law=="KVL2":    
        VB = input('SEGMA VB = ')
        IR = input('SEGMA IR = ')
        solve_equation(Law, [VB, IR])
    elif Law=="KVL IR":
        I=float(input('enter I(current):'))
        R=float(input("enter R (resistance):"))
        VB=(I*R)
        print(f"VB={VB}")
    else: 
        print ("EROR")
    complete=(input("do you want to solve an equation(yes or no)"))     
    if complete=="yes":
        def calculate_expression(x,x2,x3,y,y2,y3,z,z2,z3,a,a2,a3,b,b2,b3,c,c2,c3,d,d2,d3,n):
         return a*x + b*y + c*z - d*n
         return a2*x2 + b2*y2 + c2*z2 - d2*n
         return a3*x3 + b3*y3 + c3*z3 - d3*n
        x = float(input("Enter the value of x: "))
        x2= float(input("Enter the value of x: "))
        x3 = float(input("Enter the value of x3: "))
        y = float(input("Enter the value of y: "))
        y2 = float(input("Enter the value of y2: "))
        y3 = float(input("Enter the value of y3: "))
        z = float(input("Enter the value of z: "))
        z2 = float(input("Enter the value of z2: "))
        z3 = float(input("Enter the value of z3: "))
        a = float(input("Enter the coefficient of x (a): "))
        a2 = float(input("Enter the coefficient of x (a2): "))
        a3 = float(input("Enter the coefficient of x (a3): "))
        b = float(input("Enter the coefficient of y (b): "))
        b2 = float(input("Enter the coefficient of y (b2): "))
        b3 = float(input("Enter the coefficient of y (b3): "))
        c = float(input("Enter the coefficient of z (c): "))
        c2 = float(input("Enter the coefficient of z (c2): "))
        c3 = float(input("Enter the coefficient of z (c3): "))
        d = float(input("Enter the coefficient of n (d): "))
        d2 = float(input("Enter the coefficient of n (d2): "))
        d3 = float(input("Enter the coefficient of n (d3): "))
        n = float(input("Enter the constant term (n): "))

        result = calculate_expression(x,x2,x3,y,y2,y3,z,z2,z3,a,a2,a3,b,b2,b3,c,c2,c3,d,d2,d3,n)


        print("The result of the expression is: ", result)   
    elif complete=="no":
        print("thanks for using ")
        break
    else:
       print("Invalid input!, Please enter 'Yes' or 'No'")

def circuit_breaker_equation():
  while True:
      power = float(input("Enter the power: "))
      voltage = float(input("Enter the voltage: "))
      power_factor = float(input("Enter the power factor: "))
      device = input("Enter the device: ").lower()
      I_Overload = float((power / (voltage * power_factor)) * 1.25)
    
      if device == "ac":
          I_Overload *= 2
      if I_Overload > 1 and I_Overload < 15:
          print("8 Ampere MCB circuit breaker")
          print("1.5 mm^2 CU cable")
      elif I_Overload >= 15 and I_Overload < 21:
          print("15 Ampere MCB circuit breaker")
          print("2.5 mm^2 CU cable")
      elif I_Overload >= 21 and I_Overload < 29:
          print("20 Ampere MCB circuit breaker")
          print("4 mm^2 CU cable")
      elif I_Overload >= 29 and I_Overload < 38:
          print("30 Ampere MCB circuit breaker")
          print("6 mm^2 CU cable")
      elif I_Overload >= 38 and I_Overload < 53:
          print("40 Ampere MCB circuit breaker")
          print("10 mm^2 CU cable")
      elif I_Overload >= 53 and I_Overload < 71:
          print("60 Ampere MCB circuit breaker")
          print("16 mm^2 CU cable")
      elif I_Overload >= 71 and I_Overload < 92:
          print("80 Ampere MCB circuit breaker")
          print("25 mm^2 CU cable")
      elif I_Overload >= 92 and I_Overload < 146:
          print("125 Ampere MCB circuit breaker")
          print("50 mm^2 CU cable")
      elif I_Overload >= 146 and I_Overload < 160:
          print("150 Ampere MCB circuit breaker")
          print("70 mm^2 CU cable")
      elif I_Overload >= 160 and I_Overload < 400:
          I_Overload /= 3
          print("3 phase MCB circuit breaker")

      back = input("Do you want to go back to the main page? (Yes/No): ").lower()
      if back == "yes":
        break
      elif back == "no":
        continue
      else:
          print("Invalid input!, Please enter 'Yes' or 'No'")

  return I_Overload

print("Welcome in my task, (Kirchoff & Circuit Breaker)")
while True:
  print("1.Kirchhoff's Equation")
  print("2.Circuit Breaker Equation")
  print("3.Credits")
  print("4.Exit")
  choice = input("Enter your choice from 1 to 4: ")
  if choice == "1":
    print("#Kirchhoff's Equation!")
    kirchhoff_equation()
    print("-"*30)
    
  elif choice == "2":
    print("#Circuit Breaker Equation!")
    circuit_breaker_equation()
    print("-"*30)

  elif choice == "3":
    print("-"*31)
    print("| Kirollos Salah elmeshatshat |")
    print("-"*31)
    
  elif choice == "4":
    print("Thank you for trying our application!")
    break 
  else:
    print("Invalid choise!, please enter a number from 1 to 4")