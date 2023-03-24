import smtplib

my_email = "mailfromtanvir1@gmail.com"
password = "bcszqwwuzdzobkyq"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user = my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="hasan22205101035@diu.edu.bd",msg="Subject:This Email sent using Python\n\nHello Mahdi,\nRamadan Kareem. I am a Bot named Tobot and this massage is sent by me.\nThank You from Tanvir.")
connection.close()