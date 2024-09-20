def find_password(num):
    result = ""
    for i in range(1, num):
        for j in range(i + 1, num + 1):
            k = i + j
            if num % k == 0:
                result += f'{i}{j}'
    return result
import random
num = random.randint(3, 20)
result = find_password(num)
print("Случайное число", num, "пароль: ", result)
