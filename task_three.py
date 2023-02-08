# задача RLE необязательная. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (где только буквы присутствуют для простоты).
# например декодирование
# https://stepik.org/lesson/21300/step/2


# Sample Input:
# 3ab4c2CaB

# Sample Output:
# aaabccccCCaB

data_in = input('введи строку: ')
text = list(data_in)
text_len = len(text)
resultlist = []
for i in range(text_len):
    count = 0
    if text[i].isdigit():
        count = int(text[i])
        for k in range(count-1):  
            resultlist.append(text[i+1])
    else:
        resultlist.append(text[i]) 
res_string = ''.join(resultlist)
print(res_string)