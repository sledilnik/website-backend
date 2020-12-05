function tinyMceFilePicker(uploadUrl) {

  return function (callback, value, meta) {
    if (!(meta.filetype == "file" || meta.filetype == "image")) { return };

    var input = document.createElement('input');
    input.setAttribute('type', 'file');

    if (meta.filetype =="image") {
      input.setAttribute('accept', 'image/*');
    };

    /*
      Note: In modern browsers input[type="file"] is functional without
      even adding it to the DOM, but that might not be the case in some older
      or quirky browsers like IE, so you might want to add it to the DOM
      just in case, and visually hide it. And do not forget do remove it
      once you do not need it anymore.
    */

    input.addEventListener("change", function() {
      var file = this.files[0];
      var reader = new FileReader();

      var formData = new FormData();

      formData.append("type", meta.filetype);
      formData.append("file", file);
      formData.append("filetype", meta.filetype);

      function onLoadHandler () {
        if (this.status != 200) {
          alert("Error: " + this.statusText)
        } else {
          if (this.response.error) {
            alert("Error: " + this.response.error)
          } else {
            callback(this.response.location, {text: file.name, title: ""});
          }
        }
      };

      var request = new XMLHttpRequest();
      request.addEventListener("load", onLoadHandler);
      request.open("POST", uploadUrl);
      request.responseType = "json"
      request.send(formData);

      reader.readAsDataURL(file);
    });

    input.click();
  };
};
