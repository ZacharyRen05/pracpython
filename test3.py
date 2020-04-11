# files in python
try:
    characters = "My name is Zachary Ren, I just learned how to do some basics on files using Python. I also learned " \
                 "about some exceptions in Python. "
    file = open("filename.txt", "w")
    file.write(characters)
    print(len(characters))
finally:
    file.close()

with open("filename.txt") as f:
    file = open("filename.txt", "r")
    print(f.read())
    file.close()

# exceptions in python

numberA = 10
numberB = 0

try:
    print(numberA / numberB)
except:
    print("You cannot divide by zero")
    raise

# try to add python log framework; instead of overwriting the file, try appending the file; try to make the file
# read-only; when you write string into it, how to handle exceptions
