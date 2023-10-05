import os

if __name__ == '__main__':
    print("Welcome to roboSpeaker::: Created by Sam")
    while(True):
          str = input("Enter the Sentence u want to listen: ")
          if(str=="q"):
              os.system("I m done with you!!!")
              break
          command= f"say {str}"
          os.system(command)
