# def profile(name, age=17, main_lang="python"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

# profile("유재석")
# profile("김태호")


def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(age=20, main_lang="파이썬", name="유재석")
profile(main_lang="자바", name="김태호", age=25)