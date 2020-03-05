
    function validtionform(){
    	$('span').hide();
	var pswd = $('#id_password').val();
	var cpswd = $('#id_confirmpassword').val();
	if (pswd!=cpswd){
		msg="password not match";
		$('#span_password').text(msg);
		$('#span_password').show();
		
		return false;
	}
	return true;
}

var loadingTask = PDFJS.getDocument("../media/{{ MEDIA_URL }}{{ user.signup.upload_file }}");
loadingTask.promise.then(
  function(pdf) {
    // Load information from the first page.
    pdf.getPage(4).then(function(page) {
      var scale = 1;
      var viewport = page.getViewport(scale);

      // Apply page dimensions to the <embed> element.
      var canvas = document.getElementById("pdf");
      var context = canvas.getContext("2d");
      canvas.height = viewport.height;
      canvas.width = viewport.width;

      // Render the page into the <embed> element.
      var renderContext = {
        canvasContext: context,
        viewport: viewport
      };
      page.render(renderContext).then(function() {
        console.log("Page rendered!");
      });
    });
  },
  function(reason) {
    console.error(reason);
  }
);


