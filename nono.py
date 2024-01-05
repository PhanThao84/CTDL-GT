
# # Bubble Sort
# # Sắp xếp theo thứ tụ tăng dần làm từ cuối lên 
def BubbleSort(a, n):
    for i in range (0,n-1):
        for j in range (n-1, i, -1):
            if(a[j]< a[j-1]):
                temp=a[j]
                a[j]=a[j-1]
                a[j-1]= temp
            j-=1
        i+=1
    return a
a=[1,2,3,7,8,10,9]
n=len(a)
b=BubbleSort(a,n)
print (b)
# # Sắp xếp theo thứ tụ tăng dần làm từ đầu lên 
# def BubbleSort(a, n):
#     for i in range (0,n-1):
#         for j in range (i+1,n):
#             if(a[j]< a[i]):
#                 temp=a[j]
#                 a[j]=a[i]
#                 a[i]= temp
#     return a
# a=[1,2,3,7,9,8,10]
# n=len(a)
# b=BubbleSort(a,n)
# print (b)
# # Sắp xếp theo thứ tự giảm làm từ đầu lên
# def BubbleSort(a, n):
#     for i in range (0,n-1):
#         for j in range (i+1,n):
#             if(a[j]>a[i]):
#                 temp=a[j]
#                 a[j]=a[i]
#                 a[i]= temp
#     return a
# a=[1,2,3,7,9,8,10]
# n=len(a)
# b=BubbleSort(a,n)
# print (b)
# # Sắp xếp theo thứ tự giảm làm từ cuối lên
# def BubbleSort(a, n):
#     for i in range (0,n-1):
#         for j in range (n-1, i, -1):
#             if(a[j]> a[j-1]):
#                 temp=a[j]
#                 a[j]=a[j-1]
#                 a[j-1]= temp
#     return a
# a=[1,2,3,7,9,8,10]
# n=len(a)
# b=BubbleSort(a,n)
# print (b)


# # Quick Sort 
# Sắp xếp theo thứ tự tăng dần
def quick_sort(arr,left,right):
    if left>=right:
        return
    pivot=arr[(left+right)//2]
    i,j=left,right
    while i<=j:
        while arr[i]<pivot:
            i+=1
        while arr[j]>pivot:
            j-=1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
    quick_sort(arr,left,j)
    quick_sort(arr,i,right)
arr=[1,2,4,3,7,9,8,10]
quick_sort(arr,0,len(arr)-1)
print (arr)
# # Sắp xếp theo thứ tự giảm dần
# def quick_sort(arr,left,right):
#     if left>=right:
#         return
#     middle=arr[(left+right)//2]
#     i,j=left,right
#     while i<=j:
#         while arr[i]>middle:
#             i+=1
#         while arr[j]<middle:
#             j-=1
#         if i<=j:
#             arr[i],arr[j]=arr[j],arr[i]
#             i+=1
#             j-=1
#     quick_sort(arr,left,j)
#     quick_sort(arr,i,right)
# arr=[1,2,4,3,7,9,8,10]
# quick_sort(arr,0,len(arr)-1)
# print (arr)



# def BinarySearch(a,x):
#     n=len(a)
#     left = 0
#     right = n - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if x == a[mid]:
#             return mid  # Tìm thấy x tại mid
#         if x < a[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return -1
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# x = 5
# result = BinarySearch(a, x) 
# print(result)

# def BinarySearchAndRemove(a, x):
#     n = len(a)
#     left = 0
#     right = n - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if x == a[mid]:
#             # Remove the element at the found index
#             del a[mid]
#             return mid  # Tìm thấy x tại mid
#         if x < a[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return -1
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# x = 5
# result = BinarySearchAndRemove(a, x)
# print("Result:", result)
# print("Updated list:", a)


# def BinarySearchAndUpdate(a, x, replacement):
#     left = 0
#     right = len(a) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if x == a[mid]:
#             # Replace the element at the found index with the replacement value
#             a[mid] = replacement
#             return mid  # Tìm thấy x tại mid
#         if x < a[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return -1
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# x = 5
# replacement_value = 99
# result = BinarySearchAndUpdate(a, x, replacement_value)
# print("Result:", result)
# print("Updated list:", a)
def linear_search(a, n, x):
    i = 0
    # Thêm phần tử lính canh vào cuối dãy
    a.append(x)
    while a[i] != x:
        i += 1
    # a[i] là phần tử có khoá x
    return i

# Mảng và giá trị cần tìm kiếm
arr = [1, 3, 5, 7, 9, 2, 4, 6, 8]
value_to_find = 6

# Gọi hàm và in kết quả
result_index = linear_search(arr, len(arr), value_to_find)
print(f"Giá trị {value_to_find} được tìm thấy tại vị trí {result_index}")
