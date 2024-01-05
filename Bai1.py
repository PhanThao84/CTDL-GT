# a=int(input(''))
# b=int(input())
# print(a+b)
# print(a-b)
# print(a*b)
# if b!=0:
#     print(a/b)
# else:
#     print()
# a=int(input())
# b=int(input())
# if a!=0: print('x=',-b/a)
# else: print('Phương trình vô nghiệm')
# import math
# a=int(input('a='))
# b=int(input('b='))
# c=int(input('c='))
# if a!=0:
#     d=b*b-4*a*c
#     if d<0:
#         print("Phuong trinh vo nghiem")
#     if d==0:
#         print('Phuong trinh co nghiem kep')
#         print('x1=x2=',(-b/2*a),sep='')
#     if d>0:
#         print('Phuong trinh co hai nghiem')
#         print('x1=',(-b+math.sqrt(d))/2*a,sep='')
#         print('x2=',(-b-math.sqrt(d))/2*a,sep='')
        
# n = int(input())
# for num in range(2, n + 1):
#     a = True
#     if num > 1:
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 a = False
#                 break
#         if a:
#             print(num)
            
# n = int(input())
# for num in range(1, n + 1):
#     S = 0
#     for i in range(1, num):
#         if num % i == 0:
#             S += i
#     if  S == num:
#         print(num)

# def Nhap():
#     n=int(input('n='))
#     return n
# def giaithua(n):
#     if n<0:
#         return
#     a=1
#     i=1
#     for i in range (1,n+1):
#         a=a*i
#     return a
# def inkq(n,X):
#     print(n,'!=',X,sep='')
# n=Nhap()
# X=giaithua(n)
# inkq(n,X)
# n=int(input("n="))
# L=[]
# for i in range(1,n+1):
#     j=int(input())
#     L=L+[j]
# print(max(L))
# import math
# def Nhap():
#     a=int(input())
#     b=int(input())
#     c=int(input())
#     d=int(input())
#     e=(a*d+b*c)
#     f=(b*d)
#     return a,b,c,d,e,f
# def rutgonphanso(e,f):
#     g=math.gcd(e,f)
#     h=e//g
#     k=f//g
#     return h,k
# a,b,c,d,e,f=Nhap()
# h,k=rutgonphanso(e,f)
# print('Tong cua 2 phan so:',h,"/",k)

# # Giải đệ quy tính giai thừa
# # viết một chương trình tính giai thừa mà không sử dụng hàm đệ quy!
# def giaithualap(n):
#     giai_thua = 1
#     for i in range (1,n+1):
#         giai_thua = giai_thua * i
#     return giai_thua
# n = int(input())
# print(giaithualap(n))