// The JavaScript File

function Hi(){
    alert("Under Development.");
}

function Switch_Form(form_ID1, form_ID2){
    var ElementToDisplay = document.getElementById(form_ID1);
    var ElementToHide = document.getElementById(form_ID2);
    ElementToDisplay.style.display = "block";
    ElementToHide.style.display = "none";
    console.log("User changed the form mode.");
    return 0;
}