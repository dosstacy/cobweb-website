class NormalPrice:
    def __init__(self, p0, pN, c, periods):
        self.p0 = p0
        self.pN = pN
        self.c = c
        self.periods = periods

    def ad_exp(self):
        prices = [self.p0]
        for t in range(1, self.periods + 1):
            pt = prices[-1] + self.c * (self.pN - prices[-1])
            prices.append(pt)
        print("Final prices:", prices)
        return list(range(self.periods + 1)), prices
