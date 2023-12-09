data = [int(i) for i in open('17_5.txt').readlines()]
answer_list = []
for i in range(len(data) - 1):
    if data[i] % 5 == 0 or data[i + 1] % 5 == 0:
        if (data[i] + data[i + 1]) % 7 == 0:
            answer_list.append(data[i] + data[i + 1])
print(len(answer_list), max(answer_list))

