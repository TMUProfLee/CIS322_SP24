import sys
sys.path.append('/Users/ethom/Downloads/GitHub/CIS322_SP24/source')
from CardGames import FugitiveFirst

def test_FugitiveFirst():
    #This function requires user input
    values = []
    test = []
    fugitive_hand = FugitiveFirst()
    for i in fugitive_hand:
        values += [i.value]
    for z in values:
        if z == 1 or z == 2 or z == 3 or z == 42:
            test += [z]
    draws = []
    for x in values:
        if x != 42 and x != 2 and x != 1 and x != 3:
            draws += [x]
    Low = 0
    Mid = 0
    for y in draws:
        if y <= 14 and y >= 4:
            Low += 1
        elif y >= 15 and y <= 28:
            Mid += 1
    
    test += [Low]
    test += [Mid]
    testcase = [3,2,1,42,3,2]
    #test variable should equal [3,2,1,42,3,2] for test to pass
    assert test == testcase


#Ran this file two times to show that there can be different results based on user input
test_FugitiveFirst()
    
