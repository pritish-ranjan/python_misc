class Robot:
    
    def __init__(self, name, make):

        self.name = name
        self.make = make

    def get_robot_info(self):
        print("My name is", self.name)

# r1 = Robot()
# r1.name = "R1"
# r1.make = "Tesla"

# r2 = Robot()
# r2.name = "R2"
# r2.make = "SpaceX"

# r1.get_robot_info()
# r2.get_robot_info()

r3 = Robot("R3", "Stark")
r3.get_robot_info()

