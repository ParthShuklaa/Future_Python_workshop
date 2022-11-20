import re
fp = open("a.txt","w")
fp.write("parth.Shukla1989@gmail.com")
fp.close()

a = open("a.txt","r")
#c=a.readline()
b=a.read()
c=b.split("\n")
for d in c:
    obj = re.search(r'[\w.]+\@[\w]+',d)
    if obj:
        print("Valid Email")
    else:
        print("Invalid Email")
