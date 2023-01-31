import os
dir(os)
help(os)
os.system("dir")
x=os.system("dir")
print(x)
os.getcwd()
os.chdir()
os.listdir()
for i in os.listdir():
    print(i)
os.listdir("path")
os.mkdir("testfolder")
os.makedirs("testfolder/testdir")
os.environ.get("WINDIR")
os.rmdir("testfolder1")
##########os.path#############
dir(os.path)
os.path.exists("C:\\temp")
#########OS.walk()################
print(list(os.walk('C:\\temp')))
############OS.WALK##################
import os
for dirname,dirpath,filename in os.walk("C:\\temp\\testfolder1"):
    print(dirname)
    print(dirpath)
    print(filename)
    for file in filename:
        print(f"file name is:{file}")
        print(f" dir name is {dirname}")
        print(os.path.join(dirname,file))
        
