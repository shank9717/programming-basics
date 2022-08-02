from random import randrange
from typing import Optional, List

from Algorithms.Cryptography.AES.data import Data

CIPHERTEXT = 'ciphertext'
PLAINTEXT = 'plaintext'


class AESBlock:
    def __init__(self, key: Optional[int] = None, type: Optional[object] = 128) -> None:
        self.plaintext: Data = Data.__new__(Data)
        self.ciphertext: Data = Data.__new__(Data)
        self.iterations: Optional[int] = None
        self.type: Optional[object] = type
        if key is None:
            key = [str(randrange(0, 2)) for _ in range(128)]
            key = int('0b' + ''.join(key), base=2)
        self.key: Data = Data(Key=key)
        k = self.bytes_to_matrix(self.key.val)
        self.sub_key = self.key_expansion(k)

    def encrypt(self, plain_text: object) -> Data:
        self.plaintext.__init__(Plaintext=plain_text)
        size_plaintext = self.plaintext.bitsize
        iterations = size_plaintext / 128
        iterations = int(iterations) if int(iterations) == iterations else int(iterations) + 1
        final_cipher = 0x00
        mask = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        for i in range(iterations):
            ptext_i = (self.plaintext.val >> (iterations - 1 - i) * 128) & mask
            ctext_i = self.aes_encrypt(ptext_i)
            final_cipher ^= (ctext_i << (iterations - 1 - i) * 128)
        self.ciphertext.__init__(Ciphertext=final_cipher)
        return self.ciphertext

    def decrypt(self, ciphertext: bytes) -> Data:
        self.ciphertext.__init__(Ciphertext=ciphertext)
        size_ciphertext = self.ciphertext.bitsize
        iterations = size_ciphertext / 128
        iterations = int(iterations) if int(iterations) == iterations else int(iterations) + 1
        final_plaintext = 0x00
        mask = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        for i in range(iterations):
            ctext_i = (self.ciphertext.val >> (iterations - 1 - i) * 128) & mask
            ptext_i = self.aes_decrypt(ctext_i)
            final_plaintext ^= (ptext_i << (iterations - 1 - i) * 128)
        self.plaintext.__init__(Plaintext=final_plaintext)
        return self.plaintext

    # AES Structure
    def aes_encrypt(self, p_text: int) -> int:
        total_rounds = 10
        state = self.bytes_to_matrix(p_text)
        state = self.init_trans(state, self.sub_key[0])
        for rn in range(1, total_rounds):
            state = self.sub_bytes(state)
            state = self.shift_rows(state)
            state = self.mix_cols(state)
            state = self.add_round_key(state, self.sub_key[rn])
        state = self.sub_bytes(state)
        state = self.shift_rows(state)
        state = self.add_round_key(state, self.sub_key[10])
        return self.matrix_to_bytes(state)

    def aes_decrypt(self, c_text):
        total_rounds = 10
        state = self.bytes_to_matrix(c_text)
        state = self.init_trans(state, self.sub_key[10])
        for rn in range(1, total_rounds):
            state = self.inv_shift_rows(state)
            state = self.inv_sub_bytes(state)
            state = self.add_round_key(state, self.sub_key[10 - rn])
            state = self.inv_mix_cols(state)
        state = self.inv_shift_rows(state)
        state = self.inv_sub_bytes(state)
        state = self.add_round_key(state, self.sub_key[0])
        return self.matrix_to_bytes(state)

    # Auxiallary function
    @staticmethod
    def bytes_to_matrix(byte: int) -> List[List[int]]:
        """
        Converts 128-bit number to 4 x 4 matrix
        :param byte: 128-bit number
        :return: 2-D, 4 x 4 matrix
        """
        matrix = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(16):
            col = int(i / 4)
            row = int(i % 4)
            matrix[row][col] = (byte >> (15 - i) * 8) & 0xFF
        return matrix

    # Auxiallary function
    @staticmethod
    def matrix_to_bytes(matrix: List[List[int]]) -> int:
        """ Reverse operation of previous method """
        byte = 0
        for col in range(4):
            for row in range(4):
                subscript = 4 * col + row
                byte ^= matrix[row][col] << (15 - subscript) * 8
        return byte

    @staticmethod
    def mult_poly_poly(fx: int, gx: int, mx: int = 0b100011011) -> int:
        """
        Multiplies two polynomials a & b.
        :param a: Polynomial in integer format
        :param b: Polynomial in integer format
        :param mx: Set this parameter to 0 if multiplication is not done under any modulo
        """
        if mx == 0:
            final_ans = 0
            steps = len(bin(fx)) - 2
            for step in range(steps):
                if (fx >> step) & 0x01 == 1:
                    final_ans = final_ans ^ (gx << step)
            return final_ans
        prev_ans = gx
        final_ans = 0
        for step in range(8):
            if (fx >> step) & 0x01 == 1:
                final_ans = final_ans ^ prev_ans
            if (prev_ans & 0x80) >> 7 == 0:
                prev_ans = (prev_ans << 1) & 0xFF
            else:
                prev_ans = (prev_ans << 1) & 0xFF
                prev_ans ^= (mx & 0xFF)
        return final_ans

    def mult_inv(self, fx: int, mx: int = 0b100011011) -> int:
        """
        Finds multiplicative inverse of f(x) under mod m(x)
        :param fx: Polynomial in integer format
        :param mx: Defaults to Galois Field, GF(2^8)
        :return: Inverse in hexadecimal/number form
        """
        if fx == 0 or fx == 1:
            return fx
        x0, x1 = 1, 0
        y0, y1 = 0, 1
        r1, r2 = fx, mx
        r = -1
        while r != 1:
            a, b = r1, r2
            i = 0
            msb_r1 = len(bin(a)) - 3
            q = []
            while True:
                msb_r = len(bin(b)) - 3
                if msb_r - msb_r1 < 0:
                    break
                q.append(msb_r - msb_r1)
                b = (a << q[i]) ^ b
                if b == 0:
                    break
                i += 1
            r = b
            q = sum(pow(2, i) for i in q)
            r2 = r1
            r1 = r
            x0, x1 = x1, abs(x0 ^ self.mult_poly_poly(q, x1, mx=0))
            y0, y1 = y1, abs(y0 ^ self.mult_poly_poly(q, y1, mx=0))
        return y1

    # Initial transformation
    def init_trans(self, state: List[List[int]], k: List[int]) -> List[List[int]]:
        return self.add_round_key(state, k)

    # Substitute bytes box
    def sub_bytes(self, state: List[List[int]]) -> List[List[int]]:
        for i in range(4):
            for j in range(4):
                state[i][j] = self.sub_box(state[i][j])
        return state

    def inv_sub_bytes(self, state: List[List[int]]) -> List[List[int]]:
        for i in range(4):
            for j in range(4):
                state[i][j] = self.inv_sub_box(state[i][j])
        return state

    # Shift rows box
    @staticmethod
    def shift_rows(state: List[List[int]]) -> List[List[int]]:
        for i in range(4):
            state[i] = state[i][i:] + state[i][:i]
        return state

    @staticmethod
    def inv_shift_rows(state: List[List[int]]) -> List[List[int]]:
        for i in range(4):
            state[i] = state[i][4 - i:] + state[i][:4 - i]
        return state

    # Mix columns box
    def mix_cols(self, state: List[List[int]]) -> List[List[int]]:
        for j in range(4):
            a = self.mult_poly_poly(state[0][j], 2) ^ self.mult_poly_poly(state[1][j], 3) \
                ^ self.mult_poly_poly(state[2][j], 1) ^ self.mult_poly_poly(state[3][j], 1)

            b = self.mult_poly_poly(state[0][j], 1) ^ self.mult_poly_poly(state[1][j], 2) \
                ^ self.mult_poly_poly(state[2][j], 3) ^ self.mult_poly_poly(state[3][j], 1)

            c = self.mult_poly_poly(state[0][j], 1) ^ self.mult_poly_poly(state[1][j], 1) \
                ^ self.mult_poly_poly(state[2][j], 2) ^ self.mult_poly_poly(state[3][j], 3)

            d = self.mult_poly_poly(state[0][j], 3) ^ self.mult_poly_poly(state[1][j], 1) \
                ^ self.mult_poly_poly(state[2][j], 1) ^ self.mult_poly_poly(state[3][j], 2)
            state[0][j] = a
            state[1][j] = b
            state[2][j] = c
            state[3][j] = d
        return state

    def inv_mix_cols(self, state: List[List[int]]) -> List[List[int]]:
        for j in range(4):
            a = self.mult_poly_poly(state[0][j], 0x0E) ^ self.mult_poly_poly(state[1][j], 0x0B) \
                ^ self.mult_poly_poly(state[2][j], 0x0D) ^ self.mult_poly_poly(state[3][j], 0x09)

            b = self.mult_poly_poly(state[0][j], 0x09) ^ self.mult_poly_poly(state[1][j], 0x0E) \
                ^ self.mult_poly_poly(state[2][j], 0x0B) ^ self.mult_poly_poly(state[3][j], 0x0D)

            c = self.mult_poly_poly(state[0][j], 0x0D) ^ self.mult_poly_poly(state[1][j], 0x09) \
                ^ self.mult_poly_poly(state[2][j], 0x0E) ^ self.mult_poly_poly(state[3][j], 0x0B)

            d = self.mult_poly_poly(state[0][j], 0x0B) ^ self.mult_poly_poly(state[1][j], 0x0D) \
                ^ self.mult_poly_poly(state[2][j], 0x09) ^ self.mult_poly_poly(state[3][j], 0x0E)
            state[0][j] = a
            state[1][j] = b
            state[2][j] = c
            state[3][j] = d
        return state

    # Add round key box
    @staticmethod
    def add_round_key(state: List[List[int]], Ki: List[int]) -> List[List[int]]:
        k = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                k[j][i] = (Ki[i] >> (3 - j) * 8) & 0xFF
        for i in range(4):
            for j in range(4):
                state[i][j] ^= k[i][j]
        return state

    def sub_box(self, b: int) -> int:
        """ Implements function of S-box as specified in encryption standards of AES """
        b = str(bin(self.mult_inv(b)))[2:]
        b = '0' * (8 - len(b)) + b
        b = [int(x) for x in b]
        b.reverse()
        b = [str((b[i] + b[(i + 4) % 8] + b[(i + 5) % 8] + b[(i + 6) % 8] + b[(i + 7) % 8]
                  + 1 * (i == 0 or i == 1 or i == 5 or i == 6)) % 2) for i in range(8)]
        b.reverse()
        b = '0b' + ''.join(b)
        return int(b, base=2)

    def inv_sub_box(self, b: int):
        """ Implements function of IS-box as specified in encryption standards of AES """
        b = str(bin(b))[2:]
        b = '0' * (8 - len(b)) + b
        b = [int(x) for x in b]
        b.reverse()
        b = [str((b[(i + 2) % 8] + b[(i + 5) % 8] + b[(i + 7) % 8] + 1 * (i == 0 or i == 2)) % 2) for i in range(8)]
        b.reverse()
        b = '0b' + ''.join(b)
        b = int(b, base=2)
        return self.mult_inv(b)

    # Auxiallary function used for key expansion
    def g(self, wi: int, subscript: int) -> int:
        rc = [0x1, 0x2, 0x4, 0x8, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]
        b0 = (wi & (0xFF << 24)) >> 24
        b1 = (wi & (0xFF << 16)) >> 16
        b2 = (wi & (0xFF << 8)) >> 8
        b3 = (wi & (0xFF << 0)) >> 0
        rot_word = (b1 << 24) + (b2 << 16) + (b3 << 8) + b0
        sub_word = 0
        for i in range(4):
            temp = self.sub_box((rot_word >> (i * 8)) & 0xFF)
            sub_word += temp << (i * 8)
        rcon = rc[int(subscript / 4) - 1] << 24
        return sub_word ^ rcon

    def key_expansion(self, K: List[List[int]]) -> List[List[int]]:
        """
        Expands 128-bit key to 176 bytes
        :param K: 4 x 4 matrix of 16B input key
        :return: 11 x 4 matrix of 176B key for each round
        """
        w = [[0 for _ in range(4)] for _ in range(11)]
        k = [[0 for _ in range(4)] for _ in range(11)]
        for i in range(4):
            temp = 0
            for j in range(4):
                temp += K[j][i] << ((3 - j) * 8)
            w[0][i] = temp
        k[0] = w[0]
        for i in range(1, 11):
            for j in range(4):
                subscript = (i * 4) + j
                a, b = int((subscript - 1) / 4), ((subscript - 1) % 4)
                c, d = int((subscript - 4) / 4), ((subscript - 4) % 4)
                temp = w[a][b]
                if subscript % 4 == 0:
                    temp = self.g(temp, subscript)
                w[i][j] = temp ^ w[c][d]
            k[i] = w[i]
        return k
