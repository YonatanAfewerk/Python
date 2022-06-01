def main():
    print(get_int())
    
def get_roman(roman):
    dict = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
        }
    sum = 0
    for i in roman:
        for j in dict:
            if i == j:
                sum += dict[j]
    return sum

def get_int():
    roman = input("Input: ")
    return get_roman(roman)
    
    
    
    
if __name__ == "__main__":
    main()