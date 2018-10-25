class Pair:
    def __init__(self, v1 = 0, v2 = 0):
        self.v1 = v1
        self.v2 = v2 
    def __add__(self, other):
            v1 = self.v1 + other.v1
            v2 = self.v2 + other.v2
            return Pair(v1, v2)
    def __str__(self):
        string = 'Value 1: {}, Value 2: {}'.format(self.v1, self.v2)
        return string

    


def main():
    b = Pair()
    print(b) == print('Value 1: 0, Value 2: 0')
    assert str(b) == 'Value 1: 0, Value 2: 0'
  
   

main()