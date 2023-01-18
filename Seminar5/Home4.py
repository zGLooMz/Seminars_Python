# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('H:\Python\Seminars_Python\Seminar5\RLEdecoded.txt', 'r') as data:
    decoded_text = data.read()

def writeFile1(st):
    with open('H:\Python\Seminars_Python\Seminar5\RLEdecodedResult.txt', 'w') as data:
        data.write(st)

def encode_rle(text):

    str_code = ''
    prev_char = ''
    count = 1
    if not text: return ''
    for char in text:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        str_code += str(count) + prev_char

    return str_code
            
str_code = encode_rle(decoded_text)
writeFile1(str_code)
print(f'Исходный текст ->', decoded_text)
print(f'После сжатия   ->', str_code)

with open('H:\Python\Seminars_Python\Seminar5\RLEencoded.txt', 'r') as data:
    encoded_text = data.read()

def writeFile2(st):
    with open('H:\Python\Seminars_Python\Seminar5\RLEencodedResult.txt', 'w') as data:
        data.write(st)

def decoding_rle(text:str):
    count = ''
    str_decode = ''
    for char in text:
        if char.isdigit():
            count += char 
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

str_decode = decoding_rle(encoded_text)
writeFile2(str_decode)
print(f'Исходный текст      ->', encoded_text)
print(f'После востановления ->',str_decode)

