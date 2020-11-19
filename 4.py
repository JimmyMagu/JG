from string import digits, ascii_letters, punctuation
from itertools import product

for passcode in product(digits + ascii_letters + punctuation, repeat=4):
	print("".join(passcode))
