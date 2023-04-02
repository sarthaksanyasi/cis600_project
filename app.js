const labelRadio = document.getElementsByName("label-group");
const csvFileInput = document.getElementById("csv-file");
const csvDropdown = document.getElementById("csv-dropdown");

// Hide the dropdown initially
csvDropdown.style.display = "none";

// Listen for changes to the radio buttons
for (let i = 0; i < labelRadio.length; i++) {
    labelRadio[i].addEventListener("change", (event) => {
        if (event.target.value === "label1") {
            csvDropdown.style.display = "block";
        } else {
            csvDropdown.style.display = "none";
        }
    });
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
