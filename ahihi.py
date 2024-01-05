# Trong một hội trường có  nghế ngồi. Người ta muốn tổ chức một hội nghị và tính các phương án để đón tiếp. Biết lượng người tham dự hội nghị là  
# k. Với k và  nđược nhập trên 2 dòng từ bàn phím theo thứ tự. Hãy tính số cách sắp xếp chỗ ngồi cho hội nghị này.
# from math import factorial
# # The long way
# k=int(input())
# n=int(input())
# C = factorial(n) / (factorial(k) * factorial(n - k))
# print(int(C))

# import math
# n = int(input())
# while True:
#     original_n = n
#     sum_of_factors = 0
#     # Tìm tất cả các ước số nguyên tố của n và tính tổng chúng
#     while n % 2 == 0:
#         sum_of_factors += 2
#         n /= 2
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         while n % i == 0:
#             sum_of_factors += i
#             n /= i
#     if n > 2:
#         sum_of_factors += n
#     # Nếu tổng ước số nguyên tố bằng n ban đầu thì dừng lại
#     if sum_of_factors == original_n:
#         break
#     else:
#         n = sum_of_factors
# print(int(sum_of_factors))

# Tính giai thừa bằng đệ quy
# def giaithua(n):
#   if n<=1:
#     return 1
#   else:
#     return n*giaithua(n-1)
# n=int(input())
# print(giaithua(n))

# Số mũ tự nhiên
# N=int(input())
# P=int(input())
# print(N**P)

# Chuỗi Fibonacci
# def f(n):
#     if n==0 or n==1 or n==2:
#         return 1
#     else:
#         return f(n-1)+f(n-2)
# n=int(input())
# print(f(n))

# Tháp Hà Nội
# def thap_ha_noi(n, nguon, trung_gian, dich):
#     if n == 1:
#         print(f"Disk 1 moved from {nguon} to {dich}")
#         return
#     thap_ha_noi(n-1, nguon, dich, trung_gian)
#     print(f"Disk {n} moved from {nguon} to {dich}")
#     thap_ha_noi(n-1, trung_gian, nguon, dich)# Số lượng đĩa
# N = int(input())
# # Gọi hàm
# thap_ha_noi(N, 'A', 'B', 'C')

# Chuỗi nhị phân 
# def generate_strings(k, current, result):
#     if len(current) == k:
#         result.append(current)
#         return
#     # Luôn có thể thêm 0
#     generate_strings(k, current + "0", result)
#     # Chỉ thêm 1 nếu chữ số cuối cùng không phải là 1
#     if not current or current[-1] != '1':
#         generate_strings(k, current + "1", result)
# def main():
#     K = int(input("Enter K: "))
#     result = []
#     generate_strings(K, "", result)
#     print("Chuỗi nhị phân có kích thước {} mà không có các số 1 liên tiếp:".format(K))
#     for s in result:
#         print(s)
# if __name__ == "__main__":
#     main()
# Python3 program to Generate all binary string
# without consecutive 1's of size K

# A utility function generate all string without
# consecutive 1'sof size K

# def generateAllStringsUtil(K, str, n):	
# 	# print binary string without consecutive 1's
# 	if (n == K):		
# 		# terminate binary string
# 		print(*str[:n], sep = "", end = " ")
# 		return
# 	# if previous character is '1' then we put
# 	# only 0 at end of string
# 	# example str = "01" then new string be "000"
# 	if (str[n-1] == '1'):
# 		str[n] = '0'
# 		generateAllStringsUtil (K, str, n + 1)		
# 	# if previous character is '0' than we put
# 	# both '1' and '0' at end of string
# 	# example str = "00" then new string "001" and "000"
# 	if (str[n-1] == '0'):
# 		str[n] = '0'
# 		generateAllStringsUtil(K, str, n + 1)
# 		str[n] = '1'
# 		generateAllStringsUtil(K, str, n + 1)		
# # function generate all binary string without
# # consecutive 1's
# def generateAllStrings(K):
# 		# Base case
# 	if (K <= 0):
# 		return	
# 	# One by one stores every
# 	# binary string of length K
# 	str = [0] * K
# 	# Generate all Binary string starts with '0'
# 	str[0] = '0'
# 	generateAllStringsUtil (K, str, 1)
# 	# Generate all Binary string starts with '1'
# 	str[0] = '1'
# 	generateAllStringsUtil (K, str, 1)
# # Driver code
# K = 3
# generateAllStrings (K)

