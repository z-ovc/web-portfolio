import smtplib, ssl
ssl._create_default_https_context = ssl._create_unverified_context


def send_mail(msg):
    host = "smtp.gamil.com"
    port = 465
    context = ssl.create_default_context()
    username = "zazaovc44@gmail.com"
    password = "13741374z"
    msg = "salam"
    receiver = "statistiker74@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg)
print(ssl.get_default_verify_paths().openssl_cafile)
send_mail("sss")