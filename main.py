# int - integer
# double, short, long - decimal numbers 2.3, 4.8373
# char - 'a', 'b', c, d
# string - "word",
# boolean/bool - true/false
# var height = 6.8
# hung = true
# list/arrays = ['fire', 'water', 'sand']

class Pokemon:
  def __init__(self, name, poke_type, is_male, height, hp, has_learnable_moves): # Constructor - Run at object creation
    self.name = name
    self.poke_type = poke_type
    self.is_male = is_male
    self.height = height
    self.hp = hp
    self.has_learnable_moves = has_learnable_moves
    self.moves = []

  def __str__(self):
    return '===============================\n' + str(self.name) + '\n===============================\n' + \
    str(self.poke_type) + '\n' + str(self.is_male) + '\n' + str(self.height) + '\n' + str(self.hp) + '\n' + str(self.has_learnable_moves) + \
    '\n' + self.moves

  def attack():
      print('attacked!')

  def add_move(self, move):
      self.moves.append(move)

class Move:
  def __init__ (self, name, damage, critical_hit):
    self.name = name
    self.damage = damage
    self.critical_hit = critical_hit

  def __str__ (self):
    return str(self.name)

def main():
  squirtle = Pokemon('Squirtle', ['water'], True, 3.0, 70, True)
  charmander = Pokemon('Charmander', ['fire'], False, 3.3, 80, False)
  tackle = Move('tackle', 10, False)
  squirtle.add_move(tackle)
  print(squirtle)































if __name__ == "__main__":
  main()