# Giải đệ quy chuỗi Fibonacci" bằng phương pháp lặp
# n = int(input())
# F =[0,1,1]
# for i in range(3,n+1):
#     F.append(F[i-1]+F[i-2])
# print(F[n])

# # Giải đệ quy tính giai thừa
# # viết một chương trình tính giai thừa mà không sử dụng hàm đệ quy!
# def giaithualap(n):
#     giai_thua = 1
#     for i in range (1,n+1):
#         giai_thua = giai_thua * i
#     return giai_thua
# n = int(input())
# print(giaithualap(n))

# Chèn phần tử mảng
# n =int(input())
# a = [int(x) for x in input().split()]
# k, x = [int(y) for y in input().split()]
# a.append("")
# for i in reversed(range(k+1,n+1)):
#     a[i] = a[i-1]
# a[k]=x
# for i in range(n+1):
#     print(a[i], end=" ")

# Xóa phần tử trong mảng
# n=int(input())
# a=[int(x) for x in input().split()]
# k=int(input())
# for i in range(k,n-1):
#   a[i]=a[i+1]
# for i in range(0,n-1):
#   print(a[i],end=" ")

# Tổng của chuỗi số
# n=int(input())
# a=list(map(int,input().split()))
# S=sum(a)
# print(S)

# Cấp số cộng
# n=int(input())
# a=list(map(int,input().split()))
# C=True kiểm tra xem có phải cấp số cộng không 
# d=a[1]-a[0]
# for i in range(1,n-1):
#   if a[i+1]-a[i]!=d:
#     C=False
#     break
# if C:
#   print("YES")
# else:
#   print("NO")

# Dãy đơn điệu
# n = int(input())
# a=[int(x) for x in input().split()]
# check1 = check2 = True
# for i in range(1,n):
#     if (a[i-1]<=a[i]): check1=False
#     if (a[i-1]>=a[i]): check2=False

# if (check1 or check2): print("YES")
# else: print("NO")

# Phần tử cực trị

# n = int(input())
# arr = list(map(int, input().split()))
# # Kiểm tra phần tử đầu tiên
# if n == 1 or arr[0] >= arr[1]:
#     print(0, end=' ')
# # Kiểm tra các phần tử từ thứ hai đến thứ n-1
# for i in range(1, n-1):
#     if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
#         print(i, end=' ')
# # Kiểm tra phần tử cuối cùng
# if n > 1 and arr[n-1] >= arr[n-2]:
#     print(n-1, end=' ')

# def findPeak(arr, n) :
#   try:
#     if (n == 1) :
#       print(0, end=" ")
#     if (arr[0] >= arr[1]) :
#       print(0, end=" ")
#     if n!=1:
#       for i in range(1, n - 1) :
#         if (arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]) :
#           print(i, end=" ")
#     if (arr[n - 1] >= arr[n - 2]) :
#       print(n-1, end=" ")
#   except:
#     pass
# n = int(input())
# arr = [int(x) for x in input().split()]
# findPeak(arr, n)

# Số Narcissistic
# def is_narcissistic(num):
#     n = len(str(num))  # số chữ số của num
#     total = sum(int(digit) ** n for digit in str(num))
#     return total == num
# n = int(input())
# arr = list(map(int, input().split()))
# # Kiểm tra và in các số Narcissistic
# has_narcissistic = False
# for num in arr:
#     if is_narcissistic(num):
#         print(num, end=' ')
#         has_narcissistic = True
# if not has_narcissistic:
#     print("NO")
# n = int(input())
# arr = list(map(int, input().split()))
# has_narcissistic = False
# for num in arr:
#     power = len(str(num))
#     total = sum(int(digit) ** power for digit in str(num))
#     if total == num:
#         print(num, end=' ')
#         has_narcissistic = True
# if not has_narcissistic:
#     print("NO")

# Hệ mật AFFINE
# Hàm tìm nghịch đảo modulo cho số a dưới modulo m
# def mod_inverse(a, m):
#     for i in range(1, m):
#         if (a * i) % m == 1:
#             return i
#     return None

# # Hàm mã hóa Affine
# def affine_encrypt(text, a, b):
#     return ''.join([chr((a * (ord(char) - ord('a')) + b) % 26 + ord('a')) for char in text])

