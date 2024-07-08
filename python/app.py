import os
import time

path = "/app/a.txt"

while True:
	file_exists = os.path.exists(path)

	if file_exists:
		file = open(path, "r")
		output = file.read()
		print(output)
	else:
		print("Dosya Bulunamadi")
	time.sleep(1)
