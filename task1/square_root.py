def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    b квадрат - 4ac
    """
    return b**2 - 4*a*c

def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    D = discriminant(a, b, c)

    if D < 0:
        return None
    elif D == 0:
        x1 = (-b + D**(1/2)) / (2 * a)
        return x1
    else:
        x1 = (-b + D**(1/2)) / (2 * a)
        x2 = (-b - D**(1/2)) / (2 * a)
        return x1, x2


if __name__ == '__main__':
    solution(1, 8, 15) 
    solution(1, -13, 12)
    solution(-4, 28, -49)
    solution(1, 1, 1)
