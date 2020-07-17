while True:
    y = int(input("Enter year: "))
    m = int(input("Enter month: "))
    d = int(input("Enter date: "))
    from datetime import date
    my_date = date(y,m,d)
    if (my_date.month == 12 and my_date.day <= 23) or (my_date.month == 1 and my_date.day <= 19):
        print("Hello CAPRICORN")
    elif (my_date.month == 1 and my_date.day >= 20) or (my_date.month == 2 and my_date.day <= 19):
            print("Hello AQUARIAN")
    elif (my_date.month == 2 and my_date.day >= 20) or (my_date.month == 3 and my_date.day <= 20):
            print("Hello PISCEAN")
    elif (my_date.month == 3 and my_date.day >= 21) or (my_date.month == 4 and my_date.day <= 20):
            print("Hello ARIES")
    elif (my_date.month == 4 and my_date.day >= 21) or (my_date.month == 5 and my_date.day <= 20):
            print("Hello TAURUS")
    elif (my_date.month == 5 and my_date.day >= 21) or (my_date.month == 6 and my_date.day <= 20):
            print("Hello GEMINI")
    elif (my_date.month == 6 and my_date.day >= 21) or (my_date.month == 7 and my_date.day <= 22):
            print("Hello CANCER")
    elif (my_date.month == 7  and my_date.day >= 23) or (my_date.month == 8 and my_date.day <= 22):
            print("Hello LEO")
    elif (my_date.month == 8 and my_date.day >= 23) or (my_date.month == 9 and my_date.day <= 22):
            print("Hello VIRGO")
    elif (my_date.month == 9 and my_date.day >= 23) or (my_date.month == 10 and my_date.day <= 22):
            print("Hello LIBRA")
    elif (my_date.month == 10 and my_date.day >= 23) or (my_date.month == 11 and my_date.day <= 22):
            print("Hello SCORPIO")
    elif (my_date.month == 11 and my_date.day >= 23) or (my_date.month == 12 and my_date.day <= 21):
            print("Hello SAGITARIUS")
    else:
        print("Please Enter valid Date of Birth :)")