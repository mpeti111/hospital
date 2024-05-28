document.addEventListener('DOMContentLoaded', function(){
const loader = document.querySelector('.loader');
const content = document.querySelector('.content');

loader.addEventListener('animationend', function(){
    content.style.opacity = '1';                        
    });            
    
const regBtn = document.getElementById('register-btn');
const logBtn = document.getElementById('login-btn');
const regForm = document.getElementById('register-form');
const logForm = document.getElementById('login-form');

regBtn.addEventListener('click', function(){
    regForm.style.display = 'block';
    logForm.style.display = 'none';
    content.style.display = 'none';
    });
logBtn.addEventListener('click', function(){
    regForm.style.display = 'none';
    logForm.style.display = 'block';
    content.style.display = 'none';
    });
});

document.getElementById('register-sub').addEventListener('click', function(event){
    event.preventDefault();
    var firstName = document.getElementById('firstName').value;
    var lastName = document.getElementById('lastName').value;
    var phone = document.getElementById('phone').value;
    var login = document.getElementById('login').value;
    var password = document.getElementById('pass').value;
        
    var userData = {
        firstname: firstName,
        lastname: lastName,
        phone: phone,
        username: login,
        password: password
    };
    
    fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
    })
    .then(response => {
        if (response.ok){
            alert('Registration was successful');
            window.location.href = '../user.html';
        }
        else{
            return response.text();
        }
    })
    .catch(error => console.error('Error', error));
});

document.getElementById('login-sub').addEventListener('click', function(event){
     event.preventDefault();
    var userLogin = document.getElementById('user-login').value;
    var userPassword = document.getElementById('user-pass').value;
    
    var loginData = {
        login: userLogin,
        password: userPassword
    };
fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(loginData)
    })
    .then(response => {
        if (response.ok){
            if (response.status == 200){
                alert ('Log in succeffsul');
                window.location.href = '/doctor.html';
            }
            else if (response.status == 201){
                alert ('Log in succeffsul');
                window.location.href = '/user.html';
        }
        else{
            return response.text();
        }
        }
    })
    .then(errorMsg => {
        if (errorMsg){
            alert ('Error registration' + errorMsg)
        }
})
    .catch(error => console.error('Error', error));
});