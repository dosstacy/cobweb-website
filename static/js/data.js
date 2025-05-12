let currentLang = "";

function getCurrentLanguage() {
    return fetch('/get-lang')
        .then(response => response.json())
        .then(data => data.lang);
}

document.querySelectorAll('.table-button').forEach(button => {
    button.addEventListener('click', function () {
        if (button.id !== 'remove' && button.id !== 'removeAll') {
            let inputField;
            if (document.querySelector('#function')) {
                inputField = document.querySelector('#function');
            } else if (document.querySelector('#funkcia')) {
                inputField = document.querySelector('#funkcia');
            }else if (document.querySelector('#equation-input')) {
                    inputField = document.querySelector('#equation-input');
                }
                let cursorPos = inputField.selectionStart;
                let textBefore = inputField.value.substring(0, cursorPos);
                let textAfter = inputField.value.substring(cursorPos);
                inputField.value = textBefore + this.innerText + textAfter;
                inputField.focus();
                inputField.selectionStart = inputField.selectionEnd = cursorPos + this.innerText.length;
            }
    });
});

async function initTable() {
    currentLang = await getCurrentLanguage();
    const toggleButton = document.getElementById('toggle-view');
    const basicSymbols = document.getElementById('basic-symbols');
    const functionSymbols = document.getElementById('function-symbols');

    if (toggleButton && basicSymbols && functionSymbols) {
        toggleButton.addEventListener('click', function () {
            if (basicSymbols.style.display !== 'none') {
                basicSymbols.style.display = 'none';
                functionSymbols.style.display = '';
                if (currentLang === "en") {
                    toggleButton.textContent = 'Show numbers';
                } else {
                    toggleButton.textContent = 'Zobraziť čísla';
                }
            } else {
                basicSymbols.style.display = '';
                functionSymbols.style.display = 'none';
                if (currentLang === "en") {
                    toggleButton.textContent = 'Show functions';
                } else {
                    toggleButton.textContent = 'Zobraziť funkcie';
                }
            }
        });
    }

    window.removeAllFromField = removeAllFromField;
    window.removeLastSymbol = removeLastSymbol;
}
document.addEventListener("DOMContentLoaded", initTable);

