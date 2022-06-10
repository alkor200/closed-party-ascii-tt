import time
import random

if __name__ == '__main__':
	while True:
		with open('timetable-V2.txt', 'r') as file:
			for line in file.readlines():
				print(line, end = '')
				time.sleep(0.2)
