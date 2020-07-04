import time
from threading import Thread

# def countdown(n):
#     while n > 0:
#         print('T-minus', n)
#         n -= 1
#         time.sleep(5)


# t = Thread(target=countdown, args=(10, ))
# t.start()

# if t.is_alive():
#     print('Still Running')
# else:
#     print('complete')

class CountDownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False
    
    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)


c = CountDownTask()
t = Thread(target=c.run, args=(10,))
t.start()
# c.terminate()
t.join()


class IOTask:
    def terminate(self):
        self._running = False

    def run(self, sock):
        sock.settiomeout(5)
        while self._running:
            try:
                data = sock.recv()
                break
            except sock.timeout:
                continue
        return