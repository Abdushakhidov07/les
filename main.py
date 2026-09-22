# age = int(input("Enter your age: "))

# if age>=18:
#     print("you can voite")
# elif age<0:
#     print("Wrog enter")
# else:
#     print("You can't voite")


# color = input()

# match color:
#     case "r":
#         print("Stop")
#     case "y":
#         print("Wait")
#     case "g":
#         print("Go")
#     case _:
#         print("Eror color")



# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))

# try:
#     print(num1//num2)

# except ZeroDivisionError:
#     print("We can't devised to zero")
    
# finally:
#     print("Finish")


# i = 1
# while True:
#     if i%2 == 0:
#         i+=1
#         break
#     print(i)
#     i+=1


# a = 0
# while True:
#     pasw = input("Enter password: ")
#     if pasw == "admin":
#         print("Access granted")
#         break
#     else:
#         print("Wrong password enter again ! ")
#         a+=1
#         if a == 3:
#             print("You bloked")
#             break
        



# num1=int(input())


# if num1%3==0 and num1%5==0:
#     print("FizzBuzz")

# elif num1%3==0:
#     print("Fizz")

# elif num1%5==0:
#     print("Buzz")
    
# else:
#     print("num1")




# num1 = int(input())
# num2 = int(input())

# if num1+(num2*5)>=90:
#     print("A")
# elif num1+(num2*5)>=80:
#     print("B")
# elif num1+(num2*5)>=70:
#     print("C")
# elif num1+(num2*5)>=60:
#     print("D")
# else:
#     print("F")

# cnt = 0
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     if n < 0:
#         continue
#     cnt+=n
# print(cnt)

# weight = input()
# height = input()

# try:
#     weight = float(weight)
#     height = float(height)
#     bmi = weight /(height*height)
#     print(bmi)
# except ValueError:
#     print("You enter words not number ERROR")

# except ZeroDivisionError:
#     print("Height cannot be zero")


# name = "Abdujamil"

# for i in name:
#     print(i)


# lict = ["Abdullo", 5, 10, 80.2, True]

# lict2 = ["Abdullo", 5, 10, 80.2, True]

# lict.extend(lict2)

# lict.append("Mahmud")

# lict.insert(2,"Akbar")

# lict.remove("Abdullo")

# lict.pop(5)


# del lict
# lict.clear()

# print(*lict)

# print(lict.count(1))

# print(lict.index(10))


# lict = list(map(int, input().split()))



# print(lict)

# name = "Abdullo"

# if "o" not in name:
#     print("Yes")

# else:
#     print("No")






# lict2 = [i for i in lict if i%2==0]

# lict3 = [i for i in range(101)]

# print(lict3)
        

# n = int(input())

# cnt = 0
# for i in range(1, n+1):
#     cnt+=i
# print("Sum:",cnt)


# n=int(input())
# for i in range(1, 11):
#     print(f"{n} * {i} = {n*i}")



# lict = ("Abdullo", "Ehson", "Akbar")
# lict = list(lict)
# lict[1] = "Mahmud"
# lict = tuple(lict)
# print(lict)



# n = int(input())

# lict = []

# for i in range(1, n+1):
#     lict.append(i**2)
    
# print(lict) 


# lict = ["Abdullo", 5, 10, 80.2, True]
# print(lict[0])

# name ="Akbar"
# age = 15
# print("My name is {} and I am {} years old.".format(name, age))
# print("My name is %s and I am %d years old." % (name, age))



# text = "Hello-my-students-how-are-you?"

# k = text.split("-")
# print(k)


# m = " ".join(k)
# print(m)

# print(m.upper())
# print(m.lower())

# print(m.replace("students", "Abdullo")) 



# print(dir(m))

# data = ["Abdulloh", 16, "male", "Prafsayz", "+992 11111111", "Python", "School: 66"]


# data_dict = {
#     "name":"Abdulloh",
#     "age": 16,
#     "gender": "Male",
#     "adress": "Prafsayz",
#     "phone": "+992 11111111",
#     "group": "Python1",
#     "school_n": "66"
# }


# for key, value in data_dict.items():
#     print(key, value)



# print(data_dict.get("date_d"))


# text = "DataAnalysis"
# print(text[0:4])
# print(text[4:])

# print(text[-1])



# text = "python"
# print(text[::-1])


# print(len(data_dict.keys()))




# set1 = {"Apple", "Banan", "Pich", "Pear", "Apple"}
# set2 = {1, 2, 3, "Apple"}


# set3 = set1.union(set2)


# print(set1.intersection(set2))
# print(set1)

# print(set2.difference(set1))

# print(set1.symmetric_difference(set2))


# colors = {"red", "green"}


# colors.update(["Balck"])


# for i in colors:
#     print(i)



# def say_hello():
#     print("Hello world")
    

# say_hello()



# def sum_digit(num1, num2 ):
#     print(num1+num2)
    
    
# sum_digit(int(input()), int(input()))



