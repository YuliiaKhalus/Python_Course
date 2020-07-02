# Task 7
class RomanNumber(int):

    @staticmethod
    def int_to_roman(number):
        number = (int(number))
        ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        result = []
        for i in range(len(ints)):
            count = int(number / ints[i])
            result.append(nums[i] * count)
            number -= ints[i] * count
        return ''.join(result)

    def __new__(cls, *args, **kwargs):
        try:
            for arg in args:
                if 0 < arg < 4000:
                    instance = super().__new__(cls, *args, **kwargs)
                    return instance
                raise ValueError
        except ValueError:
            return 'The value of Roman numbers should be within the range 1-3999.'

    def __str__(self):
        return self.int_to_roman(self)

    def __add__(self, other):
        return RomanNumber(super().__add__(other))

    def __sub__(self, other):
        return RomanNumber(super().__sub__(other))

    def __mul__(self, other):
        return RomanNumber(super().__mul__(other))

    def __truediv__(self, other):
        return RomanNumber(super().__truediv__(other))


V = RomanNumber(5)
X = RomanNumber(10)
IX = RomanNumber(9)


a = X + IX
b = IX - V

print(X)
print(bin(X))
print(X + 10)
print(X + X)
print(X * 10)
print(X * X)
print(X - 9)
print(X - IX)
print(X / 3)
print(X == X)
print(X > V)
print(V < X)
print(V >= V)
print(V <= V)
print(V <= 5)
print(V != 6)
print(a)
print(b)
print(a + b)
print(V + 500000)


# Task 2
class RangeFunction:

    def __init__(self, *limits):
        self.step = 1
        if len(limits) == 2:
            self.current, self.finish = limits[0], limits[1]
        elif len(limits) == 3:
            self.current, self.finish, self.step = limits[0], limits[1], limits[2]
        else:
            self.finish = limits[0]
            self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        curr = self.current
        if curr > self.finish:
            raise StopIteration

        self.current += self.step

        return curr


range_with_2_param = RangeFunction(2, 6)
range_with_1_param = RangeFunction(9)
range_with_3_param = RangeFunction(0, 10, 2)

for i in range_with_2_param:
    print(i)

for i in range_with_1_param:
    print(i)

for i in range_with_3_param:
    print(i)

# Task 3
class Str(str):

    def __truediv__(self, other):
        if isinstance(other, str):
            return f'{self}/{other}'

    def __matmul__(self, other):
        if isinstance(other, str):
            return f'{self}@{other}.com'


path = Str('path')
prefix = Str('usr')
gmail = Str('gmail')
mail = Str('mail')

print(prefix / path)
print(mail @ gmail)






