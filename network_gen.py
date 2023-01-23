from random import randint, seed
import math

def branching(flr):
    if( flr <= 4 ):
        max_branches = 0
    else:
        max_branches = flr - 4
    branches = 0
    while(branches < max_branches):
        if(randint(1,10) >= 7):
            branches += 1  
        else:
            break
    return(branches)

def tree_split(branches, main):
    #do some math here
    #Setup
    net = [main] + [0] * branches
    divs = [1]  + [0] * branches
    br = branches
    free_floors = floors - 2 - main_len

    #Adding branches
    for i in range(1,br + 1):
        n_len = max_n_len = math.trunc(free_floors/branches)
        if branches > 1:
            n_len = randint(1, max_n_len)
        div_pos = randint(1, main_len-n_len)
        #Setup end
        net[i] = n_len
        divs[i] = div_pos

        free_floors -= n_len
        branches -= 1

    #Centering the net arch


    #

    print("\n Node lenghts: ", net,  " Division positions: ", divs)
    #print ("\n Division position: ", div_poss, " Free floors: ", free_floors, " Total divisions: ", branches)


if __name__ == "__main__":
    #seed = seed()
    floors =  randint(1, 6) + randint(1, 6) + randint(1, 6)
    branches = branching(floors)
    # min_main_len = (math.ceil((floors - 2) / (branches + 1)) + 1) if branches != 0 else (floors - 2)

    base_len = (floors - 2) / (branches + 1)
    tenth = base_len - math.trunc(base_len)
    modf = math.trunc(tenth * (branches + 1)) + (0 == tenth)
    modf = modf if modf < 3 else 2

    min_main_len = (math.trunc(base_len) + modf) if branches != 0 else (floors - 2)
    max_main_len = (floors - 2 - branches) if branches != 0 else (floors - 2)

    print ("Минимальная длинна главной ноды: ",min_main_len,"| Максимальная длинна главной ноды: ", max_main_len)
    main_len = randint(min_main_len, max_main_len)
    print ("Создана архитектура. Этажей: ", floors, "| Делений: ", branches,"| Длина главной ноды", main_len)

    if (branches != 0):
        tree_split(branches, main_len)