#email service for the helperbot
import smtplib
from email.mime.text import MIMEText

sev = {
'hotmail':['live.com',465],
'gmail':['gmail.com',587],
'yahoo':['mail.yahoo.com',465],
'aruba':['aruba.it',465]
}

def main():
	print('Your email address:')
	address = input('>')
	print('Password:')
	passw = input('>')
	print('send to:')
	sendto = input('>')
	print('email provider:')
	provider = input('>').lower()
	email(address, passw, sendto, provider)
def email(addr, pw, to, prov='gmail'):
	print('Subject:')
	subject = input('>')
	print('Type email below:')
	body  = input('>')
	msg = MIMEText(body)

	msg['From'] = addr
	msg['To'] = to

	msg['Subject'] = subject

	server = smtplib.SMTP('smtp.'+sev[prov][0], sev[prov][1])

	if prov != 'hotmail':
		server.starttls()
	server.login(addr, pw)
	server.sendmail(addr, to, msg.as_string())
	server.quit()
	print('Email sent.')



if __name__ == '__main__':
	main()
