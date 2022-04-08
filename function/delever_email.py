from yagmail.sender import SMTP


def save_email_info(info):
    f = open('./assets/email_info.yml', 'r+', encoding='utf-8')
    f.truncate()
    f.write(info)
    f.close()


def read_email_info():
    f = open('./assets/email_info.yml', 'r+', encoding='utf-8')
    final = f.read()
    final = final.split(',')
    f.close()
    return final


def deliver_email(mail_user, mail_pass, mail_port, title, text):
    # mail_user = '2232195659@qq.com'
    # mail_pass = 'pqmzuteevictdjjj'
    # mail_port = 'smtp.qq.com'
    mail = SMTP(user=mail_user, password=mail_pass, host=mail_port, smtp_ssl=True)
    mail.send(
        to=mail_user,
        subject=title,
        contents=text
    )
    print('OK!')


deliver_email('2232195659@qq.com', 'pqmzuteevictdjjj', 'smtp.qq.com', '测试标题', '测试文本')
