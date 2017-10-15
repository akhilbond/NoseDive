
f = open("emails.txt")

for line in f:
    print(line, "\n\n")
    info = line.split(",")

    name = info[0].split(":")[1]
    number = info[1].split(":")[1]
    fb = info[2].split(":")[1]
    if (len(info) == 4):
        tmp = info[3].split(":")
        if(tmp[0] == "twitterURL"):
            twitter = tmp[1]
            print("Name =", name)
            print("Number =", number)
            print("fb =", fb)
            print("twitter =", twitter)
        else:
            insta = tmp[1]
            print("Name =", name)
            print("Number =", number)
            print("fb =", fb)
            print("instagram =", insta)

        if (len(info) == 5):
            tmp = info[4].split(":")
            if(tmp[0] == "instagramURL"):
                insta = tmp[1]
                print("Name =", name)
                print("Number =", number)
                print("fb =", fb)
                print("twitter =", twitter)
                print("instagram =", insta)
            else:
                twitter = tmp[1]
                print("Name =", name)
                print("Number =", number)
                print("fb =", fb)
                print("twitter =", twitter)
                print("instagram =", insta)
