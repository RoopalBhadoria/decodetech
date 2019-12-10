import smtplib


server=smtplib.SMTP('smtp.gmail.com',587)

server.ehlo()

server.starttls()

server.login("sender's gmail" ,"sender's gmail password")

server.sendmail("sender's gmail","receiver's gmail", 'Hey !! Good Evening !!')

server.quit()