# def bio(name, age=18):
#     print(f"Your name:{name}")
#     print(f"Your age:{age}")

# bio("Abdullo", 16)


# def max1(a=0, b=0):
#     if a>b:
#         return a 
#     elif b>a:
#         return b 
#     else:
#         return a 
        
    
    
# max(5, 4)
# print(max1(5, 4))



# def sum1(*args):
#     cnt = 0 
#     for i in args:
#         cnt+=i
#     return cnt


# print(sum1(1, 2, 3,3,2,1, 4, 5, 6,))
    
    
    
    
# def bio(**k):
#     print(k)
    
# bio(name = "Abdullo", age = 15, gender = "male")




# def max1(*args):
#     maxx = -9999999
#     for i in args:
#          if i>maxx:
#              maxx=i
#     return maxx


# def min1(*args):
#     maxx = 9999999
#     for i in args:
#          if i<maxx:
#              maxx=i
#     return maxx


# def func(a, b, c):
#     print("Sum", a+b+c)
#     print("Avarage", (a+b+c)/3)
#     print("Maximum", max1(a,b,c))
#     print("Minimum", min1(a,b,c))
    
    
    
# func(int(input()),int(input()),int(input()))

# def ticket_price(age, weekend=False):
#     if weekend:
#         p = 30
#     else:
#         p = 20
#     if age < 12 or 65 < age:
#         p/=2
#     return p
# a = int(input())

# print(ticket_price(a))
# print(ticket_price(a,True))

# def number_stats(*numbers):
#     sum=0
#     cnt=0
#     for i in numbers:
#         sum+=i
#         cnt+=1
#     print("Count: ", cnt)
#     print("Totsl: ", sum)
#     print("Average: ", sum/cnt)
    
# number_stats(4, 8, 15, 16, 23, 42)
    
    
# def greed():
#     print("Hello!")
    
# greed()




# def greed(name):
#     print(f"Hello, {name}!")
  
    
# greed(input())

# lict = list(map(int, input().split()))

# i = 0


# while i<len(lict):
#     print(lict[i])
#     i+=1
    
# i =  0
# while i<=10:
#     print(i)
#     i+=1

# n = int(input())

# k = 0

# while n>0:
#     k = (k*10) + n%10
#     n//=10
    
# print(k)



# def greet(name, greeting = "Hello"):
#     print(greeting, name)
    
# name = input()
# grt = input()
# greet(name)
# greet(name, grt)



# def bio(name:str|int, age:int, number:str) -> dict:
#     bio_user = {
#         "name": name,
#         "age": age,
#         "number": number
#     }
#     return bio_user

# def hello(name:str):
#     def upper(name:str):
#         return name.capitalize()
#     return f"Hello {upper(name)}"
# print(hello("abdullo"))
    

# def max1(*args):
#     max=-999999
#     for i in args:
#         if i >= max:
#             max = i
#     return max 




# print(max1(1,2,3,4,6,-999999,1123))



# def hello():
#     print("Hello")
# cnt = 1
# for i in range(1,5+1):
#     cnt*=i

# print(cnt)

# def factorial(n):
#     if n == 1:
#         return 1
#     return n*factorial(n-1)

# print(factorial(5))







# def factorial(n, cnt=1):
#     if n == 1:
#         return cnt
#     cnt*=n
    
#     return factorial(n-1, cnt)

# print(factorial(10))



# def outer():
#     cnt = 0
    
#     def inner():
#         nonlocal cnt
#         cnt+=1
#         return cnt
    
#     return inner()

# print(outer())





# name = "Tom"
 
 
# def say_hi():
#     global name
#     name = "Bob"        # изменяем значение глобальной переменной
#     print("Hello", name)
 
 
# def say_bye():
#     print("Good bye", name)
 
 
# say_hi()    # Hello Bob
# say_bye()   # Good bye Bob







# def recursion(number):
#     if number==0:
#         return 0
#     print(number)
#     return recursion(number-1)


# recursion(int(input()))





# def sum_add(a, cnt=1):
#     if a == 1:
#         return cnt
#     cnt+=a
#     return sum_add(a-1, cnt)

# print(sum_add(5))


# def po(a,b):
#     if b == 1:
#         return a
#     return a*po(a,b-1)
# print(po(2,5))


# def sum_digits(n):
#     if n == 0:
#         return 0
#     return n % 10 + sum_digits(n // 10)

# print (sum_digits(1234))

# a="Python"
# for i in range(len(a)-1, -1, -1):
#     print(a[i], end="")
    
# def name(n):
#     if len(n)-1==-1:
#         return n-1
    
# print(name("python"))
        
        
# def revers(text, ln=None):
#     if ln == None:
#         ln = len(text)-1
#     if ln == -1:
#         return 1
#     print(text[ln], end="")
#     return revers(text, ln-1)
# revers("Pyhton")





