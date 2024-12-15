with open('input_7_2.txt', 'r', encoding='utf-8') as f:
    text = f.read()

count_dict = {}

for ch in text:
    if ch.isalpha():
        ch = ch.upper()
        count_dict[ch] = count_dict.get(ch, 0) + 1

items_list = list(count_dict.items())
items_list.sort(key=lambda x: x[1], reverse=True)

result_list = [item[0] for item in items_list]

print(result_list)