age = int(input("سن: "))
day = input("روز: ")

if age < 5:
    print("ورود رایگان!")
else:
    if age <= 12:
        price = 50000
    elif age >= 60:
        price = 60000
    else:
        price = 100000

    if day == "سه‌شنبه":
        price_end = price - (price * 0.2)

    print("قیمت بلیط:", int(price_end), "تومان")
