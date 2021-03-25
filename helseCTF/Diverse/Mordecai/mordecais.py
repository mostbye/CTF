import os
import socket
import sys
import time
from netcat import Netcat


def parse_respone(inn):
	correct = b"\xf0\x9f\x8f\xb4" 		#🏴
	almoust = b"\xf0\x9f\x8f\xb3\xef\xb8\x8f" 	#🏳️
	
	correct_count = inn.count(correct)
	almoust_count = inn.count(almoust) 
	
	print("almoust_count:", almoust_count)
	print("correct_count:", correct_count)
	
	
	return correct_count, almoust_count
	
	
def send_guess(guess, nc):
	print("guess:", guess)
	nc.write(guess + b'\n')
	temp = nc.read_until(b'>')
	print(temp)
	parse_respone(temp)
	return
    
def main():
	#print(b"\xf0\x9f\x90\xb0") 🐰
	#print(b"\xf0\x9f\x90\x87") 🐇
	#print(b"\xf0\x9f\x90\xa3") 🐣
	#print(b"\xf0\x9f\x90\xa4") 🐤
	#print(b"\xf0\x9f\x90\xa5") 🐥
	#print(b"\xf0\x9f\xa5\x9a") 🥚
	
	#print(b"\xf0\x9f\x8f\xb4") 🏴
	#print(b"\xf0\x9f\x8f\xb3\xef\xb8\x8f") 🏳️ 
	#connect("challenges.ctfd.io", 30035)
	nc = Netcat("challenges.ctfd.io", 30035)
	temp = nc.read_until(b'>')
	#print(temp)
	guess = b"\xf0\x9f\x90\xb0\xf0\x9f\x90\xb0\xf0\x9f\x90\xb0\xf0\x9f\x90\xb0" # 🐰🐰🐰🐰
	send_guess(guess, nc)
	guess = b"\xf0\x9f\x90\x87\xf0\x9f\x90\x87\xf0\x9f\x90\x87\xf0\x9f\x90\x87" # 🐇🐇🐇🐇	
	send_guess(guess, nc)
	guess = b"\xf0\x9f\x90\xa3\xf0\x9f\x90\xa3\xf0\x9f\x90\xa3\xf0\x9f\x90\xa3" # 🐣🐣🐣🐣	
	send_guess(guess, nc)
	guess = b"\xf0\x9f\x90\xa4\xf0\x9f\x90\xa4\xf0\x9f\x90\xa4\xf0\x9f\x90\xa4" # 🐤🐤🐤🐤	
	send_guess(guess, nc)
	guess = b"\xf0\x9f\x90\xa5\xf0\x9f\x90\xa5\xf0\x9f\x90\xa5\xf0\x9f\x90\xa5" # 🐥🐥🐥🐥	
	send_guess(guess, nc)
	guess = b"\xf0\x9f\xa5\x9a\xf0\x9f\xa5\x9a\xf0\x9f\xa5\x9a\xf0\x9f\xa5\x9a" # 🥚🥚🥚🥚
	send_guess(guess, nc)
	
	
	
if __name__ == "__main__":
	main()