async function initModelPage() {
    currentLang = await getCurrentLanguage();
    console.log("Lang in initModelPage:", currentLang);

    const form = document.getElementById("dataForm");

    if (form) {
        form.addEventListener("submit", function (event) {
            event.preventDefault();

            let formData = {};
            let inputs = document.querySelectorAll("input[class='data-input']");
            let isValid = true;

            for (let input of inputs) {
                let fieldsName = input.name;
                let fieldValue = input.value;
                hideError(input);

                if (fieldValue === "") {
                    console.log("Field value is empty");
                    if (currentLang === "en") {
                        showError(input, "This field is required!");
                    } else {
                        showError(input, "Povinné pole!!");
                    }
                    isValid = false;
                    continue;
                }

                if ((fieldsName.includes("price")) || (fieldsName.includes("cena"))) {
                    if (parseFloat(fieldValue) <= 0) {
                        if (currentLang === "en") {
                            showError(input, "Value must be positive!");
                        } else {
                            showError(input, "Hodnota musí byť kladná!");
                        }
                        isValid = false;
                        continue;
                    }
                }

                if (fieldsName === "previous actual price" || fieldsName === "predchádzajúca skutočná cena") {
                    fieldValue = fieldValue.replace(/,$/, '');
                    const values = fieldValue.split(',').map(v => v.trim());
                    const regex = /^[0-9,.+\-]*$/;

                    for (let numberStr of values) {
                        if (regex.test(numberStr)) {
                            if (parseFloat(numberStr) <= 0) {
                                if (currentLang === "en") {
                                    showError(input, "Value must be positive!");
                                } else {
                                    showError(input, "Hodnota musí byť kladná!");
                                }
                                isValid = false;
                            }
                        } else {
                            if (currentLang === "en") {
                                showError(input, "Field must contains numbers!");
                            } else {
                                showError(input, "Pole musí obsahovať čísla!");
                            }
                            isValid = false;
                        }
                    }
                }

                if ((fieldsName === "iterations" || fieldsName === "periods") ||
                    (fieldsName === "iterácie" || fieldsName === "obdobie")) {
                    if (parseFloat(fieldValue) % 1 !== 0) {
                        if (currentLang === "en") {
                            showError(input, "Value must be a whole number!");
                        } else {
                            showError(input, "Hodnota musí byť celé číslo!");
                        }
                        isValid = false;
                        continue;
                    }
                }

                if ((fieldsName === "adjustment factor" || fieldsName === "adaptation coefficient") ||
                    (fieldsName === "faktor úpravy" || fieldsName === "adaptačný koeficient")) {
                    if (parseFloat(fieldValue) < 0 || parseFloat(fieldValue) > 1) {
                        if (currentLang === "en") {
                            showError(input, "Value must be between 0 and 1!");
                        } else {
                            showError(input, "Hodnota musí byť od 0 do 1!");
                        }
                        isValid = false;
                        continue;
                    }
                }

                formData[fieldsName] = isNaN(fieldValue) || fieldValue.trim() === "" ? fieldValue : parseFloat(fieldValue);
            }

            const functionField = document.querySelector('#function');
            if (functionField && !validateScopes(functionField.value)) {
                if (currentLang === "en") {
                    showError(functionField, "Bracket mismatch!");
                } else {
                    showError(functionField, "Nesúlad zátvoriek!");
                }
                isValid = false;
            }


            if (isValid) {
                let functionInput = document.querySelector("select.func-selection");
                if (functionInput) {
                    formData[functionInput.name] = functionInput.value;
                }


                const modelName = document.getElementById('model-container').dataset.model;
                console.log(modelName);

                fetch("/model/" + modelName, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(formData)
                })
                    .then(response => response.json())
                    .then(data => {
                        console.log("Success:", data);

                        if (data.graph_json) {
                            const graph = JSON.parse(data.graph_json);
                            Plotly.newPlot('plot', graph.data, graph.layout, {responsive: true});
                        }

                        if (data.pp_graph_json) {
                            const pp_graph = JSON.parse(data.pp_graph_json);
                            Plotly.newPlot('pp-plot', pp_graph.data, pp_graph.layout, {responsive: true});
                        }
                    })
                    .catch(error => {
                        console.error("Error:", error);
                        if (currentLang === "en") {
                            showErrorModal("Sorry, we can't find solution. Please try another one.");
                        } else {
                            showErrorModal("Je nám ľúto, ale nemôžeme nájsť riešenie. Skúste prosím iné.")
                        }
                    });
            }
        });
    }
}
document.addEventListener("DOMContentLoaded", initModelPage);

