import random
import pyautogui

chars = " qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_-=[]\;',./<>?: "

allchar = list(chars)

pwd = pyautogui.password("Enter a password")

sample_pwd = ""

while(sample_pwd != pwd):
    sample_pwd = random.choices(allchar, k=len(pwd))
    
    print("<====" + str(sample_pwd) + "====>")
    
    if(sample_pwd == list(pwd)):
        print("The Password is : "+ "".join(sample_pwd))
        break
