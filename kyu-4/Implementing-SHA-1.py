class SHA1:
    def __init__(self):
        self.message = b''  
        self.h = [
            0x67452301,
            0xEFCDAB89,
            0x98BADCFE,
            0x10325476,
            0xC3D2E1F0
        ] 
        
    def update(self, message):
        self.message += message  

    def digest(self):
        m = self.message
        ml = len(m) * 8  
        m += b'\x80'  
        while (len(m) * 8 % 512) != 448:
            m += b'\x00'  
        
        ml_bytes = ml.to_bytes(8, 'big')
        m += ml_bytes
        
        chunks = [m[i:i+64] for i in range(0, len(m), 64)]
        for chunk in chunks:
            w = [0] * 80
            for i in range(16):
                w[i] = self.bytes_to_int(chunk[i*4:i*4+4])
            for i in range(16, 80):
                w[i] = self.leftrotate(w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16], 1)
            
            a, b, c, d, e = self.h
            
            for i in range(80):
                if 0 <= i <= 19:
                    f = (b & c) | ((~b) & d)
                    k = 0x5A827999
                elif 20 <= i <= 39:
                    f = b ^ c ^ d
                    k = 0x6ED9EBA1
                elif 40 <= i <= 59:
                    f = (b & c) | (b & d) | (c & d)
                    k = 0x8F1BBCDC
                elif 60 <= i <= 79:
                    f = b ^ c ^ d
                    k = 0xCA62C1D6
                
                temp = self.leftrotate(a, 5) + f + e + k + w[i] & 0xFFFFFFFF
                e = d
                d = c
                c = self.leftrotate(b, 30)
                b = a
                a = temp
            
            self.h[0] = (self.h[0] + a) & 0xFFFFFFFF
            self.h[1] = (self.h[1] + b) & 0xFFFFFFFF
            self.h[2] = (self.h[2] + c) & 0xFFFFFFFF
            self.h[3] = (self.h[3] + d) & 0xFFFFFFFF
            self.h[4] = (self.h[4] + e) & 0xFFFFFFFF
        
        digest_bytes = b''
        for h in self.h:
            digest_bytes += self.int_to_bytes(h, 4)
        
        return digest_bytes.hex().encode()
    
    @staticmethod
    def leftrotate(x, n):
        return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF
    
    @staticmethod
    def int_to_bytes(x, length):
        return x.to_bytes(length, 'big')
    
    @staticmethod
    def bytes_to_int(b):
        return int.from_bytes(b, 'big')
