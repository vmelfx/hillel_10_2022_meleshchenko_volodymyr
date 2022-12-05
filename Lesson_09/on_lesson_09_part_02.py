class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other: "Vector"):
        return Vector(x=self.x + other.x, y=self.y + other.y)


def main():
    # Ask user for vectors
    vector_a_repr: list[str] = input("Enter the first vector: ").split(",")
    vector_b_repr: list[str] = input("Enter the second vector: ").split(",")

    vector_a = Vector(x=int(vector_a_repr[0]), y=int(vector_a_repr[1]))
    vector_b = Vector(x=int(vector_b_repr[0]), y=int(vector_b_repr[1]))
    vector_c = vector_a + vector_b

    print(vector_a)
    print(vector_b)
    print(vector_c)


if __name__ == "__main__":
    main()