# def outer():
#     cnt = 1001
#     def inner():
#         nonlocal cnt
#         cnt+=1
#         return cnt
#     return inner
    
# closur1 = outer()
# closur2 = outer()
# print(closur1())
# print(closur1())
# print(closur2())
# print(closur2())
# print(closur2())
  



# n = 90
# pr = 15

# print(n - ((n*pr)/100))




# print(n - ((n/100)*pr))


# def create_tax_calculator(tax_percent):
#     def inner(price):
#         nonlocal tax_percent
#         return price  - ((price /100)*tax_percent)

#     return inner


# closur1 = create_tax_calculator(10)

# print(closur1(1000))
# print(closur1(10))
# print(closur1(900))

# import service

# print(service.sum_numbers(2, 4))

# from service import *


# print(sum_numbers(2, 4))







# from math import *


# print(sqrt(81))
# print(factorial(5))
# print(pi)





# from datetime import *


# dat = datetime.now()
# dat2 = date.today()

# print(dat2.strftime("%B %d %y %A"))

# dat2 = dat2+timedelta(weeks=1000)

# print(dat2.strftime("%C"))


# birth_date = "06-09-2009"

# birth_date = datetime.strptime(birth_date, "%d-%m-%Y")

# print(dat.year - birth_date.year)

# from random import *


# print(randint(10, 30))
# print(random())


# lict = ["Abdullo", "Salohiddin", "Umar", "Ehson", "Muhammadsalim", "Akbar", "Mahmud", "Abdujamil", "Abdurahmon"]


# l = choices(lict, weights=(1, 1, 1, 1, 1, 1, 1, 1, 1), k=900)

# print("Muhammadsalim=",l.count("Muhammadsalim"))
# print("Umar=",l.count("Umar"))
# print("Salohiddin=",l.count("Salohiddin"))
# print("Abdullo=",l.count("Abdullo"))
# print("Ehson=", l.count("Ehson"))
# print("Akbar=", l.count("Akbar"))
# print("Mahmud=", l.count("Mahmud"))
# print("Abdujamil=", l.count("Abdujamil"))
# print("Abdurahmon",l.count("Abdurahmon"))


# 1
# from datetime import *
# print(datetime.now())


# from datetime import *
# dt = datetime.now()
# print(dt.strftime("%d %b %Y %X %p"))


# from datetime import *
# dt = datetime.now()
# print(dt.strftime("Day of the week: %B"))




# from datetime import *
# dt = datetime.now()
# print(dt.strftime("DateTime as string: %G-%m-%d  %X"))


# from datetime import *
# dt = datetime.now()
# print("Expected Output:")
# print(dt.strftime("Year: %G"))


# print("Hello")



# class Car:
#     def __init__(self, brand, color, speed, date):
#         self.brand = brand
#         self.color = color
#         self.speed = speed
#         self.date = date
    
#     def start(self, name_user):
#         return f"Car with name {self.brand} start engine, by {name_user}"
    
    
    
    
    
# mersedes = Car("CLS 360", "Pink", 20, "2027-01-01")
# bmw = Car("M5 F90", "Pink", 25, "2027-01-01")

# print(mersedes.color)
# mersedes.color="Black"
# print(mersedes.color)




# print(bmw.color)



# print(mersedes.start("Umar"))
# print(bmw.start("Abdulloh"))






# class Students:
#     def __int__(self):
#         pass
    
    
# alijon = Students()
# Validjon = Students()
# Said = Students()



# class Cat:
#     def __init__(self,name,age,color):
#         self.name = name
#         self.age = age
#         self.color = color
        
        
# cat1=Cat("rex",99,"colorfool")
# cat2=Cat("kolya",999,"unknow")
# cat3=Cat("andrey",9999,"pink")


# print(cat1.name, cat1.age, cat1.color)
# print(cat2.name, cat2.age, cat2.color)
# print(cat2.name, cat2.age, cat2.color)
    
    
    
    
# class Car:
#     def __init__(self,brand,model,year,color):
#         self.brand=brand
#         self.model=model
#         self.year=year
#         self.color=color
# meresedes=Car("Mersedes","AMG",2028,"black")
# cls=Car("Mersedes","CLS",2029,"white")
# bmw=Car("bmw","M5 f50",2030,"red")
# bmw1=Car("bmw","m4 f44",2031,"pink")

# print(meresedes.brand,meresedes.model,meresedes.year,meresedes.color)
# print(cls.brand,cls.model,cls.year,cls.color)
# print(bmw.brand,bmw.model,bmw.year,bmw.color)
# print(bmw1.brand,bmw1.model,bmw1.year,bmw1.color)







class BankAccount:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance = balance
        
    def show_balance(self):
        print(f"Balance {self.owner}: {self.balance}")
        
        
    
user1 = BankAccount("Abdulloh", 10)
user2 = BankAccount("Ehson", 15)

user1.show_balance()
user2.show_balance()

    