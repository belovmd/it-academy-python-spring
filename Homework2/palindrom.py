number=int(input("Введите число:"))
kol_number=0
n=number
while n>0:
    n=n // 10
    kol_number+=1
# divide our number into two parts
n=kol_number // 2
kol_number-=1
# comparing first part of number with second part
for i in range(1,n+1):
    first_number=number // 10**kol_number
    last_number=number % 10

    if  first_number!=last_number:
        print("Не палиндром.")
        break
    number=number - first_number*10**kol_number - last_number
else:
    print("Палиндром!!!")