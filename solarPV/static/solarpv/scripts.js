function showContent (id) {
	var all = document.getElementsByClassName('tabCopy');
	for (var i = 0; i < all.length; i++) {
	    all[i].classList.remove('selected');
	    if (all[i].id === id) {
	    	all[i].classList.add('selected');
	    }
	}
}

function nextSlide (direction) {
	var all = document.getElementsByClassName('slide');
	var activeIndex = 0;

	for (var i = 0; i < all.length; i++) {
		if (all[i].classList.contains('active')) {
			activeIndex = i;
		}
	    all[i].classList.remove('active');
	}

	var newActiveIndex = activeIndex + direction;

	if (newActiveIndex > all.length - 1) {
		newActiveIndex = 0;
	}

	if (newActiveIndex < 0) {
		newActiveIndex = all.length - 1;
	}

	all[newActiveIndex].classList.add('active');
}

function validateField () {
	var field = event.target;
	var name = field.name;
	var value = field.value;
	var isValid = true;
	switch(name) {
	  case 'password':
	    isValid = (/^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{8,})/).test(value);
	    break;
	  case 'username':
	    isValid = value.length <= 8;
	    break;
      case 'streetaddress':
      case 'city':
      case 'state':
	  case 'zipcode':
	  case 'phonenum':
	  	isValid = (/^(?=.*[0-9])/).test(value);
	  	break;
	  case 'firstname':
	  case 'lastname':
	  case 'middlename':
	  	break;
	  default:
	  	isValid = !!value;
	}
	if (isValid) {
		field.classList.remove('invalid');
	} else {
		field.classList.add('invalid');
	}
}

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
   alert("Geolocation is not supported by this browser.");
  }
}

function showPosition(position) {
	var latlon = position.coords.latitude + "," + position.coords.longitude;
	alert('Thanks for visiting from ' + latlon);
}

function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  ev.target.appendChild(document.getElementById(data));
}
