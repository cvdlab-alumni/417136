
function createTable(x,y,z){

          var pianoGeometry = new THREE.BoxGeometry(x,y,5,20,20,5);
          var pianoMaterial = new THREE.MeshPhongMaterial({color: 0xB20000});
          var piano = new THREE.Mesh(pianoGeometry,pianoMaterial);
          var segmentoGeometry = new THREE.CylinderGeometry(5, 5, 50, 32)
          var segmentoMaterial = new THREE.MeshLambertMaterial({color: 0xB20000, wireframe:false});
          var segmento1 = new THREE.Mesh(segmentoGeometry,segmentoMaterial);
          var segmento2 = new THREE.Mesh(segmentoGeometry,segmentoMaterial);
          var segmento3 = new THREE.Mesh(segmentoGeometry,segmentoMaterial);
          var segmento4 = new THREE.Mesh(segmentoGeometry,segmentoMaterial);
          segmento1.position.set((-x/2 + x/20),(-y/2 + y/20),(-z / 2 -2));
          segmento2.position.set((-x/2 + x/20),(y/2 - y/20),(-z / 2 -2));
          segmento3.position.set((x/2 - x/20),(y/2 - y/20),(-z / 2 -2));
          segmento4.position.set((x/2 - x/20),(-y/2 + y/20),(-z / 2 -2));
          segmento1.rotation.x=Math.PI/2;
          segmento2.rotation.x=Math.PI/2;
          segmento3.rotation.x=Math.PI/2;
          segmento4.rotation.x=Math.PI/2;




          segmento1.receiveShadow = true;
          segmento1.castShadow = true;
          segmento2.receiveShadow = true;
          segmento2.castShadow = true;
          segmento3.receiveShadow = true;
          segmento3.castShadow = true;
          segmento4.receiveShadow = true;
          segmento4.castShadow = true;
          piano.receiveShadow = true;
          piano.castShadow = true;
          piano.position.set(0,0,-3)
          var tavolo = new THREE.Object3D();
          tavolo.add(segmento1);
          tavolo.add(segmento2);
          tavolo.add(segmento3);
          tavolo.add(segmento4);
          tavolo.add(piano); 
          //tavolo.receiveShadow = true;
          tavolo.piano = piano;



          
          return tavolo; 
        }


function createPlane(x,y){
    var planeGeometry = new THREE.PlaneGeometry(x,y);
    var planeMaterial =  new THREE.MeshLambertMaterial({color: 0x00FF00});
    var plane = new THREE.Mesh(planeGeometry,planeMaterial);
    plane.position.set(0,0,0);
        

return plane;
};


