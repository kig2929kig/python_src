from time import sleep

def countdown(t):
	while t > 0:
		print(t)
		t = t - 1
		sleep(1)
		
countdown(10)
