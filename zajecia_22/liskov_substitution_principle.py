# class Bird:
#     def fly(self):
#         return "I can fly"
#
# class Penguin(Bird):
#     def fly(self):
#         raise Exception("I can't fly")
#
# birds = [Bird(), Penguin()]
# for bird in birds:
#     print(bird.fly())


class Bird:
    def move(self):
        print("I can move")

class FlyingBird(Bird):
    def fly(self):
        print("I can fly")

class Peguin(Bird):
    def swim(self):
        print("I can swim")

class Raven(FlyingBird):
    pass

birds = [Bird(), FlyingBird(), Peguin()]

for bird in birds:
    bird.move()