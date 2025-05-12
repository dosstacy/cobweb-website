intros = {
    "cobweb": {
        "key": "cobweb",
        "name": "Cobweb Model",
        "intro": "This economic model describes how changes in the price and quantity of a good on the market can lead to fluctuations instead of equilibrium. It is based on the assumption that producers make decisions about future output based on current prices, but do not take into account that prices may change. If supply and demand react with a delay, the market can fluctuate, forming a “spider's web” trajectory. The price is determined using the formula: \\( p(n) = (p_0 - p_e) \\cdot \\left( \\frac{s_2}{d_2} \\right)^n + p_e \\) for a regular cobweb model, where \\(p_0\\) - is start price, \\(p_e\\) - equilibrium price, \\(s_2\\) - supply slope, \\(d_2\\) - demand slope and \\(n\\) is periods.  <br> The formula \\( x_{n+1} = r x_n (1 - x_n) \\) is used for logistic map implementation of cobweb model.",
    },
    "normal_price": {
        "key": "normal_price",
        "name": "Adaptive expectations",
        "intro": "The normal price model in economics describes how the price of a product adjusts to market supply and demand. It is based on the assumption that producers increase or decrease output in response to the difference between the current market price and the so-called normal price. The normal price is the equilibrium price at which the market is in equilibrium. If the market price is higher than the normal price, supply increases and the price falls over time. Conversely, if the price is lower than normal, producers will restrict supply, leading to an increase in price. This model uses the formula \\( p(n) = C \\left( \\frac{s_2(1-c)}{d_2}\\right)^n + p_e \\), where \\(C\\) - is constant, \\(c\\) - is adjustment factor, \\(s_2\\) - supply slope, \\(d_2\\) - demand slope, \\(n\\) - is periods and \\(p_e\\) - equilibrium price."
    },
    "demand_supply": {
        "key": "demand_supply",
        "name": "Demand and supply",
        "intro": "Demand and supply are fundamental concepts in economics. Demand refers to the quantity of a good or service that consumers are willing to buy at different prices, while supply represents how much producers are willing to offer. The interaction of demand and supply determines the market price. When demand increases and supply remains constant, prices usually rise. We can find supply and demand using these expressions \\(d(n) = d_1 + d_2p(n), s(n) = s_1 + s_2p(n)\\), where \\(s_1\\) - supply shift, \\(d_1\\) - demand shift, \\(s_2\\) - supply slope, \\(d_2\\) - demand slope.",
    },
    "adapt_exp": {
        "key": "adapt_exp",
        "name": "Adaptive expectations",
        "intro": "This model is used in economics to explain how people predict future values of economic indicators, such as price levels. It assumes that expectations about future prices are formed on the basis of previous data with gradual adjustments. If prices grow faster than expected, people begin to expect even higher growth in the future. This approach is used, for example, to analyze inflation. Here, the solution is found using the following expression \\( p(n) = C\\left[ \\left( \\frac{s_2}{d_2} - 1\\right) \\beta + 1\\right]^n.\\), where \\(C\\) - is constant, \\(\\beta\\) - is adaptation coefficient, \\(s_2\\) - supply slope, \\(d_2\\) - demand slope, \\(n\\) - is periods and \\(p_e\\) - equilibrium price.",
    },
    "diff_eq": {
        "key": "diff_eq",
        "name": "Difference equations",
        "intro": "These are mathematical equations that describe how a quantity changes at discrete points in time. They are analogous to differential equations, but are used when time is not considered continuous, but as a set of separate points (for example, years or months). Such equations are widely used in economics, physics, and computer modeling to predict the development of systems. \n\n They are useful when we want to track how something is changing step by step - for example, how price, population or stocks are evolving. We can imagine that each step represents one year or one decision. Based on what happened before, we can calculate what will happen next. \n\n These equations help us better understand the behaviour of systems over time. In economics, for example, we can track how supply and demand change. In biology, we can track the growth of animal populations. In engineering, they help us predict how different devices will work. \n\n <b> An example of an equation: </b> <i>2x(n+2) + 3x(n+1) + x(n) = 2.</i>",
    }
}

