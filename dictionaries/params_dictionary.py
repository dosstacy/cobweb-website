params = {
    "cobweb": {
        "name": "Cobweb model",
        "description": """
        <strong>Demand shift</strong>: This constant determines the position of the demand curve. Higher values shift the curve upward, meaning consumers are willing to pay more at each quantity.<br><br>
        <strong>Demand slope</strong>: This value defines how steep the demand curve is. A more negative value (e.g., -3) means that demand falls sharply when price increases.<br><br>
        <strong>Supply shift</strong>: Similar to the demand shift, this parameter moves the supply curve up or down.<br><br>
        <strong>Supply slope</strong>: It shows how responsive the quantity supplied is to price changes. A higher value indicates that producers quickly increase supply as prices rise.<br><br>
        <strong>Iterations</strong>: This represents how many periods the model should simulate. It should be a positive integer (e.g., 20).<br><br>
        <strong>Initial price</strong>: The starting market price from which the simulation begins. It should be a positive number.<br><br>
        <strong>Note:</strong> Demand slope must be negative, and supply slope must be positive for the model to behave realistically.
        """
    },
    "normal_price": {
        "name": "Normal price",
        "description": """
        <strong>Demand shift</strong>: This constant determines the position of the demand curve. Higher values shift the curve upward, meaning consumers are willing to pay more at each quantity.<br><br>
        <strong>Demand slope</strong>: This value defines how steep the demand curve is. A more negative value (e.g., -3) means that demand falls sharply when price increases.<br><br>
        <strong>Supply shift</strong>: Similar to the demand shift, this parameter moves the supply curve up or down.<br><br>
        <strong>Supply slope</strong>: It shows how responsive the quantity supplied is to price changes. A higher value indicates that producers quickly increase supply as prices rise.<br><br>
        <strong>Factor</strong>: A multiplicative coefficient that scales supply changes over time. It should be a positive number.<br><br>
        <strong>Periods</strong>: Number of iterations or time steps the model should simulate.<br><br>
        <strong>Note:</strong> Demand slope must be negative, and supply slope must be positive for the model to behave realistically.<br><br>
        """
    },

    "adapt_exp": {
        "name": "Adaptive expectations",
        "description": """
        <strong>Demand shift</strong>: Determines the base level of demand.<br><br>
        <strong>Demand slope</strong>: Defines how sensitive demand is to price. Should be negative.<br><br>
        <strong>Supply shift</strong>: Sets the baseline for supply.<br><br>
        <strong>Supply slope</strong>: Should be a positive number, representing the rate at which supply increases with price.<br><br>
        <strong>Adaptation coefficient</strong>: Controls how fast expectations adjust. Should be between 0 and 1.<br><br>
        <strong>Periods</strong>: Number of steps to simulate.<br><br>
        """
    },

    "demand_supply": {
        "name": "Demand and supply",
        "description": """
        <strong>Demand shift</strong>: Moves the demand curve up or down.<br><br>
        <strong>Demand slope</strong>: Negative value indicating sensitivity of demand to price.<br><br>
        <strong>Supply shift</strong>: Shifts the supply curve vertically.<br><br>
        <strong>Supply slope</strong>: Positive number that defines how supply reacts to price.<br><br>
        <strong>Start price</strong>: Initial market price.<br><br>
        <strong>End price</strong>: Final price range value for plotting.<br><br>
        <strong>Function</strong>: Type of demand or supply behavior. Options include linear, cosine (seasonal variation), exponential, and logarithmic. The last two are for educational purposes.<br><br>
        """
    },

    "diff_eq": {
        "key": "diff_eq",
        "name": "Difference equations calculator",
        "description": """
        <strong>Equation</strong>: Enter the nth order difference equation <em>(the calculator can solve the maximum second order equation!)</em>. You may use basic operations (+, -, , /), integer constants, and parentheses. For example: <code>x(n) = 0.5x(n+1) + 2</code>.<br><br>
        <strong>Initial condition p₀</strong>: This is the first known value of the sequence.<br><br>
        <strong>Initial condition p₁</strong>: This is the second known value and is needed for second-order and higher equations.<br><br>
    """
    }
}

