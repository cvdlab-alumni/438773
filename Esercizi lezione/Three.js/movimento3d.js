<!DOCTYPE html>
<html>
 <head> 
  <title>Example 1 - Basic skeleton</title> 
  <style>
    body{
      margin: 0;
      overflow: hidden;
    }
  </style> 
  </head> 
  <body>
    <!-- JavaScript libraries -->
    <script src="assets/libs/three.min.js"></script> 
    <script src="assets/libs/jquery.min.js"></script> 
    <script src="assets/libs/Stats.min.js"></script>
    <script src="assets/libs/dat.gui.min.js"></script>
    <script src="assets/libs/TrackballControls.js"></script>

    <!-- Javascript code that runs our Three.js examples --> 
    <script>
      // once everything is loaded, we run our Three.js stuff.
      $(  

        function () {
		
          var w_p = 60;
          var h_p = 30;
          var a1 = Math.PI/6;
          var a2;
          var a3;
          var r1 = 2;
          var r2 = 2;

      		var scene = new THREE.Scene()
      		
      		var camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
          camera.position.set(-60,20,30);
          camera.up = new THREE.Vector3(0,1,0);
          camera.lookAt(scene.position);

          var inspectedCamera = new THREE.PerspectiveCamera(10, window.innerWidth / window.innerHeight, 10, 1);

          var trackballControls = new THREE.TrackballControls(camera);

          var axisHelper = new THREE.AxisHelper(3);

      		var renderer = new THREE.WebGLRenderer();
          renderer.setClearColor(new THREE.Color(0xEEEEEE));
          renderer.setSize(window.innerWidth, window.innerHeight);

          var plane1 = generateObject3D(15);
          var plane2 = generateObject3D(15);

          var pin1 = generatePivot(15 , plane1);
          var pin2 = generatePivot(30 , plane2)

          pin1.add(pin2);

          scene.add(camera);
          scene.add(pin1);
          scene.add(axisHelper);

          var controls = new function() {
            this.alfa_y_pin1 = a1;
            this.alfa_y_pin2 = a1;
          }

          var gui = new dat.GUI();
          gui.add(controls, 'alfa_y_pin1',0,Math.PI).onChange(function (e){
            pin1.rotation.y = e;
          });
          gui.add(controls , 'alfa_y_pin2',0,Math.PI).onChange(function (e){
            pin2.rotation.y = e;
          });

          $('body').append(renderer.domElement)
          
          animation();

          function animation(){

            trackballControls.update();
            requestAnimationFrame(animation);
            renderer.render(scene, camera);
          }

          function generateObject3D(a_transl){
            var planeGeometry = new THREE.CylinderGeometry(r1,r2,20,20);
            var planeMaterial = new THREE.MeshBasicMaterial({color: 0x2E8B57});
            var cylinder = new THREE.Mesh(planeGeometry,planeMaterial);
            
            cylinder.rotation.x=-0.5*Math.PI;
            cylinder.position.set(a_transl,0,0);

            return cylinder;
          }

          function generatePivot(a_transl,toAdd){
            var pinGeometry = new THREE.SphereGeometry(1,20,20);
            var pinMaterial = new THREE.MeshBasicMaterial({color: 0xFFBF00})
            var pin = new THREE.Mesh(pinMaterial,pinGeometry);

            pin.position.set(a_transl,0,0);
            //pin1.rotation.y = a1;
            pin.add(toAdd);

            return pin;
          }

          function createArm(){
            
          }

         });
    </script>  
 </body>
</html>
