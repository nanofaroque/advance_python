def next_square():
    i = 1
    while True:
        yield i * i
        i += 1


for num in next_square():
    if num > 100:
        break
    print(num)
