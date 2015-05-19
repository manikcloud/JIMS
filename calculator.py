

def add (x, y):
    
        return x+y

def sub (x, y):
        return x-y

def mul (x, y):
      return (x*y)

def div(x,y):
        return x/y

print("Choose the options.")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Diviion")


choice = int(input("Enter the choice:"))
if choice <= 4:
    
    n1= int(input("Enter the first no."))
    n2= int(input("Enter the Second no."))



    if choice=='1':
        '''print(n1, '+', n2,'=', n1+n2)'''
        print(n1, '+', n2,'=', add(n1,n2))

    elif choice=='2':
        print(n1, '-', n2, '=', n1-n2)

    elif choice=='3':
        print(n1, '*', n2, '=', n1*n2)

    elif choice=='4':
        print(n1,'%',n2,'=',n1%n2)



else:
    print ("Invalid Input try again")
#    running=False 
        

    

   
