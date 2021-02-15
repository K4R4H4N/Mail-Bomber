import smtplib
from time import sleep as sp

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('senderdcoder@gmail.com', 'hellodcoder')
target = str(input("Kurbanın Mailini Giriniz\t \n"))
msg = str(input("\n Mesajınızı Giriniz \t \n"))
try:
  amount = int(input("\n Kaç Tane Gönderelim \n"))
except:
  print("\n Bitti <INT>. Program Durdu.|<")
  sp(1)
  quit()
if amount > 20:
  print("\n Üzgünüz.")
  sp(0.5)
  print("En Fazla 20 Tane !!!!")
  amount = 20
  sp(1.5)
  print("\n Otomatik Olarak 20 Tane Gönderiliyor")
sp(2)
print("\n ....")
sp(1)
print("\n Gönderiliyor.... \n \t")
for i in range(amount):
  try:
    server.sendmail('recentalydcoder@gmail.com', target, msg)
  except:
    print("Mail Bulunmadı Moruq. Başka Dene. ")
  finally:
    print()