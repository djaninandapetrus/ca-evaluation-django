// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function() {
    // Add event listeners to sections for smooth scrolling
    var sections = document.querySelectorAll("section");
    sections.forEach(function(section) {
      section.addEventListener("click", function() {
        smoothScroll(section.id);
      });
    });
    
    // Smooth scroll to a section
    function smoothScroll(sectionId) {
      var target = document.getElementById(sectionId);
      window.scrollTo({
        top: target.offsetTop,
        behavior: "smooth"
      });
    }
  });