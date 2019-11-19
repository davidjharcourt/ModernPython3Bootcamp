times = input("How many times do I have to tell you?")

if times.isdigit() == False:
	print("That's not a number!")
elif times:
	times = int(times)
	for time in range(times):
		print("Clean your room!")
		#time -= time
else:
	print("You didn't enter anything!")