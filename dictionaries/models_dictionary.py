models = {
    "cobweb": {"name": "Cobweb Model", "fields": ["Demand shift", "Demand slope", "Supply shift", "Supply slope", "Iterations", "Initial price"]},
    "cobweb_func": {"name": "Cobweb with function", "fields": ["Function", "Min value on X-axis", "Max value on X-axis", "Min value on Y-axis", "Max value on Y-axis", "Seed", "Iterations"]},
    "demand_supply":{"name": "Supply and Demand", "fields": ["Demand shift", "Demand slope", "Supply shift", "Supply slope", "Start price", "End price"], "functions": ["linear", "cos", "exp", "ln"]},
    "adapt_exp": {"name": "Adaptive expectations", "fields": ["Demand shift", "Demand slope", "Supply shift", "Supply slope", "Adaptation coefficient", "Periods","Constant"]},
    "normal_price": {"name": "Expected price", "fields": ["Demand shift", "Demand slope", "Supply shift", "Supply slope", "Adjustment factor", "Periods","Constant"]},
}

models_sk = {
    "cobweb": {"name": "Pavučinový model", "fields": ["Posun dopytu", "Sklon dopytu", "Posun ponuky", "Sklon ponuky", "Iterácie", "Počiatočná cena"]},
    "cobweb_func": {"name": "Pavučinový model (funkcia)", "fields": ["Funkcia", "Minimálna hodnota na osi X", "Maximálna hodnota na osi X", "Minimálna hodnota na osi Y", "Maximálna hodnota na osi Y", "Počiatočná hodnota", "Iterácie"]},
    "demand_supply":{"name": "Ponuka a dopyt", "fields": ["Posun dopytu", "Sklon dopytu", "Posun ponuky", "Sklon ponuky", "Počiatočná cena", "Konečná cena"], "functions": ["lineárna", "cos", "exp", "ln"]},
    "adapt_exp": {"name": "Adaptívne očakávania", "fields": ["Posun dopytu","Sklon dopytu", "Posun ponuky", "Sklon ponuky", "Adaptačný koeficient", "Obdobie", "Konštanta"]},
    "normal_price": {"name": "Očakávaná cena", "fields": ["Posun dopytu","Sklon dopytu", "Posun ponuky", "Sklon ponuky", "Faktor úpravy", "Obdobie", "Konštanta"]},
}