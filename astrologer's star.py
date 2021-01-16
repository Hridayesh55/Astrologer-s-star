try:
    a=int(input("enter number of rows"))
    b=int(input("enter 0 or 1"))
    '''if a==0 and b==0:
        break'''
    
    if b==1:
        print("true")
        while('*'):
            print(a*'*')
            a=a-1
            if a==0:
                break
    elif b==0:
        
        print("false")
        A=1
        while('*'):
            print(A*'*')
            A=A+1
            if A==a+1:
                break
except Exception as e:
    print("invalid input")
            
else:
    print("invalid input")
'''a=int(input("enter number of rows you want to print :"))
b=input("enter 0 or 1")
if b==0:
    num1=0
    while(num1<=a):
        print('*'*num1)
        num1=num1+1'''
        
        
    
