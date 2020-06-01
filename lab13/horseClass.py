class Horse:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print("hello!!! i am a horse :^)")

a = Horse("Seabiscuit")
b = Horse("Milo")

print(a.name)
print(b.name)

a.talk()
b.talk()