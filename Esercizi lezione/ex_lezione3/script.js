
// Esercizio 1

function pushFirstNatural(array , n){
	
	var i = 0 ;

	for( i = 0 ; i < n ; i++){
		array.push(i);
	}
}


// EX1B

function filterOdd(array){
	var result = array.filter(function(item){
						return item % 2 === 0;
					});
	return result;
}

//EX1C

function doubleEven(array){
	var numbersEven = filterOdd(array);
	var result = numbersEven.map(function(item){
					return item * 2;
				});
	return result;
}

// EX1D

function isDivisibile(array){
	var numbers = doubleEven(array);
	return numbers.filter(function(item){
		return item % 4 === 0;
	})
}

// EX1E

function sumRemainNumber(array){
	var i = 0;
	var numbers = isDivisibile(array);
	var result = 0;

	for(i = 0 ; i < array.length ; i++){
		result += array[i];
	}
	return result;
}

function sumRemainNumber2 (array) {
	return array.reduce(function(item1 , item2){
		return item1 + item2;
	})
}


console.log("Esercizio 1")

var result = [];
console.log(result);

pushFirstNatural(result , 32);
console.log(result);

result = filterOdd(result);
console.log(result);

result = doubleEven(result);
console.log(result);

result = isDivisibile(result);
console.log(result);

result = sumRemainNumber2(result);
console.log(result);


// Esercizio 2

console.log("Esercizio 2")

function pushRandomFirstNatural(array , n){
	
	var i = 0 ;

	for( i = 0 ; i < n ; i++){
		array.push(Math.radom(30));
	}
}



