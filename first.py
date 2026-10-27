#ask their name
name =input("what is your name? ").strip().title()

# split the name just write the first name of the user
first, last = name.split(" ")

#hello            
print(f"hello, {name}")