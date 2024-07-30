
def send_email(recipient, sender="university.help@gmail.com"):
    if '@' and '.com' and '.ru' and '.net' not in recipient not in sender:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


send_email('vasyok1337@gmail.com')
send_email('university.help@gmail.com')
send_email('vasyok1337@gmail.net','university.help@gmail.com')
send_email('vasyok1337@gmail.net', 'university.help@gmail.net')
