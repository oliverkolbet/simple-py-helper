import time, random, smail

attfile = open('infolog.txt','r')
att = attfile.readlines()

print('welcome, '+att[0].strip())
while True:
	a = ''
	while a == '':
		a = input(att[5].strip())
	a = a.lower().split()
	if a == 'email' or a == 'mail':
		print('What email address do you want to email to?')
		eto = input(att[5]).lower()
		print('What is your email password? (We will \u001b[4m;not\u001b[0m; save this.)')
		smail.email(att[1], epw, eto, att[2])
