import threading
import time

def print_numbers():
  for i in range(1, 6):
    print(i, end="")
    time.sleep(1)

def print_letters():
  for letter in "ABCDE":
    print(letter, end="")
    time.sleep(1)

  thread1 = threading.Thread(target=print_numbers)
  thread2 = threading.Thread(target=print_letters)

  thread1.start()
  thread2.start()

  thread1.join()
  thread2.join()

  print(datetime.now())
  print("Main thread continues execution.")


if __name__ == "__main__":
    print_letters()