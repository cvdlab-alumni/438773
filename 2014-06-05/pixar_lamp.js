  // once everything is loaded, we run our Three.js stuff.
      $(  

        function () {
		      
          /////////////////////////////
          // Configurations Variables
          // STANLEY
          /////////////////////////////

          //Camera
          var cameraX = 0;
          var cameraY = 200;
          var cameraZ = 500;
          var lookUpVector = new THREE.Vector3(0,1,0);

          //Pivot Angle
          var alfaTo = Math.PI*2;
          var betaTo = Math.PI/2;
          var gammaTo = Math.PI/2;
          var gamma2To = Math.PI*2;
          var epslonTo = Math.PI/2;

          //Variables's arm
          var rTop = 2;
          var rBottom = 2;
          var heightArm = 20;
          var segmentO = 20;

          //Variables's base
          var rTopBase = 15;
          var rBottomBase = 15;
          var heightBase = 2;

          //Variables's pivot
          var radius = 2;

          //Variables's lamp
          var r1 = 5;
          var r2 = 7;
          var r3 = 15; 
          var heightCono = 10;

          //Phong Options
          var phongOptions = { 
                               specular: 0xffffff, 
                               color: 0x3399ff, 
                               shininess: 100, 
                               metal: true
                             };

          var angleRotate = Math.PI/2;

          // Light
          var intensityDirectional = 0.7;
          var intensityLamp = 2.5;
          var castShadowDirectional = true;
          var castShadowLamp = false;
          var pointColorLightLamp = 0xADD8E6;
          var pointColorDirectional = 0xffffff; 

          /////////////////////////////
          /////////////////////////////

      		scene = new THREE.Scene()
      		
      		var camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
          camera.position.set(cameraX,cameraY,cameraZ);
          camera.up = lookUpVector;
          camera.lookAt(scene.position);

          var inspectedCamera = new THREE.PerspectiveCamera(10, window.innerWidth / window.innerHeight, 10, 1);
          var trackballControls = new THREE.TrackballControls(camera);
          var axisHelper = new THREE.AxisHelper(3);

      		var renderer = new THREE.WebGLRenderer();
          renderer.setClearColor(new THREE.Color(0xEEEEEE));
          renderer.setSize(window.innerWidth, window.innerHeight);
          renderer.shadowMapEnabled = true;

          var directionalLight = new THREE.DirectionalLight( pointColorDirectional );
          directionalLight.intensity = intensityDirectional;
          directionalLight.position.set(cameraX,cameraY,cameraZ);
          directionalLight.castShadow = castShadowDirectional;
          directionalLight.shadowCameraNear = 50;
          directionalLight.shadowCameraFar = 800;
          directionalLight.shadowCameraLeft = -500;
          directionalLight.shadowCameraRight = 500;
          directionalLight.shadowCameraTop = 500;
          directionalLight.shadowCameraBottom = -500;
          directionalLight.shadowCameraVisible = true;
          directionalLight.shadowMapHeight = 1024;
          directionalLight.shadowMapWidth = 1024;

          phongOptions['color'] = '0x3CB371';          
          var cubeGeometry = new THREE.PlaneGeometry(500,500,100,100);
          var plane = createMesh(cubeGeometry , "lambert" , {color: 0x3CB371})
          
          plane.position.set(0,0,0);
          plane.rotation.x=-0.5*Math.PI;
          plane.receiveShadow = true;

          var options = {color: 0x04FE32}
          var j1 = createJoint(heightArm , radius);
          var j2 = createJoint(heightArm , radius);
          var pivotTop = generatePivot(radius,2);

          j1.attach.add(j2);
          j2.attach.add(pivotTop);
          //positioning j1 on base
          j1.position.y = 1;

          var base = generateCylinder(heightBase , 0 , rTopBase , rBottomBase , phongOptions , "phong");
          base.add(j1);
          base.position.set(0,2,150);
          base.castShadow = true; 

          //create lamp
          var lamp = createTopLamp(r1,r2,r3,heightCono,segmentO,radius);
          j2.attach.add(lamp);

          var options = {
            size: 85,
            height: 22,
            bevelThickness: 1.3,
            bevelSize: 1.65,
            bevelSegments: 15,
            bevelEnabled: true,
            curveSegments: 20,
          };

          c = createMesh(new THREE.TextGeometry("C", options), "phong");
          v = createMesh(new THREE.TextGeometry("v", options), "phong");
          d = createMesh(new THREE.TextGeometry("d", options), "phong");
          l = createMesh(new THREE.TextGeometry("l", options), "phong");
          a = createMesh(new THREE.TextGeometry("a", options), "phong");
          b = createMesh(new THREE.TextGeometry("b", options), "phong");

          c.castShadow = true;
          v.castShadow = true;
          d.castShadow = true;
          l.castShadow = true;
          a.castShadow = true;
          b.castShadow = true;

          c.position.set(-150,2,0);
          v.position.set(-60,2,0);
          d.position.set(0,2,0);
          l.position.set(70,2,0);
          a.position.set(100,2,0);
          b.position.set(170,2,0);

          scene.add(camera);
          scene.add(base);
          //scene.add(lamp);
          scene.add(axisHelper);
          scene.add(plane);
          scene.add(directionalLight);

          scene.add(c);
          scene.add(v);
          scene.add(d);
          scene.add(l);
          scene.add(a);
          scene.add(b);

          var controls = new function() {
            this.pivot_alfa = 0;
            this.pivot_beta = 0;
            this.pivot_gamma = 0;
            this.pivot_gamma2 = 0;
            this.pivot_epslon = 0;
          }

          var gui = new dat.GUI();
          gui.add(controls, 'pivot_alfa',0,alfaTo).onChange(function (e){
            j1.rotation.y = e;
          });
          gui.add(controls, 'pivot_beta',0,betaTo).onChange(function (e){
            j1.pivot.rotation.x = e;
          });
          gui.add(controls , 'pivot_gamma',0,gammaTo).onChange(function (e){
            j2.pivot.rotation.x = e;
          });
          gui.add(controls , 'pivot_gamma2',0,gamma2To).onChange(function (e){
            j2.rotation.y = e;
          });
          gui.add(controls , 'pivot_epslon',0,epslonTo).onChange(function (e){
            lamp.pivot.rotation.x = e;
          });

          //j2.rotation.y = 3;
          //lamp.pivot.rotation.x = Math.PI/2;


          $('body').append(renderer.domElement)
          

          animation();
          //startAnimation(lamp.rotation , j2.rotation , base.position);

          directionalLight.intensity = 0.7;

          var animator = null;
          function bouncingAnimator() {
    
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
                        { x : 70 },

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
                        { y : 100 },
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
                        { z : 0 },
                      ],
                      target: base.position
                    },
                  ],
                loop: false,
                easing: TWEEN.Easing.Bounce.Out,
                duration: 3000
              });

          }

          bouncingAnimator();
          animator.start();



          function animation(){

            KF.update();
            TWEEN.update();
            trackballControls.update();
            requestAnimationFrame(animation);
            renderer.render(scene, camera);
          }



          function generateCylinder(height , trasl , rTop , rBottom , options , meshType){
            var planeGeometry = new THREE.CylinderGeometry(rBottom,rTop,height,segmentO);
            var cylinder = createMesh(planeGeometry,meshType,options)
            cylinder.position.set(0,trasl,0);
            
            return cylinder;
          }

          function generateSphere(radius ,vertical , horizontal , options){
            var geometry_m = new THREE.SphereGeometry(radius,vertical,horizontal);
            var sphere = createMesh(geometry_m,"phong",options)

            return sphere
          }

          function generatePivot(radius , transl){
            var pin = generateSphere(radius,20,20);
            pin.position.set(0,transl,0);

            return pin;
          }

          function createJoint(height , radius){

            var joint = new THREE.Object3D();

            phongOptions['color'] = 0xa331e0;
            var cylinder = generateCylinder(heightArm , (heightArm/2)+radius , rTop , rBottom ,
                           phongOptions , "phong");

            phongOptions['color'] = 0xa314e0;
            var pivot = generatePivot(radius , 2 , phongOptions);
            pivot.add(cylinder);

            var attach = new THREE.Object3D();
            attach.position.set(0,(heightArm/2),0);
            cylinder.add(attach);

            cylinder.castShadow = true;
            pivot.castShadow = true;

            joint.pivot = pivot;
            joint.arm = cylinder;
            joint.attach = attach;

            joint.add(pivot);

            return joint;
          }

          function radialWave(u , v){

             var r = 2;
             var x = Math.sin(u * 2 * Math.PI) * r;
             var y = 3
             var z = Math.cos(v * 2 * Math.PI) * r;
             return new THREE.Vector3(x, y, z);
          }

          function createMesh(geometry , meshType , options){

            var meshMaterial;
            switch(meshType){
              case "phong":
              meshMaterial = new THREE.MeshPhongMaterial(options);
                break;
              case "basic":
                meshMaterial = new THREE.MeshBasicMaterial(options);
                break;
              case "lambert":
                meshMaterial = new THREE.MeshLambertMaterial(options);
                break;
            }
            meshMaterial.doubleSide = true;
            var mesh = new THREE.Mesh(geometry , meshMaterial);

            return mesh;
          }

          function createTopLamp(r1,r2,r3,height,segmentO,radius){

            var conoGeom = new THREE.CylinderGeometry(r2,r1,height,segmentO);
            var sphereGeom = new THREE.SphereGeometry(r3,20,20,6,6.3,1.4,1.5);
            var pivot = generatePivot(radius,radius);

            phongOptions['color'] = 0x3399ff;
            var cono = createMesh(conoGeom , "phong" , phongOptions);
            var sphere = createMesh(sphereGeom , "phong" ,phongOptions);
            var bulb = generateSphere(r1-0.5,segmentO,segmentO,{color:0xffffff});

            cono.castShadow = true;
            sphere.castShadow = true;

            cono.position.set(0,(height+radius)/2,0);
            sphere.position.set(0,(height-1+r3),0);
            sphere.material.side = THREE.DoubleSide;

            pivot.add(sphere);
            pivot.add(cono);

            //Add light to lamp
            var fooTarget = generateSphere(r1-0.5,segmentO,segmentO,{color:0xffffff});
            fooTarget.position.y = 30;         

            var spotLight = new THREE.SpotLight(pointColorLightLamp);
            spotLight.intensity = intensityLamp;
            spotLight.angle = Math.PI/3;
            spotLight.target = fooTarget;
            spotLight.castShadow = castShadowLamp;
            spotLight.shadowCameraVisible = true;
            spotLight.shadowCameraNear =30;
            spotLight.shadowCameraFar = 500;
            spotLight.shadowCameraLeft = -500;
            spotLight.shadowCameraRight = 500;
            spotLight.shadowCameraTop = 500;
            spotLight.shadowCameraBottom = -500;
            spotLight.shadowCameraFov = 70;
            spotLight.shadowDarkness = 0.5;
            spotLight.shadowMapWidth = 256;
            spotLight.shadowMapHeight = 256;        
            
            bulb.position.y = 4;
            bulb.add(spotLight);
            bulb.add(fooTarget);
            cono.add(bulb);
        
            var topLamp = new THREE.Object3D();
            topLamp.pivot = pivot;
            topLamp.light = spotLight;

            topLamp.add(pivot);

            return topLamp;
          }

          function addJoint2Arm(num_join){

            if(num_join === 1){
              return createArm();
            }

            var joint = createArm();
            return joint.pivot.add(addJoint2Arm(--num_join));
          }

         });