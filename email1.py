import smtplib
smtpserver='smtp.gmail.com:587'
server = smtplib.SMTP(smtpserver)
server.starttls()
server.login('kamalimani1623@gmail.com','QKR9uzQS7GT4m5WgWxxwgNZEXuu7FyZcE5EHEmQ8sVmQccfEAwWfnTVD52z9jUMTvmH8dBQgXHUnKaJhES3vmbJyYaxe3mZHa4xv')
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
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
    print('I did it mom')
    server.sendmail('kamalimani1623@gmail.com', 'kamalimani1623@gmail.com', 'maybe this works, idk')
    #server.quit()
