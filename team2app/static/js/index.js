// document.addEventListener('DOMContentLoaded', function() {
//     var pageTop = document.getElementById('page_top');
//     pageTop.addEventListener('click', function(e) {
//         e.preventDefault();
//         window.scrollTo({ top: 0, behavior: 'smooth' });
//     });
// });

jQuery(function() {
    var appear = false;
    var pagetop = $('#page_top');
    $(window).scroll(function () {
      if ($(this).scrollTop() > 100) {  
        if (appear == false) {
          appear = true;
          pagetop.stop().animate({
            'bottom': '40px' 
          }, 300); 
        }
      } else {
        if (appear) {
          appear = false;
          pagetop.stop().animate({
            'bottom': '-120px' 
          }, 350);
        }
      }
    });
    pagetop.click(function () {
      $('body, html').animate({ scrollTop: 0 }, 500); 
      return false;
    });
  });