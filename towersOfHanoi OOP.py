class Peg:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == [] #returns true if empty

     def push(self, item):
         self.items.append(item)

     def pop(self):
         try:
             return self.items.pop()

         except:
             print("popping from empty stack")


         #if self.items == False:
         #    return self.items.pop()

     def peek(self):
         try:
              return self.items[-1].size #returns size of discs from bottom to top

         except:
              print("empty stack")


     def see(self):
         peg = []
         for i in reversed(self.items):
              peg.append(i.size)
         return(peg) #returns size of discs from bottom to top

class Disc:
    def __init__(self, size):
        self.size = size

class TowersOfHanoi:
    def __init__(self):
        self.pegA = Peg()
        self.pegB = Peg()
        self.pegC = Peg()
        self.moves = 0

        self.sizeOfGame = int(input("Number of rings "))
        for i in reversed(range(self.sizeOfGame)):
             self.pegA.push(Disc(i))

        if self.sizeOfGame % 2 == 0:
             self.even()

        else:
             self.odd()

        print("finished in",self.moves,"moves")

    def move(self,fromPeg,toPeg): #will return a True if move made
        if fromPeg.isEmpty()== True:
             return False
         
        if toPeg.isEmpty() == True:  #move if peg being moved to is empty  
             popped = fromPeg.pop()
             toPeg.push(popped)
             print(self.pegA.see(),self.pegB.see(),self.pegC.see())
             self.moves = self.moves + 1
             return True
        else:
             if fromPeg.peek() < toPeg.peek(): #move if moved peg ring is smaller
                  popped = fromPeg.pop()
                  toPeg.push(popped)
                  print(self.pegA.see(),self.pegB.see(),self.pegC.see())
                  self.moves = self.moves + 1
                  return True
               
        return False

    def complete(self):
        
        """test if puzzle solved by seeing if pegC is completed in order""" 
        if len(self.pegC.see()) == self.sizeOfGame: #if all rings are on pegA
             for i in self.pegC.see()[:-1]:#see if each ring is in order
                                          #top disk is smaller than next disc
                                          #iterate through all discs apart from last disc
                  if i > self.pegC.see()[i+1]:
                       return False
        else:
             return False
        return True

     
    def even(self):
        """
        make the legal move between pegs A and B (in either direction),
        make the legal move between pegs A and C (in either direction),
        make the legal move between pegs B and C (in either direction),
        """
        while self.complete() != True:
             if self.move(self.pegA,self.pegB) != True:
                  self.move(self.pegB,self.pegA)
             if self.complete() == True: # this is ugly i know
                  break
               
             if self.move(self.pegA,self.pegC) != True:
                  self.move(self.pegC,self.pegA)
             if self.complete() == True: # this is ugly i know
                  break

             if self.move(self.pegB,self.pegC) != True:
                  self.move(self.pegC,self.pegB)
             if self.complete() == True: # this is ugly i know
                  break
        

    def odd(self):
        """
        make the legal move between pegs A and C (in either direction),
        make the legal move between pegs A and B (in either direction),
        make the legal move between pegs B and C (in either direction),
        """
        while self.complete() != True:
             if self.move(self.pegA,self.pegC) != True:
                  self.move(self.pegC,self.pegA)
             if self.complete() == True: # this is ugly i know
                  break
               
             if self.move(self.pegA,self.pegB) != True:
                  self.move(self.pegB,self.pegA)
             if self.complete() == True: # this is ugly i know
                  break

             if self.move(self.pegB,self.pegC) != True:
                  self.move(self.pegC,self.pegB)
             if self.complete() == True: # this is ugly i know
                  break
             

        


               
                  
             




tOH = TowersOfHanoi()

#print(tOH.complete())
#print(tOH.pegA.peek())
#print(tOH.pegB.peek())

