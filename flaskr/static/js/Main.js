// Main.js 
// The FrontEnd 

function SelectToRegister() {
    document.getElementById("panelLogin").style.display = "none";
    document.getElementById("panelRegister").style.display = "block";
}
function SelectToLogin() {
    document.getElementById("panelLogin").style.display = "block";
    document.getElementById("panelRegister").style.display = "none";
}
function loginAuthCheck(){
    var form = document.forms['loginForm'];
    var backMessage = document.getElementById("loginBackMessage");
    if(form['username'].value == "" & form['password'].value == ""){
        backMessage.style.display = "block";
        backMessage.innerText = "Login Failed\nUsername and Password are not allowed to be empty.";
        return false;
    }else if(form['username'].value == ""){
        backMessage.style.display = "block";
        backMessage.innerText = "Login Failed\nUsername can not be empty!";
        return false;
    }else if(form['password'].value == ""){
        backMessage.style.display = "block";
        backMessage.innerText = "Login Failed\nPassword can not be empty!";
        return false;
    }
}
function registerAuthCheck(){
    var form = document.forms['registerForm'];
    var backMessage = document.getElementById("registerBackMessage");
    if(form['username'].value == ""){
        backMessage.style.display = "block";
        backMessage.innerText = "Register Failed\nUsername can not be empty!";
        return false;
    }else if(form['password'].value == ""){
        backMessage.style.display = "block";
        backMessage.innerText = "Register Failed\nPassword can not be empty!";
        return false;
    }else if(form['repeat_password'].value == ""){
        backMessage.style.display = "block";
        backMessage.innerText = "Register Failed\nRepeat Password can not be empty!";
        return false;
    }else if(form['email'].value == ""){
        backMessage.style.display = "block";
        backMessage.innerText = "Register Failed\n Email can not be empty!";
        return false;
    }else if(form['password'].value != form['repeat_password'].value){
        backMessage.style.display = "block";
        backMessage.innerText = "Register Failed\n The password inputed twice are different!";
        return false;
    }
}
function avatarChecking(){
    var form = document.forms['avatarChanging'];
    if(form['file'].value == ""){
        alert("Empty File are not allowed to update.");
        return false;
    }
}
function displayUploader(){
    var uploader = document.getElementById('mask');
    if(uploader.style.display == "block"){
        uploader.style.display = "none";
    }else{
        uploader.style.display = "block";
    }
}
function uploaderChecking(){
    // Frontend checking.
    var form = document.forms['uploader'];
    if(form['Title'].value == ""){
        alert("Title is not allowed to be empty.");
        return false;
    }else if(form['Description'].value == ""){
        alert("Description is required.");
        return false;
    }else if(form['Picture'].value == ""){
        alert("No file selected!")
        return false;
    }
}
function OpenFullImage(numID){
    let ClassObject = document.getElementsByClassName('displayedImages')[numID - 1];
    let ImageUUID = ClassObject.alt;

    window.open( "/remark/" + ImageUUID);
}

function OpenImageOnNewWindow(){
    let Image = document.getElementById("FullSizeImage");

    window.open(Image.src);
}

function GetUUIDfromVirutalInput(){
    let inputValue = document.getElementById("VirtualInput");
    let postUUID = document.getElementById("FullSizeImage");
    inputValue.value = postUUID.alt;
}

GetUUIDfromVirutalInput();

function ReplyTo(numID){
    scrollTo(0,0);
    let ReplyTo = document.getElementsByClassName("Reply")[numID - 1];
    let ReplyToUser = document.getElementsByClassName("ReplyToUser")[numID - 1];
    let ReplyToDate = document.getElementsByClassName("ReplyToDate")[numID - 1];
    let InputValueOfReplyTo = document.getElementById("ReplyTo");
    let InputValueOfReplyToUser = document.getElementById("ReplyToUser");
    let InputValueOfReplyToDate = document.getElementById("ReplyToDate");
    InputValueOfReplyTo.value = ReplyTo.value;
    InputValueOfReplyToUser.value = ReplyToUser.innerText;
    InputValueOfReplyToDate.value = ReplyToDate.innerText;

    SendComments();
}

function SendComments() {
    scrollTo(0,0);
    var Commenter = document.getElementById('mask');
    if(Commenter.style.display == "block"){
        Commenter.style.display = "none";
    }else{
        Commenter.style.display = "block";
    }
}
function ClearReply(){
    let InputValueOfReplyTo = document.getElementById("ReplyTo");
    let InputValueOfReplyToUser = document.getElementById("ReplyToUser");
    let InputValueOfReplyToDate = document.getElementById("ReplyToDate");
    InputValueOfReplyTo.value = "";
    InputValueOfReplyToUser.value = "";
    InputValueOfReplyToDate.value = "";
}