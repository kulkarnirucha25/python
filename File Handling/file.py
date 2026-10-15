#OPEN A FILE AND READ
# f = open("File Handling/Example.txt","r")
# print(f.read())
# f.close()


#OPEN A FILE USING WITH AND READ
# with open("File Handling/Example.txt","r") as f:
#      print(f.read())


#WRITE TO A FILE
# with open("File Handling/Example.txt","w") as f:
#    f.write("Hello Python\n")
# with open("File Handling/Example.txt", "r") as f:
#     print(f.read())


#APPEND TO A FILE
# with open("File Handling/Example.txt","a") as f:
#     f.write("Appended Text\n")
# with open("File Handling/Example.txt","r") as f:
#     print(f.read())


#READLINE
# f = open("File Handling/Example.txt","r")
# print(f.readline())


#READLINES
# f = open("File Handling/Example.txt","r")
# print(f.readlines())


#READ AND WRITE
# with open("File Handling/Example.txt","r+") as f:   
#     print(f.read())
#     f.write("Appended Text\n")
# with open("File Handling/Example.txt","r") as f:
#   print(f.read())


# WRITE AND READ
# with open("File Handling/Example.txt","w+") as f:
#  f.write("Python is a popular programming language. It is easy to learn and is used for web development, data science and artificial intelligence. Python also provides file handling features to read, write, and modify files easily.\n")
# with open("File Handling/Example.txt","r") as f:
#   print(f.read())


#APPEND AND READ
# with open("File Handling/Example.txt","a+") as f:
#     f.write("New Text\n")
# with open("File Handling/Example.txt","r") as f:
#   print(f.read())


#CREATE A NEW FILE
with open("File Handling/NewFile.txt","x") as f:    
  f.write("This is a new file.\n")
with open("File Handling/NewFile.txt","r") as f:
  print(f.read())


# READ AND WRITE BINARY FILE
# with open("File Handling/example.txt", "rb+") as f:
#     f.write("Hello Python".encode())
#     f.seek(0)
#     print(f.read().decode())


# WRITE AND READ BINARY FILE
# with open("File Handling/example.txt", "wb+") as f:
#     f.write("Hello Python".encode())
#     f.seek(0)
#     print(f.read().decode())


#BINARY DATA OF IMAGE
# with open("File Handling/image.jpg", "rb") as f:
#     data = f.read()
#     print(data)


#SEEK AND TELL
with open("File Handling/Example.txt", "r") as f:
    print(f.tell())
    print(f.read(3))
    print(f.tell())