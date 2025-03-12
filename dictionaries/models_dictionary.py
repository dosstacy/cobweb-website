models = {
    "cobweb": {"name": "Cobweb Model", "fields": ["Demand shift", "Demand slope", "Supply shift", "Supply slope", "Iterations", "Initial price"]},
    "cobweb_func": {"name": "Cobweb with function", "fields": ["Function", "Min value on X-axis", "Max value on X-axis", "Min value on Y-axis", "Max value on Y-axis", "Seed", "Iterations"]},
    "adapt_exp": {"name": "Adaptive expectations", "fields": ["Previous price", "Normal price", "Adjustment factor", "Periods"]},
    "demand_supply":{"name": "Supply and Demand", "fields": ["Demand shift", "Demand slope", "Supply shift", "Supply slope", "Start price", "End price"], "functions": ["linear", "cos", "exp", "ln"]},
}