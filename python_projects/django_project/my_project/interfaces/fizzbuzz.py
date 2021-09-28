class Fizzbuzz:
    try:
        def calculate(self, number):

            if number % 3 == 0 and number % 5 == 0:
                return "fizzbuzz"

            if number % 3 == 0:
                return "fizz"

            if number % 5 == 0:
                return "buzz"
            
            return number
    
    except Exception as error:
        raise Exception("Not a number!", error)