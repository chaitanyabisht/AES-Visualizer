import copy

class AES:
    # AES Sbox
    sbox =  [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67,
        0x2b, 0xfe, 0xd7, 0xab, 0x76, 0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59,
        0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 0xb7,
        0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1,
        0x71, 0xd8, 0x31, 0x15, 0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05,
        0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75, 0x09, 0x83,
        0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29,
        0xe3, 0x2f, 0x84, 0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
        0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf, 0xd0, 0xef, 0xaa,
        0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c,
        0x9f, 0xa8, 0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc,
        0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2, 0xcd, 0x0c, 0x13, 0xec,
        0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19,
        0x73, 0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee,
        0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb, 0xe0, 0x32, 0x3a, 0x0a, 0x49,
        0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4,
        0xea, 0x65, 0x7a, 0xae, 0x08, 0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6,
        0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a, 0x70,
        0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9,
        0x86, 0xc1, 0x1d, 0x9e, 0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e,
        0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf, 0x8c, 0xa1,
        0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0,
        0x54, 0xbb, 0x16]
    
    inv_sbox = [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3,
        0x9e, 0x81, 0xf3, 0xd7, 0xfb , 0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f,
        0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb , 0x54,
        0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b,
        0x42, 0xfa, 0xc3, 0x4e , 0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24,
        0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25 , 0x72, 0xf8,
        0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d,
        0x65, 0xb6, 0x92 , 0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda,
        0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84 , 0x90, 0xd8, 0xab,
        0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3,
        0x45, 0x06 , 0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1,
        0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b , 0x3a, 0x91, 0x11, 0x41,
        0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6,
        0x73 , 0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9,
        0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e , 0x47, 0xf1, 0x1a, 0x71, 0x1d,
        0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b ,
        0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0,
        0xfe, 0x78, 0xcd, 0x5a, 0xf4 , 0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07,
        0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f , 0x60,
        0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f,
        0x93, 0xc9, 0x9c, 0xef , 0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5,
        0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61 , 0x17, 0x2b,
        0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55,
        0x21, 0x0c, 0x7d]

    round_steps = {}

    def __init__(self, key = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]):
        self.key = key
        self.round_keys = self.key_expansion()
        self.state = [[None, None, None, None]*4]
    
    rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]

    def key_expansion(self):

        round_keys = [self.key]
        # shift down the last column

        for round in range(10):
            l = copy.deepcopy(round_keys[-1])
            l[0][3], l[1][3], l[2][3], l[3][3] = l[1][3], l[2][3], l[3][3], l[0][3]
            

            for i in range(4):
                l[i][3] = self.sbox[l[i][3]]
            
            # xor with rcon
            l[0][3] ^= self.rcon[round]

            # xor with first column of previous key
            for i in range(4):
                l[i][0] = l[i][3] ^ round_keys[-1][i][0]

            for col in range(1, 4):
                for row in range(0, 4):
                    l[row][col] = l[row][col - 1] ^ round_keys[-1][row][col]
            
            round_keys.append(l)

        return round_keys


    def key_expansion_steps(self, r):
        r = r - 1
        round_keys = [self.key]
        # shift down the last column
        sub_round_keys = []
        for round in range(10):
            l = copy.deepcopy(round_keys[-1])
            if (round == r):
                # print('Round Key')
                # AES.pretty_print(l)
                sub_round_keys.append(copy.deepcopy(l))
                # print()
            
            l[0][3], l[1][3], l[2][3], l[3][3] = l[1][3], l[2][3], l[3][3], l[0][3]
            
            if (round == r):
                # print('Take last column of previous key and move top byte to bottom')
                # AES.pretty_print(l)
                sub_round_keys.append(copy.deepcopy(l))
                # print()
            
            for i in range(4):
                l[i][3] = self.sbox[l[i][3]]
            
            if (round == r):
                # print('Substitute each byte of the last column with the corresponding byte in the S-Box')
                # AES.pretty_print(l)
                sub_round_keys.append(copy.deepcopy(l))
                # print()
            
            # xor with rcon
            l[0][3] ^= self.rcon[round]

            if (round == r):
                # print('XOR the top byte of the last column with the corresponding byte in the Round Constant Table')
                # AES.pretty_print(l)
                sub_round_keys.append(copy.deepcopy(l))
                # print()

            for i in range(4):
                l[i][0] = l[i][3] ^ round_keys[-1][i][0]
            
            if (round == r):
                # print('XOR the first column of the new key with the last column of the previous key')
                # AES.pretty_print(l)
                sub_round_keys.append(copy.deepcopy(l))
                # print()

            for col in range(1, 4):
                for row in range(0, 4):
                    l[row][col] = l[row][col - 1] ^ round_keys[-1][row][col]
            
            if (round == r):
                # print('XOR the remaining columns of the new key with the corresponding columns of the previous key')
                # AES.pretty_print(l)
                sub_round_keys.append(copy.deepcopy(l))
                # print()
            
            round_keys.append(l)
        return sub_round_keys

    def get_round_key(self, round):
        return self.round_keys[round]

    def set_state(self, state):
        self.state = state
    
    def get_state(self):
        return copy.deepcopy(self.state)
    
    def __str__(self):
        table = PrettyTable()
        table.hrules = True
        for i in range(0, 4):
            table.add_row([hex(j) for j in self.state[i]])
        return table.get_string(header=False, border=True)

    def pretty_print(obj, hex_val = True):
        table = PrettyTable()
        table.hrules = True
        for i in range(0, 4):
            if (hex_val):
                table.add_row([hex(j) for j in obj[i]])
            else:
                table.add_row(obj[i])
        print(table.get_string(header=False, border=True))

    def dec2hex(obj):
        return [[hex(j) for j in i] for i in obj]
    
    def hex2dec(obj):
        return [[int(j, 16) for j in i] for i in obj]


    def add_round_key(self, round):
        round_key = self.get_round_key(round)
        for i in range(0, 4):
            for j in range(0, 4):
                self.state[i][j] ^= round_key[i][j]


    def sub_bytes(self):
        for i in range(0, 4):
            for j in range(0, 4):
                self.state[i][j] = self.sbox[self.state[i][j]]
    
    def inv_sub_bytes(self):
        for i in range(0, 4):
            for j in range(0, 4):
                self.state[i][j] = self.inv_sbox[self.state[i][j]]

    def shift_rows(self):
        for i in range(1, 4):
            self.state[i] = self.state[i][i:] + self.state[i][:i]

    def mult(x, y):                  # mpy two 8 bit values
        p = 0b100011011             # mpy modulo x^8+x^4+x^3+x+1
        m = 0                       # m will be product
        for i in range(8):
            m = m << 1
            if m & 0b100000000:
                m = m ^ p
            if y & 0b010000000:
                m = m ^ x
            y = y << 1
        return m

    def mix_cols(self):
        for i in range(0, 4):
            s0 = self.state[0][i]
            s1 = self.state[1][i]
            s2 = self.state[2][i]
            s3 = self.state[3][i]
            self.state[0][i] = AES.mult(0x02, s0) ^ AES.mult(0x03, s1) ^ s2 ^ s3
            self.state[1][i] = s0 ^ AES.mult(0x02, s1) ^ AES.mult(0x03, s2) ^ s3
            self.state[2][i] = s0 ^ s1 ^ AES.mult(0x02, s2) ^ AES.mult(0x03, s3)
            self.state[3][i] = AES.mult(0x03, s0) ^ s1 ^ s2 ^ AES.mult(0x02, s3)

    
    def round_enc(self, round):
        self.round_steps[round] = []
        self.round_steps[round].append(copy.deepcopy(self.state))
        if (round == 1):
            self.add_round_key(0)
            self.round_steps[round].append(copy.deepcopy(self.state))

        self.sub_bytes()
        self.round_steps[round].append(copy.deepcopy(self.state))

        self.shift_rows()
        self.round_steps[round].append(copy.deepcopy(self.state))

        self.mix_cols()
        self.round_steps[round].append(copy.deepcopy(self.state))

        self.add_round_key(round)
        self.round_steps[round].append(copy.deepcopy(self.state))
    
    def get_round_steps(self):
        self.round_enc(1)
        self.round_enc(2)
        self.round_enc(3)
        self.round_enc(4)
        self.round_enc(5)
        self.round_enc(6)
        self.round_enc(7)
        self.round_enc(8)
        self.round_enc(9)
        self.final_round_enc(10)
        return self.round_steps


    def final_round_enc(self, round):
        self.round_steps[round] = []
        self.round_steps[round].append(copy.deepcopy(self.state))

        self.sub_bytes()
        self.round_steps[round].append(copy.deepcopy(self.state))

        self.shift_rows()
        self.round_steps[round].append(copy.deepcopy(self.state))

        self.add_round_key(round)
        self.round_steps[round].append(copy.deepcopy(self.state))

    def XOR(obj1, obj2):
        return [[obj1[i][j] ^ obj2[i][j] for j in range(4)] for i in range(4)]
        