#morsetree.py
#Program for translating Morse code strings.
#By Timothy Cohen

class MorseCodeTree:
    
    def __init__(self):#Building the tree
        self.root = _listNode()
        letterList = ["A","B",'C','D','E','F','G','H','I','J','K','L','M','N',\
                      'O','P','Q','R','S','T','U','V','W','X','Y','Z',".","`"]
        morseList = [".-","-...",'-.-.','-..','.','..-.','--.','....','..',\
                     '.---','-.-','.-..','--','-.','---','.--.','--.-','.-.',\
                     '...','-','..-','...-','.--','-..-','-.--','--..',\
                     ".-.-.-",".----."]
        count = -1#Necessary for incrementing correctly
        for letter in letterList:
            curNode = self.root#reset current node to root each time
            count += 1
            code = morseList[count]
            self._setCharacter(letter,code)
          
    def _setCharacter(self,character,code):
        curNode = self.root#reset current node to root each time
        codeLength = len(code)
        for index in range(0,codeLength):
            direction = code[index]
            if direction == ".":
            #If we haven't reached this part of the tree yet, we set it as a\
            #linked list object, but we must check beacuse otherwise we will\
            #overwrite previously-placed letters
                if curNode.left is None: 
                    curNode.left = _listNode()
                curNode = curNode.left
            else:
                if curNode.right is None:
                    curNode.right = _listNode()
                curNode = curNode.right 
        curNode.data = character        
            
    def translate(self,codeseq):
        code = codeseq.split(" ")
        for sequence in code:#Each morse sequence is 1 coded letter
            space = False
            probe = self.root
            sequenceLength = len(sequence)
            if sequenceLength == 0:#If it's a space:
                space = True
            for index in range(0,sequenceLength):
                direction = sequence[index]
                if direction == ".":
                    if probe.left is None:#If we've fallen off the tree
                        assert("Invalid!")
                        yield " $$$"
                        return
                    else:
                        probe = probe.left
                else:
                    
                    if probe.right is None:
                        assert("Invalid!")
                        yield " $$$"
                        return
                    else:
                        probe = probe.right
            if space:
                probe.data = " "
            yield probe.data#Return the letter and continue looping
            
class _listNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None