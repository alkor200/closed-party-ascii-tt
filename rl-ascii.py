import os
import time
import itertools

display_size = 200
		

if __name__ == '__main__':
	os.system('clear')
	with open('ascii-endless.txt', 'r') as file:
		lines = []
		for line in file:
			lines.append(itertools.cycle(line.strip('\n')))
		while True:
			for line in lines:
				counter = 0
				for char in line:
					print(char, end='')
					counter += 1
					if counter == display_size:
						print()
						break

			time.sleep(0.3)
			os.system('clear')

