

class map_one:

    def to_integer(self, number):
        return int (number)

    def list_to_integer(self, numbers):
        return list(map(self.to_integer, numbers))


class map_two:

    def add_ten(self, number):
        return number + 10

    def add_ten_to(self, numbers):
        return list(map(self.add_ten, numbers))

class map_three:

    def to_farenheit(self, celcius):
        return celcius * 1.8 + 32

    def to_farenheits(self, list_of_celcius):
        return list(map(self.to_farenheit, list_of_celcius))

