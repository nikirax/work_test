class FirstMethodQueue:
    def __init__(self ,array):
        print(f"Array: {array}")
        self.array = array
    def FirstIn(self, number):
        try:
            self.array = self.array + [number]
            print(f"Successfully added a number: {number}")
        except Exception as ex:
            print(ex)
    def FirstOut(self):
        try:
            out_element = self.array[0]
            self.array = self.array[1:]
            print(f"You have received an item: {out_element}")
            return out_element
        except Exception as ex:
            print(ex)
class SecondMethodQueue:
    def __init__(self, array):
        print(f"Array: {array}")
        self.array = array

    def FirstIn(self, number):
        self.array.append(number)
        print(f"Successfully added a number: {number}")

    def FirstOut(self):
        if self.array:
            out_element = self.array.pop(0)
        else:
            out_element = None
        print(f"You have received an item: {out_element}")
        return out_element

if "__main__" == __name__:
    array1 = FirstMethodQueue(array=[1,2,3,4])
    num1 = array1.FirstOut()
    array1.FirstIn(20)
    print(array1.array, num1)
    array2 = SecondMethodQueue(array=[1,2,3,4])
    num2 = array2.FirstOut()
    array2.FirstIn(20)
    print(array2.array, num2)

