
function EventEmitter(){
	this.handlers = {};
}

EventEmitter.prototype.on = function( event , handler){
	var handlers_list = this.handlers[event];
	
	if(handlers_list === undefined){
		handlers_list = this.handlers[event] = [];
	}

	handlers_list.push(handler);
};

EventEmitter.prototype.emit = function( event ){
	var handlers_list = this.handlers[event];
	
	if ( handlers_list === undefined){
		return;
	}

	handlers_list.forEach(function(handler){
		handler();
	});
};


function Shape (x, y) {
	EventEmitter.call(this);
	this.x = x;
	this.y = y;
}

Shape.prototype = Object.create(EventEmitter.prototype);
Shape.prototype.constructor = Shape;

Shape.prototype.move = function (x, y) {
    this.x += x;
    this.y += y;
    this.emit('moved');
};

Shape.prototype.info = function () {
  console.log('x: ', this.x, ', y: ', this.y);
};


// definizione logger

function Logger(){
}

Logger.prototype.show_long_message = function(shape){
	console.log("Print shape's info " + shape.info());
}

Logger.prototype.show_short_message = function(shape){
	console.log("Print shape short");
}

// ------ 

var shape_emit = new Shape(2, 5);

shape_emit.on('moved', function(){
	//console.log('do something...');
	var logger = new Logger();
	logger.show_short_message();
});

shape_emit.on('moved' , function(){
	//console.log('do something else...');
	var logger = new Logger();
	logger.show_long_message(shape_emit);
});

shape_emit.move(6, 7);
