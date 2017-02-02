var indice = 0
function photo(lImage,x, max) {
		// givig the value of time the samfunction below starts the loop
	var image = document.getElementById('image');
	if(x > max){indice = max;}
	if(indice == 0){indice = 0;}
	image.src = lImage[indice];
}
