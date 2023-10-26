username: str = input()
password = input


if username == 'user':
    print('Hello, user')
    if password == 'nobodywillguessthis':
        print('Access Granted')
    else:
        print('Access Denied')