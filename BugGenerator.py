import string
import random
from time import sleep
import argparse
import cv2
import threading as th

keep_going = True


ap = argparse.ArgumentParser()
ap.add_argument('-f', '--flag', required=True, help='path to port number from Left Camera')
args = ap.parse_args()

flag = args.flag

if (str(flag) == "true"):
    flag = True
elif (str(flag) == "false"):
    flag = False


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def key_capture_thread():
    global keep_going
    input()
    global flag
    if flag == True:
        flag = False
    elif flag == False:
        flag = True


def do_stuff():
    th.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
    while keep_going:
        print('still going...')


if __name__ == '__main__':
    str = ""
    length = 0
    time_delay = 0


    exceptionList= [
        AssertionError,
        AttributeError,
        EOFError,
        FloatingPointError,
        GeneratorExit,
        ImportError,
        ModuleNotFoundError,
        IndexError,
        KeyError,
        KeyboardInterrupt,
        NotImplementedError,
        NotADirectoryError

    ]

    successList = [
        "Sever",
        "GPU",
        "Program",
        "Functionality",
        "Test",
        "Integration",
        "GUI - Mobile",
        "Database",
        "Mobird Test",
        "System Test",
        "Database CRUD",
        "CRUD 1"

    ]

    while True:

        if flag==False:
            th.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
            exeption = exceptionList[random.randint(0, len(exceptionList)-1)]
            print(bcolors.FAIL+ "Throw Exception, ERROR: Serious troubles occurs:" +exeption.__name__  + bcolors.ENDC)

            length = random.randint(0,150)
            time = random.randint(0,300)
            str = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(length))
            print(bcolors.FAIL+ str + bcolors.ENDC)
            # press 'q' to exit

            sleep(time / 1000)

        elif flag == True:

            th.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()

            sucess = successList[random.randint(0, len(successList) - 1)]

            print(bcolors.OKGREEN + "Success: Sever Running Good:" + sucess + bcolors.ENDC)

            length = random.randint(0, 150)
            time = random.randint(0, 300)
            str = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(length))
            #print(bcolors.FAIL + str + bcolors.ENDC)

            sleep(time / 1000)

