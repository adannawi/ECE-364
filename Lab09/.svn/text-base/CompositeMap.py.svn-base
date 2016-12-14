class Entry:

    def __init__(self, k1, k2, v):
        if type(k1) is not int:
            raise TypeError("k1 is not an int!")
        if type(k2) is not int:
            raise TypeError("k2 is not an int!")
        if type(v) is not str:
            raise TypeError("v is not a string!")
        self.k1 = k1
        self.k2 = k2
        self.v = v
        self.key = (k1, k2)


    def __str__(self):
        return "({}, {}): \"{}\"".format(self.k1, self.k2, self.v)

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        if self.__hash__() == other.__hash__():
            return True
        return False

class Lookup:

    def __init__(self, name):
        if len(name) == 0:
            raise ValueError("Name can not be empty!")
        self._name = name
        self._container = set()
    def __str__(self):
        return "[\"{}\": {} Entries]".format(self._name, len(self._container)-1)

    def add(self, entry):
        for item in self._container:
            if item.__hash__() == entry.__hash__():
                raise KeyError("Entry already exists in store!")
        self._container.add(entry)

    def update(self, entry):
        found = 0
        for item in self._container:
            if item.__hash__() == entry.__hash__():
                self._container.remove(item)
                self._container.add(entry)
                found = 1
        if found == 0:
            raise KeyError("Entry does not exist!")

    def addOrUpdate(self, entry):
        updating = 0
        for item in self._container:
            if item.__hash__() == entry.__hash__():
                self.update(entry)
                updating = 1
        if updating == 0:
            self.add(entry)
    def remove(self, entry):
        found = 0
        for item in self._container:
            if item.__hash__() == entry.__hash__():
                found = 1
        if found == 0:
            raise KeyError("Value not found!")
        self._container.remove(entry)

    def count(self):
        return len(self._container)

    def __getitem__(self, item):
        if (type(item) is int and item > self.count()):
            raise KeyError("Could not find entry, index is out of range!")
        if type(item) is tuple:
            for setItem in self._container:
                if setItem.k1 == item[0] and setItem.k2 == item[1]:
                    returnItem = setItem.__str__()
                    return returnItem
        if type(item) is int:
            entryList = list(self._container)
            fixedList = [i.__str__() for i in entryList]
            fixedList.sort()
            returnItem = fixedList[item]
            return returnItem
        raise KeyError ("Could not find desired entry!")

    def __setitem__(self, item, value):
        updated = 0
        for setItem in self._container:
            if setItem.k1 == item[0] and setItem.k2 == item[1]:
                self.update(Entry(item[0], item[1], value))
                updated = 1
        if updated == 0:
            newEntry = Entry(item[0], item[1], value)
            self.add(newEntry)

if __name__ == '__main__':
    entry1 = Entry(1, 1, "yes")
    entry2 = Entry(1, 10, "my keyboard")
    entry3 = Entry(1, 10, "who now?")
    entry4 = Entry(4, 5, "duck duck")
    entry5 = Entry(1, 1, "goose")
    lookUp = Lookup("My Lookup")
    lookUp.add(entry1)
    lookUp.add(entry2)
    lookUp.update(entry3)
    lookUp.update(entry2)
    lookUp.addOrUpdate(entry4)
    lookUp.addOrUpdate(entry5)
    print(lookUp[(1,1)])
    print(lookUp.count())
    lookUp[(10,5)] = "Hello World!"
    print(lookUp[(10,5)])
    print(lookUp.count())
    lookUp[(10,5)] = "Updating, wow!"
    print(lookUp[(10,5)])
    print(lookUp.count())

