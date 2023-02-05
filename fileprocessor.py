with open('fileprocessor.input', 'r') as file:
    lines = file.readlines()

print("Printing out User Data:")
for line in lines:
    if line[0] == "#":
        print("" + line.split(":")[0][1:] + " is skipped because it starts with a hashtag (is commented out)")
    else:
        line = line.strip().split(":")
        print("The user " + line[0] + " has a password of " + line[1] + " and has userid " + line[2] + " and groupid " + line[3])

print("End of User Data")
