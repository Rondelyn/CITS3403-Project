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



