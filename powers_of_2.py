## Did you know that (1/2^1) + (1/2^2) + (1/2^3) + (1/2^4) +....+ (1/2^∞) = 1

pwr = 1
tot = 0
from time import sleep
while True:
	tot += (1/2**pwr)
	print("(1/{0}) = {1:.200f}".format(2**pwr, 1/2**pwr))
	print("Total = {0:.200f}\n".format(tot))
	pwr += 1
	sleep(.3)
