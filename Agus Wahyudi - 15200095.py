print("******************************************************************")
print("PROGRAM STUDI    : ILMU KOMPUTER ")
print("MATA KULIAH      : STRUKTUR DATA ")
print("KELAS            : 15.2A.31      ")
print("TIM KELOMPOK 3                   ")
print("             1. DIMAS RAMADHAN AGUSTINA      (15200384)")
print("             2. AGUS WAHYUDI                 (15200095)")
print("             3. LAKSMONO ADZANI              (15200170)")
print("             4. GHIFARUL AZHAR               (15200234)")
print("******************************************************************")

# By Coddingan Agus Wahyudi
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push (self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s=Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
print("******************************************************************")