# # Hàm giải mã Affine
# def affine_decrypt(cipher, a, b):
#     a_inv = mod_inverse(a, 26) # Tìm nghịch đảo của a dưới modulo 26
#     if a_inv is None: # Nếu không tìm thấy nghịch đảo, trả về None
#         return None
#     return ''.join([chr(a_inv * (ord(char) - ord('a') - b) % 26 + ord('a')) for char in cipher])

# # Nhập khóa a và b
# a, b = map(int, input().split())

# # Nhập văn bản cần mã hóa
# text = input()

# # Kiểm tra xem a có nghịch đảo dưới modulo 26 hay không
# if mod_inverse(a, 26) is None:
#     print("Can't Encrypted and Decrypted this Message")
# else:
#     # Mã hóa và in văn bản đã mã hóa
#     encrypted_text = affine_encrypt(text, a, b)
#     print("Encrypted Message is :", encrypted_text)
    
#     # Giải mã và in văn bản đã giải mã
#     decrypted_text = affine_decrypt(encrypted_text, a, b)
#     print("Decrypted Message is :", decrypted_text)
# # Nhập khóa a và b
# a, b = map(int, input().split())
# # Nhập văn bản cần mã hóa
# text = input()
# # Tìm nghịch đảo modulo cho số a dưới modulo 26
# a_inv = None
# for i in range(1, 26):
#     if (a * i) % 26 == 1:
#         a_inv = i
#         break
# # Kiểm tra xem a có nghịch đảo dưới modulo 26 hay không
# if a_inv is None:
#     print("Can't Encrypted and Decrypted this Message")
# else:
#     # Mã hóa văn bản
#     encrypted_text = ''.join([chr((a * (ord(char) - ord('a')) + b) % 26 + ord('a')) for char in text])
#     print("Encrypted Message is :", encrypted_text)

#     # Giải mã văn bản đã mã hóa
#     decrypted_text = ''.join([chr(a_inv * (ord(char) - ord('a') - b) % 26 + ord('a')) for char in encrypted_text])
#     print("Decrypted Message is :", decrypted_text)

# Viết chương trình in xâu đảo ngược không đệ quy
# các1 sử dụng chỉ số
# s = input("Nhập xâu: ")
# reversed_str = ""
# for char in s:
#     reversed_str = char + reversed_str
# print("Xâu đảo ngược:", reversed_str)
# cách 2 sử dụng Python
# s = input("Nhập xâu: ")
# reversed_str = s[::-1]
# print("Xâu đảo ngược:", reversed_str)

# Viết chương trình in xâu đảo ngược bằng đệ quy
# def reverse_string(s):
#     if len(s) <= 1:
#         return s
#     return s[-1] + reverse_string(s[:-1])
# input_string = input("Nhập xâu: ")
# print("Xâu đảo ngược:", reverse_string(input_string))


# Tách từ
# s = str(input())
# result="Ket qua tach tu:"
# for word in s:
#     if ord(word) >=65 and ord(word)<=90:
#         result = result +" "+ chr(ord(word)+32)
#     else: result = result + word
# print(result)

# Xóa khoảng trắng
# s = str(input())
# while (s[0]==" "):
#     s = s.lstrip(" ")
# while (s[-1]==" "):
#     s = s.rstrip(" ")
# while (s.find("  ")>0):
#     s= s.replace("  "," ")
# print(s)
# Xác định mật khẩu mạnh
# import re
# def is_strong_password(password: str) -> bool:
#     if len(password) <= 6:
#         return False
#     if not re.search(r"[0-9]", password):
#         return False
#     if not re.search(r"[a-z]", password):
#         return False
#     if not re.search(r"[A-Z]", password):
#         return False
#     if not re.search(r"[!@#$%^&*()\-\+]", password):
#         return False
#     return True
# # Kiểm thử:
# password = input("")
# if is_strong_password(password):
#     print("TRUE")
# else:
#     print("FALSE")
# def checkPassStrength(password):
#     # check password's length
#     if len(password) < 5:
#         return False
#     # Are there any uppercase, lowercase, number letters?
#     special_characters = "!@#$%^&*()-+"
#     if any(c in special_characters for c in password):
#         pass
#     else:
#         return False
#     count_uppercase = count_lowercase = count_number = 0
#     for Character in password:
#         if Character.isupper():
#             count_uppercase += 1
#         elif Character.islower():
#             count_lowercase += 1
#         elif Character.isdigit():
#             count_number += 1
#     if count_uppercase == 0 or count_lowercase == 0 or count_number == 0:
#         return False
#     # All the conditions were passed:
#     return True
# s = input()
# if (checkPassStrength(s)):
#     print("TRUE")
# else: print("FALSE")

