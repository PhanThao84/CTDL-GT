# Bai1
# def Tongbangdequy(n):
#     if n==1:
#         return 1
#     else:
#         return n+Tongbangdequy(n-1)
# n=int(input())
# print(Tongbangdequy(n))

# Bai2
# n=int(input())
# S=0
# for i in range(1,n+1):
#     S+=i
#     i+=1
# print(S)

# Bai3
# def Tichdequy(n):
#     if n==1:
#         return 1
#     else:
#         return n*Tichdequy(n-1)
# n=int(input())
# print(Tichdequy(n))

# Bai4
# n=int(input())
# Tich=1
# for i in range(1,n+1):
#     Tich*=i
# print(Tich)

# Bai5
# import math
# def KTSNTdequy(n):
#     if n<2:
#         return 
#     else:
#         C=True
#         for i in range(2,int(math.sqrt(n)+1)):
#             if n%i==0:
#                 C=False
#                 break
#         if C:
#             print(n)
#         KTSNTdequy (n-1)
# n=int(input())
# KTSNTdequy(n-1)
                
# # Bài 6
# import math
# n=int(input())
# for i in range(2,n):
#     C=True
#     for j in range (2,int(math.sqrt(i)+1)):
#         if i%j==0:
#             C=False
#             break
#     if C:
#         print(i)

# Bai7
# n=int(input())
# if n<=2:
#     print(1)
# else:
#     b=1
#     c=1
#     for i in range (3,n+1):
#         a=b+c
#         b=a
#         c=b
#     print(a)

# Bai 8
# s = input("Nhập xâu: ")
# S_str = s[::-1]
# print("Xâu đảo ngược:", S_str)

# Bai9
# def HaNoi(n,A,B,C):
#     if n==1:
#         print(A,"-->",C)
#     else:
#         HaNoi(n-1,A,C,B)
#         HaNoi(1,A,B,C)
#         HaNoi(n-1,A,B,C)
# A="A"
# B="B"
# C="C"
# n=int(input())
# HaNoi(n,A,B,C)

# def Try(i,a,x):
#     for j in range(1, n+1):
#         if a[j]==true:
#             x[i]=j
#             a[j]=false;
#         if i==k:
#             print(x)
#  else 
#  Try(i+1,a,x)
#  a[j]=true
#  for i in range (1,n+1): 
#  a[i]=true
#  x[i]=0
# Try(1,a,x)

# def Try(i,n,k,A,S):
#     for j in range(0,n):
#         if A[j]==1:
#             S[i]=j
#             A[j]=0
#             if i==k-1: print(S[0:k])
#             else: Try(i+1,n,k,A,S)
#             A[j]=1
# n=int(input())
# k=int(input())
# A=[]
# S=[]
# for i in range (0,k): S.append(0)
# for i in range (0,n): A.append(1)
# Try(0,n,k,A,S)

# def Tim(i,k,n,x):
#     for j in range(0,n):
#         x[i]=j 
#         if i==k-1:
#             print(x)
#         else:
#             Tim(i+1,k ,n, x)
# x=[]
# k=4
# n=3
# for i in range (0,k):
#     x.append(0)
# Tim(0,k,n,x)
import random
import math
n=input().split(" ")
A=[]
while len(A) < math.factorial(len(n)): 
    # để cho chạy đc n! phần tử khác nhau rồi dừng
    B=n.copy()
    # tạo ra 1 list mới để tiến hành tráo vị trí
    random.shuffle(B)
    # để tráo vị trí của các phần tử
    if B not in A:
        A.append(B)
dem=0
for i in A:
    print(i)
    dem=dem+1
print(dem)