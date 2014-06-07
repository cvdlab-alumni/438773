

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

function bouncingLamp(target){

	var bouncing = new TWEEN.Tween(target)
		.to({ x: 70 , y: 2 , z: 0 })
		.easing(TWEEN.Easing.Bounce.In)
		.start();

}

var animator;


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
	bouncingAnimator(bouncingTarget);
}












       