from multiprocessing import Process, Event
import time

def worker(process_wait=None):
    print("hello world")
    time.sleep(3)
    if process_wait is not None:
        process_wait.set()
    return True, True

process_wait = Event()
process = Process(target=worker, args=(process_wait,))

try:
    process.start()
    if process_wait.wait(timeout=200):
        print("finished")
    else:
        print("timeouted")
        process.terminate()
        process.join()
except:
    process.terminate()
     
