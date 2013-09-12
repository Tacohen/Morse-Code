#decode.py
#Driver program for translating Morse code strings.
#By Timothy Cohen

from morsetree import MorseCodeTree

def main(filename):
    file = open(filename, 'r')
    for line in file:
        line = line.rstrip("\n")
        tree = MorseCodeTree()
        words = tree.translate(line)
        words = ''.join(words)#Convert the discrete letters into one string
        print(line)
        print (words)
        
filename = "morse.txt"        
if __name__ == "__main__":#Call the main
    main(filename)