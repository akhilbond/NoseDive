
f = open("emails.txt")

for line in f:
	info = line.split(",")
	name = info[0]
	fb = info[1]

	if len(info) == 3:
		twitter = info[2]
		print("Name =", name )
		print("fb =", fb )
		print("twitter =", twitter )

	if len(info) == 4:
		twitter = info[2]
		insta = info[3]

		print("Name =", name )
		print("fb =", fb )
		print("twitter =", twitter )
		print("insta =", insta )


