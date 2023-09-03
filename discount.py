def discount(number):
    return number*0.85;

num = float(input("Enter price:"))
rounded_num = round(num, 1)
print(discount(rounded_num))
