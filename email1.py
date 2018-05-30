import smtplib
import socket  
smtpserver='smtp.gmail.com:587'
server = smtplib.SMTP(smtpserver)
server.starttls()
server.login('kamalimani1623@gmail.com','QKR9uzQS7GT4m5WgWxxwgNZEXuu7FyZcE5EHEmQ8sVmQccfEAwWfnTVD52z9jUMTvmH8dBQgXHUnKaJhES3vmbJyYaxe3mZHa4xv')
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              smtpserver='smtp.gmail.com:587'):
    #import smtplib
    global server
    header = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    if not cc_addr_list is None:
        header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message

    #server = smtplib.SMTP(smtpserver)
    #server.starttls()
    #server.login(login,password)
    server.sendmail(from_addr, to_addr_list, message)
    #server.quit()	
hostname = socket.gethostname()   
IPAddr = socket.gethostbyname(hostname)   
print("Your Computer Name is:" + hostname)   
print("Your Computer IP Address is:" + IPAddr)   
sendemail("kamalimani1623@gmail.com", "kamalimani1623@gmail.com", "None", "Lizo", "Your Computer IP Address is:" + IPAddr)
