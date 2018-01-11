// Regex-pattern to check URLs against. 
// It matches URLs like: http[s]://[...]stackoverflow.com[...]

var p = document.getElementsByClassName("sc-price");
console.log(p);

for (var i = 0; i < p.length; i++) {
	var realValue = "$100.00"
	var addText = document.createElement('span');
	addText.setAttribute('class', 'real-price');
	addText.innerHTML = realValue;
	p[i].parentNode.appendChild(addText);
}