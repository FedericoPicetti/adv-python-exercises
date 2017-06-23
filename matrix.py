"""Provides a Matrix class"""

class Matrix:
    def __init__(self, l):
        x = map(len, l)
        if len(set(x))!=1:
            raise ValueError("List lenghts aren't consistent!")
        self.l = l


    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.l == other.l

    def copy(self):
        return Matrix([row.copy() for row in self.l])

    def __str__(self):
        return str(self.l)

    def __add__(a, b):
        if len(a.l) != len(b.l):
            raise ValueError("Matrices dimensions don't match!")
        return Matrix([[a.l[i][j] + b.l[i][j] for j in range(len(a.l[i]))] for i in range(len(a.l))])
    def __mul__(self, n):
        return Matrix([[self.l[i][j] * n for j in range(len(self.l[i]))] for i in range(len(self.l))])
    def __matmul__(a,b):
        n = len(a.l) # righe di a
        m = len(b.l[0]) #colonne di b
        p = len(b.l) #dimensione comune alle due matrici
        if (p != len(a.l[0])):
            raise ValueError("Matrices dimensions don't match!")
        newm = []
        for i in range(n):
            newline = []
            for j in range(m):
                newcell = 0
                for h in range(p):
                    newcell += a.l[i][h] * b.l[h][j]
                newline.append(newcell)
            newm.append(newline)
        return Matrix(newm)

    def transpose(self):
        newm = [[self.l[j][i] for j in range(len(self.l[i]))] for i in range(len(self.l))]
        return Matrix(newm)

    def norm(self):
        tr = self.transpose()
        return max([sum(map(abs, col)) for col in tr.l])



if __name__ == "__main__":
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[1, 2], [3, 4]])
    print(a != b)
    a = Matrix([[1, 3], [2, 4]])
    print(a != b)
    c = Matrix([[1]])
    print(a == c)
    print(a != c)
    print("Proviamo la copy")
    b = a
    print (b is a)
    b = a.copy()
    print (b is a)
    print(b==a)
    print("proviamo la somma")
    a = Matrix([[1, 2], [3, 4]])
    print(a)
    print(b)
    c = a+b
    print(c)
    print(a)
    print(b)
    print("proviamo la mul scalare")
    print(a*4)
    print("proviamo la matmul")
    i = Matrix([[1,0],[0,1]])
    print(a@i)
    print(a@b)
    print("proviamo transpose")
    print(a.transpose())
