
def print_all_links(page):
    while True: 
    	url, endpos = get_next_target(page)
        if url: 
        	print url
        	page = page[endpos:] # advance page to next position
        else: 
        	break

print print_all_links('this is a <a href="http://udacity.com">link!</a> sdfsafd this is a <a href="http://udacity.com">link!</a> ddfawefef this is a <a href="http://udacity.com">link!</a>')
