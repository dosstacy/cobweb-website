class NormalPrice:

    def __init__(self, demand_shift, demand_slope, supply_shift, supply_slope, factor, periods, start_price):
        self.demand_shift = demand_shift
        self.demand_slope = demand_slope
        self.supply_shift = supply_shift
        self.supply_slope = supply_slope
        self.factor = factor
        self.periods = periods
        self.start_price = start_price

    def ad_exp(self):
        prices = []
        times = []

        equilibrium_price = (self.supply_shift - self.demand_shift) / (self.demand_slope - self.supply_slope)

        r = (self.supply_slope * (1 - self.factor)) / self.demand_slope
        constant = self.start_price - equilibrium_price

        for t in range(1, self.periods):
            pt = constant * (r ** t) + equilibrium_price
            prices.append(pt)
            times.append(t)

        return times, prices