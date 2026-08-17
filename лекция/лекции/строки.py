"""Строки начальный курс"""
""" 0123456789"""

s = 'Здравствуйте, гости!'


print(s[19])
print(s[:12])
print(s[4:])
print(s[4::-1])
print(s[::-1])
s1 = 'казак'
print(s1[:])
print(s1[::-1])

if s1 == s1[::-1]:
    print('yes')
else:
    print ('No')
print(__doc__)

s = 'ЗдраВствуйте, гости!\n'
s1 = '34567п'
print(s1.isalpha())  #состоит ли строка из букв
print(s1.isdigit()) #состоит ли строка из цифр
print(s1.isalnum()) #состоит ли строка из букв и / или цифр
print(s1.isspace()) #является ли строка пробелом
print(s.isupper()) # #все ли в строке буквы прописные
print(s.islower()) # #все ли в строке из букв
print(s.startswith('ЗдраВ')) #начинается ли строка с подстроки в скобках
print('раВ' in s) #входит ли подстрока в переменную s
print(s.endswith('!')) # входит ли знак в строку
s1 = s.lower()
print(s, s1)
print(s.upper()) # все буквы строчные
#s = '\033[4mЗдраВствуйте, гости!\033[0m' # режим подчеркивания
print(s)
print(s.title())
print(s.capitalize())
print(s.center(40))
print(s.rjust(40))
print(s.ljust(40))
print(s.swapcase())
print(s.strip('! З'))
print(s.rstrip())
print(s.lstrip())
print(s.index( 'т',  7, 11))
print(s.find('т',  11, 20))
print(s.replace('т', 'Т', 2).replace(',', '.'))
ls = s.split(', ') #превращает строку на список слов по разделетилю
print(ls)
print(''.join(ls))  #собирает строковые объекты списка в строку

# s1 = 'aaa bbb ccc ddd eee fff '
# s2 = '111 222 333 444 '
# # 'aaa 111 bbb 222 ccc 333 ddd 444'
# res=''
# for i in range(0, len(s2), 4):
#     res += s1[i:i + 4] + s2[i:i + 4]
#
#
# print(res)

s = '12x^2 +4x-6=0'





# for i in range(len(s)):
#     print(i, s[i], end='   ')
# print()
# for i in s:
#     print(i, end=' ')
# print()
# print(len(s))
# #101 = 1 * 2**2 + 2**0
#       4   +   1   = 5