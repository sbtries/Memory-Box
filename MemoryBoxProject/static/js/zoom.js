// hovering album images
function hover(element) {
    element.setAttribute('src', '{% static 'images/open-box.png' %}');
  }
  function unhover(element) {
    element.setAttribute('src', 'http://dummyimage.com/100x100/000/fff');
  }
