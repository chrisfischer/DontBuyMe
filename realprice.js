var savingsArray = [];
var savingsCount = 0;
var priceArray = [];
var itemNames = document.getElementsByClassName("a-size-medium sc-product-title a-text-bold");

$(document).ready(function() {
	if(priceArray.length > 0) calcSavings();
	var checkDelete = function () {
	    var deletes = document.getElementsByClassName("a-size-small sc-action-delete");
		for(var j = 0; j < deletes.length; j++)
		{
			deletes[j].addEventListener("click", function() {
				var totalElem = document.getElementsByClassName("a-size-medium a-color-price sc-price sc-white-space-nowrap  sc-price-sign");
				var price = totalElem[0].innerHTML;
				priceArray[savingsCount] = price;
				calcSavings();
				/*animate();*/
			});
		}
	}
	checkDelete();
});

function calcSavings() {
	var totalElem = document.getElementsByClassName("a-size-medium a-color-price sc-price sc-white-space-nowrap  sc-price-sign");
	if(totalElem.length > 0) {
		var newString = totalElem[0].innerHTML;
		var newprice = parseFloat(newString.substring(1, newString.length));
		console.log(newprice);

		var today = new Date();
		var dd = today.getDate();
		var mm = today.getMonth() + 1;
		var yyyy = today.getFullYear();
		if(dd < 10) { dd = '0' + dd 
		}
		if(mm < 10) { mm = '0' + mm
		}
		today = yyyy + '-' + mm + '-' + dd;

		var itemArray = [];
		var itemsLeft = document.getElementsByClassName("a-size-medium sc-product-title a-text-bold");
		var pricesLeft = document.getElementsByClassName("a-size-medium a-color-price sc-price sc-white-space-nowrap sc-product-price sc-price-sign a-text-bold");
		var itemPrice = 0;
		for(var m = 0; m < pricesLeft.length-1; m++) {
			if(pricesLeft[m].hidden == false) {
				priceString = pricesLeft[m].innerText;
				itemPrice = itemPrice + parseFloat(priceString.substring(1,priceString.length));
			}
		}

		for(var k = 0; k < itemsLeft.length; k++)
		{
			itemArray[k] = itemsLeft[k].innerHTML;
		}
		var itemName = "";
		for(var i = 0; i < itemNames.length; i++)
		{
			if(itemArray.indexOf(itemNames[i].innerHTML) < 0) {
				itemName = itemNames[i].innerHTML;
			}
		}
		var actualPrice = Math.round((newprice - itemPrice)*100)/100;
		savingsArray.push({date:today, vendor:'AMAZON.COM', price:actualPrice});
		console.log(savingsArray);
		savingsCount++;
		postData(savingsArray);
	}
}

function postData(array) {

    for(var i = 0; i < array.length; i++) {
	    const d = array[i];
	    var jsondata = JSON.stringify({
				'date': d.date,
	        	'vendor': d.vendor,
	        	'price': d.price
		});
		$.ajax({
			url: 'https://nessie-credit.herokuapp.com/api',
			type: 'POST',
			data: {
				'date': d.date,
	        	'vendor': d.vendor,
	        	'price': d.price,
	        	'key': '896c897b5f52485fd3e9b049b4af1cc5',
	        	'account': '5a5796596514d52c7774a389'
			},
			success: function(d) {
				alert("YAY!");
			}
		
	});
}};

function animate() {
	console.log("CREATING ELEMENT");

	var btn = document.createElement("BUTTON");        // Create a <button> element
	btn.innerHTML = '<img src="http://bbcpersian7.com/images/images-of-an-arrow-1.jpg" />';
	btn.style.width = '10%';                                // Append the text to <button>
	document.body.appendChild(btn); 
	var pos = 0;
	var id = setInterval(frame, 5);
	function frame() {
	    if (pos == 350) {
	      clearInterval(id);
	    } else {
	      pos++; 
	      btn.style.top = pos - 'px'; 
	      btn.style.left = pos - 'px'; 
	    }
	  }

	console.log("MOVING BUTTON");
}
