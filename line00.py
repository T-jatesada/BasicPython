# pip install songline
# From: jate[BOT]
# To: Uncle Line Bot Test
#######################################################################
from songline import Sendline

token = 'YfdYitzp7mZ0UINxWOgq92MQXXo4vcFHQPS2GquSp8V'
pic = 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png'

messenger = Sendline(token)

#send message
# messenger.sendtext('5555')

#send sticker
# messenger.sticker(620,4)

#send image
messenger.sendimage(pic)