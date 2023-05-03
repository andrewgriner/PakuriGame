class Pakuri():
  def __init__(self, species): #this initalizes the class
    self.species = species
    #The next lines set up the base stats for the pakuri
    self.defense = 17+len(species)*5
    self.speed = 13+len(species)*6
    self.attack = 9+len(species)*7

  def evolve(self): #This function increases attack deffense and speed
    self.attack = self.attack+self.attack
    self.defense = self.defense+self.defense+self.defense+self.defense
    self.speed = self.speed+self.speed+self.speed
 #The last functions care for the Pakuri objects and returns a new attribuleand values
  def get_defense(self):
    return self.defense

  def get_species(self):
    return self.species

  def get_attack(self):
    return self.attack

  def get_speed(self):
    return self.speed

  def set_attack(self, new_attack):
    self.attack = new_attack