async function initCalculatorPage() {
    currentLang = await getCurrentLanguage();
    console.log("Lang in initCalculatorPage:", currentLang);

    const calcForm = document.getElementById("calc-form");

    if (calcForm) {
        calcForm.addEventListener("submit", function (event) {
            event.preventDefault();

            let equation = document.getElementById("equation-input");
            let p0 = document.getElementById("p0");
            let p1 = document.getElementById("p1");
            let isValid = true;
            let eqData = {};

            hideError(equation);
            hideError(p0);
            hideError(p1);

            if (!equation.value.includes("=")) {
                showError(equation, currentLang === "en"? "Please add the right side of equation!" : "Doplňte pravú stranu rovnice!");
                isValid = false;
            } else {
                if ((equation.value.split("=").length - 1) > 1) {
                    showError(equation, currentLang === "en"? "Duplicates of '='" : "Duplikáty znakov '='");
                    isValid = false;
                }
            }

            if (!validateScopes(equation.value) && isValid) {
                showError(equation, currentLang === "en"? "Bracket mismatch!" : "Nesúlad zátvoriek!");
                isValid = false;
            }

            const maxOrder = getMaxOrder(equation.value);
            console.log("Max order: " + maxOrder);
            if(isValid) {
                if (maxOrder > 2) {
                    showError(equation, currentLang === "en" ? "Maximum allowed order - (n±2)" : "Maximálny povolený stupeň - (n±2)");
                    isValid = false;
                } else {
                    if (maxOrder === 1 && p1.value.trim() !== "") {
                        showError(p1, currentLang === "en" ? "Equation of the 1 order must have only p0 initial condition" : "Rovnica 1. rádu musí mať iba počiatočnú podmienku p0");
                        isValid = false;
                    } else if (maxOrder === 0 && p1.value.trim() !== ""  && p0.value.trim() !== "") {
                        showError(p0, currentLang === "en" ? "Equation don't need initial conditions" : "Rovnica nepotrebuje začiatočné podmienky");
                        showError(p1, currentLang === "en" ? "Equation don't need initial conditions" : "Rovnica nepotrebuje začiatočné podmienky");
                    } else if (maxOrder === 0 && p0.value.trim() !== "") {
                        showError(p0, currentLang === "en" ? "Equation don't need initial conditions" : "Rovnica nepotrebuje začiatočné podmienky");
                    } else if (maxOrder === 0 && p1.value.trim() !== "") {
                        showError(p1, currentLang === "en" ? "Equation don't need initial conditions" : "Rovnica nepotrebuje začiatočné podmienky");
                        isValid = false;
                    }
                }
            }

            console.log("Is valid: " + isValid);
            if(isValid) {
                if (validateNExpressions(equation.value, equation, currentLang)) {
                    isValid = false;
                }
            }

            if (isValid) {
                eqData["equation"] = equation.value;
                eqData["p0"] = p0.value;
                eqData["p1"] = p1.value;

                fetch("/calculator", {
                    method: "POST",
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify(eqData)
                })
                    .then(response => response.json())
                    .then(data => generateAnswerContainer(data))
                    .catch(error => {
                        console.error("Error:", error);
                        if (currentLang === "en") {
                            showErrorModal("There was an error - couldn't solve the equation or you entered the equation incorrectly (please check if there is no symbol \"*\" before (n), (n+1) etc. - it's the most common problem).");
                        } else {
                            showErrorModal("Vyskytla sa chyba - rovnicu sa nepodarilo vyriešiť alebo ste ju zadali nesprávne (skontrolujte, či pred (n), (n+1) atď. nie je symbol \"*\" - je to najčastejší problém).");
                        }
                    });

            }
        });
    }
}
document.addEventListener("DOMContentLoaded", initCalculatorPage);

function removeLastSymbol() {
    let inputField;
    if (document.querySelector('#function')) {
        inputField = document.querySelector('#function');
    } else if (document.querySelector('#equation-input')) {
        inputField = document.querySelector('#equation-input');
    }

    const start = inputField.selectionStart;
    const end = inputField.selectionEnd;

    if (start === end && start > 0) {
        inputField.value = inputField.value.slice(0, start - 1) + inputField.value.slice(end);
        inputField.setSelectionRange(start - 1, start - 1);
    }

    inputField.focus();
}

function removeAllFromField() {
    let inputField;
    if (document.querySelector('#function')) {
        inputField = document.querySelector('#function');
    } else if (document.querySelector('#equation-input')) {
        inputField = document.querySelector('#equation-input');
    }
    inputField.value = '';
}

function validateScopes(value) {
    if (value === null || value === undefined || value.trim() === '') {
        return true;
    }

    const stringValue = String(value);
    let stack = [];

    for (let i = 0; i < stringValue.length; i++) {
        const char = stringValue[i];
        if (char === "(") {
            stack.push(char);
        } else if (char === ")") {
            if (stack.length === 0) {
                return false;
            }
            stack.pop();
        }
    }
    return stack.length === 0;
}

function showError(inputElement, message) {
    const errorMessage = inputElement.parentElement.querySelector(".error-message");
    if (errorMessage) {
        errorMessage.textContent = message;
    }

    errorMessage.classList.add('show');
}

