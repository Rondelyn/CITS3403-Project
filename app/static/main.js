// Used to toggle the login page to the signup view 
function showSignup(){
    document.getElementById('signup form').style.display="block";
    document.getElementById('login form').style.display="none"; 
}
  
// Used to toggle the login page to the login view 
function showLogin(){
    document.getElementById('login form').style.display="block";
    document.getElementById("signup form").style.display="none"; 
}

// An event listener that takes place upon page load and sets the background of the page to the stored value otherwise sets it to alice blue by default 
document.addEventListener('DOMContentLoaded', function() {
  const colorPicker = document.getElementById('myColor');
  const storedColor = localStorage.getItem('backgroundColor');

  document.body.style.backgroundColor = storedColor || '#f0f8ff';
  
  if (colorPicker) {
    // Only access the 'value' property if the element exists
    colorPicker.value = storedColor || '#f0f8ff';
    colorPicker.addEventListener('input', handleColorPickerChange);
    colorPicker.addEventListener('input', handleColorPickerChange);
  }

});

// Gets called whenever the value in colour picker changes and sets that value to the new stored background colour 
function handleColorPickerChange(event) {
  const selectedColor = event.target.value;
  document.body.style.backgroundColor = selectedColor;
  localStorage.setItem('backgroundColor', selectedColor);
}


function imagePreview(input){
  let filesAmount = input.files.length;
  $('upload-img').html("");

  for(let i = 0; i < filesAmount; i++){
  
    let reader = new FileReader();
    reader.onload = function(event){
        let html = `
            <div class = "container">
                <img src = "${event.target.result}" class ="col img-fluid rounded">
                <button type = "button" class = "btn-close">                 
            </div>
        `;
        $(".upload-img").append(html);
    }
    reader.readAsDataURL(input.files[i]);
  }

  $('.upload-img').css('padding', "20px");
}

// Used to remove stars
function removeActiveStars(container) {
  const stars = container.querySelectorAll(".star");
  stars.forEach(function(star) {
      star.classList.remove("active");
  });
}

// Used to light up stars behind the selected star
function lightUpPreviousStars(star) {
  const stars = star.parentNode.querySelectorAll(".star");
  let selected = false;
  for (let i = stars.length - 1; i >= 0; i--) {
      const s = stars[i];
      if (s === star) {
          selected = true;
      }
      if (selected) {
          s.classList.add("active");
      } else {
          s.classList.remove("active");
      }
  }
}


// Used to define star rating behaviours and call the other functions
document.addEventListener("DOMContentLoaded", function() {
  const stars = document.querySelectorAll(".star");

  stars.forEach(function(star) {
      star.addEventListener("click", function() {
          const value = this.getAttribute("data-value");
          const imageId = this.closest(".rating-box").getAttribute("data-image-id");

          // Send the rating to the server
          // saveRating(imageId, value);

          function getrating(){
            return Int16Array(value)
          }

          // Update UI
          const container = this.closest(".stars");
          removeActiveStars(container);
          this.classList.add("active");
          lightUpPreviousStars(this);
      });
  });
}); 

// Used for previewing images on the createRequest page
document.addEventListener("DOMContentLoaded", function() {
  // Check if the page is createRequest.html
  if (document.title === "Rate My Fit - Post") {
    // Function to handle image upload and preview
    $("#imgUpload").change(function () {
      // Remove previous image previews
      $(".upload-img").empty();

      // Loop through each uploaded file
      for (let i = 0; i < this.files.length; i++) {
        const file = this.files[i];

        // Check if the uploaded file is an image
        if (file && file.type.startsWith("image/")) {
          const reader = new FileReader();

          // Read the uploaded image file and display it as a preview
          reader.onload = function(e) {
            $(".upload-img").append('<img src="' + e.target.result + '" class="img-thumbnail" width="150" />');
          }
          reader.readAsDataURL(file);
        }
      }
    });
  }
});



