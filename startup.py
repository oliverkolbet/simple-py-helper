#file is a placeholder while other files are being made.
from time import sleep

name = ''
email = ''
nick = ''
bio = ''
prov = ''

print('Hello! welcome to version 1 of the python helperBot.')
sleep(0.6)
print('What is your name?')
name = input('>')
sleep(0.6)
print('Hello, '+name+'!')
sleep(0.7)
print('What would you like me to call you?')
nick = input('>')
sleep(0.6)
print('We need your email for our email service.')
print('What is your email?')
email = input('>')
print('We also need the name of your provider.i.e, Gmail, Hotmail, Yahoo, etc')
prov = input('>').lower()
print('Thanks! Now, could you tell us a little about yourself?')
bio = input('>')
print('Alright! finishing up some things and then your helper will be ready!')
info = [name, '\n', email, '\n', nick, '\n', bio, '\n', prov]
attfile = open('infolog.txt','w')
attfile.writelines(info)
sleep(3)
print('Done!')