function hideError(inputElement) {
    const errorMessage = inputElement.parentElement.querySelector(".error-message");
    errorMessage.textContent = "";
    errorMessage.classList.remove('show');
}

function getMaxOrder(equationStr) {
    const regex = /[a-zA-Z]\(n([+-]\d+)?\)/g;
    let match;
    let maxOrder = 0;

    while ((match = regex.exec(equationStr)) !== null) {
        const offsetStr = match[1];
        const offset = offsetStr ? parseInt(offsetStr) : 0;
        if (Math.abs(offset) > maxOrder) {
            maxOrder = Math.abs(offset);
        }
    }
    console.log(maxOrder);
    return Math.abs(maxOrder);
}

function generateAnswerContainer(data) {
    const targetElement = document.querySelector('.rectangle.calc-rect.before');

    if (targetElement) {
        const generalEqCont = document.createElement('div');
        generalEqCont.className = 'general-eq-cont';

        const eqAnswerCont = document.createElement('div');
        eqAnswerCont.className = 'eq-answer-cont';

        const eqAnswer = document.createElement('div');
        eqAnswer.className = 'eq-answer';
        eqAnswer.id = 'solution-container';

        eqAnswerCont.appendChild(eqAnswer);
        generalEqCont.appendChild(eqAnswerCont);

        targetElement.appendChild(generalEqCont);

        targetElement.classList.remove('before');
        targetElement.classList.add('after');
    }

    document.getElementById("solution-container").innerHTML = data.html;
    if (window.MathJax && window.MathJax.typeset) {
        MathJax.typeset();
    }
}

function validateNExpressions(equation, field, lang) {
    const parts = equation.split('=');

    const leftSide = parts[0].trim();
    const rightSide = parts[1].trim();

    const patterns = [
        { label: "(n)", regex: /\(n\)/g },
        { label: "(n+1)", regex: /\(n\+1\)/g },
        { label: "(n+2)", regex: /\(n\+2\)/g },
        { label: "(n-1)", regex: /\(n-1\)/g },
        { label: "(n-2)", regex: /\(n-2\)/g }
    ];

    let hasPatternOnLeft = false;
    let errors = false;

    patterns.forEach(({ label, regex }) => {
        const leftMatches = leftSide.match(regex);
        const leftCount = leftMatches ? leftMatches.length : 0;

        if (leftCount > 0) {
            hasPatternOnLeft = true;
        }

        if (leftCount > 1) {
            showError(field, lang === "en" ?
                `Expression ${label} appears more than once on the left side` :
                `Výraz ${label} sa objaví viac ako raz na ľavej strane`);
            errors = true;
        }

        const rightMatches = rightSide.match(regex);
        const rightCount = rightMatches ? rightMatches.length : 0;

        if (rightSide.includes('x')) {
            showError(field, lang === "en" ?
                `Expression \"x\" is not allowed on the right side` :
                `Výraz \"x\" nie je povolený na pravej strane`);
            errors = true;
        }

        if (rightCount > 0) {
            showError(field, lang === "en" ?
                `Expression ${label} is not allowed on the right side` :
                `Výraz ${label} nie je povolený na pravej strane`);
            errors = true;
        }
    });

    if (!hasPatternOnLeft) {
        showError(field, lang === "en" ?
            "The left side must contain at least one of these patterns: (n), (n+1), (n+2), (n-1), (n-2)" :
            "Ľavá strana musí obsahovať aspoň jeden z týchto vzorov: (n), (n+1), (n+2), (n-1), (n-2)");
        errors = true;
    }

    return errors;
}

function showErrorModal(message) {
    const modal = document.getElementById("errorModal");
    const modalMessage = document.getElementById("modal-message");
    modalMessage.textContent = message;
    modal.classList.remove("hidden");
}

document.getElementById("closeModal").onclick = function () {
    document.getElementById("errorModal").classList.add("hidden");
};

