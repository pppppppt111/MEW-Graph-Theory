class MEW:
    def __init__(self, key_size=32):
        self.key_size = key_size
        self.km1 = self._generate_key_matrix()
        self.km2 = self._generate_key_matrix()

    def _generate_key_matrix(self):
        """Generate a key_size x key_size matrix with random bytes (0-255)"""
        matrix = []
        for i in range(self.key_size):
            row = []
            for j in range(self.key_size):
                row.append(secrets.randbelow(256))
            matrix.append(row)
        return matrix

    def _get_move(self,byte_val):
        pass
    def _move(self):
        pass
    def _unmove(self):
        pass
    def _pass_encrypt(self)
        pass
    def _pass_decrypt(self)
        pass
    def encrypt(self):
        pass
    def decrypt(self):
        pass
        