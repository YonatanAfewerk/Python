def main():
    while True:
        try:
            x = float(input("Enter x: "))
            break
        except ValueError:
            continue

    while True:
        try:
            y = float(input("Enter y: "))
            break
        except ValueError:
            continue
        
        
    Choice = int(input("Choose Sub(1), add(2), Multi(3), div(4): "))

    if (Choice == 1):
        sub_(x,y)
    elif(Choice == 2):
        add_(x,y)
    elif(Choice == 3):
        times_(x,y)
    elif(Choice == 4):
        div_(x,y)
        
    

def add_(a, b):
    print(a + b)


def sub_(a, b):
    print(a - b)    

def times_(a, b):
    z = a * b
    print(f"{z:,}")


def div_(a, b):
    z = a / b
    print(f"{z:.4f}")    



    
    
main()