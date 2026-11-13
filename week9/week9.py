# def is_odd(n):
#     if n%2 != 0:
#         return "True"
#     else:
#         return "False"
# #return n%2 == 1 bu da olur.
# print(is_odd(8))


# def find_leap_year(year):
#     if year % 400 == 0:
#         return "True"
#     elif year % 100== 0:
#         return "False"
#     elif year % 4 == 0:
#         return"True"
#     else:
#         return"False"
# print(find_leap_year(2000))


# def print_triangular_numbers(n):
#     total = 0
#     for i in range(1,n+1):
#         total = total +i
#         print(i,total)
# print_triangular_numbers(6)


# def is_prime(n):
#     if  n<2:
#         return "False"
#     for i in range(2,n):
#         if n%i == 0:
#             return "False"
#     return "True"
# print(is_prime(9))



# def reverse_slice(s):
#     return s[::-1]
#
# print(reverse_slice("hello world"))


# def remove_all_occurrences(sub,s):
#     return s.replace(sub,"")
# print(remove_all_occurrences("l","Hello World"))
#


# def substitute(message,key):
#     alphabet ="abcdefgğhıijklmnoöprsştuüvyz"
#     result=""
#     for ch in message:
#         index = alphabet.find (ch.lower())
#         if index == -1:
#             result = result + ch
#         elif ch.isupper():
#             result + result + key[index].upper()
#         else:
#             result = result + key[index].lower()
#     return result
#
# key = "qtghfjhjklopşğpıuytmbniçöxmer"
# print (substitute("helloworld",key))



# def remove_dups(string):
#     result = ""
#     for char in string:
#         if char not in result:
#             result += char
#
#     return result
# print(remove_dups("helloo world"))