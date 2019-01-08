class Optimus:
    """ Arguments -
        prime - Prime number lower than 2147483647
        inverse - The inverse of prime such that (prime * inverse) & 2**31-1 == 1
        xor - A large random integer lower than 2147483647"""
    def __init__(self,prime, inverse, xor):
        self.prime = int(prime)
        self.inverse = int(inverse)
        self.xor = int(xor)
        self.max = int((2**31) - 1)
        self.__validate(prime = self.prime,inverse = self.inverse,random = self.xor)
        
    def encode(self,value):
        """
        Accepts a integer value and returns obfuscated integer
        """
        self.__check_arg(value)
        return (int(value*self.prime) & self.max) ^ self.xor

    def decode(self,value):
        """
        Accepts obfuscated integer generated via encode method and returns the original integer
        """
        self.__check_arg(value)
        return ((value ^ self.xor)*self.inverse) & self.max

    def __check_arg(self,value):
        if not isinstance(value, int):
            raise Exception('Argument should be an integer')
    
    def __validate(self,**kwargs):
        if kwargs['prime'] >= 2147483647:
            raise Exception('The prime number should be less than 2147483647')
        if ((kwargs['prime'] * kwargs['inverse']) & (2**31 -1)) != 1:
            raise Exception('The inverse does not satisfy the condition "(prime * inverse) & 2**31-1 == 1"')
        if kwargs['random'] >= 2147483647:
            raise Exception('The random integer should be less than 2147483647')  