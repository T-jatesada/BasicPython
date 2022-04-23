# while1.py

money = 1000
transfer = 10000

print('check', money < transfer)

while money < transfer:
    print('again please..')
    transfer = int(input('New transfer: '))
    if transfer > 1000000:
        print('GM !!!')
        break
    
print('OK.. transfered')