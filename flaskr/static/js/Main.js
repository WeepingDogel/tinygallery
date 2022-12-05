// The JavaScript File

function Hi(){
    alert("Under Development.");
}
function Register(){
    document.getElementById("Panel_Login").style.display = "none";
    document.getElementById("Panel_Register").style.display = "block";
}
function loginPage(){
    document.getElementById("Panel_Register").style.display = "none";
    document.getElementById("Panel_Login").style.display = "block";
}
function SignUP(){
    var username = document.forms['registerForm']['userName_Register'].value;
    var password = document.forms['registerForm']['passWord_Register'].value;
    var password_repeat = document.forms['registerForm']['passWord_Repeat'].value;
    var email = document.forms['registerForm']['Email'].value;
    if(username == "" | username == null){
        alert("用户名不得为空! 一切不得为空，否则禁止注册！");
        return false;
    }else if(password == "" | password == null){
        alert("密码不得为空! 一切不得为空，否则禁止注册！");
        return false;
    }else if(password_repeat == "" | password_repeat == null){
        alert("重复密码不得为空! 一切不得为空，否则禁止注册！");
        return false;
    }else if(email == "" | email == null){
        alert("邮箱不得为空! 一切不得为空，否则禁止注册！");
        return false;
    }
}

function SignIn(){
    var username = document.forms['loginForm']['username'].value;
    var password = document.forms['loginForm']['password'].value;
    if(username == "" | username == null){
        alert("用户名不得为空!");
        return false;
    }else if(password == "" | password == null){
        alert("密码不得为空！");
        return false;
    }else{
        window.location.replace("/index");
    }
}