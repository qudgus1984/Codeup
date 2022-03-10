# codeup 6021

from tkinter import N


s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# codeup 6022

ymd = input()
print(ymd[0:2],ymd[2:4],ymd[4:6],sep=' ')

# codeup 6023

hms = input().split(':')
print(hms[1])

# codeup 6024

x,y = input().split()
z = x + y
print(z)

# codeup 6025

x,y = map(int, input().split())
z = x + y
print(z)

# codeup 6026

x = float(input())
y = float(input())
z = x + y
print(z)

# codeup 6027

num = input()
hexa = int(num)
print('%x' %hexa) # %x : 16진수 소문자로 출력

# codeup 6028

num = input()
hexa = int(num)
print('%X' %hexa) # %X : 16진수 대문자로 출력

# codeup 6029

x = input()
n = int(x, 16)
print('%o'%n)

# codeup 6030

n = ord(input())
print(n)

