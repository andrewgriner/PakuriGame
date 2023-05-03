from pakuri import Pakuri
class Pakudex():

  def __init__(self, total_size=20): #initializes Pakudex with total capsity of the user choce
    self.pakudex = []
    self.total_size = total_size

  def get_species_array(self): #This returns a array of the species in the Pakudex
    if len(self.pakudex) == 0:
      return None
    else:
      return [p.species for p in self.pakudex]

  def add_pakuri(self, species): #Adds a new pakuri if there is enough capacity it will return true if there isnt false
    if self.total_size == len(self.pakudex):
      return False
    else:
      present=False
      for i in self.pakudex:
        if i.get_species() == species:
          present=True
    if not present:
      self.pakudex.append(Pakuri(species))
      return True
    else:
      return False

  def evolve_species(self, species): #Evolves pakuri with the species and the pakudex
    for i in self.pakudex:
      if i.get_species() == species:
        i.evolve()
        return True
    return False #returns false if there is no pakuri by that name

  def get_stats(self, species): #This one returns the stats of the pakuri of the selectred species
    in_pakudex = False
    for i in self.pakudex:
      if i.get_species() == species:
        in_pakudex = True
        return [i.get_attack(), i.get_defense(), i.get_speed()]
    if not in_pakudex:
      return None #if it isnt in pakedex it will return none resembling such

  def sort_pakuri(self): #Sorts the pakudex by alphabetal order
    def comparison(x):
      return x.get_species()
    self.pakudex.sort(key=comparison)

  def get_size(self): #this returns the number of Pakuri
    return len(self.pakudex)

  def get_capacity(self): #Returns the total number of Pakuri
    return self.total_size