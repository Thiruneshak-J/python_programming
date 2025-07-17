import os
import datetime as dt
"""
# 1-------------file and Directory oprations ( directory = folder)

#getcwd,chdir,listdir
print("1 current working directory",os.getcwd())  #getcwd----> to show the Current Working Directory
os.chdir("D:\\")                                  #chdir----->to change cwd
print("2 changing the directory",os.getcwd())     #listdir-----> to show all the directory of the path
os.chdir("C:\\Users\\ADMIN\\OneDrive\\Desktop\\python")
print(os.getcwd())
print(os.listdir("D:\\"))
print(os.listdir())

#create a file and folder --> mkdir,makesdir
#os.mkdir("oobs") #or os.makesdir("oobs")        #mkdir----> to create single directory or folder
#os.makedirs("thiruneshak\\thiru\\mohana")       #makedirs-->to create one or many directories in directory

#remove a file and folder --->remove,rmdir,removedirs
#os.rmdir("oobs")                               #rmdir---->to remove single directory only if it is EMPTY
#os.remove("oobs\\thiru emp.pdf")               #remove--->to remove only file
#os.removedirs("thiruneshak\\thiru\\mohana")    #removedir--->to remove all empty directories in the directory

#rename ,replace
#os.rename("oobs","oobs23")                    #rename----> to rename a exist directory
#os.replace("oobs23","oobs")                    #replace--> to replace the exist directory by overwriting

#status
#print(os.stat("C:\\Users\\ADMIN\\OneDrive\\Desktop\\python")) #os.stat()--->to show status of file

# 2----> file and path operations
#join

#path=os.path.join("oobs","pac_os.py")             #os.path.join----> to join file in directory or directory in directory
#print(path)
#print(os.path.join("thirunesak","oobs"))

#check
print(os.path.exists("oobs"))
print(os.path.exists("oob1"))
print(os.path.isfile("oobs\\thiru emp.pdf"))
#os.chdir("C:\\Users\\ADMIN\\Downloads")
#print(os.path.isfile("thiru emp.pdf"))
print(os.path.isdir("thiruneshak"))
print(os.path.isdir("thiru"))

#get
print(os.path.basename("thiruneshak\\thiru\\mohana"))
print(os.path.dirname("thiruneshak\\thiru\\mohana"))
print(os.path.splitext("thiru emp.pdf"))
print(os.path.getsize("thiruneshak"))
t=os.path.getmtime("oobs")
r=dt.datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S")
print(f"last modified time:{r}")
print(os.path.abspath("oobs"))"""

# 3---> process and info
print(os.name)
print(os.getlogin())
print(os.getpid())
print(os.getppid())
print(os.cpu_count())

# 4 running commands
print(os.system("oobs\\thiru emp.pdf"))
print(os.popen("dir"))
#os.startfile("C:\\Users\\ADMIN\\OneDrive\\Desktop\\python\\(5)import_sample")
#print(os.execv())

#file descriptor operations
os.open("C:\\Users\\ADMIN\\OneDrive\\Desktop\\python\\(5)import_sample",os.O_CREAT)









         