# Đếm tần suất ký tự trong chuỗi
# n=list((input()))
# j = len(n)
# while True:
#     dem = 0
#     x = n[0]
#     print(x,end="")
#     for k in reversed(range(0,j)):
#         if n[k]==x:
#             dem+=1;
#             n.pop(k)
#     print(dem,end=" ")
#     j = len(n)
#     if j ==0: break

# Sudoku
# a=[]
# for i in range(0, 9):
#     a.append([(x) for x in input().split()])
# #check hang
# def checkRow(row):
#     temp= []
#     for i in range (0,9):
#         if a[row][i]!=".":
#             temp.append(int(a[row][i]))
#     if len(temp) != len(set(temp)):
#         return 0
#     return 1
# def checkCol(col):
#     temp = []
#     for i in range(0, 9):
#         if a[i][col] != ".":
#             temp.append(int(a[i][col]))
#     if len(temp) != len(set(temp)):
#         return 0
#     return 1
# #Check oo vuoong bes 3x3
# def checkSub():
#     for row in range (0,9,3):
#         for col in range (0,9,3):
#             temp =[]
#             for r in range(row,row+3):
#                 for c in range(col,col+3):
#                     if a[r][c]!=".":
#                         temp.append(int(a[r][c]))
#             if len(temp) != len(set(temp)):
#                 return 0
#     return 1
# dapan = "TRUE"
# if checkSub==0: print("FALSE")
# else:
#     for i in range(0,9):
#         if checkRow(i)*checkCol(i)==0:
#             dapan="FALSE"
#             break
#     print(dapan)

# Ma trận chuyển vị
# a = []
# b = []
# m, n = [int(x) for x in input().split()]
# b = [[0 for x in range(n)] for y in range(m)]
# for i in range(0, n):
#     a.append([int(x) for x in input().split()])
# for i in range(0,m):
#     for j in range(0,n):
#         b[i][j]=a[j][i]
# for i in range (0,m):
#     for j in range(0,n):
#         print(b[i][j], end=" ")
#     print()

# Ma trận xoắn ốc
# n = int(input())
# a = [[0 for x in range(n)] for y in range(n)]
# hang=0
# cot=n-1
# count = 1
# for i in range(0,n//2+1):
#     for j in range(hang,cot+1):
#         a[hang][j] = count
#         count+=1
#     for j in range (hang+1, cot+1):
#         a[j][cot] = count
#         count+=1
#     for j in reversed(range(hang,cot)):
#         a[cot][j] = count
#         count+=1
#     for j in reversed(range(hang+1,cot)):
#         a[j][hang]=count
#         count+=1
#     hang+=1
#     cot -=1
# for i in range(0, n):
#     print("{}".format(a[i]).replace(",", "").replace("[", "").replace("]", ""))

# Đảo ngược chuỗi
# def reverse_string(s: list) -> None:
#     left, right = 0, len(s) - 1
#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1
# # Nhận chuỗi đầu vào và chuyển thành list
# input_string = list(input("Nhập chuỗi của bạn: "))
# # Đảo ngược chuỗi
# reverse_string(input_string)
# # In kết quả
# print("".join(input_string))

# Gộp dãy số theo thứ tự
# Python program to merge two sorted arrays/
# def mergeArrays(arr1, arr2, n1, n2, arr3):
# 	i = 0
# 	j = 0
# 	k = 0
# 	# traverse the arr1 and insert its element in arr3
# 	while(i < n1):
# 		arr3[k] = arr1[i]
# 		k += 1
# 		i += 1
# 	# now traverse arr2 and insert in arr3
# 	while(j < n2):
# 		arr3[k] = arr2[j]
# 		k += 1
# 		j += 1

# 	# sort the whole array arr3
# 	arr3.sort()
# # Driver code
# m = int(input())
# arr1 = [int(x) for x in input().split()]
# n = int(input())
# arr2 = [int(x) for x in input().split()]
# arr3 = [0 for i in range(n+m)]
# mergeArrays(arr1, arr2, m, n, arr3)
# for i in range(n + m):
# 	print(arr3[i], end=" ")

