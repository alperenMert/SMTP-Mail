#SMTP ile TLC üzrinden mail gönderme işlemi

import smtplib
from email.mime.text import MIMEText
#mimetext utf-8 ayarlaması

smtp_adres= "smtp.gmail.com"
smtp_port= 587
kullanici_adi= "...@gmail.com"
sifre= "şifre"

gonderilecek_adres= ["...@gmail.com"]
konu= "Deneme"
icerik="""
Python ile gönderilecek mail içeriği
<br><br>
Merhaba bu bir test mesajıdır   
"""

try:
    #e-mail verilerinin düzenlenmesi
    mail=MIMEText(icerik, "html", "utf-8")

    #gönderilen mail adresi
    mail["From"]=kullanici_adi

    #mail konusu
    mail["Subject"]= konu

    #mailin gönderileceği adres
    mail["To"]=", ".join(gonderilecek_adres)

    #mail bilgilerinin düzenlenmesi
    mail=mail.as_string()

    #bilgilendirme mesajı
    print("Lütfen bekleyin...")

    s= smtplib.SMTP(smtp_adres, smtp_port)

    #TLS bağlantısı(Şifreli bağlantı)
    s.starttls()

    #SMTP sunucusuna giriş
    s.login(kullanici_adi, sifre)

    #Gönder
    s.sendmail(kullanici_adi, gonderilecek_adres, mail)
    print("Mail gönderme işlemi başarılı.")

except Exception as e:
    print(str(e))







