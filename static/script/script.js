window.onload = function () {

    $(".registerbtn").submit(function (event) {
        event.preventDefault();
        $(".error span").hide();
        if (!validateForm()) {
            $(".error span").show();
            return false;
        }
        else {
            alert("done")
            form.submit();
        }
    })
    $(".updatebtn").submit(function (event) {
        event.preventDefault();
        $(".error span").hide();
        if (!validateForm()) {
            $(".error span").show();
            return false;
        }
        else {
            alert("done")
            form.submit();
        }
    })


    $(".cancel").click(function () {

        var form = document.getElementById("property_form");
        var elements = form.elements;
        for (var i = 0; i < elements.length; i++) {
            var field = elements[i];
            if (field.type !== "button" && field.type !== "submit" && field.type !== "reset") {
                field.value = "";
            }
        }
    })

};
function validateForm() {
    // Get form fields
    const propnumber = document.getElementById('id_propnumber');
    const OwnerName = document.getElementById('id_OwnerName');
    const Village = document.getElementById('id_Village');
    const City = document.getElementById('id_City');
    const State = document.getElementById('id_State');
    const Location = document.getElementById('id_Location');
    const Size = document.getElementById('id_Size');
    const Bookvalue = document.getElementById('id_Bookvalue');
    const guidelinevalue = document.getElementById('id_guidelinevalue');

    // Flag to track form validity
    let isValid = true;

    // Check propnumber field
    if (propnumber.value.trim() === '') {
        $(".propnumber").html('Property number is required.');
        isValid = false;
    } else if (isNaN(propnumber.value)) {
        $(".propnumber").html('Property number must be a number.');
        isValid = false;
    }

    // Check OwnerName field
    if (OwnerName.value.trim() === '') {
        $(".OwnerName").html('Owner name is required.');
        isValid = false;
    }

    // Check Village field
    if (Village.value.trim() === '') {
        $(".Village").html('Village is required.');
        isValid = false;
    }

    // Check City field
    if (City.value.trim() === '') {
        $(".City").html('City is required.');
        isValid = false;
    }

    // Check State field
    if (State.value.trim() === '') {
        $(".State").html('State is required.');
        isValid = false;
    }

    // Check Location field
    if (Location.value.trim() === '') {
        $(".Location").html('Location is required.');
        isValid = false;
    }

    // Check Size field
    if (Size.value.trim() === '') {
        $(".Size").html('Size is required.');
        isValid = false;
    }

    // Check Bookvalue field
    if (Bookvalue.value.trim() === '') {
        $(".Bookvalue").html('Book value is required.');
        isValid = false;
    } else if (isNaN(Bookvalue.value)) {
        $(".Bookvalue").html('Book value must be a number.');
        isValid = false;
    }

    // Check guidelinevalue field
    if (guidelinevalue.value.trim() === '') {
        $(".guidelinevalue").html('Guideline value is required.');
        isValid = false;
    } else if (isNaN(guidelinevalue.value)) {
        $(".guidelinevalue").html('Guideline value must be a number.');
        isValid = false;
    }

    // Return form validity
    return isValid;
}