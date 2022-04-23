import time

tt = time.localtime()
current_time = time.strftime("%H:%M:%S", tt)
current_time2 = time.strftime("%H", tt)
print('Now ! ',current_time)
print('..........')
# print(type(current_time2))
t = int(current_time2)
# print(tt,type(tt))

if (5 <= t and t < 12):
    print("Good morning")
elif(t < 17):
    print("Good evening.")
else:
    print("Good night.")
print('..........')
print('Bye Bye.')


# # current_time = time.strftime("%H:%M:%S", t)
# current_time = time.strftime("%H", t)
# print(current_time)