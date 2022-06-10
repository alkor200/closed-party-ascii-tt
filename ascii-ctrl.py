import time
import random

if __name__ == '__main__':
	while True:
		with open('ascii.txt', 'r') as file:
			for line in file.readlines():
				sleep = random.randrange(0,25,1)/100
				print(line, end = '')
				time.sleep(sleep)
