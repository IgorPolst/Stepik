def send_watch(num=1):

    if num < 4:
        print((f"{num}" * ((5 - num) * 4)).center(16))
        send_watch(num + 1)
    print((f"{num}" * ((5 - num) * 4)).center(16))


send_watch()
