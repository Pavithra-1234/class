class users:
  def __init__ (self,name,location,kilometer):
    self.name=name
    self.location=location
    self.kilometer=kilometer
    
  def address(self):
    addr=f'Name:{self.name}\nLocation:{self.location}\nKilometer:{self.kilometer}'
    return addr
user1=users('pavi','sholingnallur',10)
user2=users('bavi','tambaram',25)

print(user1.address())
print(user2.address())
