
// Esercizio 1

var first = 1;
var i;
var j;

result = " "
for(i = 1 ; i <= 10 ; i++){
		result += "\n"
	for(j = 1; j <= 10 ; j++){
		result += i*j + "\t";
	}	
}

document.getElementById("ex1").innerHTML = result;
alert(result);

// Esercizio 2

result2 = " "
for(i = 1 ; i <= 10 ; i++){
		result2 += "\n"
	for(j = 1; j <= 10 ; j++){
		 j !== 10 ? result2 += i*j + ",\t" : result2 += i*j + "\t"; 	
	}	
}

document.getElementById("ex2").innerHTML = result2;

// Esercizio 3

result3 = " "
for(i = 1 ; i <= 10 ; i++){
		result3 += "\n"
	for(j = 1; j <= 10 ; j++){
		 j !== i ? result3 += 0 + ",\t" : result3 += 1 + ",\t"; 	
	}	
}

document.getElementById("ex3").innerHTML = result3;




