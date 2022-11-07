
class User:
    name = "Tristan"
    age = 17
  
    def update_age(self, new_age):
        self.age = new_age
    
user = User()
user.update_age(200)
print(user.age)