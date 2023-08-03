#myfile = open("testfile.txt","a+")
#for i in range(10):
 #   myfile.write("There is some new text\n")
#myfile.close()    


from importlib.resources import contents


myfile = open("testfile.txt","r")
if myfile.mode == 'r':
    contents = myfile.read()
    print(contents)