# Sắp xếp giá trị bình phương
# def sorted_squares(nums):
#     n = len(nums)
#     # Khởi tạo mảng kết quả với tất cả giá trị là 0
#     result = [0] * n
    
#     # Khởi tạo hai con trỏ
#     left, right = 0, n - 1
#     position = n - 1  # Vị trí hiện tại trong mảng kết quả

#     while left <= right:
#         left_square = nums[left] ** 2
#         right_square = nums[right] ** 2

#         # So sánh hai giá trị bình phương
#         if left_square > right_square:
#             result[position] = left_square
#             left += 1
#         else:
#             result[position] = right_square
#             right -= 1

#         position -= 1

#     return result

# # Nhập mảng từ bàn phím
# input_str = input("Nhập mảng các số, cách nhau bởi dấu cách: ")
# nums = list(map(int, input_str.split()))

# print(sorted_squares(nums))

# n=int(input())
# x=int(input())
# A=[]
# for i in range(n):
#     k=int(input())
#     A.append(x)
# if x in A:
#     print(x,"co ton tai trong A")
    
 
# class Sinhvien:
#     def __init__(self, ma, ten, diem1, diem2):
#         self.MaSV = ma
#         self.HoTen = ten
#         self.Diem1 = diem1
#         self.Diem2 = diem2
#         self.DiemTB = (self.Diem1 + self.Diem2) / 2

#     def tinhtbSinhvien(self):
#         DiemTB=(self.Diem1 + self.Diem2) / 2


#     def printSinhvien(self):
#         print('[', self.MaSV, ']', '[', self.HoTen, ']', '[', self.Diem1, ']', '[', self.Diem2, ']', '[', self.DiemTB, ']')

# class DSSinhvien:
#     def __init__(self):
#         self.DSSV = []

#     def themSinhvien(self):
#         ma = input("Nhap ma sinh vien: ")
#         ten = input("Nhap go ten:")
#         diem1 = float(input())
#         diem2 = float(input())
#         newstudent = Sinhvien(ma, ten, diem1, diem2)
#         self.DSSV.append(newstudent)

#     def inDSSV(self):
#         for sv in self.DSSV:
#             sv.printSinhvien()

#     def tinhTBSV(self):
#         for sv in self.DSSV:
#             sv.tinhtbSinhvien()

#     def TBDiem1(self):
#         Tongmon1=0
#         for sv in self.DSSV:
#             Tongmon1=Tongmon1+sv.Diem1
#         return Tongmon1 / len(self.DSSV)

#     def TBDiem2(self):

#         Tongmon2=0
#         for sv in self.DSSV:
#             Tongmon2=Tongmon2+sv.Diem2
#         return Tongmon2 / len(self.DSSV)
    
#     def TBtong(self):
#         Tong=0
#         for sv in self.DSSV:
#             Tong=Tong+sv.DiemTB
#         return Tong/len(self.DSSV)

#     def xepHocLuc(self):
#         for sv in self.DSSV:
#             if sv.DiemTB >= 9: sv.HL = "Xuất sắc"
#             elif sv.DiemTB >= 8: sv.HL = "Giỏi"
#             elif sv.DiemTB >= 6.5: sv.HL = "Khá"
#             elif sv.DiemTB >= 5.0: sv.HL = "Trung Bình"
#             else: sv.HL = "Yếu"
# QLSV= DSSinhvien()
# ToDo=1
# while ToDo!=0:
#     print('\n   ***********************************************************')
#     print('   *                            * M E N U *                            *')
#     print('   *   1. Them sinh vien                         *')
#     print('   *   2. Xoa sinh vien                           *')
#     print('   *   3. Sua sinh vien                           *')
#     print('   *   4. Xem danh sach sinh vien                 *')
#     print('   *   5. Tinh diem trung binh cho tung sinh vien  *')
#     print('   *   6. Tinh diem trung binh mon1, mon2 cua toan bo sinh vien *')
#     print('   *   8. In thong tin sinh vien co diem trung binh cao nhat*')
#     print('   *   9. In thong tin sinh vien co diem trung binh thap nhat *')
#     print('   *   10. Sap xep danh sach sinh vien theo lop va diem trung binh *')
#     print('   *   11. Xep loai hoc luc cho tung sinh vien *')
#     print('   *   0. Thoat khoi chuong trinh  *')
#     print('>>>',end=' ')
#     ToDo=int(input("xin mời chọn chức năng"))
#     if ToDo==0:   break
#     elif ToDo==1:   
#         QLSV.themSinhvien()
#         print("Da them 1 sinh vien.")
#     elif ToDo==2: 
#         print("Nhap ma sinh vien cua SV muon xoa: ",end='')
#         maSV=input()
#         QLSV.XoaSinhVien(maSV)
#     elif ToDo==3:  
#         print("Nhap ma sinh vien cua SV muon sua thong tin: ",end='')
#         maSV=input()
#         QLSV.CapnhatSinhVien(maSV)
#     elif ToDo==4:
#         print("Danh sach sinh vien:\n")
#         QLSV.inDSSV()
#     elif ToDo==5: 
#         QLSV.tinhTBSV()  
#         print("Diem trung binh cua toan bo sinh vien da duoc tinh la:",QLSV.TBtong())
#     elif ToDo==6:
#         print("Diem trung binh mon1, mon2 cua toan bo sinh vien:",QLSV.TBDiem1(),QLSV.TBDiem2())
    
