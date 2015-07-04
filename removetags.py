

def remove_tags(page):
	split_page = page.split("<")
	print split_page
	my_list=[]
	for each in split_page:
		if each != "":
			words=each.replace("\n","")
			words=words.strip()
			words=words.split(">")[1]
			if words != "":
				my_list.append(words)
	return my_list
		
print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("there are no tags")
#>>> []

