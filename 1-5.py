#11SE 2027 (minus syon)
a = input("first string? ")
b = input("second string? ")
c = input("third string? ")
longest = a #assume first word is longest

if len(b) > len(longest):
    longest = b
if len(c) > len(longest):
    longest = c
print("The longest line was", longest)

#Calvin's

##a = input("first string? ")
##b = input("second string? ")
##c = input("third string? ")
##longest = ""
##
##
##if len(a) > len(b):
##    longest = a
##if len(b) > len(c):
##    longest = b
##if len(c) > len(a):
##    longest = c
##    
##print("The longest line was", longest)


#Riya's:
##a = input("first string? ")
##b = input("second string? ")
##c = input("third string? ")
##longest = ""
##
##
##if len(a) >= len(longest):
##    longest = a
##if len(b) > len(longest):
##    longest = b
##if len(c) > len(longest):
##    longest = c
##    
##print("The longest line was", longest)

#Correy's solution - error when len(a) is between len(b) and len(c) 
##a = input("first string? ")
##b = input("second string? ")
##c = input("third string? ")
##longest = ""
##
##if len(a) >= len(b):
##    longest = a
##elif len(c) > len(b):
##    longest = c
##else:
##    longest = b
##    
##print("The longest line was", longest)
