def get_next_target(page):
    start_link = page.find('<a href=') # HINT: put something into the code here
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def print_all_links(page):
	url = 1
	while url != None:
		url, endpos = get_next_target(page)
		if url != None:
			print url
		page = page[endpos:] 
#url, endpos = get_next_target(page)

#page = 'no llinks here'
page = 'contents <a href="somelinkhere"> text </a> of some web page as a string contents <a href="somelinkhere2"> text </a> of some web page as a stringcontents <a href="somelinkhere3"> text </a> of some web page as a string'
print_all_links(page)
