# # f = open("demofile.txt", "w")
# # f = open("demofile.txt", "x")
# # f = open("demofile.txt", "r")
# f = open("demofile.txt", "a")
# f.write("Hello! Welcome, to the world of Python.")
# f.write("\nThis is a new line.")
# # f.seek(60)
# f.seek(0)
# line = f.read()
# # print("Line one", line)
# print(line)

# f.close()


# with open("demofile.txt", "w+") as newf:
with open("demofile.txt", "a+") as newf:
  newf.write("Asslamaulaikum! Welcome, Welcome, Welcome")
  newf.seek(0)
  print(newf.read())