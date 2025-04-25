f=open("C:/Users/sugam/Documents/pyExtra/hello.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()

f=open("C:/Users/sugam/Documents/pyExtra/hello.txt","w")
mode=f.write("\nBut you are doing great!!")
f.close

f=open("C:/Users/sugam/Documents/pyExtra/hello.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()
f=open("C:/Users/sugam/Documents/pyExtra/hello.txt","r")
mode=f.read()
print(mode)
f.close()

f=open("C:/Users/sugam/Documents/pyExtra/hello.txt","a")
f.write("\nbut its fine that i see u doing well keep pushing forward!!")
f.close()

f1=open("C:/Users/sugam/Documents/pyExtra/hello.txt","r")
mode2=f1.read()
print(mode2)
f1.close()

with open("C:/Users/sugam/Documents/pyExtra/hello.txt","r") as f:
  print(f.read())
  
with open("C:/Users/sugam/Documents/pyExtra/hello.txt","w") as f:
  f.write("\nAre u doing well!!")

with open("C:/Users/sugam/Documents/pyExtra/hello.txt","r") as f:
  print(f.read())
  
with open("C:/Users/sugam/Documents/pyExtra/hello.txt","a") as f:
  f.write("\nAre u doing well!!")
  


with open("sample.txt", "a+") as f:
    # Append first line
    f.write("Hello, how are you doing")
    
    # Go back to start and read everything
    f.seek(0)
    print("After first write:")
    print(f.read())          # prints current content
    
    # Append second line
    f.write(" , That's the spirit!!")
    
    # Go back to start and read the updated content
    f.seek(0)
    print("\nAfter second write:")
    print(f.read())
