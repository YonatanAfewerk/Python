def main():
        # take in the user choice and decide which path to take
    print("For Decimal To Binary (1)")
    print("For Binary To Decimal (2)")
    choice = int(input())
    
    if choice == 1:
        my_int = int(input("Enter Decimal Number: "))
        print(f"Binary Number: {convert_decimal(my_int)}")
    elif choice == 2:
        my_bin = input("Enter Binary Number: ")
        print(f"Decimal Number: {convert_bin(my_bin)}")
    else:
        print("Wrong choice!")
        
def convert_decimal(my_int):
    n1 = bin(my_int).replace("0b", "") 
    return n1

def convert_bin(my_bin):
    n2 = int(my_bin, 2)
    return n2


if __name__ == '__main__':
    main()