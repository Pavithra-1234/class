class Book:
	def __init__(self,name,pages,author):
		self.name=name
		self.pages=pages
		self.author=author
#str method	
	def __str__(self):
		book=f"Name:{self.name}\nPages:{self.pages}\nAuthor:{self.author}"
		return book
#repr method	
	def __repr__(self):
		book=f"Name:{self.name}\nPages:{self.pages}\nAuthor:{self.author}"
		return book
		
bk1=Book("Thirukkural",1330,"Thiruvalluvar")
bk2=Book("Life of pi",300,"Wilson")
#str output
print(bk1)
#repr output
print([bk1])
