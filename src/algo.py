import numpy


class UUID:
    def uuid_dialna(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        identifier = ""
        for i in range(0, 36):
            if i % 4 == 0 and 21 >= i >= 7:
                identifier += "-"
            identifier += alphabet[numpy.random.randint(0, 36)]
        return identifier


identifier = UUID().uuid_dialna()

print(identifier)
