# main.py -- put your code here!

lcd = pyb.LCD('X')
lcd.light(True)

n = 1000000
i = 2
result = 0

print("mainScript.py")

lcd.write("mainScript.py")