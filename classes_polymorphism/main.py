from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values
    # TODO: add your code here
    def __add__(self, other):
        return [f"{i} {other}" for i in self.values]








if __name__ == "__main__":
    # check if this code is working
    print(Counter([1, 2, 3]) + "mississippi")
