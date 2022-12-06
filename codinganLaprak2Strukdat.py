class PriorityQueueWithBinaryTree:
    def __init__(self) :
        self.penampung = [0]*1000
        self.size = -1


    def _parent(self,i) :
        return (i - 1) // 2

    def _leftChild(self,i) :
        return ((2 * i) + 1)

    def _rightChild(self,i) :
        return ((2 * i) + 2)
        

    def _swap(self,i, j) :
        
        temp = self.penampung[i]
        self.penampung[i] = self.penampung[j]
        self.penampung[j] = temp
    def _shiftUp(self,i) :
        while (i > 0 and self.penampung[self._parent(i)] < self.penampung[i]) :
            self._swap(self._parent(i), i)
            i = self._parent(i)
            
    def _shiftDown(self,i) :

        maxIndex = i
        
        l = self._leftChild(i)
        
        if (l <= self.size and self.penampung[l] > self.penampung[maxIndex]) :
        
            maxIndex = l
        
        r = self._rightChild(i)
        
        if (r <= self.size and self.penampung[r] > self.penampung[maxIndex]) :
        
            maxIndex = r
        
        if (i != maxIndex) :
        
            self._swap(i, maxIndex)
            self._shiftDown(maxIndex)


    def insert(self,p) :
        self.size = self.size + 1
        self.penampung[self.size] = p

        self._shiftUp(self.size)

    def getMax(self) :

        return self.penampung[0]

pqbt=PriorityQueueWithBinaryTree()
daftar_char={"childe":2_500_000,"eula":5_000_000,"hu tao":1_500_000,"mona":2_000_000,"diluc":700_000,"zhongli":300_000,"raiden":1_000_000}
daftar_char2=dict(((j,i) for i, j in daftar_char.items()))
pqbt.insert(daftar_char['childe'])
pqbt.insert(daftar_char['eula'])
pqbt.insert(daftar_char['hu tao'])
pqbt.insert(daftar_char['mona'])
pqbt.insert(daftar_char['diluc'])
pqbt.insert(daftar_char['zhongli'])
pqbt.insert(daftar_char['raiden'])

i = 0
print("Daftar karakter berdasarkan Priority Queue : ")
while (i <= pqbt.size) :

	print(f"Priority-{i+1} : {daftar_char2[pqbt.penampung[i]]} ==> {pqbt.penampung[i]}")
	i += 1

print()
damage_maksimum=pqbt.getMax()
print(f"Karakter yang memiliki damage terbesar yaitu {daftar_char2[damage_maksimum]} sebesar {damage_maksimum}")





