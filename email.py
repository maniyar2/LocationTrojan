import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("kamalimani1623@gmail.com", "QKR9uzQS7GT4m5WgWxxwgNZEXuu7FyZcE5EHEmQ8sVmQccfEAwWfnTVD52z9jUMTvmH8dBQgXHUnKaJhES3vmbJyYaxe3mZHa4xv")
 
msg = "YOUR MESSAGE!"
server.sendmail("kamalimani1623@gmail.com", "kamalimani1623@gmail.com", msg)
server.quit()
