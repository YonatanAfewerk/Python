def main():
    x, y = get_start_end()
    print(f"Prime Number Between {x}-{y} are: ")
    get_prime(x, y)
    
    
    
def get_start_end():
        # input the start and end
    x = int(input("Enter Start: "))
    y = int(input("Enter End: "))
    return x, y
    
def get_prime(start, end):
    for num in range(start, end + 1):
        # all prime numbers are > 1, only factors are 1 and the number itself
        if num > 1:
                # check to find a num that can divide it between 2-num if none its a prime
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num, end=" ")
            
            
if __name__ == '__main__':
    main()