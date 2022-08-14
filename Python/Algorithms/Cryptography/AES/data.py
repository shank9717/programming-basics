from binascii import hexlify
from math import log
from typing import Optional

CIPHERTEXT = 'ciphertext'
PLAINTEXT = 'plaintext'


class Data:
    def __init__(self, **kwargs):
        self.type: Optional[int] = None
        self.val: Optional[object] = None
        for key, val in kwargs.items():
            self.type = key
            self.val = val
        if self.type.lower() == PLAINTEXT or self.type.lower() == CIPHERTEXT:
            if type(self.val) == bytes:
                temp = hexlify(self.val)
                self.val = int(temp, base=16)
            elif type(self.val) == str:
                self.val = [hex(ord(c))[2:] for c in list(self.val)]
                self.val = '0x' + ''.join(self.val)
                self.val = int(self.val, base=16)
        elif self.type.lower() == 'key':
            if type(self.val) == str:
                if self.val[:2] != "0x":
                    self.val = "0x" + self.val
                self.val = int(self.val, base=16)
        self.bitsize = self.bit_size(self.val)

    def __repr__(self):
        return hex(self.val)

    @staticmethod
    def bit_size(var):
        return int(log(var, 2)) + 1

    def remove(self):
        self.val = None
