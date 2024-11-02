import logging
import os
from history_manager import HistoryManager
from config import Config
from plugins import advanced_operations

class Calculator:
    def __init__(self):
        self.history_manager = HistoryManager()

    def add(self, a, b):
        result = a + b
        self.history_manager.log_calculation("add", a, b, result)
        return result

    def subtract(self, a, b):
        result = a - b
        self.history_manager.log_calculation("subtract", a, b, result)
        return result

    def multiply(self, a, b):
        result = a * b
        self.history_manager.log_calculation("multiply", a, b, result)
        return result

    def divide(self, a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            logging.error("Attempted to divide by zero.")
            return None
        self.history_manager.log_calculation("divide", a, b, result)
        return result

    def repl(self):
        print("Welcome to the Advanced Calculator. Type 'exit' to quit.")
        while True:
            command = input("Enter operation (add, subtract, multiply, divide): ")
            if command == 'exit':
                break
            try:
                x, y = map(float, input("Enter two numbers separated by space: ").split())
                if command == "add":
                    print("Result:", self.add(x, y))
                elif command == "subtract":
                    print("Result:", self.subtract(x, y))
                elif command == "multiply":
                    print("Result:", self.multiply(x, y))
                elif command == "divide":
                    print("Result:", self.divide(x, y))
                else:
                    print("Unknown command")
            except ValueError:
                print("Invalid input")

if __name__ == "__main__":
    Calculator().repl()