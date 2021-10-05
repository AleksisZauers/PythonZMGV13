
bums=open('aste.txt', 'r', encoding='utf-8')
print(bums.read())

bums=open('aste.txt', 'x', encoding='utf-8')
print(bums.read())


bums.close()