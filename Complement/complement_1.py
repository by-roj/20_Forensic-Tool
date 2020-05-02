message = 'B8 9B 8C E0 89 9F 9D 98 8C 89 91 91 8E 9C E0 97 8D E0 BD 91 AB 92 8C'

num = message.split(' ')
num2 = []

for i in range(0, len(num)):
    result = ''

    binary = int(num[i], 16)
    binary = bin(binary)
    binary = binary[2:]

    # 2's complement(2의 보수) 계산
    result = (0xFF ^ int(binary, 2)) + 1  

    result = chr(result)
    num2.append(result)

res_msg = ''.join(num2)
print(res_msg)