intros_sk = {
    "cobweb": {
        "key": "cobweb",
        "name": "Pavučinový model",
        "intro": "Tento ekonomický model popisuje, ako zmeny ceny a množstva tovaru na trhu môžu viesť k výkyvom namiesto rovnováhy. Vychádza z predpokladu, že výrobcovia sa rozhodujú o budúcej produkcii na základe súčasných cien, ale neberú do úvahy, že ceny sa môžu zmeniť. Ak ponuka a dopyt reagujú s oneskorením, trh môže kolísať a vytvárať „pavučinovú“ trajektóriu. Cena sa určuje podľa vzorca: \\( p(n) = (p_0 - p_e) \\cdot \\left( \\frac{s_2}{d_2} \\right)^n + p_e \\) pre obyčajný pavučinový model, kde \\(p_0\\) - je počiatočná cena, \\(p_e\\) - rovnovážna cena, \\(s_2\\) - sklon ponuky, \\(d_2\\) - sklon dopytu a \\(n\\) sú obdobia.  <br> Vzorec \\( x_{n+1} = r x_n (1 - x_n) \\) sa používa na implementáciu logistickej mapy pavučinového modelu.",
    },
    "normal_price": {
        "key": "normal_price",
        "name": "Normálna cena",
        "intro": "Model normálnej ceny v ekonómii opisuje, ako sa cena výrobku prispôsobuje dopytu a ponuke na trhu. Vychádza z predpokladu, že výrobcovia zvyšujú alebo znižujú produkciu v reakcii na rozdiel medzi aktuálnou trhovou cenou a tzv. normálnou cenou. Normálna cena je rovnovážna cena, pri ktorej je trh v rovnováhe. Ak je trhová cena vyššia ako normálna, ponuka sa zvyšuje a cena časom klesá. Naopak, ak je cena nižšia ako normálna, výrobcovia obmedzia ponuku, čo vedie k rastu ceny. Tento model používa vzorec \\( p(n) = C \\left( \\frac{s_2(1-c)}{d_2}\\right)^n + p_e \\), kde \\(C\\) - je konštanta, \\(c\\) - je faktor úpravy, \\(s_2\\) - sklon ponuky, \\(d_2\\) - sklon dopytu, \\(n\\) - je obdobie a \\(p_e\\) - rovnovážna cena.",
    },
    "demand_supply": {
        "key": "demand_supply",
        "name": "Dopyt a ponuka",
        "intro": "Dopyt a ponuka sú základné pojmy v ekonómii. Dopyt označuje množstvo tovarov alebo služieb, ktoré sú spotrebitelia ochotní kúpiť pri rôznych cenách, zatiaľ čo ponuka vyjadruje množstvo, ktoré sú výrobcovia ochotní poskytnúť. Ich vzájomná interakcia určuje trhovú cenu. Keď sa dopyt zvyšuje a ponuka zostáva rovnaká, ceny zvyčajne rastú. Ponuku a dopyt môžeme zistiť pomocou týchto výrazov \\(d(n) = d_1 + d_2p(n), s(n) = s_1 + s_2p(n)\\), kde \\(s_1\\) - posun ponuky, \\(d_1\\) - posun dopytu, \\(s_2\) - sklon ponuky, \\(d_2\) - sklon dopytu.",
    },
    "adapt_exp": {
        "key": "adapt_exp",
        "name": "Adaptívne očakávania",
        "intro": "Tento model sa používa v ekonómii na vysvetlenie toho, ako ľudia predpovedajú budúce hodnoty ekonomických údajov, ako je napríklad cena. Predpokladá, že očakávania o budúcich cenách sa vytvárajú na základe predchádzajúcich údajov s postupnými úpravami. Ak ceny rastú rýchlejšie, ako sa očakávalo, ľudia začnú v budúcnosti očakávať ešte vyšší rast. Tento prístup sa používa napríklad pri analýze inflácie. Tu sa riešenie nájde pomocou nasledujúceho výrazu \\( p(n) = C\\left[ \\left( \\frac{s_2}{d_2} - 1\\right) \\beta + 1\\right]^n \\), kde \\(C\\) - je konštanta, \\(\\beta\\) - je koeficient prispôsobenia, \\(s_2\\) - sklon ponuky, \\(d_2\\) - sklon dopytu, \\(n\\) - je obdobie a \\(p_e\\) - rovnovážna cena.",
    },
    "diff_eq": {
        "key": "diff_eq",
        "name": "Diferenčné rovnice",
        "intro": "Ide o matematické rovnice, ktoré opisujú, ako sa veličina mení v diskrétnych časových bodoch. Sú analogické diferenciálnym rovniciam, ale používajú sa vtedy, keď sa čas nepovažuje za spojitý, ale za súbor jednotlivých bodov (napríklad rokov alebo mesiacov). Takéto rovnice sa široko používajú v ekonómii, fyzike a počítačovom modelovaní na predpovedanie vývoja systémov. \n\n Sú užitočné, keď chceme sledovať, ako sa niečo mení krok po kroku – napríklad ako sa vyvíja cena, populácia alebo zásoby. Môžeme si predstaviť, že každý krok predstavuje jeden rok alebo jedno rozhodnutie. Na základe toho, čo sa stalo predtým, vieme vypočítať, čo sa stane ďalej. \n\n Tieto rovnice nám pomáhajú lepšie pochopiť správanie systémov v čase. Napríklad v ekonomike môžeme sledovať, ako sa mení ponuka a dopyt. V biológii môžeme sledovať rast populácie zvierat. V technike zas pomáhajú predvídať fungovanie rôznych zariadení. \n\n <b> Príklad rovnice: </b> <i>2x(n+2) + 3x(n+1) + x(n) = 2.</i>"
    }
}
