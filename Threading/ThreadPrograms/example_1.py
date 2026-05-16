import threading

def worker():
    print("Thread is running")

t = threading.Thread(target = worker)
t.start()