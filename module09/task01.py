class Elevator:
    def __init__(self, bottom, top):
        self.floor = bottom

    def floor_up(self):
        self.floor += 1
        print("Floor:", self.floor)

    def floor_down(self):
        self.floor -= 1
        print("Floor:", self.floor)

    def go_to_floor(self, target):
        while self.floor < target:
            self.floor_up()
        while self.floor > target:
            self.floor_down()

h = Elevator(1, 10)
print("Going to floor 5:")
h.go_to_floor(5)
print("\nGoing back to the bottom floor:")
h.go_to_floor(1)