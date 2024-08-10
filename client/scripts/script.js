/* Dropdown menu */
const toggleButton = document.querySelector('.toggle_btn')
const toggleButtonIcon = document.querySelector('.toggle_btn i')
const dropdownMenu = document.querySelector('.dropdown_menu')

toggleButton.onclick = function () {
  dropdownMenu.classList.toggle('open')
  const isOpen = dropdownMenu.classList.contains('open')

  toggleButtonIcon.classList = isOpen
    ? 'fa-solid fa-xmark'
    : 'fa-solid fa-bars'
}

let food;
let piechart2;

/* Upload photo */
var loadFile = function (event) {
  var output = document.getElementById('output');
  output.style.display = 'block';

  var uploadBtn = document.getElementById('upload-btn');
  uploadBtn.style.display = 'none';

  var info = document.querySelector('.right');
  info.style.display = 'flex';

  let file = event.target.files[0];
  output.src = URL.createObjectURL(file);

  if (file) {
    let reader = new FileReader();

    reader.onload = function (e) {
      // Get the base64 data
      let base64Data = e.target.result;

      // Extract the format from the data URL
      let formatMatch = base64Data.match(/^data:image\/(.*);base64,/);
      if (formatMatch && formatMatch.length > 1) {
        let format = formatMatch[1];

        // Remove the data URL prefix to get the base64-encoded bytes
        let base64Bytes = base64Data.replace(/^data:image\/(.*);base64,/, '');

        // Create the dictionary
        let data = {
          'format': format,
          'bytes': base64Bytes
        };

        // Log the dictionary to the console (you can use it further as needed)
        console.log(data);

        fetch('http://127.0.0.1:5000/get_food', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
        })
          .then(response => {
            if (!response.ok) {
              throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
          })
          .then(result => {

            console.log('Success:', result);

            food = result.food;

            if (food.name == "ciorba_de_burta")
              document.getElementById("food_title").innerText = "Ciorbă de Burtă";
            else if (food.name == "papanasi")
              document.getElementById("food_title").innerText = "Papanași";
            else
              document.getElementById("food_title").innerText = food.name.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');

            document.getElementById("calories1").innerText = food.calories + " calories";

            var ctx1 = document.getElementById('piechart1').getContext('2d');
            new Chart(ctx1, {
              type: "pie",
              data: {
                labels: ["Proteins", "Fats", "Carbohydrates"],
                datasets: [{
                  backgroundColor: [
                    "#b91d47",
                    "#00aba9",
                    "#2b5797"
                  ],
                  data: [Math.round(food.proteins), Math.round(food.fats), Math.round(food.carbs)]
                }]
              },
              options: {
                plugins: {
                  legend: {
                    display: false
                  }
                },
                title: {
                  display: false,
                  text: "Macros per 100g"
                }
              }
            });

            /* Enable button */
          })
          .catch(error => {
            console.error('Error:', error);
            let errorOutput = document.createElement('pre');
            errorOutput.textContent = `Error: ${error.message}`;
            document.body.appendChild(errorOutput);
          });

      } else {
        console.error('Unable to extract format from the data URL.');
      }
    };

    reader.onerror = function (error) {
      console.error('Error reading file:', error);
    };

    reader.readAsDataURL(file); // Read the file as a data URL (base64)
  } else {
    console.error('No file selected.');
  }
};

function chooseFile() {
  document.getElementById("fileInput").click();
};

function submitWeight() {

  weight = document.getElementById('weightInput').value;

  if (weight > 0) {
    rightMacros = document.querySelector('.rightmacros');
    rightMacros.style.display = 'flex';

    leftMacros = document.querySelector('.leftmacros');
    leftMacros.style.borderRight = '1mm dotted white';

    document.getElementById('forWeight').innerText = 'For ' + weight + ' g';

    var calories = Math.round(weight / 100 * food.calories);
    var proteins = Math.round(weight / 100 * food.proteins);
    var fats = Math.round(weight / 100 * food.fats);
    var carbs = Math.round(weight / 100 * food.carbs);

    document.getElementById("calories2").innerText = calories + " calories";

    var ctx2 = document.getElementById('piechart2').getContext('2d');

    if (piechart2) {
      piechart2.destroy();
    }

    piechart2 = new Chart(ctx2, {
      type: "pie",
      data: {
        labels: ["Proteins", "Fats", "Carbohydrates"],
        datasets: [{
          backgroundColor: [
            "#b91d47",
            "#00aba9",
            "#2b5797"
          ],
          data: [proteins, fats, carbs]
        }]
      },
      options: {
        plugins: {
          legend: {
            display: false
          }
        },
        title: {
          display: false,
          text: "Macros per 100g"
        }
      }
    });
  }
};