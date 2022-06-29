class SymbolsIterator:
    def __init__(self, symbol, count):
        self.symbol = symbol
        self.count = count
        self.current_value = symbol

    def __next__(self):
        previous_value = self.current_value
        if len(self.current_value) <= self.count:
            self.current_value += self.symbol
            return previous_value
        else:
            raise StopIteration

    def __iter__(self):
        self.current_value = self.symbol
        return self


if __name__ == "__main__":
    my_sum = SymbolsIterator(symbol="N", count=5)
    for item in my_sum:
        print(item)
