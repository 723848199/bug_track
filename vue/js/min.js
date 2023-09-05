document.getElementById('btn').addEventListener('click', function() {
    fetch('/bom')
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            console.log(data);
        })
        .catch(function(error) {
            console.error(error);
        });
});
