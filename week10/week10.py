# myList=[76,92.3,"hello",True,4,76]
# myList.append("apple")
# myList.append(76)
# myList.insert(3,"cat")
# myList.insert(0,99)
# print(myList)
# print(myList.index("hello"))
# print(myList.count(76))
# myList.remove(76)
# print(myList)
# myList.pop(myList.index(True))
# print(myList)
#

#
# def sum_of_squares(list):
#     sum= 0
#     for number in list:
#         sum += number**2
#     return sum
# list=[1,2,3,4,5]
# print(sum_of_squares(list))


# myList=[1,2,3,4,5,6,7,8,9]
# def sum_even_numbers(myList):
#    total=0
#    for number in myList:
#        if number % 2== 0:
#            total+= number
#    return total
# print(sum_even_numbers(myList))



# def count_five_letter(words):
#     counter=0
#     for word in words:
#         if len(word)==5:
#             counter += 1
#     return counter
# words = ["apple","cat","lemon","python"]
# print(count_five_letter(words))


# def sum_odd_number(list):
#     sum= 0
#     for number in list:
#         if number%2==0:
#             break
#         sum += number
#     return sum
# list= [1,3,4,5,6,7,8,9]
# print(sum_odd_number(list))


# def count_words_until_sam(words):
#     counter =0
#     for word in words:
#         if word == "sam":
#             counter += 1
#             break
#         counter += 1
#     return counter
# words=["alice","bob","sam","jone"]
# print(count_words_until_sam(words))




# def replace(s, old, new):
#     pieces= s.split(old)
#     return new.join(pieces)
#
#
# def test(actual,expected):
#     if actual == expected:
#         print("passed")
#     else:
#         print("failed")
# test(replace("Mississippi","i","I"),"MIssIssIppI")



# def max(list):
#     biggest = list[0]
#     for x in list:
#         if x > biggest:
#             biggest = x
#     return biggest
# list = [1,2,3,4,5,6,7]
# print(max(list))