class Coodinate(object):
    def __init__(self, x, y):
        """Setam valorile lui x si y"""
        self.x = x
        self.y = y

    def __str__(self):
        """ Returnam self ca si string"""
        return "<" + str(self.x) + "," + str(self.y) + ">"

    def distance(self, other):
        """ Returnam disntanta euclidiana dintre cele doua puncte"""
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5


punct = Coodinate(1, 2)
print(punct)
print(punct.x)
print(punct.y)

