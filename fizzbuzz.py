class Fizzbuzz(object):
    @staticmethod
    def value_of(i):
        if i % 3 == 0 and i % 5 == 0:
            return "FizzBuzz"
        if i % 3 == 0:
            return "Fizz"
        if i % 5 == 0:
            return "Buzz"
        return i