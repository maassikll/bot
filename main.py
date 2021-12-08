#you must dowload PyWhatKit_DB
#enjot
import pyautogui,time,pywhatkit
#enter the number when you want send the spam
#the number 21 and 1 correspond is the time when the message will sent
pywhatkit.sendwhatmsg("number_phone","hello im the bot spammer ....",21,1,10)
time.sleep(10)
for i in range(100):
     pyautogui.write("i love you")
     #press enter in the keyboard
     pyautogui.press("enter")
