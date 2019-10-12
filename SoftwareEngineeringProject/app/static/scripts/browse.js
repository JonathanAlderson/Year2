$(document).ready(function()
{
  function openNav() {
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
  }

  function closeNav() {
    document.getElementById("mySidebar").style.width = "0px";
    document.getElementById("main").style.marginLeft= "0";
  }

  function changeColour() {
    document.getElementById("button").style.backgroundColor = "red";
  }


});
