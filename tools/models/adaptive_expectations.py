class AdaptiveExpectations:

    def __init__(self, demand_shift, demand_slope, supply_shift, supply_slope, adapt_coeff, periods, constant):
        self.demand_shift = demand_shift
        self.demand_slope = demand_slope
        self.supply_shift = supply_shift
        self.supply_slope = supply_slope
        self.adapt_coeff = adapt_coeff
        self.periods = periods
        self.constant = constant


    def find_adapt_expectation(self):
        pt = []
        times = []
        for i in range(1, self.periods):
            value = self.constant * ((((self.supply_slope / self.demand_slope) - 1) * self.adapt_coeff + 1) ** i) + (
                                (self.supply_shift - self.demand_shift) / (self.demand_slope - self.supply_slope))
            pt.append(value)
            times.append(i)

        print("Equilibrium price")
        print((self.supply_shift - self.demand_shift) / (self.demand_slope - self.supply_slope))

        print("Lambda")
        print(((self.supply_slope / self.demand_slope) -1) * (self.adapt_coeff + 1))
        return times, pt

