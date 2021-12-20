##1st assignement		
		## Program to count the digit in a number
		
		n = int(input('Enter a number - '))
		print('number is ', n)
		count = 0
		while n != 0:
		    n = n//10
		    count += 1
		print('Number of digit in given number is ', count)




##2nd assignement		
#Answer2	--Program to reverse the string without manupulating special chahrecters position. 
            def revstrng(text):
		    indx = -1
		
		    # Loop from last index until half of the index
		    for i in range(len(text) - 1, int(len(text) / 2), -1):
		
		        # match character is alphabet or not
		        if text[i].isalpha():
		            temp = text[i]
		            while True:
		                indx += 1
		                if text[indx].isalpha():
		                    text[i] = text[indx]
		                    text[indx] = temp
		                    break
		    return text
		
		
		s = revstrng(list('a,b$c'))
		print("".join(s))
