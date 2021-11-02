from collections.abc import Iterator, Iterable


class MyIterator(Iterator):
    def __init__(self, iter_obj):
        self.iter_obj = iter_obj
        self.index = 0

    def __next__(self):
        try:
            word = self.iter_obj[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word


class Company:
    def __init__(self, employee_list):
        self.employee_list = employee_list

    def __iter__(self):
        return MyIterator(self.employee_list)


com = Company(['aa', 'bb', 'cc'])
for i in com:
    print(type(i))
    print(i)
