import os
import time

j = 0
commands = ["u", "i", "j", "k"]

for i in (0, 3):
	for i in range(0, 3):
		launchChrome = f"/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome https://eurosport.com/ --args --profile-directory=\"coinlist{j}\" &"
		os.system(launchChrome)
		time.sleep(5)
		cmd = f"osascript -e 'tell application \"System Events\" to keystroke \"{commands[i]}\" using " + "{option down, control down}'"
		# minimize active window
		os.system(cmd)
		j = j + 1

	cmd = f"osascript -e 'tell application \"System Events\" to key code 124 using " + "{control down}'"
	os.system(cmd)
	j = j + 1