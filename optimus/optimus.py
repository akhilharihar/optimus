class Optimus:
    SIZE = 31
    def __init__(self,prime, inverse, xor):
        self.prime = int(prime)
        self.inverse = int(inverse)
        self.xor = int(xor)
        self.max = int((2**Optimus.SIZE) - 1)
        
    def encode(self,value):
        Optimus.check_arg(value)
        return (int(value*self.prime) & self.max) ^ self.xor

    def decode(self,value):
        Optimus.check_arg(value)
        return ((value ^ self.xor)*self.inverse) & self.max

    @classmethod
    def check_arg(cls,value):
        if not isinstance(value, int):
            raise Exception('Argument should be an integer')