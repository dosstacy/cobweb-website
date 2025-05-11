params = {
    "cobweb": {
        "name": "Cobweb model",
        "description": """
        <strong>Demand shift</strong>: This constant determines the position of the demand curve. Higher values mean that consumers are willing to pay more at each quantity. Moves the demand curve up or down.<br><br>
        <strong>Demand slope</strong>: This value determines how strongly the quantity demanded changes when the price changes. A more negative value (e.g. -10) means that even a small increase in price will cause a significant decrease in demand.<br><br>
        <strong>Supply shift</strong>: This constant determines the position of the supply curve. Higher values mean that producers offer larger quantities at each price. Shifts the supply curve vertically.<br><br>
        <strong>Supply slope</strong>: It shows how responsive the quantity supplied is to price changes. A higher value indicates that producers quickly increase supply as prices rise.<br><br>
        <strong>Iterations</strong>: This represents how many periods the model should simulate. It should be a positive integer (e.g., 20).<br><br>
        <strong>Initial price</strong>: The starting market price from which the simulation begins. It should be a positive number.<br><br>
        <strong>Note:</strong> Demand slope must be negative, and supply slope must be positive for the model to behave realistically.
        """
    },
    "normal_price": {
        "name": "Normal price",
        "description": """
        <strong>Demand shift</strong>: This constant determines the position of the demand curve. Higher values mean that consumers are willing to pay more at each quantity. Moves the demand curve up or down.<br><br>
        <strong>Demand slope</strong>: This value determines how strongly the quantity demanded changes when the price changes. A more negative value (e.g. -10) means that even a small increase in price will cause a significant decrease in demand.<br><br>
        <strong>Supply shift</strong>: This constant determines the position of the supply curve. Higher values mean that producers offer larger quantities at each price. Shifts the supply curve vertically.<br><br>
        <strong>Supply slope</strong>: It shows how responsive the quantity supplied is to price changes. A higher value indicates that producers quickly increase supply as prices rise.<br><br>
        <strong>Factor</strong>: A multiplicative coefficient that scales supply changes over time. It should be a positive number.<br><br>
        <strong>Periods</strong>: Number of iterations or time steps the model should simulate.<br><br>
        <strong>Note:</strong> Demand slope must be negative, and supply slope must be positive for the model to behave realistically.<br><br>
        """
    },

    "adapt_exp": {
        "name": "Adaptive expectations",
        "description": """
        <strong>Demand shift</strong>: This constant determines the position of the demand curve. Higher values mean that consumers are willing to pay more at each quantity. Moves the demand curve up or down.<br><br>
        <strong>Demand slope</strong>: This value determines how strongly the quantity demanded changes when the price changes. A more negative value (e.g. -10) means that even a small increase in price will cause a significant decrease in demand.<br><br>
        <strong>Supply shift</strong>: This constant determines the position of the supply curve. Higher values mean that producers offer larger quantities at each price. Shifts the supply curve vertically.<br><br>
        <strong>Supply slope</strong>: It shows how responsive the quantity supplied is to price changes. A higher value indicates that producers quickly increase supply as prices rise.<br><br>
        <strong>Adaptation coefficient</strong>: Controls how fast expectations adjust. Should be between 0 and 1.<br><br>
        <strong>Periods</strong>: Number of steps to simulate.<br><br>
        """
    },

    "demand_supply": {
        "name": "Demand and supply",
        "description": """
        <strong>Demand shift</strong>: This constant determines the position of the demand curve. Higher values mean that consumers are willing to pay more at each quantity. Moves the demand curve up or down.<br><br>
        <strong>Demand slope</strong>: This value determines how strongly the quantity demanded changes when the price changes. A more negative value (e.g. -10) means that even a small increase in price will cause a significant decrease in demand.<br><br>
        <strong>Supply shift</strong>: This constant determines the position of the supply curve. Higher values mean that producers offer larger quantities at each price. Shifts the supply curve vertically.<br><br>
        <strong>Supply slope</strong>: It shows how responsive the quantity supplied is to price changes. A higher value indicates that producers quickly increase supply as prices rise.<br><br>
        <strong>Start price</strong>: The starting market price from which the simulation begins. It should be a positive number.<br><br>
        <strong>End price</strong>: Final price range value for plotting.<br><br>
        <strong>Function</strong>: Type of demand or supply behavior. Options include linear, cosine (seasonal variation), exponential, and logarithmic. The last two are for educational purposes.<br><br>
        """
    },

    "diff_eq": {
        "key": "diff_eq",
        "name": "Difference equations calculator",
        "description": """
        <strong>Equation</strong>: Enter your own difference equation in this field. Please keep the following requirements:<br>- There must not be an x term on the right-hand side of the equation. <br>- The equation can be at most second order, i.e. it can contain terms such as x(n+2).<br>- Terms with the same index, such as x(n+1) or x(n), must not be repeated in the equation.<br><br><i>Example of correct entry:</i> x(n+1) + 2*x(n) = 2*n.<br><i>Note:</i> The calculator currently supports solving equations of at most second order and may not be able to solve complex or non-standard equations.<br><br>
        <strong>Initial condition p₀</strong>: This is the first known value of the sequence.<br><br>
        <strong>Initial condition p₁</strong>: This is the second known value and is needed for second-order and higher equations.<br><br>
    """
    }
}

