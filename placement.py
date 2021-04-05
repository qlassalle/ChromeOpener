import os
import time
import random

magnet_shortcut = ["u", "i", "j", "k"]

for j in range(0, 4):
	for i in range(0, 4):
		profile_number = random.randint(1,100000)
		launch_chrome_cmd = f"/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome https://apple.com/fr --args --profile-directory=Person{profile_number} &"
		os.system(launch_chrome_cmd)
		time.sleep(random.randint(5,12))
		cmd = f"osascript -e 'tell application \"System Events\" to keystroke \"{magnet_shortcut[i]}\" using " + "{option down, control down}'"
		os.system(cmd)

	cmd = f"osascript -e 'tell application \"System Events\" to key code 124 using " + "{control down}'"
	os.system(cmd)
