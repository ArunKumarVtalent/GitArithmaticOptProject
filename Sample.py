class Sample:
    def Add(self, a, b):
        return a + b

    def Subtract(self, a, b):
        return a - b

    def Multiply(self, a, b):
        return a * b

    def Divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed."

    def Remainder(self, a, b):
        if b != 0:
            return a % b
        else:
            return "Error: Division by zero is not allowed."
