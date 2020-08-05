$(document).ready(function(){
  var regBtn = $(".register");
  var regMask = $(".reg-mask");
  var logBtn = $(".login-redirect span")
  
  regBtn.click(function(){
    regMask.addClass("show-reg-mask");
  });
  
  logBtn.click(function(){
    regMask.removeClass("show-reg-mask");
  });
});