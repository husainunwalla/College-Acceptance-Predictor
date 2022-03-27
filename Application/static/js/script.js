function predict() {
    fetch('/predictAll')
        .then(function (response) {
            return response.json();
        }).then(function (text) {
            console.log('GET response:');
            my_dat = JSON.parse(text)
            console.log(my_dat);
        });
}
