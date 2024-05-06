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

// Function to validate login criteria
function validatelogin(){
  event.preventDefault();
  var username = $('#InputUsername').val();
    var password = $('#Password').val();
    var termsagreed = $('#termsandconditions').is(':checked');

   
    if (username === '' || password === ''){
      alert("username or password is missing")
      return;
    }
    
    if (!termsagreed){
      alert("agree to terms and conditions or else");
      return;
      
    }
    
    alert("yay");
    return;
}

// An event listener that takes place upon page load and sets the background of the page to the stored value otherwise sets it to alice blue by default 
document.addEventListener('DOMContentLoaded', function() {
  const colorPicker = document.getElementById('myColor');
  const storedColor = localStorage.getItem('backgroundColor');

  document.body.style.backgroundColor = storedColor || '#f0f8ff';

  colorPicker.value = storedColor || '#f0f8ff';

  colorPicker.addEventListener('input', handleColorPickerChange);
});

// Gets called whenever the value in colour picker changes and sets that value to the new stored background colour 
function handleColorPickerChange(event) {
  const selectedColor = event.target.value;
  document.body.style.backgroundColor = selectedColor;
  localStorage.setItem('backgroundColor', selectedColor);
}

// Function to validate signup criteria 
function validatesignup(){
  event.preventDefault();
  var username = $('#signInputUsername').val();
    var password = $('#signPassword').val();
    var termsagreed = $('#signtermsandconditions').is(':checked');

   
    if (username === '' || password === ''){
      alert("username or password is missing")
      return;
    }

    if (password.length <= 4){
      alert("password must have more than 4 characters")
      return;

    }
    

    if (!termsagreed){
      alert("agree to terms and conditions or else");
      return;
      
    }
    
    showLogin();
    return;
}

// this function is called to redirect to the signup view of the login page
function redirectToSignup() {
  window.location.href = "/login?signup=true"; 
}

// This function determines the view of the login page
document.addEventListener("DOMContentLoaded", function() {
  var signup = document.body.getAttribute("data-signup");
  
  function showSignupForm() {
      if (signup === 'true') {
          showSignup();
      } else {
          showLogin();
      }
  }
  
  showSignupForm();
});



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

          const container = this.closest(".stars");
          removeActiveStars(container);
          this.classList.add("active");
          lightUpPreviousStars(this);
      });
  });
}); 