params_sk = {
    "cobweb": {
        "name": "Pavučinový model",
        "description": """
        <strong>Posun dopytu</strong>: Táto konštanta určuje polohu krivky dopytu. Vyššie hodnoty posúvajú krivku smerom nahor, čo znamená, že spotrebitelia sú ochotní zaplatiť viac pri každom množstve.<br><br>
        <strong>Sklon dopytu</strong>: Táto hodnota určuje, ako strmá je krivka dopytu. Zápornejšia hodnota (napr. -3) znamená, že dopyt pri zvýšení ceny prudko klesá.<br><br>
        <strong>Posun ponuky</strong>: Podobne ako pri posune dopytu, aj tento parameter posúva krivku ponuky nahor alebo nadol.<br><br>
        <strong>Sklon ponuky</strong>: Vyjadruje, ako rýchlo sa zvyšuje ponuka pri rastúcich cenách. Vyššie číslo znamená rýchlejšiu reakciu výrobcov.<br><br>
        <strong>Iterácie</strong>: Označuje počet období, ktoré sa majú v simulácii zobraziť. Musí to byť celé kladné číslo (napr. 20).<br><br>
        <strong>Počiatočná cena</strong>: Je to cena, od ktorej simulácia začína. Mala by byť kladná.<br><br>
        <strong>Poznámka:</strong> Sklon dopytu by mal byť záporný a sklon ponuky kladný, aby bol model realistický.
        """
    },
    "normal_price": {
        "name": "Model očakávanej ceny s použitím normálnej ceny",
        "description": """
        <strong>Posun dopytu</strong>: Táto konštanta určuje polohu krivky dopytu. Vyššie hodnoty posúvajú krivku nahor – spotrebitelia sú ochotní platiť viac pri každom množstve.<br><br>
        <strong>Sklon dopytu</strong>: Určuje, ako strmo klesá dopyt pri zvýšení ceny. Čím zápornější je hodnota (napr. -3), tým prudšie dopyt klesá.<br><br>
        <strong>Posun ponuky</strong>: Podobne ako pri dopyte, táto hodnota posúva krivku ponuky hore alebo dolu.<br><br>
        <strong>Sklon ponuky</strong>: Ukazuje, ako pružne reaguje ponuka na zmeny ceny. Vyššia hodnota znamená rýchlejšie zvyšovanie ponuky pri raste cien.<br><br>
        <strong>Faktor</strong>: Násobiteľ, ktorý upravuje zmeny ponuky v čase. Má byť kladný.<br><br>
        <strong>Počet období</strong>: Počet simulovaných časových krokov.<br><br>
        <strong>Poznámka:</strong> Sklon dopytu musí byť záporný a sklon ponuky kladný pre realistické správanie modelu.<br><br>
        """
    },

    "adapt_exp": {
        "name": "Adaptívne očakávania",
        "description": """
        <strong>Posun dopytu</strong>: Určuje základnú úroveň dopytu.<br><br>
        <strong>Sklon dopytu</strong>: Ukazuje citlivosť dopytu na cenu. Mal by byť záporný.<br><br>
        <strong>Posun ponuky</strong>: Nastavuje základnú hodnotu ponuky.<br><br>
        <strong>Sklon ponuky</strong>: Mal by byť kladný a vyjadruje rýchlosť rastu ponuky pri zvyšovaní ceny.<br><br>
        <strong>Koeficient adaptácie</strong>: Určuje rýchlosť prispôsobovania očakávaní. Má byť medzi 0 a 1.<br><br>
        <strong>Počet období</strong>: Počet simulovaných krokov.<br><br>
        """
    },

    "demand_supply": {
        "name": "Ponuka a dopyt",
        "description": """
        <strong>Posun dopytu</strong>: Posúva krivku dopytu nahor alebo nadol.<br><br>
        <strong>Sklon dopytu</strong>: Záporná hodnota, ktorá vyjadruje, ako citlivo dopyt reaguje na zmenu ceny.<br><br>
        <strong>Posun ponuky</strong>: Vertikálne posúva krivku ponuky.<br><br>
        <strong>Sklon ponuky</strong>: Kladná hodnota ukazujúca reakciu ponuky na cenu.<br><br>
        <strong>Začiatočná cena</strong>: Počiatočná trhová cena.<br><br>
        <strong>Koncová cena</strong>: Konečná cena, do ktorej sa vykresľuje graf.<br><br>
        <strong>Funkcia</strong>: Typ správania dopytu alebo ponuky. Používateľ môže zvoliť lineárnu, kosínusovú (sezónne kolísanie), exponenciálnu alebo logaritmickú funkciu. Posledné dva slúžia len na výučbové účely.<br><br>
        """
    },

    "diff_eq": {
        "key": "diff_eq",
        "name": "Kalkulačka diferenčných rovníc",
        "description": """
        <strong>Rovnica</strong>: Zadajte diferenčnú rovnicu n-tého rádu <em>(kalkulačka dokáže vyriešiť rovnicu maximálneho druhého radu!)</em>. Môžete používať základné operácie (+, -, , /), celé konštanty a zátvorky. Napríklad: <code>x(n) = 0.5x(n+1) + 2</code>.<br><br>
        <strong>Počiatočná podmienka p₀</strong>: Prvá známa hodnota postupnosti. Je potrebná pri riešení rovníc prvého a vyššieho rádu.<br><br>
        <strong>Počiatočná podmienka p₁</strong>: Druhá známa hodnota, potrebná pri riešení rovníc druhého a vyššieho rádu.<br><br>
        """
    }

}
