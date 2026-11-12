x = str(input())
alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
glas = 'AEIYOU'
numb = '0123456789'
if x in numb:
    print('Является цифрой')
if x in alph or x in alph.lower():
    print('Является буквой')
    if x in glas or x in glas.lower():
        print('Является гласной')
    if x in alph:
        print('Является прописной')
    else:
        print('Является строчной')
if x not in alph and x not in alph.lower() and x not in numb:
    print('Символ не является ни буквой, ни цифрой')
