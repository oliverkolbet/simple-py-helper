import time, random, smail

attfile = open('infolog.txt','r')
att = attfile.read().split('\n')
name = att[0]
prompt = att[5]
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
		print('What is your email password? (We will \u001b[4m;not\u001b[0m; save this.)')
		epw = input(prompt)
		smail.email(att[1], epw, eto, att[2])
	elif a[0] == 'exit' or a[0] == 'quit' or a[0] == 'leave' or a[0] == 'bye' or a[0] == 'goodbye':
		print('Helper ended. info synced.')
		break
	elif a[0] == 'prompt':
		print('What do you want your prompt to be? Default is ">".')
		prompt = input(prompt)
		attfile = open('infolog.txt','w+')
		att = attfile.readlines()
		att[5] = prompt
		print('Prompt is now '+prompt)
