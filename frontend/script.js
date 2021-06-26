var resultPanel = document.getElementById("pizzaResult");
var pizzaButton = document.getElementById("getPizzaButton");

function getPizza() {
fetch('http://localhost:5001/pizza')
    .then(r => {
        r.json()
            .then(c => resultPanel.innerText = c)
            .catch(c => console.log(c));
    })
    .catch(r => console.log)
}

pizzaButton.addEventListener('click', getPizza)