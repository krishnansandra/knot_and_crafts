// small UX enhancements
document.addEventListener('DOMContentLoaded', function(){
  // smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(a=>{
    a.addEventListener('click', e=>{
      e.preventDefault();
      document.querySelector(a.getAttribute('href')).scrollIntoView({ behavior:'smooth' });
    })
  })
})
