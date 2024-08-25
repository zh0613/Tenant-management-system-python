
def program():
    print("Python Program")
    print("1.PRODUCT")
    print("2.LARGEST")
    try:
        num1=int(input("Enter first number: "))
        num2=int(input("Enter second number: "))
    except ValueError:
        print("not a integer")
    except:
        print("not a integer")
    
    try:
        option=int(input("Choose any of the given options:"))
    except ValueError:
        print("Wrong option")
    except:
        print("Wrong option")
    if option == 1:
        product(num1,num2)
    elif option == 2:
        largest(num1,num2)
    else:
        print('unavailable options')

def product(num1,num2):
    total = num1*num2
    print((str(num1))+" * "+str(num2)+" = "+str(total))

def largest(num1,num2):
    if num1>num2:
        print(str(num1)+" number is Largest number")
    elif num1==num2:
        print("two numbers are equal")
    else:
        print(str(num2)+" number is Largest Number")


def main():
    list=[]
    while True:
        print("0.continue")
        print("-1.terminate")
        
        try:
            option=int(input("Enter options above"))
        except ValueError:
            print("wrong option")
        if option ==0:
            try: 
                add= int(input("Enter score: "))
            except ValueError:
                print("Enter a number")
            
            if validation(add) is True:
                list.append(add)
                print(list)
                average(list)
        if option ==-1:
            print(list)
            average(list)
            break
        else:
            print()

def average(list):
    a=0
    for i in list:
        a=a+i
    print(a/len(list))

def validation(value):
    if value<0 or value>100:
        return False
    else:
        return True

main()