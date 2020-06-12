class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity#amount of space possible
        self.current = 0#set to zero to start
        self.storage = [None]*capacity #learn this format here: https://stackoverflow.com/questions/10155510/how-to-grow-a-list-to-fit-a-given-capacity-in-python
#it works great!
    def append(self, item):
        self.storage[self.current] = item#storage at the current and make equal to item
        if self.current == self.capacity-1:#current node is at last spot in capacity
            self.current = 0#then current will go to the first in location
        else:
            self.current += 1#then increase the index location of each newly added item

    def get(self):#returns the list of items in the ring buffer
        result = []
        for item in [x for x in self.storage if x]:
            result.append(item)
        return result
    