print('----------- \033[97;44mTABUADA\033[m -----------')
tb = int(input('A tabuada de qual número você quer que mostre? '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(tb, c, c*tb))
print('--FIM--')
