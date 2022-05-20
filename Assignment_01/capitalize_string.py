
char=input("Enter the String:")
char1= char.lower()
j=0
str=list(char1)
str+='\0'
for i in range(len(str)):
    if i==0 or str[i-1]==' ':
        str[i]=str[i].upper()
    elif str[i]==' ' or str[i]=='\0':
        str[i-1] = str[i-1].upper()

print("Your String is:", "".join(str))