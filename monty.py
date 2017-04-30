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

    # do one thousand trials and record results
    success = 0
    failure = 0
    for i in range(1000):
        result = test_hall()
        if result:
            success += 1
        else:
            failure += 1

    print(str(success) + " successes")
    print(str(failure) + " failures")
if __name__ == "__main__":

    main()