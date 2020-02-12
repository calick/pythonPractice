class FizzBuzz():
    def __init__(self,num):
        self.fizzbuzz = ""
        self.toFizzBuzz(num)

    def printFizzBuzz(self):
        print(self.fizzbuzz)

    def toFizzBuzz(self,num):
        if (num % 3) == 0 and (num % 5) == 0:
            self.fizzbuzz = "FizzBuzz!"
        elif (num % 3) == 0:
            self.fizzbuzz = "Fizz!"
        elif (num % 5) == 0:
            self.fizzbuzz = "Buzz!"
        else:
            self.fizzbuzz = num

