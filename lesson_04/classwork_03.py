n = int(input())
result = 0

while n >= 0:
    result += n ** 3
    n -= 1
print(result)