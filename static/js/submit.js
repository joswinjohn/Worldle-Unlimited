$("#guess_form").submit(function(e) {
    e.preventDefault();
    if ($("#submit_btn").val() == "Guess") {
        inputs = $(".inputs[type=text]").toArray();
        current_input = null;

        inputs.forEach( function(e) {
            console.log(e.value);

            if (!$(e).attr('readonly')) {
                current_input = e;
                console.log(current_input.value);
            }
        })
        console.log(current_input.value);

        // use regex to make this more efficent and faster later
        switch ($(current_input).attr('id')) {
            case "input_1":
                $(current_input).attr('readonly', 'true');

                if (check_country(current_input.value)) {
                    alert("Correct!")
                    $("#submit_btn").val("Continue");
                    break;
                }

                $("#input_2").removeAttr('readonly')
                break;
            case "input_2":
                $(current_input).attr('readonly', 'true');

                if (check_country(current_input.value)) {
                    alert("Correct!")
                    $("#submit_btn").val("Continue");
                    break;
                }

                $("#input_3").removeAttr('readonly')
                break;
            case "input_3":
                $(current_input).attr('readonly', 'true');

                if (check_country(current_input.value)) {
                    alert("Correct!")
                    $("#submit_btn").val("Continue");
                    break;
                }

                $("#input_4").removeAttr('readonly')
                break;
            case "input_4":
                $(current_input).attr('readonly', 'true');

                if (check_country(current_input.value)) {
                    alert("Correct!")
                    $("#submit_btn").val("Continue");
                    break;
                }

                $("#input_5").removeAttr('readonly')
                break;
            case "input_5":
                $(current_input).attr('readonly', 'true');

                if (check_country(current_input.value)) {
                    alert("Correct!")
                }

                $("#submit_btn").val("Continue");
                break;
                    
        }
    } else {
        location.reload()
    }
});

function check_country(country) {
    var request = new XMLHttpRequest();
    request.open("GET", "https://gist.githubusercontent.com/joswinjohn/69cb28dd25dc5eb36e0d9d12a3001adb/raw/6e1d44352b112bdcb8299555b63a757a2689e225/countries.json", false);
    request.send(null)
    var countries_json = JSON.parse(request.responseText);

    console.log(countries_json)

    for (var i = 0; i < countries_json.length; i++) {
        var object = countries_json[i];
        if (country.toUpperCase() == object.name.toUpperCase()) {
            return true;
        }
    }

    return false;
}