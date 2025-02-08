
message=" HELLO EV"

print (f"message :  {message}") # message : HELLO EV

result = message.capitalize()

print(f"message after capitalize : {result}")


result = message.upper()

print(f"message after upper : {result}")


result = message.casefold()

print(f"message after casefold : {result}")


result = message.lower()

print(f"message after lower : {result}")

result = message.title()

print(f"message after title: {result}")


position =  message.find("EV")
print(f"message after title : {position}")

position = message.index("EV")
print(f" position of \"EV\"  in message : {position}")

result = message.lstrip()

print(f"message after lstrip: {result}")

result = message.rstrip()

print(f"message after rstrip: {result}")

result = message.strip()

print(f"message after strip: {result}")

#-------REplace-----
result = message.replace("Shah", "EVOLUTION")
print(f"message after replace :{result}")

message2= "IMTIAZ DYNASTY"
result2= message2.replace("hi","hello")
print(f"message2 after replace :{result2}")


