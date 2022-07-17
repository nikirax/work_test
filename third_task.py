import time
import random as rnd
def sort(array):
    for i in range(len(array)):
        min_id = i
        for j in range(i+1, len(array)):
            if array[min_id] > array[j]:
                min_id = j
        array[i], array[min_id] = array[min_id], array[i]

if "__main__" == __name__:
    n = rnd.randrange(0, 100)
    array = []
    for i in range(0, n): 
        array.append(rnd.randrange(0, 100))
    start_time = time.time()
    print(sort(array))
    print("--- %s seconds ---" % (time.time() - start_time))
# это обычная сортировка выборкой по тестам она одна из быстрейших. Но идеального ничего не бывает)