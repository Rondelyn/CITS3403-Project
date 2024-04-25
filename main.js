/* Used to toggle the login page to the signup view */
function showsignup(){
    document.getElementById('signup form').style.display="block";
    document.getElementById('login form').style.display="none"; 
}
  
/* Used to toggle the login page to the login view */
function showlogin(){
    document.getElementById('login form').style.display="block";
    document.getElementById("signup form").style.display="none"; 
}

/* Function to validate login criteria */
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

/* Function to validate signup criteria */
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
    
    showlogin();
    return;
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






