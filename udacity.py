#7.1
def bigger(x,y):
    if x>=y:
        d=x
    if y>=x:
        d=y
    return d

#print bigger(9,9)

#8.1
def is_friend(name):
    if name[0] == 'D':
        return True
    else:
        return False

#print is_friend('Diane')
#print is_friend('Ned')

#9.1

#def biggest(a,b,c):
    if a>=b:
        if a>=c:
            x = a
        elif c>=a:
            x = c
    elif b>=c:
        x = b
    else: 
        x = c
    print x


#biggest(3,3,1)


#11.1
#i = 0
#while i != 10:
#      i = i + 2
#      print i

#11.3

def print_numbers(num):
	i=1
	while i <= num:
		print i
		i = i + 1

#print_numbers(3)

#12.1

def factorial(n):
	x = n
	while n > 1:
		n = n-1
		x = x * n
		#print x
		#print n
	return x

#print factorial(5)


#15.1

def get_next_target(page):
    start_link = page.find('<a href=') 
    if start_link > 0:
    	start_quote = page.find('"', start_link)
    	end_quote = page.find('"', start_quote + 1)
    	url = page[start_quote + 1:end_quote]
    	return url, end_quote
    else: 
        return None

url, endpos = get_next_target(page)
#print url,',', endpos


#16.1

def print_all_links(page):
    start_link = page.find('<a href=') 
    while start_link > 0: # what goes as the test condition for the while?
    	url, endpos = get_next_target(page)
        if url != 'None': # test whether the url you got back is None
        	print url
        	page = page[endpos:] # advance page to next position
        else: 
        	break
# if there was no valid url, then '''get_next_target''' did not find a link then do something else. What do you need to do?
print print_all_links('this is a <a href="http://udacity.com">link!</a> sdfsafd this is a <a href="http://udacity.com">link!</a> ddfawefef this is a <a href="http://udacity.com">link!</a>')
