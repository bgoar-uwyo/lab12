
class Display:
    ascii_art = [ # List that contains 10 ASCII images
'''
   +---+
       |
       |
       |
      ===
''',
'''
   +---+
   O   |
       |
       |
      ===
''',
'''
   +---+
   O   |
   |   |
       |
      ===
''',
'''
   +---+
   O   |
  /|   |
       |
      ===
''',
'''
   +---+
   O   |
  /|\  |
       |
      ===
''',
'''
   +---+
   O   |
  /|\  |
  /    |
      ===
''',
'''
   +---+
   O   |
  /|\  |
  / \  |
      ===
''',
'''
   +---+
  (O   |
  /|\  |
  / \  |
      ===
''',
'''
   +---+
  (O)  |
  /|\  |
  / \  |
      ===
''',
'''
   +---+
  (O)  |
  /*\  |
  / \  |
      ===
'''
]

    def __init__(self):
        pass

    def show_man(self, n) :
        if n >= 0 and n < len(self.ascii_art): # If value n matches up with an entry in the list
            print ( self.ascii_art[n] ) # Print the image
        else:
            print ( "to big" ) # Print that there isn't an ASCII image for the input n

# Test Code.

if __name__ == "__main__":
    art = Display()
    print ( "=> ", end="" )
    x = int(input())
    art.show_man ( x )
