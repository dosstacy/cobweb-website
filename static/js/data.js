document.querySelectorAll('.table-button').forEach(button => {
    button.addEventListener('click', function () {
        if (button.id !== 'remove' && button.id !== 'removeAll') {
            let inputField = document.querySelector('#function');
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
                    const values = fieldValue.split(',').map(v => v.trim());
                    for (let numberStr of values) {
                        if (parseFloat(numberStr) <= 0) {
                            showError(input, "Value must be positive!");
                            isValid = false;
                            continue;
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

function removeLastSymbol() {
    let inputField = document.querySelector('#function');

    const start = inputField.selectionStart;
    const end = inputField.selectionEnd;

    if (start === end && start > 0) {
        inputField.value = inputField.value.slice(0, start - 1) + inputField.value.slice(end);
        inputField.setSelectionRange(start - 1, start - 1);
    }

    inputField.focus();
}

function removeAllFromField() {
    let inputField = document.querySelector('#function');
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
    errorMessage.classList.add('show');
}

function hideError(inputElement) {
    const errorMessage = inputElement.nextElementSibling;
    errorMessage.classList.remove('show');
}

