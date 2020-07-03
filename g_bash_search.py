try: 
	from googlesearch import search 
except ImportError: 
	print("No module named 'google' found") 

# to search 
query = "porno"

for j in search(query, tld="com", num=10, stop=10, pause=2): 
	print(j) 
