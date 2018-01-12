// Regex-pattern to check URLs against.
// It matches URLs like: http[s]://[...]stackoverflow.com[...]

var p = document.getElementsByClassName("sc-price");

for (var i = 0; i < p.length; i++) {
	var realValue = "$100.00"
	var addText = document.createElement('span');
	addText.setAttribute('class', 'real-price');
	addText.style.cssText = 'text-decoration: none !important;font-weight: bold;left:300px;color: green;';
	addText.innerHTML = realValue;
	p[i].style.cssText = 'text-decoration: line-through;'
	p[i].parentNode.appendChild(addText);
}
