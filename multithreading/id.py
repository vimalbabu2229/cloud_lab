#PRINT PROCESS ID , THREAD ID AND TREAD NAMES
import threading 
import os

def task1():
    print(f"Process ID of task1 = {os.getpid()}\n")
    print(f"Thread ID of task1 = {threading.current_thread().ident}\n")
    print(f"Thread name of task1 = {threading.current_thread().name}\n")

def task2():
    print(f"Process ID of task2 = {os.getpid()}\n")
    print(f"Thread ID of task2 = {threading.current_thread().ident}\n")
    print(f"Thread name of task2 = {threading.current_thread().name}\n")

if __name__ == "__main__":
    
    print(f"Process ID of Main = {os.getpid()}\n")
    print(f"Thread ID of Main = {threading.current_thread().ident}\n")
    print(f"Thread name of Main = {threading.current_thread().name}\n")

    t1 = threading.Thread(target=task1, name='thread1')
    t2 = threading.Thread(target=task2, name='thread2')

    t1.start()
    t2.start()
    t1.join()
    t2.join()