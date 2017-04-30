# MontyHall
A simple implementation to test the monty hall problem.

def test_hall():

    doors = []
    doors[0] = True
    doors[1] = False
    doors[2] = False
    pick_num = randint(0,2)

    print(pick_num);
    print(doors);

    choices = [0, 1, 2]
    choices.remove(pick_num)

    for choice in choices:
        if door[choice] == True:
            print('you win');
            return

    print('you lost');

def main():

    test_hall();
    test_hall();
    test_hall();
    test_hall();
    test_hall();
    test_hall();
    test_hall();
    test_hall();
    test_hall();
    test_hall();

    def main():
    # my code here

if __name__ == "__main__":
    print('test');
    main()