

var alfaTarget = -Math.PI/2; 
var time = 2000;  

function turnLightLamp(target1 , target2 , directionalLight){

	var turnBack = new TWEEN.Tween(target2)
		.to({ y: alfaTarget} , 3000); 

	var turnLeft = new TWEEN.Tween(target2)
		.to({ y: alfaTarget*2/3} , 3000);

	var downLight = new TWEEN.Tween(target1)
		.to({ x: alfaTarget } , time)
		.easing(TWEEN.Easing.Circular.Out)
		.chain(turnLeft)
		.start();

	var turnRight = new TWEEN.Tween(target2)
		.to({ y: -alfaTarget} , 3000)
		.easing(TWEEN.Easing.Circular.Out)
		.delay(1000)
		.start();
}

function lightIntensity(directionalLight){

	directionalLight.intensity = 0.7;
}

function turnBackLamp(target){


  var turnLeft = new TWEEN.Tween(target)
    .to({ y: -alfaTarget*2/3} , time);

  var turnBack = new TWEEN.Tween(target)
    .to({ z: -alfaTarget*2.6 } , time)
    .easing(TWEEN.Easing.Circular.Out)
    .start();
}

var animator = null;
var animator3 = null;
function bouncingAnimator(base , l) {
    
  animator = new KF.KeyFrameAnimator;
  animator.init({ 
    interps:
      [
        { 
          keys:[0, .2, .4 , .6 , .8, 1], 
          values:[
            { x : 0 },
            { x : 14 },
            { x : 28 },
            { x : 42 },
            { x : 56 },
            { x : 80 },

          ],
          target: base.position
        },
        {
          keys:[0, .2, .4 , .6 , .8, 1], 
          values:[
            { y : 2 },
            { y : 100 },
            { y : 2 },
            { y : 100 },
            { y : 2  },
            { y : 90 },
          ],
          target: base.position
        },
        {
          keys:[0, .2, .4 , .6 , .8, 1], 
          values:[
            { z : 150 },
            { z : 120  },
            { z : 90 },
            { z : 60 },
            { z : 30 },
            { z : 16 },
          ],
          target: base.position
        },
      ],
    loop: false,
    easing: TWEEN.Easing.Bounce.Out,
    duration: 3000
  });

  animator3 = new KF.KeyFrameAnimator;
  animator3.init({ 
    interps:
      [
        {
          keys:[0, .1 , .2 , .3 , .4 , .5 , .6 , .7 , .8, 1], 
          values:[
            { y : 90 },
            { y : 150 },
            { y : 90 },
            { y : 150 },
            { y : 90 },
            { y : 150 },
            { y : 90 },
            { y : 150 },
            { y : 10  },
            { y : 10 },
          ],
          target: base.position
        },
        {
          keys:[0, .4 , .6 , .7 , .8, 1], 
            values:[
              { y :  1 },
              { y :  1 },
              { y :  1 },
              { y :  1 },
              { y :  .1 },
              { y :  .1 },
              { y : .1 },
            ],
            target: l.scale
        }
      ],
    loop: false,
    easing: TWEEN.Easing.Quadratic.In,
    duration: 2000
  });
}

function getAnimator(){
    
    return animator.start();
}


/*
//define animations
      var animator = null;
      var duration = 4; // sec
      var loopAnimation = false;

      function initAnimator() {
        animator = new KF.KeyFrameAnimator;
        animator.init({ 
          interps:
            [
              { 
                keys:[0, .2, 1],     //a tempo 0 z vale o, al 20% z vale Math.PI, alla fine vale Math.PI*2 (è un array, posso 
                					   mettere quanti valori voglio)
                values:[
                  { z : 0 },
                  { z : Math.PI  },
                  { z : Math.PI * 2 },
                ],
                target:cube.rotation 	//Qui gli dico che questa animazione interessa il cubo
              },						//Per ogni target posso definire un oggetto di questo tipo, per animare contemporaneamente
              							più oggetti
			  { 
                keys:[0, .3, .8, 1],     
                values:[
                  { z : 0 },
                  { z : Math.PI  },
                  { z : Math.PI * 2 },
                ],
                target:cube.rotation 	
              },		
            ],
          loop: loopAnimation,
          duration: duration * 1000,
          easing: TWEEN.Easing.Bounce.Out
        });
      }

      initAnimator();

      // call the render function
      render();
      animator.start();

      function render() {
        stats.update();
        trackballControls.update();
        KF.update();

        ...
      }
 */

function startAnimation(target1 , target2 , bouncingTarget){

	turnLightLamp(target1 , target2);
	//lightIntensity(directionalLight);
	//bouncingLamp(bouncingTarget);
}












       