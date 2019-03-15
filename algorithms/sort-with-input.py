print('write nums and press enter')
print(' for the end press enter')

a = int(input('-->> '))
rices = []

while True:
    try:
        rices.append(a)
        rices.sort()
        a = int(input('-->> '))
    except:
        break
print(rices)
