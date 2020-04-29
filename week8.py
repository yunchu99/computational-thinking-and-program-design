hours=input("Enter movie time hours:")
minutes=input("Enter movie time minutes")

hours=int(hours)
minutes=int(minutes)

length=hours*60+minutes
print(hours,"Hours","minute","Minutes","movie length is",length,"minutes")

hours1=length//60
print(hours1)

minutes1=length%60
print(minutes1)

print(length,"Minutes equals",hours1,"Hours",minutes1,"Minutes")