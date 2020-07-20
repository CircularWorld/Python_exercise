# from threading import Thread, Event
#
# msg = None
#
#
# def yangzirong(e):
#     print("杨子荣前来拜山头")
#     global msg
#     msg = "天王盖地虎"
#     e.set()
#
# def main():
#     e = Event()
#     t = Thread(target=yangzirong,args=(e,))
#
#     t.start()
#     print("说对口令是自己人")
#     e.wait()
#     if msg == "天王盖地虎":
#         print("宝塔镇河妖")
#         print("九当家浪起来")
#     else:
#         print("你屎淋到头了")
#     t.join()
#
# main()

from threading import Thread,Event
msg = None

def yangzirong(e):
    print("拍汕头")
    global msg
    msg = '你妈炸了'
    e.set()


def main():
    e = Event()
    t = Thread(target=yangzirong,args=(e,))
    t.start()
    e.wait()
    if msg == '你妈炸了':
        print("welcome")
    else:
        print("go die")

    t.join()

if __name__ == '__main__':
    main()