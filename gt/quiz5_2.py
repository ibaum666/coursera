import sympy as sp
p = sp.Symbol('p')

payoffs = [3 if i % 2 else 1 for i in range(1, 10)]
weighted_payoffs = [pay * p ** i for i, pay in enumerate(payoffs)]
print sp.expand(sum(weighted_payoffs))


grim_payoff = 5. / (1. - p)
defect_payoff = 6. + 2. / (1. - p)
print 'Q3, estimated probability threshold for grim'
print sp.solve(grim_payoff - defect_payoff, p)


grim_payoff = 5. / (1. - p)
defect_payoff = 10 + 1. / (1. - p)
print 'Q7, estimated probability threshold for grim'
print sp.solve(grim_payoff - defect_payoff, p)

print 'Q8'
payoffs = [4 for i in range(10)]
print sp.expand(sum([4 * p ** i for i in range(10)]))
print sp.expand(sum([5 * p ** i if not i % 2 else 1 * p ** i for i in range(10)]))
