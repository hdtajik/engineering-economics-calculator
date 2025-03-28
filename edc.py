
# Standard Library
from sys import argv

# Local Library
from cfc import pf, fp, af, fa, ap


class DepreciationMethod:

    def __init__(self, original_cost, salvage_value, period):
        self.original_cost = original_cost
        self.salvage_value = salvage_value
        self.period = period

    def depreciation(self):
        pass

    def book_value(self):
        pass

    def depreciation_present_worth(self, interest):
        return sum([d * pf(interest, m + 1) for m, d in enumerate(self.depreciation())])

    def depreciation_equivalent_uniform_annual(self, interest):
        return self.depreciation_present_worth(interest) * ap(interest, self.period)


class StraightLine(DepreciationMethod):

    def depreciation(self):
        return [(self.original_cost - self.salvage_value) / self.period for _ in range(0, self.period)]

    def book_value(self):
        return [self.original_cost - m * self.depreciation()[0] for m in range(0, self.period + 1)]


class SumOfTheYearsDigits(DepreciationMethod):

    def __init__(self, original_cost, salvage_value, period):
        super().__init__(original_cost, salvage_value, period)
        self.SYD = 0.5 * self.period * (self.period + 1)

    def depreciation(self):
        return [(self.period - m + 1) / self.SYD * (self.original_cost - self.salvage_value) for m in range(1, self.period + 1)]

    def book_value(self):
        return [self.original_cost - m * (self.period - m / 2 + 0.5) / self.SYD * (self.original_cost - self.salvage_value) for m in range(0, self.period + 1)]


class SinkingFund(DepreciationMethod):

    def __init__(self, original_cost, salvage_value, period, interest):
        super().__init__(original_cost, salvage_value, period)
        self.interest = interest

    def depreciation(self):
        return [(self.original_cost - self.salvage_value) * af(self.interest, self.period) * fp(self.interest, m - 1) for m in range(1, self.period + 1)]

    def book_value(self):
        return [self.original_cost - ((self.original_cost - self.salvage_value) * af(self.interest, self.period) * fa(self.interest, m)) for m in range(0, self.period + 1)]


class DecliningBalance(DepreciationMethod):

    def __init__(self, original_cost, salvage_value, period, depreciation_rate):
        super().__init__(original_cost, salvage_value, period)
        self.depreciation_rate = depreciation_rate

    def depreciation(self):
        return [self.depreciation_rate * bv for bv in self.book_value()[0: self.period]]

    def book_value(self):
        return [self.original_cost * pow(1 - self.depreciation_rate, m) for m in range(0, self.period + 1)]


class QuantityPerTotalEstimated(DepreciationMethod):

    def __init__(self, original_cost, salvage_value, quantities_per_period):
        self.quantities_per_period = quantities_per_period
        self.total_estimated = sum(self.quantities_per_period)
        period = len(self.quantities_per_period)
        super().__init__(original_cost, salvage_value, period)

    def depreciation(self):
        return [(self.original_cost - self.salvage_value) * quantity / self.total_estimated for quantity in self.quantities_per_period]

    def book_value(self):
        return [self.original_cost - sum(self.depreciation()[0: year]) for year in range(0, self.period + 1)]


class UnitOfProduction(QuantityPerTotalEstimated):
    pass


class OperationTime(QuantityPerTotalEstimated):
    pass


if __name__ == '__main__':

    original_cost = float(argv[argv.index('--oc') + 1])
    salvage_value = float(argv[argv.index('--sv') + 1])
    period = int(argv[argv.index('-n') + 1])
    interest_rate = float(argv[argv.index('-i') + 1])

    if 'soyd' in argv:
        method = SumOfTheYearsDigits(original_cost, salvage_value, period)
        method_name = 'Sum Of The Years Digits'

    elif 'sf' in argv:
        method = SinkingFund(original_cost, salvage_value, period, interest_rate)
        method_name = 'Sinking Fund'

    elif 'db' in argv:
        depreciation_rate = float(argv[argv.index('-d') + 1]) if '-d' in argv else 1 - pow(salvage_value / original_cost, 1 / period)
        method = DecliningBalance(original_cost, salvage_value, period, depreciation_rate)
        method_name = 'Declining Balance'

    elif 'up' in argv:
        produced_unit = eval(argv[argv.index('--um') + 1])
        method = UnitOfProduction(original_cost, salvage_value, produced_unit)
        method_name = 'Unit of Production'

    elif 'ot' in argv:
        operated_time = eval(argv[argv.index('--qm') + 1])
        method = OperationTime(original_cost, salvage_value, operated_time)
        method_name = 'Operation Time'

    else:
        method = StraightLine(original_cost, salvage_value, period)
        method_name = 'Straight Line'

    print('Economics Depreciation Calculator', method_name, sep=' - ')
    print('Year', 'Depreciation', 'Book Value', sep='\t\t')

    for index in range(period):
        print(index + 1, round(method.depreciation()[index], 2), round(method.book_value()[index + 1], 2), sep='\t\t')

    print('Original Cost:', original_cost)
    print('Salvage value:', salvage_value)
    print('No. periods:', period)
    print('Interest rate:', f'{interest_rate * 100}%')
    print('PW (depreciation):', round(method.depreciation_present_worth(interest_rate), 2))
    print('EUA (depreciation):', round(method.depreciation_equivalent_uniform_annual(interest_rate), 2))

