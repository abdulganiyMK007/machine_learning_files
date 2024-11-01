function getSibspValue() {
  var sibsp = document.getElementsByName("sibsp");
  for (var i in sibsp) {
    if (sibsp[i].checked) {
        return parseInt(i);
    }
  }
  return -1; // Invalid Value
}

function getParchValue() {
  var sibsp = document.getElementsByName("parch");
  for (var i in sibsp) {
    if (sibsp[i].checked) {
        return parseInt(i);
    }
  }
  return -1; // Invalid Value
}

function onClickedPredict() {
  
  var prediction = document.getElementById("predictionMessage");
  
  console.log("Predict button clicked")
  var pclass = document.querySelector('input[name="pclass"]:checked');
  var age = document.getElementById("age").value;
  var sibsp = getSibspValue();
  var parch = getParchValue();
  var fare = document.getElementById("fare").value;
  var sex = document.querySelector('input[name="sex"]:checked');
  var embarked = document.querySelector('input[name="embarked"]:checked');

  var url = "http://127.0.0.1:5000/predict";

  $.post(url, {
    pclass: pclass.value,
    age: age,
    sibsp: sibsp,
    parch: parch,
    fare: parseFloat(fare.value),
    sex: sex.value,
    embarked: embarked.value
  }, function(data, status) {
      var result = data.survival_prediction;
      var color;
      var message;
      
      if (result == '0') {
        message = "Survived? NO 😭";
        color = "#f44336";
      } else {
        message = "Survived? YES 😃";
        color = "#4CAF50";
      }

      prediction.innerHTML = message;
      prediction.style.display = "block";
      prediction.style.backgroundColor = color;
      console.log(status);
  });
}


// Function to clear the form
function clearForm() {
  document.getElementById("titanicForm").reset();

  // Hide the "Survived" message if visible
  document.getElementById("predictionMessage").style.display = "none";
}

