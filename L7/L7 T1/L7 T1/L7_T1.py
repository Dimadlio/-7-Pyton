a1=(input('Введите слово что бы определить является ли она палиндромом:'  ))
a2=a1[::-1]
if a2==a1:
    print('Yes')
else:
    print('No')