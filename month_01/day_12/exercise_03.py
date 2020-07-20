class Vector2:
    """
        二维向量
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return Vector2(self.x * other.x, self.y * other.y)

    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y
        return self


vec01 = Vector2(1, 3)
print(id(vec01))
vec02 = Vector2(2, 4)
vec01 = vec01 * vec02
print(vec01.__dict__)
vec01 *= vec02
print(id(vec01))
print(vec01.__dict__)
