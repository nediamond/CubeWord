#!/usr/bin/env python
 
 # Cubifies words.  Currently only works with strings of even length.
 
 # Todo: turn this into an aws(or other service) api?
 
usr_str = raw_input("Enter string to be cubified: ")
print

if len(usr_str) % 2 != 0:
        print "Sorry, this only works with strings of even length."
        quit()

mid = len(usr_str)/2
ret_str = (" "*mid)+usr_str+"\n"

for i in range(1, mid):
	ret_str += " " * (mid-i)
	ret_str += "/"
	ret_str += " " * (i - 1)
	ret_str += usr_str[i]
	ret_str += " " * (len(usr_str)-i-2)
	ret_str += "/"
	ret_str += " " * (i - 1)
	ret_str += usr_str[-i-1]
		
	ret_str+="\n"
	
ret_str += usr_str
ret_str += " " * (mid - 1)
ret_str += usr_str[mid-1] + "\n"

for i in range(1, mid-1):
	ret_str += usr_str[i]
	ret_str += " " * (mid-1)
	ret_str += usr_str[mid+i]
	ret_str += " " * (len(usr_str)-mid-2)
	ret_str += usr_str[-i-1]
	ret_str += " " * (mid-1)
	ret_str += usr_str[-mid-i-1]
	
	ret_str+="\n"
	
ret_str += usr_str[mid-1]
ret_str += " " * (mid-1)
ret_str += usr_str[::-1] + "\n"


for i in range(0, len(usr_str)-mid-1):
	ret_str += usr_str[mid+i]
	ret_str += " " * (mid-i-2)
	ret_str += "/"
	ret_str += " " * (mid+i-1)
	ret_str += usr_str[-mid-i-1]
	ret_str += " " * (mid-i-2)
	ret_str += "/"
	
	ret_str += "\n"

ret_str += usr_str[::-1] + "\n"

print ret_str
