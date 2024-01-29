print("""
  ____               __         __  _       ____     __            
 / __ \__ _____ ____/ /______ _/ /_(_)___  / __/__  / /  _____ ____
/ /_/ / // / _ `/ _  / __/ _ `/ __/ / __/ _\ \/ _ \/ / |/ / -_) __/
\___\_\_,_/\_,_/\_,_/_/  \_,_/\__/_/\__/ /___/\___/_/|___/\__/_/   
                                                                   

 This program will work with any quadratic equation in the form ax²+bx+c , ax²+bx or ax²+c where 
 x is an unknown and a,b and c are known INTEGER values that the user will input below. If there is no b 
 or c value in your equation, simpily input 0. The 'a' value cannot equal zero.

 Form: ax²+bx+c
""") 

b_val = 0
c_val = 0

a_val = int(input(" 'a' value: "))                         # a value info
if a_val == 0:
    print("The 'a' value cannot be zero.")
    print("")
    while a_val == 0:
        a_val = int(input(" 'a' value: "))
        if a_val == 0:
            print("The 'a' value cannot be zero.")
print("")

b_val = int(input(" 'b' value: "))                         # b value info   ### int needs fixed
print("")

c_val = int(input(" 'c' value: "))                         # c value info
print("")

if b_val != 0 and c_val != 0:
    if b_val < 0 and c_val < 0: 
        print(str("Your equation: ") + str(a_val) + str("x²") + str(b_val) + str("x") + str(c_val)) 
    elif b_val > 0 and c_val > 0:
        print(str("Your equation: ") + str(a_val) + str("x²+") + str(b_val) + str("x+") + str(c_val))
    elif b_val < 0:
        print(str("Your equation: ") + str(a_val) + str("x²") + str(b_val) + str("x+") + str(c_val))
    elif c_val < 0:
        print(str("Your equation: ") + str(a_val) + str("x²+") + str(b_val) + str("x") + str(c_val))  
elif c_val == 0:
    if b_val > 0:
        print(str("Your equation: ") + str(a_val) + str("x²+") + str(b_val) + str("x"))
    elif b_val < 0:
        print(str("Your equation: ") + str(a_val) + str("x²") + str(b_val) + str("x"))
elif b_val == 0:
    if c_val > 0:
        print(str("Your equation: ") + str(a_val) + str("x²+") + str(c_val))
    elif c_val < 0:
        print(str("Your equation: ") + str(a_val) + str("x²") + str(c_val))
print("")

root_val = (b_val**2 - 4*a_val*c_val)           # 'root' refers to the square root in quadratic formula
if root_val < 0:
    zero_one = str("DNE") 
    zero_two = str("DNE")
if root_val >= 0:
    zero_one = (-b_val + root_val**0.5)/(2*a_val)
    zero_two = (-b_val - root_val**0.5)/(2*a_val)

if root_val >= 0:
    zero_one = round(zero_one, 3) 
    zero_two = round(zero_two, 3)
    print("  Zeros")
    print("")
    if zero_one != zero_two:
        print("x = " + str(zero_one))
        print("x = " + str(zero_two))
    elif zero_one == zero_two:
        print("x = " + str(zero_one))
    print("")
elif root_val < 0:
    print("There are no roots")
    print("")

if root_val > 0:
    vertex_x = (zero_one + zero_two)/2 
    vertex_y = ((vertex_x**2) * a_val) + (vertex_x * b_val) + c_val     # works for fx with zeros
    vertex_x = round(vertex_x, 3)
    vertex_y = round(vertex_y, 3)
    print("Vertex: (" + str(vertex_x) + "," + str(vertex_y) + ")")
    print("")
if root_val < 0:                                                        # works for fx without zeros
    vertex_x = -b_val/(2*a_val) 
    vertex_y = (vertex_x**2)*a_val + (vertex_x*b_val) + c_val
    vertex_x = round(vertex_x, 3)
    vertex_y = round(vertex_y, 3)
    print("Vertex: (" + str(vertex_x) + "," + str(vertex_y) + ")")
    print("")

if c_val == 0:
    print("Y-Intercept = 0")
else:
    print("Y-Intercept = " + str(c_val))
print("")

a_der = a_val * 2 
b_der = b_val  
# c_der will always be zero

if b_val != 0:
    if b_val > 0:
        derivative = str(a_der) + str("x+") + str(b_der) 
    elif b_val < 0:
        derivative = str(a_der) + str("x") + str(b_der)
else:
    derivative = str(a_der) + str("x")

print("First Derivative: " + str(derivative))
print("")

choice = 0
while choice != 3:
    print("""
1. Find a point 
2. Version History
3. Close program
""") 
    choice = input(str("Input: ")) 
    print("")
    if choice == "1":
        print("  ~~ Coordinate Locator ~~") 
        print("")
        x_val = int(input("X Value: "))
        y_val = (x_val**2)*a_val + (x_val*b_val) + c_val 
        print("")
        print("Coordinate: " + "(" + str(x_val) + "," + str(y_val) + ")") 
    elif choice == "2":
        print("  ~~ Version History ~~") 
        print("") 
        print("Current Version: V 1.1" )
        print("Added: title, version history, coordinate locator.") 
        print("-------------------------------------------------")
    elif choice == "3" or choice == "exit" or choice == "end":
        print("Program Exited") 
        exit()
    
