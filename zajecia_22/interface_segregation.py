from abc import ABC, abstractmethod

# class Worker(ABC):
#
#     @abstractmethod
#     def work(self):
#         pass
#
#     @abstractmethod
#     def eat(self):
#         pass
#
#     def get_salary(self):
#         print("I get salary")
#
#
# class HumanWorker(Worker):
#
#     def work(self):
#         print("Human is working")
#
#     def eat(self):
#         print("Human is eating")
#
# class RobotWorker(Worker):
#
#     def work(self):
#         print("Robot is working")
#
#     def eat(self):
#         raise Exception("Robot can't eat")


class Worker(ABC):

    @abstractmethod
    def work(self):
        pass

class Eater(ABC):

    @abstractmethod
    def eat(self):
        pass

class HumanWorker(Worker, Eater):

    def work(self):
        print("Human is working")

    def eat(self):
        print("Human is eating")

class RobotWorker(Worker):

    def work(self):
        print("Robot is working")

