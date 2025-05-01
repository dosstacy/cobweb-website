class NormalPrice:
    # def __init__(self, p0, pN, c, periods):
    #     self.p0 = p0
    #     self.pN = pN
    #     self.c = c
    #     self.periods = periods
    #
    # # def ad_exp(self):
    #     prices = [self.p0]
    #     for t in range(1, self.periods + 1):
    #         pt = prices[-1] + self.c * (self.pN - prices[-1])
    #         prices.append(pt)
    #     print("Final prices:", prices)
    #     return list(range(self.periods + 1)), prices

    def __init__(self, demand_shift, demand_slope, supply_shift, supply_slope, factor, periods, constant):
        self.demand_shift = demand_shift
        self.demand_slope = demand_slope
        self.supply_shift = supply_shift
        self.supply_slope = supply_slope
        self.factor = factor
        self.periods = periods
        self.constant = constant

    def ad_exp(self):
        prices = []
        times = []

        for t in range(1, self.periods):
            pt = self.constant * ((self.supply_slope * (1 - self.factor))/ self.demand_slope) ** t + (
                            (self.supply_shift - self.demand_shift) / (self.demand_slope - self.supply_slope))
            prices.append(pt)
            times.append(t)

        return times, prices
