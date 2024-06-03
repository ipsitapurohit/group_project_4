// Function to get the value of the selected number of bathrooms
function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    // Iterate through the bathroom radio buttons
    for(var i in uiBathrooms) {
        if(uiBathrooms[i].checked) {
            return parseInt(i) + 1;  // Return the index of the checked button plus one
        }
    }
    return -1; // Return -1 if no valid value is found
}

// Function to get the value of the selected number of bedrooms
function getBedValue() {
    var uiBed = document.getElementsByName("uiBed");
    // Iterate through the bedroom radio buttons
    for(var i in uiBed) {
        if(uiBed[i].checked) {
            return parseInt(i) + 1;  // Return the index of the checked button plus one
        }
    }
    return -1; // Return -1 if no valid value is found
}

// Function to handle the "Estimate Price" button click event
function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft").value;
    var bed = getBedValue();
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations").value;
    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = "http://127.0.0.1:5000/api/predict_home_price";

    // Make an AJAX POST request to get the estimated price
    $.ajax({
        url: url,
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            total_sqft: parseFloat(sqft),
            bed: bed,
            bath: bathrooms,
            location: location
        }),
        success: function(data, status) {
            console.log(data.estimated_price);
            // Display the estimated price in the UI
            estPrice.innerHTML = "<h2>$" + data.estimated_price.toString() + "</h2>";
            console.log(status);
        }
    });
}

// Function to handle page load event
function onPageLoad() {
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/api/get_location_names";

    // Make a GET request to get the list of location names
    $.get(url, function(data, status) {
        console.log("got response for get_location_names request");
        if (data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();  // Clear existing options
            // Populate the dropdown with location names
            for (var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
}

// Set onPageLoad to run when the window loads
window.onload = onPageLoad;
