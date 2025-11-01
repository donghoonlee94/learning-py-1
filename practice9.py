# 사이트별로 비밀번호를 만들어주는 프로그램
url = "http://naver.com"
my_str = url.replace("http://", "")
# 처음부터 . 이전까지 문자열 추출
my_str = my_str[:my_str.index(".")]
print(my_str.count("e"))
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password))