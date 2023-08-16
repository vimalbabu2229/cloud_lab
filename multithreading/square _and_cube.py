# FIND SQUARE AND CUBE OF A NUMBER 
import threading 
def print_square(num):
    print(f"The square value = {num * num}")

def print_cube(num):
    print(f"The cube value = {num * num * num}")

if __name__ == "__main__":
    #thread for print_square
    thread1 = threading.Thread(target=print_square, args=(10, ))
    #thread for print_cube
    thread2 = threading.Thread(target=print_cube, args=(10, ))
    #as passing the args you should keep a trailing comma 
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()