params_sk = {
    "cobweb": {
        "name": "Pavučinový model",
        "description": """
        <strong>Posun dopytu</strong>: Táto konštanta určuje polohu krivky dopytu. Vyššie hodnoty znamenajú, že spotrebitelia sú ochotní zaplatiť viac pri každom množstve. Posúva krivku dopytu nahor alebo nadol.<br><br>
        <strong>Sklon dopytu</strong>: Táto hodnota určuje, ako silne sa mení množstvo dopytu pri zmene ceny. Zápornejšia hodnota (napr. -10) znamená, že aj malé zvýšenie ceny spôsobí výrazný pokles dopytu.<br><br>
        <strong>Posun ponuky</strong>: Táto konštanta určuje polohu krivky ponuky. Vyššie hodnoty znamenajú, že výrobcovia ponúkajú väčšie množstvo pri každej cene. Vertikálne posúva krivku ponuky.<br><br>
        <strong>Sklon ponuky</strong>: Vyjadruje, ako rýchlo sa zvyšuje ponuka pri rastúcich cenách. Vyššie číslo znamená rýchlejšiu reakciu výrobcov.<br><br>
        <strong>Iterácie</strong>: Označuje počet období, ktoré sa majú v simulácii zobraziť. Musí to byť celé kladné číslo (napr. 20).<br><br>
        <strong>Počiatočná cena</strong>: Je to cena, od ktorej simulácia začína. Mala by byť kladná.<br><br>
        <strong>Poznámka:</strong> Sklon dopytu by mal byť záporný a sklon ponuky kladný, aby bol model realistický.
        """
    },
    "normal_price": {
        "name": "Model očakávanej ceny s použitím normálnej ceny",
        "description": """
        <strong>Posun dopytu</strong>: Táto konštanta určuje polohu krivky dopytu. Vyššie hodnoty znamenajú, že spotrebitelia sú ochotní zaplatiť viac pri každom množstve. Posúva krivku dopytu nahor alebo nadol.<br><br>
        <strong>Sklon dopytu</strong>: Táto hodnota určuje, ako silne sa mení množstvo dopytu pri zmene ceny. Zápornejšia hodnota (napr. -10) znamená, že aj malé zvýšenie ceny spôsobí výrazný pokles dopytu.<br><br>
        <strong>Posun ponuky</strong>: Táto konštanta určuje polohu krivky ponuky. Vyššie hodnoty znamenajú, že výrobcovia ponúkajú väčšie množstvo pri každej cene. Vertikálne posúva krivku ponuky.<br><br>
        <strong>Sklon ponuky</strong>: Vyjadruje, ako rýchlo sa zvyšuje ponuka pri rastúcich cenách. Vyššie číslo znamená rýchlejšiu reakciu výrobcov.<br><br>
        <strong>Faktor</strong>: Násobiteľ, ktorý upravuje zmeny ponuky v čase. Má byť kladný.<br><br>
        <strong>Počet období</strong>: Počet simulovaných časových krokov.<br><br>
        <strong>Poznámka:</strong> Sklon dopytu musí byť záporný a sklon ponuky kladný pre realistické správanie modelu.<br><br>
        """
    },

    "adapt_exp": {
        "name": "Adaptívne očakávania",
        "description": """
        <strong>Posun dopytu</strong>: Táto konštanta určuje polohu krivky dopytu. Vyššie hodnoty znamenajú, že spotrebitelia sú ochotní zaplatiť viac pri každom množstve. Posúva krivku dopytu nahor alebo nadol.<br><br>
        <strong>Sklon dopytu</strong>: Táto hodnota určuje, ako silne sa mení množstvo dopytu pri zmene ceny. Zápornejšia hodnota (napr. -10) znamená, že aj malé zvýšenie ceny spôsobí výrazný pokles dopytu.<br><br>
        <strong>Posun ponuky</strong>: Táto konštanta určuje polohu krivky ponuky. Vyššie hodnoty znamenajú, že výrobcovia ponúkajú väčšie množstvo pri každej cene. Vertikálne posúva krivku ponuky.<br><br>
        <strong>Sklon ponuky</strong>: Vyjadruje, ako rýchlo sa zvyšuje ponuka pri rastúcich cenách. Vyššie číslo znamená rýchlejšiu reakciu výrobcov.<br><br>
        <strong>Koeficient adaptácie</strong>: Určuje rýchlosť prispôsobovania očakávaní. Má byť medzi 0 a 1.<br><br>
        <strong>Počet období</strong>: Počet simulovaných krokov.<br><br>
        """
    },

    "demand_supply": {
        "name": "Ponuka a dopyt",
        "description": """
        <strong>Posun dopytu</strong>: Táto konštanta určuje polohu krivky dopytu. Vyššie hodnoty znamenajú, že spotrebitelia sú ochotní zaplatiť viac pri každom množstve. Posúva krivku dopytu nahor alebo nadol.<br><br>
        <strong>Sklon dopytu</strong>: Táto hodnota určuje, ako silne sa mení množstvo dopytu pri zmene ceny. Zápornejšia hodnota (napr. -10) znamená, že aj malé zvýšenie ceny spôsobí výrazný pokles dopytu.<br><br>
        <strong>Posun ponuky</strong>: Táto konštanta určuje polohu krivky ponuky. Vyššie hodnoty znamenajú, že výrobcovia ponúkajú väčšie množstvo pri každej cene. Vertikálne posúva krivku ponuky.<br><br>
        <strong>Sklon ponuky</strong>: Vyjadruje, ako rýchlo sa zvyšuje ponuka pri rastúcich cenách. Vyššie číslo znamená rýchlejšiu reakciu výrobcov.<br><br>
        <strong>Začiatočná cena</strong>: Počiatočná trhová cena.<br><br>
        <strong>Koncová cena</strong>: Konečná cena, do ktorej sa vykresľuje graf.<br><br>
        <strong>Funkcia</strong>: Typ správania dopytu alebo ponuky. Používateľ môže zvoliť lineárnu, kosínusovú (sezónne kolísanie), exponenciálnu alebo logaritmickú funkciu. Posledné dva slúžia len na výučbové účely.<br><br>
        """
    },

    "diff_eq": {
        "key": "diff_eq",
        "name": "Kalkulačka diferenčných rovníc",
        "description": """
        <strong>Rovnica</strong>: Do tohto poľa zadajte vlastnú diferenčnú rovnicu. Prosíme, aby ste dodržiavali nasledujúce podmienky:<br> - Na pravej strane rovnice sa nesmie nachádzať výraz <code>x</code>.<br> - Rovnica môže byť najviac druhého rádu, t. j. môže obsahovať členy ako <code>x(n+2)</code>.<br> - V rovnici sa nesmú opakovať výrazy s rovnakým indexom, ako napríklad <code>x(n+1)</code> alebo <code>x(n)</code>. <br><br><i>Príklad správneho zápisu:</i> <code>x(n+1) + 2*x(n) = 2*n</code> <br><em>Upozornenie:</em> Kalkulačka aktuálne podporuje riešenie rovníc maximálne druhého rádu a nemusí byť schopná vyriešiť zložité alebo neštandardné rovnice.<br><br>
        <strong>Počiatočná podmienka p₀</strong>: Prvá známa hodnota postupnosti. Je potrebná pri riešení rovníc prvého a vyššieho rádu.<br><br>
        <strong>Počiatočná podmienka p₁</strong>: Druhá známa hodnota, potrebná pri riešení rovníc druhého a vyššieho rádu.<br><br>
        """
    }

}