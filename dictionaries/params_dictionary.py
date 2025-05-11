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
    },

    "cobweb_func": {
        "name": "Cobweb model with function",
        "description": """
        <strong>Function</strong>: This defines the mathematical function used to model supply or demand. For example, it can be a logistic function such as <code>f(x) = cos(x). </code><br><br>
        <strong>Min value on X-axis</strong>: Specifies the minimum price value shown on the horizontal axis of the graph. It helps control the visible range of prices in the plot. <br><br>
        <strong>Max value on X-axis</strong>: Specifies the maximum price value on the horizontal axis. This sets the upper bound for the graph’s price range. <br><br>
        <strong>Min value on Y-axis</strong>: Defines the lowest quantity (demand or supply) displayed on the vertical axis. <br><br>
        <strong>Max value on Y-axis</strong>: Sets the maximum quantity shown on the vertical axis, affecting the visible scale of the demand and supply curves. <br><br>
        <strong>Seed</strong>: This is the initial price used as a starting point for the iteration process. It determines where the cobweb simulation begins. <br><br> 
        <strong>Iterations</strong>: Indicates the number of steps (time periods) to simulate in the cobweb model. More iterations allow you to observe long-term behavior (e.g., convergence, divergence, cycles).
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
    },

    "cobweb_func": {
        "name": "Pavučinový model s funkciou",
        "description": """
        <strong>Funkcia</strong>: Určuje matematickú funkciu, ktorou modelujeme dopyt alebo ponuku. Môže to byť napríklad logistická funkcia, ako napr. <code>f(x) = cos(x). </code><br><br>
        <strong>Minimálna hodnota na osi X</strong>: Určuje najnižšiu hodnotu ceny zobrazenú na vodorovnej osi grafu. Pomáha nastaviť rozsah cien na grafe. <br><br>
        <strong>Maximálna hodnota na osi X</strong>: Definuje najvyššiu hodnotu ceny na osi X. Slúži na obmedzenie cenového rozsahu zobrazeného na grafe. <br><br>
        <strong>Minimálna hodnota na osi Y</strong>: Označuje najmenšie množstvo (dopytu alebo ponuky), ktoré sa zobrazí na zvislej osi. Umožňuje priblíženie alebo oddialenie zobrazenia. <br><br>
        <strong>Maximálna hodnota na osi Y</strong>: Určuje najväčšie množstvo zobrazené na zvislej osi. Tým ovplyvňuje mierku a viditeľnosť kriviek dopytu a ponuky. <br><br>
        <strong>Počiatočná hodnota</strong>: Je to počiatočná cena, z ktorej sa začína simulácia. Určuje východiskový bod pre konštrukciu pavúčej dynamiky.<br><br>
        <strong>Iterácie</strong>: Udávajú počet krokov (časových období) v simulácii pavúčieho modelu. Viac iterácií umožňuje sledovať dlhodobé správanie (napr. konvergenciu, divergenciu, cykly).
        """
    }

}