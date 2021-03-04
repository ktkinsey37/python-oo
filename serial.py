"""Python serial number generator."""

class SerialGenerator:
    """Receives a number to start at as input. Creates serial numbers based on that starter.
    Able to generate next number and to reset back to original input serial.
    """
    def __init__(self, start):
        self.serial = start - 1
        self.starting_serial = start

    def generate(self):
        self.serial += 1
        return self.serial
        
    def reset(self):
        self.serial = self.starting_serial - 1