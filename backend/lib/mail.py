def log(msg):
	print(msg)

class MailConfig:
	POP_FUDAN = "mail.fudan.edu.cn" 
	SMTP_FUDAN = "mail.fudan.edu.cn"

	POP_163 = "pop3.163.com"
	SMTP_163 = "smtp.163.com"

import poplib, smtplib
from email import message_from_string, mime
from email.utils import *
from email.Header import decode_header

class PopClient:
	def __init__(self, user, pwd, host = MailConfig.POP_FUDAN):
		self.server = poplib.POP3(host)
		self.server.user(user)
		self.server.pass_(pwd)
	
	def count(self):
		"""
		return number of mails
		"""
		return self.server.stat()[0]

	def fetch(self, index):
		"""
		index starts from 1
		"""
		raw = self.server.top(index, 0)[1]
		msg = message_from_string('\n'.join(raw))
		ret = {}
		for item in ['From', 'Date']:
			ret[item] = decode_header(msg[item])
			for x in range(len(ret[item])):
				ret[item][x] = ret[item][x][0]
		tmp = decode_header(msg['Subject'])
		if tmp[0][1]:
			ret['Subject'] = tmp[0][0].decode(tmp[0][1])
		ret['Date'] = mktime_tz(parsedate_tz(ret['Date'][0]))
		return ret

class SmtpClient:
	def __init__(self, user, pwd, host = MailConfig.SMTP_FUDAN):
		self.server = smtplib.SMTP(host)
		self.server.login(user, pwd)
			
	def send(self, fro, to, subject, content):
		"""
		send an email from 'fro' to 'to'
		'to' should be a list
		"""
		msg = mime.Multipart.MIMEMultipart()
		msg['From'] = fro
		msg['To'] = ', '.join(to)
		msg['Subject'] = subject 
		msg['Date'] = formatdate(localtime=True) 
		msg.attach(mime.Text.MIMEText(content.encode('utf-8')))
		
		self.server.sendmail(fro, to, msg.as_string())

if __name__ == '__main__':
	pass
	#smtp.send("10300240067@fudan.edu.cn", ["x_c0@163.com"], "tasdasdest", "hehehehehehe")
