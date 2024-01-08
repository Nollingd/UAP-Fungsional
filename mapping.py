result = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 1, range(10))))
print(result)