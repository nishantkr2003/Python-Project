from time import *
import random as r

def mistake(paragraph,user_test):
    error = 0
    for i in range(len(paragraph)):
        try:
            if paragraph[i] != user_test[i]:
                error = error + 1
        except :
            error = error + 1
    return error

def speed_time(time_start,time_end,userinput):
    time_delay=time_end - time_start
    time_roundof= round(time_delay,2)
    speed = len(userinput)/time_roundof
    return round(speed)

if __name__ == '__main__':

    while True:
        check = input("ready to test your typing speed : yes or no ")
        if check=="yes":

            test=["No one can make you feel inferior without your consent.","My name is Nishant Kumar","I am a student of B.Tech"]

            test1 = r.choice(test)
            print("***** typing speed *****")
            print(test1)
            print()
            print()

            time1=time()
            testinput =input(" Enter : ")
            time2=time()

            print('speed : ',speed_time(time1,time2,testinput) , " w/sec")
            print("Error : ",mistake(test1,testinput))
        elif check== "no":
            print("thank you")
            break
        else:
            print("Wrong input")


            