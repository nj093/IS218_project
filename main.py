from calculator import Calculator
from plugins import advanced_operations, statistics_operations

def run_examples():
    calc = Calculator()

    # Basic operations
    print("Addition (5 + 3):", calc.add(5, 3))
    print("Subtraction (10 - 4):", calc.subtract(10, 4))
    print("Multiplication (7 * 6):", calc.multiply(7, 6))
    print("Division (8 / 2):", calc.divide(8, 2))

    # Advanced operations using plugins
    print("Square Root (16):", advanced_operations.square_root(16))
    print("Power (2^3):", advanced_operations.power(2, 3))
    print("Sine (30 degrees):", advanced_operations.sine(30))
    print("Cosine (60 degrees):", advanced_operations.cosine(60))

    # Statistical operations
    data = [1, 3, 5, 7, 9]
    print("Mean of [1, 3, 5, 7, 9]:", statistics_operations.mean(data))
    print("Median of [1, 3, 5, 7, 9]:", statistics_operations.median(data))

if __name__ == "__main__":
    run_examples()
