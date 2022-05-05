def main():
    d_out = get_date('Date: ')

    x = int(d_out[0])
    y = int(d_out[1])
    z = int(d_out[2])

    # output that same date in YYYY-MM-DD format.

    if y <= 9 and z <= 9:
        print(f'{x}-0{y}-0{z}')
    elif y >= 10 and z >= 10:
        print(f'{x}-{y}-{z}')
    elif y <= 9 and z >= 10:
        print(f'{x}-0{y}-{z}')
    elif y >= 10 and z <= 9:
        print(f'{x}-{y}-0{z}')


def get_date(prompt):
    date_list = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]
    p = '/'

    # input is not a valid date in either format, prompt the user again
    while True:
        try:
            date_in = input(prompt).title()
            if p in date_in:
                list_ = date_in.split('/')
                
                k = list_[0]
                k = int(k)
                
                if k > 12:
                    raise ValueError
                elif k < 12:       
                    return first_form(date_in)
            else:
                x, y, z = date_in.split(" ")

                y = y.split(',')
                c = y[0]
                c = int(c)

                if c >= 32:
                    raise ValueError

                if x in date_list:
                    n  = date_list.index(x)
                    n += 1
                    
                    if n > 12:
                        raise ValueError
                    elif n <= 12:
                        return sec_form(date_in, n)
        except ValueError:
            pass


def first_form(x):
    ans_list = []

    list_ = x.split('/')
    
    ans_list.append(list_[2])
    ans_list.append(list_[0])
    ans_list.append(list_[1])

    return ans_list


def sec_form(l, n):
    ans_list = []
    x, y, z = l.split(" ")
    x = n # month after getting the index from the list and adding 1 to it

    y_n = "".join(str(i) for i in y)

    y = y.split(',')
    c = y[0]
    c = int(c)

    if c >= 10:
        new_y = y_n.replace(y_n, y_n[0:2])
    else:
        new_y = y_n.replace(y_n, y_n[0])

    ans_list.append(z)
    ans_list.append(x)
    ans_list.append(new_y)

    return ans_list

main()


