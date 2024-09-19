def generate_password(num):
    password = []
    for i in range(1, 21):
        for j in range(1,21):
            if num % (i + j) == 0:
                password += str(i)
                password += str(j)
    return password
num = int(input('Введите число: '))
if 3 <= num <= 20:
    result = generate_password(num)
    print(result)
else:
    print('Error')
