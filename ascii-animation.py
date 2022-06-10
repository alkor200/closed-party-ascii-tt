import os
import time

os.system('clear')

frame_name_list = ['frame_1.txt', 'frame_2.txt', 'frame_3.txt', 'frame_4.txt']

frames = []


for name in frame_name_list:
	with open(name, 'r', encoding='utf8') as f:
		frames.append(f.readlines())
		print(frames)

while True:
	for frame in frames:
		print("".join(frame))
		time.sleep(0.2)
		os.system('clear')