
def send_email(message, recipient, sender="university.help@gmail.com"):
    if '@' or '.com' or '.ru' or '.net' not in recipient not in sender:
        print(f"Невозможно отправить {message} с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print(f"Нельзя отправить {message} самому себе!")
    elif sender == 'university.help@gmail.com':
        print(f"{message} успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! {message} отправлено с адреса {sender} на адрес {recipient}")


send_email('письмо', 'vasyok1337@gmail.com')
send_email('письмо', 'university.help@gmail.com')
send_email('письмо', 'vasyok1337@gmail.net', 'university.help@gmail.com')
send_email('письмо', 'vasyok1337@gmail.net', 'university.help@gmail.net')
