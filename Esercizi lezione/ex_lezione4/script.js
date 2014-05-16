
// Esercizio 2

// EX04

function select(data, key, values){
	
	var result = data.filter(function(item1){
		return values.some(function(item2){
			return item1[key] === item2;
		});
	});
	return result;
}

// test

var data = [  {id:'01', name:'duffy'},  
		{id:'02', name:'michey'}, 
		{id:'03', name:'donald'},  
		{id:'04', name:'goofy'},  
		{id:'05', name:'minnie'},  
		{id:'06', name:'scrooge'} ]; 

var key = 'name';
var values = ['goofy', 'scrooge'];

select(data, key, values);


// EX05

function randomizeTree(){
	
	var i = 0;
	var number = 0;
	var random_num ;

	for( i = 0; i < 3; i++){
		random_num = Math.random(100);
		if random_num > number ? number = random_num : number = number;
	}
	return number;
}

randomizeTree();



















