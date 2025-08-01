metros = float(input('Digite um valor: '))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000
print('A medida de {} metros corresponde a:'.format(metros))
print('{} km'.format(km))
print('{} hm'.format(hm))
print('{} dam'.format(dam))
print('{:.0f} dm'.format(dm))
print('{:.0f} cm'.format(cm))
print('{:.0f} mm'.format(mm))