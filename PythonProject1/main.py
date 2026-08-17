h = float(input(' ведите время суток: '))
if h >= 4 and h < 12:
    print('Morning')
elif 12 <= h < 17:
    print('Day')
elif h >= 17 and h < 24:
    print('Evening')
elif h >= 0 and h < 4 or h ==24:
    print('Night')
else:
    print('Время суток не соответствует.')