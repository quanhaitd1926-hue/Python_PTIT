import smtplib 
server = smtplib.SMTP("localhost", 1025) 
from_addr = "alice@test.local" 
to_addr = "bob@test.local" 
msg = """Subject: Test Local Email 
Hello Bob, this is a test mail! 
""" 
server.sendmail(from_addr, [to_addr], msg) 
server.quit() 