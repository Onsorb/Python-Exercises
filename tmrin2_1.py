
num1 = float(input("عدد اول را وارد کنید: "))
num2 = float(input("عدد دوم را وارد کنید: "))

print("عملیات را انتخاب کنید:")
print("1. جمع (+)")
print("2. تفریق (-)")
print("3. ضرب (*)")
print("4. تقسیم (/)")

choice = input("عدد عملیات را وارد کنید (1/2/3/4): ")

if choice == '1':
    result = num1 + num2
    print("نتیجه جمع:", result)
elif choice == '2':
    result = num1 - num2
    print("نتیجه تفریق:", result)
elif choice == '3':
    result = num1 * num2
    print("نتیجه ضرب:", result)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("نتیجه تقسیم:", result)
    else:
        print("خطا: تقسیم بر صفر مجاز نیست!")
else:
    print("انتخاب نامعتبر است.")
