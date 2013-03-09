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
		for item in ['From', 'Subject', 'Date']:
			ret[item] = decode_header(msg[item])
			for x in range(len(ret[item])):
				try:
					ret[item][x] = ret[item][x][0].decode(ret[item][x][1]) if ret[item][x][1] else ret[item][x][0]
				except:
					ret[item][x] = ret[item][x][0]
		ret['From'] = ret['From'][1] if len(ret['From']) == 2 else ret['From'][0]
		ret['Subject'] = ret['Subject'][0]
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
		msg.attach(mime.Text.MIMEText(content.encode('utf-8'), 'plain','UTF-8'))
		
		self.server.sendmail(fro, to, msg.as_string())

if __name__ == '__main__':
	me = '10300240067@fudan.edu.cn'
	tg = 'x_c0@163.com'
	sub = 'hello'
	pop = PopClient('10300240067@fudan.edu.cn', 'z8dfn33_m221s')
	smtp = SmtpClient('RippleServer@163.com', 'chaomataiqiangle', 'smtp.163.com')
	#smtp.send("10300240067@fudan.edu.cn", ["x_c0@163.com"], "tasdasdest", "hehehehehehe")
