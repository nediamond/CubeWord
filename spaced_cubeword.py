#!/usr/bin/env python
 
# Cubifies words.  Currently only works with strings of even length.

# Todo: turn this into an aws(or other service) api?

def cubify(usr_str):
	spaced_str = reduce(lambda x,y: x+" "+y, usr_str, "").strip()
	odd = len(usr_str)%2
	mid = len(usr_str)/2
	ret_str = ("  "*(mid))+spaced_str+"\n"

	for i in range(1, mid):
		ret_str += "  " * (mid-i)
		ret_str += "/ "
		ret_str += "  " * (i-1)
		ret_str += usr_str[i]
		ret_str += " " * (2*(len(usr_str)-i-2)+1)
		ret_str += "/ "
		ret_str += "  " * (i-1)
		ret_str += usr_str[-i-1]
			
		ret_str+="\n"
		
	ret_str += spaced_str
	ret_str += " " * (2*(mid)-1)
	ret_str += usr_str[mid-((len(usr_str)+1)%2)] + "\n"

	for i in range(1, mid-1+odd):
		ret_str += usr_str[i]
		ret_str += " " * (2*(mid-1)+1)
		ret_str += usr_str[mid+i]
		ret_str += " " * (2*(len(usr_str)-mid-2)+1)
		ret_str += usr_str[-i-1]
		ret_str += " " * (2*(mid-1)+1)
		ret_str += usr_str[-mid-i-1]
		
		ret_str+="\n"
		
	ret_str += usr_str[mid-1+odd]
	ret_str += " " * (2*(mid-1)+1)
	ret_str += spaced_str[::-1] + "\n"


	for i in range(0, len(usr_str)-mid-1-odd):
		ret_str += usr_str[mid+i+odd]
		ret_str += "  " * ((mid-i-2))
		ret_str += " /"
		ret_str += " " * (2*(mid+i-1)+1+odd)
		if odd: ret_str += " "
		ret_str += usr_str[-mid-i-1-odd]
		ret_str += "  " * ((mid-i-2)+odd)
		ret_str += " /"
		
		ret_str += "\n"

	ret_str += spaced_str[::-1] + "\n"

	return ret_str

if __name__=="__main__":
	usr_str = raw_input("Enter string to be cubified: ")
	print
	print cubify(usr_str)
