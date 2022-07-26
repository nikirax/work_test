import random
import time

def test1(text):
    while(True):
        print(text[random.randrange(0,25)])
        time.sleep(10)
def test2(text):
    keys = []
    for item in text:
        keys.append(item)
    while(True):
        if keys.__len__() > 0:
            index = random.choice(keys)
            print(text[index])
            keys.remove(index)
            time.sleep(10)
        else:
            print("Test complete!")
            break

hiragana = {
    0:"su",
    1:"shi",
    2:"u",
    3:"ko",
    4:"a",
    5:"ka",
    6:"sa",
    7:"i",
    8:"chi",
    9:"wa",
    10:"e",
    11:"mi",
    12:"ku",
    13:"o",
    14:"n",
    15:"ta",
    16:"ki",
    17:"yu",
    18:"tsu",
    19:"ri",
    20:"ra",
    21:"ma",
    22:"so",
    23:"ha",
    24:"te",
    }
answer = input("Choose \"test_1\" or \"test_2\": ")
if answer.lower() == "test_1":
    test1(hiragana)
elif answer.lower() == "test_2":
    test2(hiragana)
else:
    print("Not found")