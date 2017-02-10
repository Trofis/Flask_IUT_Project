var indice = 0
function photo(lImage,x) {
		// givig the value of time the samfunction below starts the loop
	var image = document.getElementById('image');
	if(x == 1 && indice == lImage.length-1){indice = max;}
	if(indice == 0 && x == -1){indice = 0;}
	else{indice += x;}
	res = "static/images/"+lImage[indice];
	image.setAttribute("src", res);
}
