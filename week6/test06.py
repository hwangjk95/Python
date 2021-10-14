def greet_users(names):
    if isinstance(names,list):
        for name in names:
            msg = f"hello, {name.title()}"
            print(msg)

usernames = ['kim inha','park inha']
greet_users(usernames)
greet_users('kim inha')
greet_users({'1': 'kim inha','2':'park inha'})