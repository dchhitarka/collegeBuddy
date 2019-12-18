window.onload = ()=>{
    config.load_data();
    backup();
    let input = document.getElementById("restore_file");
	input.addEventListener("change", function() {
	    restore();
	});
}

function backup() {
    var data_string = JSON.stringify(config.data);
    var data_uri = "data:application/json; charset=utf-8," + encodeURIComponent(data_string);

    var file_name = "timetable_data_backup.json";

    var link_element = document.getElementById("backup");
    link_element.setAttribute("href", data_uri);
    link_element.setAttribute("download", file_name);
}

function restore() {
    let input = document.getElementById("restore_file");
    let file = input.files[0];

    let reader = new FileReader();
    reader.onload = function(e) {
        try {
            let content_json = e.target.result;
            let content = JSON.parse(content_json);
            config.save_data(content);
            alert("Settings have been restored. Changes will take effect after page refresh.");
        }

        catch(e) {
            alert("There has been an error restoring your data.");
        }
    }

    reader.readAsText(file);
}

function reset() {
    console.log("Reset");
    config.reset_data();
    alert("Data successfully reset.")
}

const save = ()=>{
    config.save_data(config.data);
    alert("General settings have been saved. Changes will take effect after page refresh.");
}
