file=open("my_file.txt","w")
a=file.write("saloni\naarti\nsheetal")
file.close()



file=open("my_file.txt","r")
a=file.read()
print(a)
file.close()



file=open("my_file.txt","a")
a=file.write("\nmuskan")
file.close()