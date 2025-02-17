# #area or circle
# from math import pi
# r=float(input('Enter the radius:'))
# area=pi*r**2
# print(area)

# #reverse full name
# fname=str(input('Enter first name:'))
# lname=str(input('Enter last name:'))
# print(lname,fname)

# #list and tuple generator
# no=input('Enter the nos:')
# l1=no.split(',')
# t1=tuple(l1)
# print(l1)
# print(t1)

# #fist and last colours
# color_list=['Red','Green','White','Black']
# first_color=color_list[0]
# last_color=color_list[-1]
# print(first_color,last_color)

# #date formatter
# date1=(11,12,2024)
# d1=list(date1)
# date2=(f'{d1[0]}/{d1[1]}/{d1[2]}')
# print(date2)
# #or
# '''exam_st_date = (11, 12, 2014)

# # Extracting the day, month, and year
# day, month, year = exam_st_date

# # Formatting and displaying the date
# print(f"The examination will start from : {day} / {month} / {year}")
# '''

# #no.s expansion
# n=int(input('Enter the no:'))
# exp=n+n*n+n*n*n
# print(exp)

# #calendar display
# import calendar
# y=int(input('Enter year:'))
# m=int(input('Enter month:'))
# print(calendar.month(y,m))

# #days b/w dates
# from datetime import date
# fd=date(2014,7,2)
# ld=date(2014,7,11)
# print(ld-fd)

# #sphere volume calculator
# from math import pi
# r=int(input('Enter the radius'))
# vol=4/3*pi*r**3
# print(vol)

# #diff from 17
# n=int(input('Enter the number'))
# if n<=17:
#     print(f'{17-n}')
# else:
#     print(f'{(n-17)*2}')

# #triple sum calc
# n1=int(input('Enter a int:'))
# n2=int(input('Enter a int:'))
# n3=int(input('Enter a int:'))
# if n1==n2==n3:
#     print(f'{(n1+n1+n3)*3}')
# else:
#     print(f'{n1+n2+n3}')

# #prefix 'is'
# txt=input()
# if txt.startswith('Is'):
#     print(txt)
# else:
#     print('Is'+txt)

# #n copies of str
# t=str(input())
# n=int(input())
# print(n*t) 
# '''or for i in range(n+1):
#         print(t)'''

# #even odd for a list 
# n=(input())
# n1=n.split()#splits str to list of str
# for i in n1:
#     i=int(i)
#     if i%2==0:
#         print(i,'-even')
#     else:
#         print(i,'-odd')

# #even numbers until
# start=int(input('Enter start:'))
# end=int(input('Enter end:'))
# for i in range(start,end+1):
#     if i%2==0:
#         print(i)

# #area of triangle
# b=int(input('Enter base:'))
# h=int(input('Enter height:'))
# area=1/2*b*h
# print(area)

# #/7&/5(1500,2700)
# for i in range(1500,2701):
#     if i%7==0 and i%5==0:
#         print(i)

# #c to f
# c=int(input('Enter temp in celsius'))
# f=(c*9/5)+32
# print(f)

# #guess no
# def guess():
#     import random
#     num = random.randint(1, 10)
#     g = None  
#     while g != num:
#         g = int(input('Guess the number: '))
#         if g < num:
#             print('Too low')
#         elif g > num:
#             print('Too high')
#     print('Yes! You guessed correctly')
# guess()

# #pattern
# n=int(input('Enter number of rows:'))
# for i in range(n):
#     for j in range(i):
#         print('*',end="")
#     print("")
# for i in range(n,0,-1):
#     for j in range (i):
#         print('*',end="")
#     print("")

# #word reverse
# word=str(input())
# w=word.split()
# for i in w:
#     print(i[::-1])

# #even/odd count
# n=input().split()
# ec=0
# oc=0
# for i in n:
#     i1=int(i)
#     if i1%2==0:
#         ec+=1
#     else:
#         oc+=1
# print(f'no of even nos:{ec}')
# print(f'no of odd nos:{oc}')

# #datatypes
# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
# for i in datalist:
#     print(f'datatype of {i} is {type(i)}')

# #continue
# for i in range(1, 7):
#     if i==3 or i==6:
#         continue
#     print(i)

# #fibonacci
# f=[0,1]
# for i in range(2,50):
#         i1=f[i-1]+f[i-2]
#         if i1>50:
#             break
#         f.append(i1)
# print(f)

# #sum of list of numbers
# def sum(n):
#     s=0
#     for i in n:
#         s+=i
#     return s
# a=list(map(int, input().split()))
# print(sum(a))

# #sum recursion lists using recursion
# def sum(n):
#     st=0
#     for i in n:
#         if type(i)==list:
#             st+=sum(i)
#         else:
#             st+=i
#     return st
# print(sum([1,2,[3,4],[5,6]]))

# #factorial of non-neg using recursion
# def fac(n):
#     if n==0 or n==1
#         return 1
#     else:
#         return n*fac(n-1)
# print(fac(5))

# #fibonacci using recursion
# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(7))

# #sum of non-neg using recursion
# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return n%10 +sum(n//10)
# print(sum(345))

# #+sum for n+(n-2)+(n-4)...
# def sum(n):
#     if n<=0:
#         return 0
#     else:
#         return n+sum(n-2)
# print(sum(7))

# #harmonic sum
# def hsum(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return 1/n+hsum(n-1)
# print(hsum(7))

# #geometric sum upto n
# def gsum(n):
#     if n==0:
#         return 0
#     else:
#         return 1/(2**(n-1))+gsum(n-1)
# n=int(input())
# print(gsum(n))

# #a**b
# def p(a,b):
#     if a==0:
#         return 0
#     elif b==0:
#         return 1
#     elif b==1:
#         return a
#     else:
#         return a*p(a,b-1)
# print(p(2,3))  

# #GCD using recursion
# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
# print(gcd(48,18))

# #str len
# def sl(n):
#     if n==" ":
#         return 0
#     else:
#         n1=n.replace(' ','')
#         return len(n1)
# print(sl("Hello world!"))

#