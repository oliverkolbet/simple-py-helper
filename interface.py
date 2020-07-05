import time, random, smail, pomodoro
from threading import Thread

def fileadd(text, number):
	attfile = open('infolog.txt','r')
	att = attfile.read()
	att = att.split('|')
	att[number] = text
	attfile = open('infolog.txt','w')
	attfile.write('|'.join(att))



attfile = open('infolog.txt','r')
att = attfile.read()
att = att.split('|')
name = att[0]
prompt = att[5].strip()
email = att[1]
prov = att[4]
nick = att[2]
bio = att[3]

print('welcome, '+name)
while True:
	a = ''
	while a == '':
		a = input(prompt)
	a = a.lower().split()
	if a[0] == 'email' or a[0] == 'mail':
		print('What email address do you want to email to?')
		eto = input(prompt)
		print('What is your email password? (We will \u001b[4mnot\u001b[0m save this.)')
		epw = input(prompt)
		smail.email(att[1], epw, eto, att[2])
	elif a[0] == 'exit' or a[0] == 'quit' or a[0] == 'leave' or a[0] == 'bye' or a[0] == 'goodbye':
		print('Helper ended. info synced.')
		timer_thread.stop()
		break
	elif a[0] == 'prompt':
		print('What do you want your prompt to be? Default is ">".')
		prompt = input(prompt)
		attfile = open('infolog.txt','r')
		att = attfile.read()
		att = att.split('|')
		att[5] = prompt
		attfile = open('infolog.txt','w')
		attfile.write('|'.join(att))
		print('Prompt is now '+prompt)
	elif a[0] == 'timer' or a[0] == 'pomodoro':
		timer_thread = Thread(target=pomodoro.run, args=(pomodoro.main()))
		timer_thread.start()
	elif a[0] == 'name':
		print('What would you like your name to be?')
		name = input(prompt)
		fileadd(name, 0)
