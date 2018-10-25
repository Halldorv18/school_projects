class MyString:
    def __init__(self, a_string):
        self.string = len(a_string)
    
    def __str__(self):
        return "{}".format(self.string)

    def __sub__(self, other):
        if self.string > other.string:
            return str(self.string - other.string)
        else:
            return str(other.string - self.string)
    
    def __gt__(self, other):
        if self.string > other.string:
            return True
        else:
            return False


a = MyString("This is a string.")
b = MyString("What's up.")
print(a-b)