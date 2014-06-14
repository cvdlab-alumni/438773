

function Door(width , height , options){

  this.width = width;
  this.height = height;
  //this.texture = texture;
  this.options = options;
  this.mesh;
  this.hinge;

  Door.prototype.open = function (){

    var openTween = new TWEEN.Tween(this.hinge.rotation)
      .to({y : Math.PI/2} , 1000)
      .easing(TWEEN.Easing.Linear.None)
      .start();
  };

  Door.prototype.close = function (){

    var closeTween = new TWEEN.Tween(this.hinge.rotation)
      .to({y : 0} , 1000)
      .easing(TWEEN.Easing.Linear.None)
      .start();
  }

  Door.prototype.openAndClose = function (){

    var closeTween = new TWEEN.Tween(this.hinge.rotation)
      .to({y : 0} , 1000);

    var openTween = new TWEEN.Tween(this.hinge.rotation)
      .to({y : Math.PI/2} , 1000);

    var openCloseTween = new TWEEN.Tween(this.hinge.rotation)
      .chain(openTween)
      .delay(1000)
      .chain(closeTween)
      .start();
  }

  Door.prototype.createHinge = function (){

    var hinge = new THREE.Object3D();

    hinge.add(this.mesh);

    this.hinge = hinge;
  }

  Door.prototype.createMesh = function (){

    var doorGeometry = new THREE.BoxGeometry(width,height,1);
    var doorMaterial = new THREE.MeshLambertMaterial(options)
    var door = new THREE.Mesh(doorGeometry , doorMaterial);
    door.castShadow = true;
    door.position.y = height/2;
    door.position.x = width/2;

    this.mesh = door;
  }
  
}