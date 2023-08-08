import telepot
import random
import time, datetime
import RPi.GPIO as GPIO
from telepot.loop import MessageLoop


now = datetime.datetime.now()


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)


def action(msg):

    chat_id = msg['chat']['id']

    command = msg['text']


    print('Received: %s' % command)


    if command == '/Hi':

        telegram_bot.sendMessage (chat_id, str("Chào bạn, rất vui khi được gặp bạn"))

    elif command == '/time':

        telegram_bot.sendMessage(chat_id, str(now.hour)+str(":")+str(now.minute))

    elif command == '/Logo':

        telegram_bot.sendPhoto(chat_id, photo = open('/home/pi/Desktop/project/anh.jpg', 'rb'))

    elif command == '/File':

        telegram_bot.sendDocument(chat_id, document= open('/home/pi/Desktop/project/tele.py'))

    elif command == '/Audio':

        telegram_bot.sendAudio(chat_id, audio = open('/home/pi/Desktop/project/nhac.mp3', 'rb'))
        
    elif command == '/soso':
        
        telegram_bot.sendMessage(chat_id, str(random.randint(1, 100)))
        
    elif command == '/onled1':
        print('onled1')
        GPIO.output(3, GPIO.HIGH)
    elif command == '/offled1':
        print('offled1')
        GPIO.output(3, GPIO.LOW)
        
    elif command == '/onled2':
        print('onled2')
        GPIO.output(5, GPIO.HIGH)
    elif command == '/offled2':
        print('offled2')
        GPIO.output(5, GPIO.LOW)
    elif command == '/onled3':
        print('onled3')
        GPIO.output(7, GPIO.HIGH)
    elif command == '/offled3':
        print('offled3')
        GPIO.output(7, GPIO.LOW)
    elif command == '/onledall':
        print('onled 1 2 3')
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(7, GPIO.HIGH)
    elif command == '/offledall':
        print('offled 1 2 3')
        GPIO.output(3, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(7, GPIO.LOW)
telegram_bot = telepot.Bot('6031958610:AAFFSFpnzqLz2nmQPXjvFsFmX4lpxToDBqM')

print (telegram_bot.getMe())


MessageLoop(telegram_bot, action).run_as_thread()

print('Up and Running....')


while 1:

    time.sleep(2)