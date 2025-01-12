import time

class TowersOfHanoi:

    tower_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    tower_b = []
    tower_c = []

    def print_towers():
        print(TowersOfHanoi.tower_a)
        print(TowersOfHanoi.tower_b)
        print(TowersOfHanoi.tower_c)
        print("\n")
        #time.sleep(1/10)

    def solve(plate, home, intermediate, finish):
        if plate == 1:
            finish.append(home.pop())
            TowersOfHanoi.print_towers()
        else:
            TowersOfHanoi.solve(plate - 1, home, finish, intermediate)
            finish.append(home.pop())
            TowersOfHanoi.print_towers()
            TowersOfHanoi.solve(plate - 1, intermediate, home, finish)

print("Running...")
TowersOfHanoi.solve(15, TowersOfHanoi.tower_a, TowersOfHanoi.tower_b, TowersOfHanoi.tower_c)
print("Complete")