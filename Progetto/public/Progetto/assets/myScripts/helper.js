

function loadObjModel(obj_name , texture_name){

  var obj_model = null;
  var loader = new THREE.OBJLoader();
  loader.load("assets/obj_models/" + obj_name, function (obj) {

    var texture = THREE.ImageUtils.loadTexture("assets/textures/" + texture_name);
    var material = new THREE.MeshPhongMaterial();
    material.map = texture;

    obj.traverse(function (child) {
      if (child instanceof THREE.Mesh) {
        child.material = material;
      }
    });

    obj_model = obj;
  });

  return obj_model;
}