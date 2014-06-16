

function loadObjModel(obj_name , texture_name , scene , options){

   obj_model = null;
  var loader = new THREE.OBJLoader();
  loader.load("assets/obj_models/" + obj_name, function (obj) {

    var texture = THREE.ImageUtils.loadTexture("assets/textures/" + texture_name);
    var material = new THREE.MeshLambertMaterial({color: 0xffffff, shading: THREE.FlatShading});
    //var material = new THREE.MeshPhongMaterial();
    //material.map = texture;

    obj.traverse(function (child) {
      if (child instanceof THREE.Mesh) {
        child.material = material;
      }
    });

    obj_model = obj;
    obj.scale.set(20, 20, 20);
    obj.position.set(10,10,10);
    obj.rotation.x = -0.3;
    scene.add(obj);
  });
}