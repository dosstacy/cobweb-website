from tools.models import eq_price

class AdaptiveExpectations:

    def __init__(self, demand_shift, demand_slope, supply_shift, supply_slope, adapt_coeff, periods, start_price):
        self.demand_shift = demand_shift
        self.demand_slope = demand_slope
        self.supply_shift = supply_shift
        self.supply_slope = supply_slope
        self.adapt_coeff = adapt_coeff
        self.periods = periods
        self.start_price = start_price

    def find_adapt_expectation(self):
        pt = []
        times = []
        pt.append(self.start_price)

        equilibrium_price = eq_price(self.supply_shift, self.demand_shift, self.demand_slope, self.supply_slope)
        lam = ((self.supply_slope / self.demand_slope) - 1) * self.adapt_coeff + 1
        constant = self.start_price - equilibrium_price

        for i in range(1, self.periods+1):
            price = constant * (lam ** i) + equilibrium_price
            pt.append(price)
            times.append(i)
            print(times)

        return times, pt

