import sys
from random import randint

def test_hall():

    doors = [True, False, False]
    pick_num = randint(0,2)

    #print(pick_num);
    #print(doors);

    choices = [0, 1, 2]
    choices.remove(pick_num)

    for choice in choices:
        if doors[choice] == True:
            return True


    return False

def main():

    # First argument is number of trials, otherwise default to 1000
    print(sys.argv)
    if len(sys.argv) >= 2:
        trials = int(sys.argv[1])
    else:
        trials = 1000

    success = 0
    failure = 0
    for i in range(trials):
        result = test_hall()
        if result:
            success += 1
        else:
            failure += 1

    # win percentage is success divided by total.
    percent = success / (success + failure)
    print("Win percentage when swapping: " + str(percent))
if __name__ == "__main__":

    main()
