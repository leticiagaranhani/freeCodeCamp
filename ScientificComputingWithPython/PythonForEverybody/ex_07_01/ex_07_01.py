print("PY4E - Exercise 7.1")
# mbox-short.txt
# write a program to read through a file and print the file contents (line by line) all in upper case.
print("*** 1st code version ***")
file_name = input("Enter a file name:")
hand_file = open(file_name)
print(hand_file.read().upper())
hand_file.close()

print("*** 2nd code version ***")
file_name = input("Enter a file name:")
hand_file = open(file_name)
count = 1

for line in hand_file:
    print(line.strip().upper())
    if count == 5:
        break
    count+=1

hand_file.close()

