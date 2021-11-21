class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # add adittional resposabilities 
    # ability to save 
    # it can be at first a good idea, but it's not, because 
    # you might want to change this persistancy method from time to time 
    # for every object, so, implement it in another class, and not 
    # inside this class

class PersistenceManager:

    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

j = Journal()
j.add_entry('I cried today.')
j.add_entry('I ate a bug.')
print(f'Journal entries:\n{j}')

file = r'/media/vpb/GD_/USP/DS/_1Git/_10_designpatterns_python/data/journals.txt'
PersistenceManager.save_to_file(j, file)

# read the file
with open(file) as fh:
    print(fh.read())
