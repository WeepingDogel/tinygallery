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

var winX = null;
var winY = null;
window.addEventListener('scroll',
function () { 
    if (winX !== null && winY !== null) { 
        window.scrollTo(winX, winY); 
    } 
});

function disableWindowScroll() { 
    winX = window.scrollX; winY = window.scrollY; 
}

function enableWindowScroll() { 
    winX = null; winY = null; 
}


function displayUploader(){
    var uploader = document.getElementById('mask');
    if(uploader.style.display == "block"){
        uploader.style.display = "none";
        enableWindowScroll();
    }else{
        uploader.style.display = "block";
        disableWindowScroll();
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
    let InputValueOfReplyTo = document.getElementById("ReplyTo");
    let InputValueOfReplyToUser = document.getElementById("ReplyToUser");
    InputValueOfReplyTo.value = ReplyTo.value;
    InputValueOfReplyToUser.value = ReplyToUser.innerText;

    SendComments();
}

function SendComments() {
    scrollTo(0,0);
    var Commenter = document.getElementById('mask');
    if(Commenter.style.display == "block"){
        Commenter.style.display = "none";
        enableWindowScroll();
    }else{
        Commenter.style.display = "block";
        disableWindowScroll();
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


function SendLikedData(numID, LikeStatus){
    xmlhttp = new XMLHttpRequest();
    let LikeButton = document.getElementsByClassName("likeStatus0")[numID - 1];
    let unlikeButton = document.getElementsByClassName('likeStatus1')[numID - 1];
    let ImageUUID = document.getElementsByClassName('displayedImages')[numID - 1];
    let LikesNum = document.getElementsByClassName('LikesNum')[numID - 1];

    if(LikeStatus == "Like"){
        LikeButton.style.display = "none"
        xmlhttp.open('GET','/action/likeCheck?UUID=' + ImageUUID.alt + "&LikeStatus=1", true);
        xmlhttp.send();

    }else if(LikeStatus == 'Unlike'){
        unlikeButton.style.display = "none"
        xmlhttp.open('GET','/action/likeCheck?UUID=' + ImageUUID.alt + "&LikeStatus=0", true);
        xmlhttp.send();
    }

    xmlhttp.onreadystatechange=function(){

        if (xmlhttp.readyState==4 && xmlhttp.status==200){
            JsonData = JSON.parse(xmlhttp.response);
            if(JsonData.Status == 1){
                unlikeButton.style.display = "inline";
                LikesNum.innerText = "Likes:" + JsonData.Dots;
            }else if(JsonData.Status == 0){
                LikeButton.style.display = "inline";
                LikesNum.innerText = "Likes:" + JsonData.Dots;
            }
        }

    }
}

function SendLikedDataInFullImage(ImageUUID,LikeStatus){
    xmlhttp = new XMLHttpRequest();
    let LikeButton = document.getElementById('likeStatus0');
    let unlikeButton = document.getElementById('likeStatus1');
    let likesNum = document.getElementById('likesNum');

    if(LikeStatus == 'Like'){
        LikeButton.style.display = "none";
        xmlhttp.open('GET','/action/likeCheck?UUID=' + ImageUUID + "&LikeStatus=1", true);
        xmlhttp.send();
    }else if(LikeStatus == 'Unlike'){
        unlikeButton.style.display = "none"
        xmlhttp.open('GET','/action/likeCheck?UUID=' + ImageUUID + "&LikeStatus=0", true);
        xmlhttp.send();
    }
    xmlhttp.onreadystatechange=function(){

        if (xmlhttp.readyState==4 && xmlhttp.status==200){
            JsonData = JSON.parse(xmlhttp.response);
            if(JsonData.Status == 1){
                unlikeButton.style.display = "inline";
                likesNum.innerText = "Likes:" + JsonData.Dots;
            }else if(JsonData.Status == 0){
                LikeButton.style.display = "inline";
                likesNum.innerText = "Likes:" + JsonData.Dots;
            }
        }

    }
}

function deleteAccount(){
    confirming = window.confirm('Are you sure for that? It will also delete your publishment, comments and everything!');
    if(confirming == true){
        window.location.replace('/auth/deleteAccount');
    }
}