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
            } else if (document.querySelector('#equation-input')) {
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
                        console.log("Hello from here");
                        showError(input, "This field is required!");
                    } else {
                        showError(input, "Povinné pole!!");
                        console.log("Hello from else");
                    }
                    isValid = false;
                    continue;
                }

                if ((fieldsName.includes("price") && fieldsName !== "previous actual price") ||
                    (fieldsName.includes("cena") && fieldsName !== "predchádzajúca skutočná cena")) {
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
                    (fieldsName === "iterácie" || fieldsName === "obdobia")) {
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
                        alert("Sorry, we can't find solution for your function. Please try another one.")
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
                if (currentLang === "en") {
                    showError(equation, "Please add the right side of equation!");
                } else {
                    showError(equation, "Doplňte pravú stranu rovnice!");
                }
                isValid = false;
            } else {
                if ((equation.value.split("=").length - 1) > 1) {
                    if (currentLang === "en") {
                        showError(equation, "Duplicates of '='");
                    } else {
                        showError(equation, "Duplikáty znakov '='");
                    }
                    isValid = false;
                }
            }

            if (!validateScopes(equation.value)) {
                if (currentLang === "en") {
                    showError(equation, "Bracket mismatch!");
                } else {
                    showError(equation, "Nesúlad zátvoriek!");
                }
                isValid = false;
            }

            const maxOrder = getMaxOrder(equation.value);
            if (maxOrder > 2) {
                console.log(maxOrder);
                if (currentLang === "en") {
                    showError(equation, "Maximum allowed order - (n±2)");
                } else {
                    showError(equation, "Maximálny povolený stupeň - (n±2)");
                }
                isValid = false;
            } else {
                if (maxOrder === 1 && p1.value.trim() !== "") {
                    if (currentLang === "en") {
                        showError(p1, "Equation of the 1 order must have only p0 initial condition");
                    } else {
                        showError(p1, "Rovnica 1. rádu musí mať iba počiatočnú podmienku p0");
                    }
                    isValid = false;
                } else if (maxOrder === 0 && (p1.value.trim() !== "" || p1.value.trim() !== "")) {
                    if (currentLang=== "en") {
                        showError(p0, "Equation don't need initial conditions");
                        showError(p1, "Equation don't need initial conditions");
                    } else {
                        showError(p0, "Rovnica nepotrebuje začiatočné podmienky");
                        showError(p1, "Rovnica nepotrebuje začiatočné podmienky");
                    }
                    isValid = false;
                }
            }

            if (hasInvalidAsterisk(equation.value)) {
                if (currentLang === "en") {
                    showError(equation, "The expression contains an invalid * before the brackets with n or n");
                } else {
                    showError(equation, "Výraz obsahuje neplatné * pred zátvorkami s n alebo n");
                }
                isValid = false;
            }

            // if (containsOnlyValidNForms(equation.value)) {
            //     showError(equation, "The equation must contain n, (n), (n+1), (n-2), etc.");
            //     isValid = false;
            // }

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
                        alert("Сталася помилка. Спробуйте інше рівняння.");
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
    console.log("Hello from showError");
    const errorMessage = inputElement.nextElementSibling;
    console.log("nextElementSibling: " + errorMessage.name);
    errorMessage.textContent = message;
}

function hideError(inputElement) {
    const errorMessage = inputElement.nextElementSibling;
    errorMessage.textContent = '';
}

function getMaxOrder(equationStr) {
    const regex = /[a-zA-Z]\(n([+-]\d+)?\)/g;
    let match;
    let maxOrder = 0;

    while ((match = regex.exec(equationStr)) !== null) {
        const offsetStr = match[1];
        const offset = offsetStr ? parseInt(offsetStr) : 0;
        if (offset > maxOrder) {
            maxOrder = offset;
        }
    }
    console.log(maxOrder);
    return maxOrder;
}

function hasInvalidAsterisk(expression) {
    const pattern1 = /\*\s*\(.*?n.*?\)/;

    return pattern1.test(expression);
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

// function containsOnlyValidNForms(expression) {
//     const allowedPattern = /\b(n|\(n(\s*[\+\-]\s*\d+)?\))\b/g;
//
//     // Знайдемо всі підозрілі "n", навіть неправильні
//     const allNLike = expression.match(/\b\(?n[\+\-\d\s]*\)?\b/g) || [];
//
//     // Знайдемо тільки валідні
//     const validNLike = expression.match(allowedPattern) || [];
//
//     // Якщо кількість "n"-подібних частин = кількість валідних — усе ок
//     return allNLike.length === validNLike.length;
// }
