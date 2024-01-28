$(document).ready(function() {

    $.getJSON("http://localhost:8000/api/customerlist", function(data) {

        data.map((item) => {
            $('#id').append($('<option>').text(item.firstname + " " + item.lastname).val(item.id))

        })

    })
})