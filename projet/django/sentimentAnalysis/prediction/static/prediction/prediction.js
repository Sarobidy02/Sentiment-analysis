const button = document.getElementById("predict");
const result = document.getElementById("result");
const textArea = document.getElementById("text-to-predict");
const url = '/prediction';

button.addEventListener('click', (event) => {
    const text = textArea.value;
    //input not empty
    if(text){
        fetch(url + '/score', {
            method: 'POST',
            body: JSON.stringify({'text': text})
        })
        .then(response => response.json())
        .then(data => {
            //inject the result into the page
            const sentiment = data.sentiment
            const proba = data.proba;
            result.innerHTML = `<div class="p-3 border bg-light">
            <p class="text-center">${sentiment} <strong>${proba}%</strong></p>
            </div>`;
        })
        .catch(error => {})

        
    }
    
})