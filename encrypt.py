alphabet='abcdefghijklmnopqrstuvwxyz_'  
key = 3  
newmsg=""  
message = input("Enter Your Message : ")  
for character in message:  
     position = alphabet.find(character)  
     newposition = (position+key)%27  
     newchar = alphabet[newposition]  
     print('Encrypted new character is :',newchar)  
     newmsg+=newchar  
print('The encrypted message is ', newmsg)  
