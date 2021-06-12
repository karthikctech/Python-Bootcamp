# opening file
with open("files.txt") as sk:
    contents = sk.read()
    print(contents)

# write into the file
with open("files.txt", mode="a") as ka:
    contents1 = ka.write("\none step back")
    print(contents1)

# to create new folder and write something
with open("new_file.txt", mode="w") as ck:
    contents2 = ck.write("HELLOW WORLD")
    print(contents2)