function createLamp(){
	// base lampada
	var result = new THREE.Object3D(); 
	var geometry = new THREE.CylinderGeometry( 9, 12, 2, 32 );
	var material = new THREE.MeshPhongMaterial( {color: 0x8F8F8F, shininess: 80} );
	var cylinderBase = new THREE.Mesh( geometry, material );
    cylinderBase.position.set(0,0,1);
    cylinderBase.rotation.x=Math.PI/2;
    result.add(cylinderBase);
    //primo giunto
    var geometry = new THREE.SphereGeometry( 4, 20, 20 );
    var material = new THREE.MeshPhongMaterial( {color: 0xffff00, shininess: 80} );
    var pivot = new THREE.Mesh(geometry, material);
    pivot.position.set(0,0,6);
    //primo braccio
    var geometry = new THREE.CylinderGeometry( 1, 1, 18, 32 );
	var material = new THREE.MeshPhongMaterial( {color: 0x8F8F8F, shininess: 80} );
	var cylinder2 = new THREE.Mesh( geometry, material );
	cylinder2.position.set(1.5,0,12);
	cylinder2.rotation.x=Math.PI/2;
	var geometry = new THREE.CylinderGeometry( 1, 1, 18, 32 );
	var material = new THREE.MeshPhongMaterial( {color: 0x8F8F8F, shininess: 80} );
	var cylinder2_2 = new THREE.Mesh( geometry, material );
	cylinder2_2.position.set(-1.5,0,12);
	cylinder2_2.rotation.x=Math.PI/2;
  var hook = new THREE.Object3D();
  hook.add(cylinder2);
  hook.add(cylinder2_2);
	pivot.add(hook);


	//secondo giunto
    var geometry = new THREE.SphereGeometry( 4, 20, 20 );
    var material = new THREE.MeshPhongMaterial( {color: 0xffff00, shininess: 80} );
    var pivot2 = new THREE.Mesh(geometry, material);
    pivot2.position.set(0,0,24);

    //secondo braccio
    var geometry = new THREE.CylinderGeometry( 1, 1, 18, 32 );
	var material = new THREE.MeshPhongMaterial( {color: 0x8F8F8F, shininess: 80} );
	var cylinder3 = new THREE.Mesh( geometry, material );
	cylinder3.position.set(1.5,0,12);
	cylinder3.rotation.x=Math.PI/2;
	var geometry = new THREE.CylinderGeometry( 1, 1, 18, 32 );
	var material = new THREE.MeshPhongMaterial( {color: 0x8F8F8F, shininess: 80} );
	var cylinder3_3 = new THREE.Mesh( geometry, material );
	cylinder3_3.position.set(-1.5,0,12);
	cylinder3_3.rotation.x=Math.PI/2;
  var hook2 = new THREE.Object3D();
  hook2.add(cylinder3);
  hook2.add(cylinder3_3);
  pivot2.add(hook2);
	
	



	//terzo giunto
    var geometry = new THREE.SphereGeometry( 4, 20, 20 );
    var material = new THREE.MeshPhongMaterial( {color: 0xffff00, shininess: 80} );
    var pivot4 = new THREE.Mesh(geometry, material);
    pivot4.position.set(0,0,24);



	

	//supporto lampadina
    var geometry = new THREE.SphereGeometry( 10, 20, 20, 0, Math.PI);
    var material = new THREE.MeshPhongMaterial( {color: 0x8F8F8F, shininess: 80, side:THREE.DoubleSide, metal:true} );
    var supportLamp = new THREE.Mesh(geometry, material);
    supportLamp.position.set(0,0,13);
    supportLamp.rotation.x=Math.PI;

    pivot4.add(supportLamp);
    

    //lampadina
    var bulb = new THREE.Object3D(); 
	  var geometry = new THREE.CylinderGeometry( 2.5, 1.5, 5, 32 );
	  var material = new THREE.MeshPhongMaterial( {color: 0x404040, shininess: 80} );
	  var bulb1 = new THREE.Mesh( geometry, material );
	  bulb1.position.set(0,0,6);
	  bulb1.rotation.x=Math.PI/2;
	  var geometry = new THREE.SphereGeometry( 4, 20, 20 );
    var material = new THREE.MeshPhongMaterial( {color: 0xfcfbf9, opacity:0.7, transparent:true} );
    var bulb1_1 = new THREE.Mesh(geometry, material);
    bulb1_1.position.set(0,0,11);



	
	
    var spotlight = new THREE.SpotLight(0xffffff, 3);
    spotlight.castShadow = true;
    spotlight.position.set(0,0,12);
    spotlight.shadowCameraNear = 2;
    spotlight.shadowDarkness = 0.5;
    spotlight.intensity = 1;
    spotlight.shadowCameraVisible = false;
    var lightTarget = new THREE.Object3D();
    lightTarget.position.set(0,0,15);
    bulb.add(lightTarget);
    spotlight.target = lightTarget;

    bulb.add(spotlight);
	

    

  



	bulb.add(bulb1);
	bulb.add(bulb1_1);
	pivot4.add(bulb);

	hook2.add(pivot4);
  hook.add(pivot2);

  pivot4.rotation.x=1.5;
	pivot2.rotation.x=1.7;
	pivot.rotation.z=Math.PI/2;
	pivot.rotation.y=-0.9;


    result.add(pivot);
    result.pivot4 = pivot4;
    result.pivot2 = pivot2;
    result.pivot = pivot;
    result.bulb = bulb;
    result.bulb1_1 = bulb1_1;
    result.hook = hook;
    result.hook2 = hook2;
    result.spotlight = spotlight;


return result;
};


function addObject(name,x,y){
	var result = new THREE.Object3D(); 
	if(name === "sfera"){
    var geometry = new THREE.SphereGeometry( 10, 20, 20 );
    var material = new THREE.MeshPhongMaterial( {color: 0x228b22, shininess: 80} );
    var sfera = new THREE.Mesh(geometry, material);
    sfera.castShadow = true;
    sfera.receiveShadow = true;
    sfera.shadowDarkness = 1;
    sfera.position.set(x,y,10);
	result.add(sfera);}

	if(name === "cubo"){
    var cubeGeometry = new THREE.BoxGeometry(16,16,16);
    var cubeMaterial = new THREE.MeshLambertMaterial({color: 0x228b22, shininess: 80});
    var cube = new THREE.Mesh(cubeGeometry, cubeMaterial);
    cube.castShadow = true;
    cube.receiveShadow = true;
    cube.shadowDarkness = 1;
    cube.position.set(x,y,8);

	result.add(cube);}

      result.receiveShadow = true;
      result.castShadow = true;



  result.sfera = sfera;
  result.cube = cube;

return result

}


