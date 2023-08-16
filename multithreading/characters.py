#TO FILTER THE CHARACTERS FORM THE INPUT TEXT FILE
#AND STORE THEM IN DIFFERENT FILES 
import threading 

def process_file(output_file, char_type):
    with lock:
        with open('multithreading/files/characters.txt', 'r') as file:
            characters =  file.read()
        temp_str = ""
        #reading each character and check for the type
        for x in characters:
            if char_type(x):
                temp_str += x
        #write output file
        with open(output_file, 'w') as file:
            file.write(temp_str)

if __name__ == '__main__' :
    #creating a lock for synchronization
    lock = threading.Lock()
    thread1 = threading.Thread(target=process_file, args=('multithreading/files/alphabets.txt', str.isalpha))
    thread2 = threading.Thread(target=process_file, args=('multithreading/files/digits.txt', str.isdigit))
    thread3 = threading.Thread(target=process_file, args=('multithreading/files/special_char.txt', lambda x : not str.isalnum(x)))

    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()
    print("Successfully filtered the characters and created the files >> ")