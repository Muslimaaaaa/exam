class Product:
  @save
  def save(self):
    with open("data/users.json", encoding="utf-8") as file:
      data = json.load(file)

    with open("data/users.json", "w") as f:
      new_user = {
        "first_name": self.first_name,
        "last_name": self.last_name,
        "username": self.username,
        "password": self.get_password,
        "status": self.status,
        "create_date": self.create_date
      }
      data["users"].append(new_user)
      json.dump(data, f, indent=6)
    print("Register Successfully")