#     elif ToDo==11: 
#         QLSV.xepHocLuc()  
#         print("Toan bo sinh vien da duoc xep hoc luc.")
#     input("\nBam Enter de tiep tuc.")
# L=[1,3,2,5,8,4,9]
# for i in range(0, len(L)):
#     for j in range(i+1,len(L)):
#         if L[i]>L[j]:
#             a=L[j]
#             L[j]=L[i]
#             L[i]=a
# b=6
# for i in range( len(L),0,-1):
    # for j in range(i+1,len(L)):
    #     if L[i]>L[j]:
    #         a=L[j]
    #         L[j]=L[i]
    #         L[i]=a  \
    # if L[i]>b:
    #     L[i+1]=L[i]
    # else: 
    #     L[i+1]=b
    #     break    
        
# k=4  
# for i in range(0,len(L)):
#     if L[i]==k:
#         print(i)
#         L=L[:i]+L[(i+1):]   
# print(L)

# 1.	Định nghĩa các phép toán cho stack và sử dụng nó để chuyển cơ số từ cơ số 10, sang cơ số y
# class stack:
#     def __init__(self):
#         self.stack=[]
#         self.size=0
#     def push(self,x):
#         self.stack.append(x)
#         self.size+=1
#     def pop(self):
#         if self.size>0:
#             self.size-=1
#             return self.stack.pop()
#     def isEmpty(self):
#         if self.size>0: return False
#         else: return True
#     def getTop(self):
#         if self.size > 0:
#             return self.stack[self.size-1]
# a=int(input('Nhap so can chuyen: '))
# y=int(input('Chuyen sang co so: '))
# I = stack()
# Thuong = a
# while Thuong!= 0:
#     soDu=Thuong%y
#     I.push(soDu)
#     Thuong=Thuong//y
#     print(soDu)
# s=''
# while I.isEmpty is False:
#     s=s+str(I.pop())
# print (s)
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
# def Try(i, a, x):
#     for j in range(1, n + 1):
#         if a[j]:
#             x[i] = j
#             a[j] = False
#             if i == k:
#                 print(x[1:k+1])
#             else:
#                 Try(i+1, a, x)
#             a[j] = True
# n = 4
# k = 3
# a = [True] * (n + 1)
# x = [0] * (n + 1)
# Try(1, a, x)
# def mergeSort(arr):
#     if len(arr) > 1:
#         middle = len(arr) // 2
#         left_half = arr[:middle]
#         right_half = arr[middle:]
#         mergeSort(left_half)
#         mergeSort(right_half)
#         i = j = k = 0
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1
#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1
#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1
# arr = [38, 27, 43, 3, 9, 82, 10]
# mergeSort(arr)
# print("Danh sách đã sắp xếp:", arr)
# def insertion_sort(List):
#     for i in range (1,len(List)):
#         pos=List[i]
#         j=i-1
#         while j>=0 and List[j]>pos:
#             List[j+1]=List[j]
#             j=j-1
#         List[j+1]=pos
# L=[9,1,15,6,2,4,3,8]
# insertion_sort(L)
# print(L)
