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

document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.getElementById('toggle-view');
    const basicSymbols = document.getElementById('basic-symbols');
    const functionSymbols = document.getElementById('function-symbols');

    if (toggleButton && basicSymbols && functionSymbols) {
        toggleButton.addEventListener('click', function () {
            if (basicSymbols.style.display !== 'none') {
                basicSymbols.style.display = 'none';
                functionSymbols.style.display = '';
                toggleButton.textContent = 'Show numbers';
            } else {
                basicSymbols.style.display = '';
                functionSymbols.style.display = 'none';
                toggleButton.textContent = 'Show functions';
            }
        });
    }

    window.removeAllFromField = removeAllFromField;
    window.removeLastSymbol = removeLastSymbol;
});

document.addEventListener("DOMContentLoaded", function () {
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
                    showError(input, "This field is required!");
                    isValid = false;
                    continue;
                }

                if (fieldsName.includes("price") && fieldsName !== "previous actual price") {
                    if (parseFloat(fieldValue) <= 0) {
                        showError(input, "Value must be positive!");
                        isValid = false;
                        continue;
                    }
                }

                if (fieldsName === "previous actual price") {
                    fieldValue = fieldValue.replace(/,$/, '');
                    const values = fieldValue.split(',').map(v => v.trim());
                    const regex = /^[0-9,.+\-]*$/;

                    for (let numberStr of values) {
                        if (regex.test(numberStr)) {
                            if (parseFloat(numberStr) <= 0) {
                                showError(input, "Value must be positive!");
                                isValid = false;
                            }
                        } else {
                            showError(input, "Field must contains numbers!");
                            isValid = false;
                        }
                    }
                }

                if (fieldsName === "iterations" || fieldsName === "periods") {
                    if (parseFloat(fieldValue) % 1 !== 0) {
                        showError(input, "Value must be a whole number!");
                        isValid = false;
                        continue;
                    }
                }

                if (fieldsName === "adjustment factor" || fieldsName === "adaptation coefficient") {
                    if (parseFloat(fieldValue) < 0 || parseFloat(fieldValue) > 1) {
                        showError(input, "Value must be between 0 and 1!");
                        isValid = false;
                        continue;
                    }
                }

                formData[fieldsName] = isNaN(fieldValue) || fieldValue.trim() === "" ? fieldValue : parseFloat(fieldValue);
            }

            const functionField = document.querySelector('#function');
            if (functionField && !validateScopes(functionField.value)) {
                showError(functionField, "Bracket mismatch!");
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
});

document.addEventListener("DOMContentLoaded", function () {
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
                showError(equation, "Please add the right side of equation");
                isValid = false;
            } else {
                if ((equation.value.split("=").length - 1) > 1) {
                    showError(equation, "Duplicates of '='");
                    isValid = false;
                }
            }

            if (!validateScopes(equation.value)) {
                showError(equation, "Bracket mismatch!");
                isValid = false;
            }

            const maxOrder = getMaxOrder(equation.value);
            if (maxOrder > 2) {
                console.log(maxOrder);
                showError(equation, "Maximum allowed order - (n±2)");
                isValid = false;
            } else {
                if (maxOrder === 1 && p1.value.trim() !== "") {
                    showError(p1, "Equation of the 1 order must have only p0 initial condition");
                    isValid = false;
                } else if (maxOrder === 0 && (p1.value.trim() !== "" || p1.value.trim() !== "")) {
                    showError(p0, "Equation don't need initial conditions");
                    showError(p1, "Equation don't need initial conditions");
                    isValid = false;
                }
            }

            if (hasInvalidAsterisk(equation.value)) {
                showError(equation, "The expression contains an invalid * before the brackets with n or n");
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
});

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
    const errorMessage = inputElement.nextElementSibling;
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


