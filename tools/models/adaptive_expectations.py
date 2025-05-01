class AdaptiveExpectations:
    # def __init__(self, exp_old_price, old_prices, coefficient):
    #     self.exp_old_price = exp_old_price
    #     self.old_prices = self.parse_prices(old_prices)
    #     self.coefficient = coefficient

    # def find_adapt_expectation(self):
    #     expected_prices = [self.exp_old_price]
    #     periods = []
    #
    #     for t in range(1, len(self.old_prices)+1):
    #         p_e_t = expected_prices[-1] + self.coefficient * (self.old_prices[t - 1] - expected_prices[-1])
    #         print("Old price: ", p_e_t)
    #         print("Expected price: ", expected_prices[-1], " coefficient: ", self.coefficient, " old price: ", self.old_prices[t - 1], " expected price: ", expected_prices[-1])
    #         expected_prices.append(p_e_t)
    #         periods.append(t)
    #
    #     expected_prices.pop(0)
    #     print("expected prices: ", expected_prices)
    #     return periods, expected_prices
    #
    # def parse_prices(self, prices):
    #     return [float(x) for x in prices.split(",")]

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
        return times, pt