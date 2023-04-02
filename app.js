const csvFileInput = document.getElementById("csv-file");
const csvDropdown = document.getElementById("csv-dropdown");

function toggleDropdown() {
    if (document.getElementById("label1").checked) {
        csvDropdown.style.display = "block";
    } else {
        csvDropdown.style.display = "none";
    }
}

csvFileInput.addEventListener("change", (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = (event) => {
        const csv = event.target.result;
        const rows = csv.split("\n");
        const headers = rows[0].split(",");

        headers.forEach((header) => {
            const option = document.createElement("option");
            option.textContent = header;
            csvDropdown.appendChild(option);
        });
    };

    reader.readAsText(file);
});


/* old code start

const csvFileInput = document.getElementById("csv-file");
const csvDropdown = document.getElementById("csv-dropdown");

csvFileInput.addEventListener("change", (event) => {
  const file = event.target.files[0];
  const reader = new FileReader();

  reader.onload = (event) => {
    const csv = event.target.result;
    const rows = csv.split("\n");
    const headers = rows[0].split(",");

    headers.forEach((header) => {
      const option = document.createElement("option");
      option.textContent = header;
      csvDropdown.appendChild(option);
    });
  };

  reader.readAsText(file);
});


old code end*/