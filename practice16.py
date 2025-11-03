# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in range(0, 6):
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print(f"{customer}, 커피가 준비되었습니다.")


#while
# customer = "토르"
# index = 5
# while index >= 1:
#     print(f"{customer}, 커피가 준비되었습니다. {index}번 남았어요.")
#     index -= 1
#     if index == 0:
#         print("커피가 폐기처분되었습니다.")
#         break

# customer = "아이언맨"
# index = 1
# while True:
#     print(f"{customer}, 커피가 준비되었습니다. 호출 {index}회")
#     index += 1


# curtomer = "토르"
# person = "Unknown"

# while person != curtomer:
#     print("{0}, 커피가 준비되었습니다".format(curtomer))
#     person = input("이름이 어떻게 되세요? ")



# absent = [2, 5]
# no_book = [7]
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))   
#         break
#     print("{0}, 책을 읽어봐".format(student))

students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

students = ["iron man", "thor", "i am groot"]
students = [i.replace("i", "I") for i in students]
print(students)

