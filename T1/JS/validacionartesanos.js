const validateEmail=(email)=>{
    if(!email) return false;
     //length validation 
    let  lengthValid=email.length<=30;
  
  //format validation 
  let re=/^[\w.]+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
  let formatValid=re.test(email);
  
  return lengthValid && formatValid;
  }
  

  const validatePhoneNumer=(phoneNumber)=>{
   if(!phoneNumber)return false;
  
   let lengthValid=phoneNumber.length<=15;
  
   let re=/^(\+569|(\+562))\s\d{4}\d{4}$/;
   let formatValid=re.test(phoneNumber);
   return lengthValid && formatValid;
  }


  const validateFiles=(files)=>{
   if(!files) return false;
   
   let lengthValid=1 <=files.length && files.length<=3;

   let typeValid=true;
    
   for(const file of files){
    let fileFamily=file.type.split("/")[0];
    typeValid &&= fileFamily=="image"; 

    return lengthValid && typeValid;}}
  

  const validateName=(name)=>{
   if(!name) return false; 

   let lengthValid=3 <=name.length && name.length<=80;
   return lengthValid;
  }

  const valideartesania = (artesanias) => {
    if (!artesanias || !Array.isArray(artesanias)) return false;
  
    let selectedCount = 0;
    for (const opcion of artesanias) {
      if (opcion.selected) {
        selectedCount++;
      }
    }
  
    return selectedCount >= 1 && selectedCount <= 3;
  }
  
  
  function cargaTipo(){
    let select = document.getElementById("alimento");
    let alimento = select.value;
    
    let selectTipos = document.getElementById("tipoAlimento");
    selectTipos.innerHTML = "";
    
    if (alimento == "Arica y Parinacota") {
      (["Arica", "Camarones", "General Lagos", "Putre"]).forEach(
       (element) => {
        let option = document.createElement("option");
        option.text = element;
        option.value= element;
        selectTipos.add(option);
       });
      
    } else if (alimento == "Tarapaca") {
      (["Alto Hospicio", "Camiña", "Colchane", "Huara", "Iquique", "Pica", "Pozo Almonte"]).forEach(
       (element) => {
        let option = document.createElement("option");
        option.text = element;
        option.value= element;
        selectTipos.add(option);
       });
    }
  
    else if (alimento == "Antofagasta") {
      (["Antofagasta", "Calama", "María Elena", "Mejillones", "Ollagüe", "San Pedro de Atacama", "Sierra Gorda", "Taltal", "Tocopilla"]).forEach(
       (element) => {
        let option = document.createElement("option");
        option.text = element;
        option.value= element;
        selectTipos.add(option);
       });
    }
  
  
  
    else if (alimento == "Atacama") {
      (["Alto del Carmen", "Caldera", "Chañaral", "Copiapó", "Diego de Almagro", "Freirina", "Huasco", "Tierra Amarilla", "Vallenar"]).forEach(
       (element) => {
        let option = document.createElement("option");
        option.text = element;
        option.value= element;
        selectTipos.add(option);
       });
    }
  
  
    else if (alimento == "Coquimbo") {
      (["Andacollo", "Canela", "Combarbalá", "Coquimbo", "Illapel", "La Higuera", "La Serena", "Los Vilos", "Monte Patria", "Ovalle", "Paihuano", "Punitaqui", "Río Hurtado", "Salamanca", "Vicuña"]).forEach(
       (element) => {
        let option = document.createElement("option");
        option.text = element;
        option.value= element;
        selectTipos.add(option);
       });
    }
  
  
    else if (alimento == "Valparaiso") {
      (["Algarrobo", "Cabildo", "Calera", "Calle Larga", "Cartagena", "Casablanca", "Catemu", "Concón", "El Quisco", "El Tabo", "Hijuelas", "Isla de Pascua", "Juan Fernández", "La Cruz", "La Ligua", "Limache", "Llaillay", "Los Andes", "Nogales", "Olmué", "Panquehue", "Papudo", "Petorca", "Puchuncaví", "Putaendo", "Quillota", "Quilpué", "Quintero", "Rinconada", "San Antonio", "San Esteban", "San Felipe", "Santa María", "Santo Domingo", "Valparaíspo", "Villa Alemana", "Viña del Mar", "Zapallar"]).forEach(
       (element) => {
        let option = document.createElement("option");
        option.text = element;
        option.value= element;
        selectTipos.add(option);
       });
    }
  
    else if (alimento == "Metropolitana") {
      (["Alhué", "Buin", "Calera de Tango", "Cerrillos", "Cerro Navia", "Colina", "Conchalí", "Curacaví", "El Bosque", "El Monte", "Estación Central", "Huechuraba", "Independencia", "Isla de Maipo", "La Cisterna", "La Florida", "La Granja", "Lampa", "La Pintana", "La Reina", "Las Condes", "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macúl", "Maipú", "María Pinto", "Melipilla", "Ñuñoa", "Padre Hurtado", "Paine", "Pedro Aguirre Cerda", "Peñaflor", "Peñalolén", "Pirque", "Providencia", "Pudahuel", "Puente Alto", "Quilicura", "Quinta Normal", "Recoleta", "Renca", "San Bernardo", "San Joaquín", "San José de Maipo", "San Miguel", "San Pedro", "San Ramón", "Santiago", "Talagante", "Tiltil", "Vitacura"]).forEach(
       (element) => {
        let option = document.createElement("option");
        option.text = element;
        option.value= element;
        selectTipos.add(option);
       });
    }
  
    
    else if (alimento == "Libertador Bernardo Ohiggins") {
      (["Chépica", "Chimbarongo", "Codegua", "Coínco", "Coltauco", "Doñihue", "Graneros", "La Estrella", "Las Cabras", "Litueche", "Lolol", "Machalí", "Malloa", "Marchihue", "Mostazal", "Nancagua", "Navidad", "Olivar", "Palmilla", "Paredones", "Peralillo", "Peumo", "Pichidegua", "Pichilemu", "Placilla", "Pumanque", "Quinta de Tilcoco", "Rancagua", "Rengo", "Requínoa", "San Fernando", "Santa Cruz", "San Vicente"]).forEach(
       (element) => {
        let option = document.createElement("option");
        option.text = element;
        option.value= element;
        selectTipos.add(option);
       });
    }
    
  
   
  
  
    else if (alimento == "Maule") {
      (["Cauquenes", "Chanco", "Colbún", "Constitución", "Curepto", "Curicó", "Empedrado", "Hualañé", "Licantén", "Linares", "Longaví", "Maule", "Molina", "Parral", "Pelarco", "Pelluhue", "Pencahue", "Rauco", "Retiro", "Río Claro", "Romeral", "Sagrada Familia", "San Clemente", "San Javier", "San Rafael", "Talca", "Teno", "Vichuquén", "Villa Alegre", "Yerbas Buenas"]).forEach(
       (element) => {
        let option = document.createElement("option");
        option.text = element;
        option.value= element;
        selectTipos.add(option);
       });
    }
  
    else if (alimento == "Ñuble") {
      (["Bulnes", "Chillán", "Chillán Viejo", "Cobquecura", "Coelemu", "Coihueco", "El Carmen", "Ninhue", "Ñiquén", "Pemuco", "Pinto", "Portezuelo", "Quillón", "Quirihue", "Ránquil", "San Carlos", "San Fabián", "San Ignacio", "San Nicolás", "Treguaco", "Yungay"]).forEach(
       (element) => {
        let option = document.createElement("option");
        option.text = element;
        option.value= element;
        selectTipos.add(option);
       });
    }
  
  
    else if (alimento == "Biobio") {
      (["Alto Biobío", "Antuco", "Arauco", "Cabrero", "Cañete", "Chiguayante", "Concepción", "Contulmo", "Coronel", "Curanilahue", "Florida", "Hualpén", "Hualqui", "Laja", "Lebu", "Los Alamos", "Los Angeles", "Lota", "Mulchén", "Nacimiento", "Negrete", "Penco", "Quilaco", "Quilleco", "San Pedro de la Paz", "San Rosendo", "Santa Bárbara", "Santa Juana", "Talcahuano", "Tirúa", "Tomé", "Tucapel", "Yumbel"]).forEach(
       (element) => {
        let option = document.createElement("option");
        option.text = element;
        option.value= element;
        selectTipos.add(option);
       });
    } 
  
  
   
  
    else if (alimento == "La Araucania") {
      (["Angol", "Carahue", "Cholchol", "Collipulli", "Cunco", "Curacautín", "Curarrehue", "Ercilla", "Freire", "Galvarino", "Gorbea", "Lautaro", "Loncoche", "Lonquimay", "Los Sauces", "Lumaco", "Melipeuco", "Nueva Imperial", "Padre Las Casas", "Perquenco", "Pitrufquén", "Pucón", "Purén", "Renaico", "Saavedra", "Temuco", "Teodoro Schmidt", "Toltén", "Traiguén", "Victoria", "Vilcún", "Villarrica"]).forEach(
       (element) => {
        let option = document.createElement("option");
        option.text = element;
        option.value= element;
        selectTipos.add(option);
       });
    }
  
  
    
   
  
    else if (alimento == "Los Rios") {
      (["Alto del Carmen", "Caldera", "Chañaral", "Copiapó", "Diego de Almagro", "Freirina", "Huasco", "Tierra Amarilla", "Vallenar"]).forEach(
       (element) => {
        let option = document.createElement("option");
        option.text = element;
        option.value= element;
        selectTipos.add(option);
       });
    }
  
  
    else if (alimento == "Los Lagos") {
      (["Ancud", "Calbuco", "Castro", "Chaitén", "Chonchi", "Cochamó", "Curaco de Vélez", "Dalcahue", "Fresia", "Frutillar", "Futaleufú", "Hualaihué", "Llanquihue", "Los Muermos", "Maullín", "Osorno", "Palena", "Puerto Montt", "Puerto Octay", "Puerto Varas", "Puqueldón", "Purranque", "Puyehue", "Queilén", "Quellón", "Quemchi", "Quinchao", "Río Negro", "San Juan de la Costa", "San Pablo"]).forEach(
       (element) => {
        let option = document.createElement("option");
        option.text = element;
        option.value= element;
        selectTipos.add(option);
       });
    }
    
  
    
  
    else if (alimento == "Aysen") {
      (["Aysén", "Chile Chico", "Cisnes", "Cochrane", "Coyhaique", "Guaitecas", "Lago Verde", "O'Higgins", "Río Ibáñez", "Tortel"]).forEach(
       (element) => {
        let option = document.createElement("option");
        option.text = element;
        option.value= element;
        selectTipos.add(option);
       });
    }
     
    
  
  
    else if (alimento == "Magallanes y de la Antartica Chilena") {
      (["Antártica", "Cabo de Hornos", "Laguna Blanca", "Natales", "Porvenir", "Primavera", "Punta Arenas", "Río Verde", "San Gregorio", "Timaukel", "Torres del Paine"]).forEach(
       (element) => {
        let option = document.createElement("option");
        option.text = element;
        option.value= element;
        selectTipos.add(option);
       });
    }
  
  }

 
  const btnAbrirModal=document.querySelector("#submit-btn")
  const btnCerrarModal= document.querySelector("#btn-cerrar-modal")
  const modal=document.querySelector("#modal")
  const btnconfirmar=document.querySelector("#confirmar")
 
 btnCerrarModal.addEventListener("click",()=>{
 
   modal.close()
 })
 
 btnconfirmar.addEventListener("click",()=>{
 
    alert("Hemos recibido el registro de hincha.Muchas gracias")
   
 })
  const validateForm=()=> {

   let myForm=document.forms["myForm"];
   let email=myForm["email"].value;
   let phoneNumber=myForm["phone"].value;
   let files=myForm["files"].files;
   let name=myForm["username"].value;
   let artesanias = myForm["artesania"].options;

   let selectedArtesanias = Array.from(artesanias).filter((opcion) => opcion.selected);

   let invalidInputs=[];
   let isValid=true;
   const setInvalidInput=(inputName)=>{

    invalidInputs.push(inputName);
    isValid &&= false;}
   

   //lo que sale en el box
   if(!validateEmail(email)){
    setInvalidInput("Email");
   }

   if(!validatePhoneNumer(phoneNumber)){
    setInvalidInput("Phone number");
   }

   if(!validateFiles(files)){

    setInvalidInput("Picture(s)");
   }

   if(!validateName(name)){
    setInvalidInput("name")}
   
    if (!valideartesania(selectedArtesanias)) { // Pasa las opciones seleccionadas
      setInvalidInput("Artesanías");
    }
    



 let validationBox=document.getElementById("val-box");
 let validationMessageElem=document.getElementById("val-msg");
 let validationListElem=document.getElementById("val-list");

 if(!isValid){
   validationListElem.textContent="";

   for(input of invalidInputs){

    let listElement=document.createElement("li");
    listElement.innerText=input;
    validationListElem.append(listElement);
   }

   validationMessageElem.innerText="Los siguientes campos son invalidos";

   validationBox.hidden=false;
 }else{
  
    modal.showModal()
 }
  };

  let submitBtn=document.getElementById("submit-btn");
  submitBtn.addEventListener("click",validateForm);