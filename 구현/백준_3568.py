string = input()

string_list = string.split(' ')

basic_type = string_list[0]

# 삭제
del string_list[0]

for s in string_list:
    s = s.replace(",", '').replace(";", '')
    print(basic_type, end='')

    # 뒤에서 부터 출력
    for i in range(len(s) - 1, 0, -1):

        # 알파벳이 아닌 추가적인 변수형 출력
        if not s[i].isalpha():
            if s[i] == ']':
                print('[', end='')
            elif s[i] == '[':
                print(']', end='')
            else:
                print(s[i], end='')

    # 공백 출력
    print(' ', end='')

    # 기본 변수명(알파벳) 출력
    for i in range(len(s)):
        if s[i].isalpha():
            print(s[i], end='')

    # 세미콜론(';') 출력
    print(';')