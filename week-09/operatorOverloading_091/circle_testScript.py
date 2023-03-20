from circle_091 import Point, Circle

def main():
    p1 = Point(2, 3)
    c1 = Circle(p1, 5)
    assert(c1.centre is p1)
    assert(c1.radius == 5)

    c2 = Circle()
    assert(isinstance(c2.centre, Point))
    assert(c2.radius == 1)

    c3 = Circle()
    assert(c3.centre is not c2.centre)

    print(c1)
    print(c2)
    print(c3)

if __name__ == '__main__':
    main()
