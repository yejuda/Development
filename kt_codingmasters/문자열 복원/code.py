# 알파벳은 1~26까지 존재한다.
# 세번째 자리수가 0이고 1,2자리수가 10~26이면 1,2 자리수를 알파벳으로 변환.
# 1,2자리수가 1~9이면 그 값 그대로 알파벳으로 변환
# 입력이 1100인 경우 앞에서 부터 숫자를 알파벳으로 변환하면, 끝나 0에서 변환이 제대로 이루어지지 않는다.
# 숫자가 두자리인 경우, 뒤에 무조건 0이 붙는다.
# 10,20인 경우는 따로 처리를 해야 한다.

# 1601180201
# 1100

n = str(input())
tmp = []
i = len(n)-1   # 입력받은 문자열의 인덱스 위치

while i >= 0:
    # 세자리 숫자이고, 백/십의자리가 알파벳 범위에 해당하고, 일의자리가 0일 경우 chr(11 + ord('a')-1)  # 1100
    if (i-2 >= 0) and (int(n[i]) == 0) and (10 <= int(n[i-2:i]) <= 26):
        tmp.append(chr(int(n[i-2:i]) + ord('a') - 1))
        i -= 3
    # 두자리 숫자이고, 알파벳 범위에 해당하는 경우(10, 20에 대한 경우 확인)
    elif (i-1 >= 0) and (10 <= int(n[i-1:i]) <= 26):
        tmp.append(chr(int(n[i-1:i]) + ord('a') - 1))
        i -= 2
    # 한자리 숫자이고, 알파벳 범위에 해당하는 경우(1~9)
    else:
        tmp.append(chr(int(n[i]) + ord('a') - 1))
        i -= 1

# 거꾸로 탐색했으므로 reverse하기.
tmp = tmp[::-1]

print(''.join(tmp))
