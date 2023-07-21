from point import Point


def initialize_points() -> list[Point]:
    points = []

    points.append(Point(-0.5, -0.5, -0.5, -0.5))
    points.append(Point(0.5, -0.5, -0.5, -0.5))
    points.append(Point(0.5, 0.5, -0.5, -0.5))
    points.append(Point(-0.5, 0.5, -0.5, -0.5))
    points.append(Point(-0.5, -0.5, 0.5, -0.5))
    points.append(Point(0.5, -0.5, 0.5, -0.5))
    points.append(Point(0.5, 0.5, 0.5, -0.5))
    points.append(Point(-0.5, 0.5, 0.5, -0.5))

    points.append(Point(-0.5, -0.5, -0.5, 0.5))
    points.append(Point(0.5, -0.5, -0.5, 0.5))
    points.append(Point(0.5, 0.5, -0.5, 0.5))
    points.append(Point(-0.5, 0.5, -0.5, 0.5))
    points.append(Point(-0.5, -0.5, 0.5, 0.5))
    points.append(Point(0.5, -0.5, 0.5, 0.5))
    points.append(Point(0.5, 0.5, 0.5, 0.5))
    points.append(Point(-0.5, 0.5, 0.5, 0.5))

    return points


def initialize_projected_points(points: list[Point]) -> list[list[int]]:
    return [[n, n] for n in range(len(points))]
