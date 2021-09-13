files = ['1.txt', '2.txt', '3.txt']

def get_file_length(files):
    res = []
    for name in files:
        with open(name, encoding="utf8") as file:
            data = file.readlines()
            res.append((name, len(data), data))
    return res

res = sorted(get_file_length(files), key = lambda i:i[1])

for i in res:
    with open("result.txt", "a", encoding="utf8") as file:
        file.write(i[0] + '\n')
        file.write(str(i[1]) + '\n')
        for line in i[2]:
            file.write(line)
        file.write('\n')
    print(i)