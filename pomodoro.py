#Basic pomodoro timer widget
#Uses main() for testing
#version 1

import time, os

def main():
	global mlength, mbreaklen, mbreak, mendcm, mcm
	mbreaklen = ''
	mcm = ''
	print('Welcome to the simple pomodoro!')
	print('How much time do you want the timer to run for?')
	mlength = input('=>')
	mlength = float(mlength)
	print('Do you want a break in between sessions?')
	mbreak = input('=>')
	if 'y' in mbreak.lower():
		mbreak = True
		print('How long do you want the break to be?')
		mbreaklen = input('=>')
		mbreaklen = float(mbreaklen)
	else:
		mbreak = False
	print('Do you want a shell command to run at the end?')
	mendcm = input('=>')
	if 'y' in mendcm.lower():
		mendcm = True
		print('What command do you want?')
		mcm = input('=>')
	else:
		mendcm = False
	return mlength, mbreaklen, mbreak, mendcm, mcm
def run(length, breaklen, breakt, endcm, cm):
	while True:
		print('Timer starting at '+str(length)+'.')
		time.sleep(length*60)
		if endcm == True:
			os.system(cm)
			print('Shell command "'+cm+'" has been run.')
		if breakt == True:
			print('Time up! take a '+str(breaklen)+' minute break.')
			time.sleep(60*breaklen)
			print('Type anything or press enter to start the next session. Otherwise, type "end".')
			ctn = input('=>')
			if ctn.lower() != 'end' and ctn.lower() != 'quit':
				print('Starting next '+str(length)+' minutes...')
			else:
				print('Timer ended.')
				break
		else:
			print('Session ended.')
if __name__ == '__main__':
	main()
