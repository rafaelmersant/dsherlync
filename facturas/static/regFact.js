var RegCOUNT = 0;
var $i = 0;
var $cambio = 0;

var $dataFacturar = {};
var itemsfactura = [];

var $dataApartar = {};
var itemsApartar = [];

// VARIABLE PARA EL CONTENIDO DE LA TABLA DE PRODUCTOS
var contenido = $('#productosajax');
var contenido2 = $('#clientesajax');

//*****************************************************************************************************
//*****************************************************************************************************
//INICIO DE EVENTOS
//*****************************************************************************************************
//*****************************************************************************************************

$(document).ready(function() {
	localStorage.clear();

	// VARIABLE QUE CONTIENE TODOS LOS PRODUCTOS EN UNA TUPLA
	prodLS = localStorage;
	RegCOUNT = 0;

	if(window.location.pathname == '/apartados/'){
		prodLS['display'] = 'displaynone';
		$('#idHeaderApartar').addClass(prodLS['display']);
	}
	else{
		prodLS['display'] = '';
	}
});


$(function(){
	$('#idFecha').datepicker();
	$('#id_fecha_entrada').datepicker();

	});

// SELECCIONAR TEXTO COMPLETO CUANDO ENTRA EL FOCUS
$('#iProd').click(function () {
   $(this).select();
});

// CUANDO SEA QUITADO EL FOCUS DE LA BUSQUEDAD DE PRODUCTOS
$('#iProd').blur(function(){
	$('#productosajax').fadeOut('fast');
});

// SELECCIONAR TEXTO COMPLETO CUANDO ENTRA EL FOCUS PARA CLIENTES
$('#iCte').click(function () {
   $(this).select();
});

// CUANDO SEA QUITADO EL FOCUS DE LA BUSQUEDAD DE CLIENTES
$('#iCte').blur(function(){
	$('#clientesajax').fadeOut('fast');
});


// FUNCION DEL BOTON AGREGAR
$('#btNew').click(function(){
	location.reload();
	$('#btnImprimir').removeClass('InhabilitaBoton');

});

// FUNCION DEL BOTON AGREGAR CLIENTE
$('#btNewCte').click(function(){
	$('#clienteForm').toggleClass('nuevoClienteForm');
	$('#id_nombre').val($('#iCte').val());
	$('#id_telefono').focus();
});

// FUNCION DEL BOTON AGREGAR CLIENTE
$('#btcerrarCte').click(function(){
	$('#clienteForm').toggleClass('nuevoClienteForm');
});




//CADA VEZ QUE SE DIGITE EN EL PRECIO DE CUALQUIER LINEA SE RECALCULE
$('#iPrecio').on('input',CalculaLinea);

//CADA VEZ QUE SE DIGITE EN LA CASILLA DE PAGO ACTUALIZA LA DEVUELTA AL CLIENTE.
$('#iPagoF').on('input', function(){

	DevueltaAlCliente();
})

//PARA ENVIAR A MONTO A PAGAR CUANDO SE PRESIONE ENTER EN LA CASILLA DE PRODUCTO
$('#iProd').on('keypress', function(e) {
	//SI ES ENTER MOVER HACIA EL MONTO A PAGAR
	if (event.charCode == 13){
		$('#iPagoF').focus().select();
	}

});
//**************************************************************

//PARA EJECUTAR LA FUNCION IMPRIMIR CUANDO SE HAYA DIGITADO EL MONTO A PAGAR
$('#iPagoF').on('keypress', function(e) {
	if (event.charCode == 13){
		facturarImprimir();
	}

});
//**************************************************************

// FUNCION PARA BUSCAR LOS PRODUCTOS EN LA API Y DIBUJAR LA TABLA CON LOS PRODUCTOS ENCONTRADOS
$('#iProd').on('input', function(e){
	e.defaultPrevented = false;

	$.ajax({
        type: "GET",
        url: 'http://127.0.0.1:8000/api/productos/' + $('#iProd').val() +'/?format=json',
        dataType: "json",
        success: function(data) {
			contenido.html('');

			if (data.length > 0){
				$.each(data, function(index, element) {
					contenido.append(
						// '<tr class="DetailsItemSearch" id=\"' + RegCOUNT +'\">' + 
						'<tr class="DetailsItemSearch" id=' + RegCOUNT +'>' + 
						'<td id="idCod" class="CellItemDetailSearch '+ element['departamento'] +'">' + element['codigo'] +'</td>' +					
						'<td id="idDescrp" class="CellItemDetailSearch '+ element['departamento'] +'">'
							+'<a href="javascript:void(0);" class="'+ element['departamento'] + '"' 	
							+'onclick="agregarProducto(&quot;' 
								+ element['codigo'] + '&quot;, &quot;' 
								+ element['descripcion'] + '&quot;, &quot;'
								+ element['departamento'] + '&quot;, &quot;'
								+ element['precio'] + '&quot;); return false;">' + element['descripcion'] +'</a></td>' +
						'<td id="idPrecio" class="CellItemDetailSearchRight '+ element['departamento'] +'">' + element['precio'] +'</td>' +
						'</tr>'
						);
				});
			}
			else{
				contenido.html('<p class="margenNoExiste"> NO EXISTE EL PRODUCTO ESPECIFICADO. </p>');
			}

			contenido.hide();
			contenido.fadeIn('fast');
		},
        error: function(response) {
			contenido.html('<p class="margenNoExiste"> NO EXISTE EL CLIENTE ESPECIFICADO. </p>');
        }
	});
});

// FUNCION PARA BUSCAR CLIENTES EN LA API Y DIBUJAR LA TABLA CON LOS CLIENTES ENCONTRADOS
$('#iCte').on('input', function(e){
	e.defaultPrevented = false;

	$.ajax({
        type: "GET",
        url: 'http://127.0.0.1:8000/api/clientes/' + $('#iCte').val() +'/?format=json',
        dataType: "json",
        success: function(data) {
			contenido2.html('');

			if (data.length > 0){
				$.each(data, function(index, element) {
					contenido2.append(
						'<tr class="DetailsItemSearch" id=' + RegCOUNT +'>' + 
						'<td id="idCod" class="CellItemDetailSearch idCodCte">' + element['id'] +'</td>' +					
						'<td id="idNombre" class="CellItemDetailSearch">'
							+'<a href="javascript:void(0);" class="clsCte"' 	
							+'onclick="agregarCliente(&quot;' 
								+ element['id'] + '&quot;, &quot;' 
								+ element['nombre'] + '&quot;); return false;">' + element['nombre'] +'</a></td>' +
						'</tr>'
						);
				});
			}
			else{
				contenido2.html('<p class="margenNoExiste"> NO EXISTE EL CLIENTE ESPECIFICADO. </p>');
			}

			contenido2.hide();
			contenido2.fadeIn('low');
		},
        error: function(response) {
			contenido2.html('<p class="margenNoExiste"> NO EXISTE EL CLIENTE ESPECIFICADO. </p>');
        }
	});
});
//*****************************************************************************************************
//*****************************************************************************************************
//FIN DE EVENTOS
//*****************************************************************************************************
//*****************************************************************************************************





//*****************************************************************************************************
//*****************************************************************************************************
//INICIO DE FUNCIONES
//*****************************************************************************************************
//*****************************************************************************************************

// FUNCION PARA AGREGAR UN PRODUCTO A LA TABLA
function agregarProducto(codigo, descrp, departamento, varprecio){

	$cambio = 1;
	$('#Items').removeClass('HideItem');

	$content = $('#Items');
	RegCOUNT = RegCOUNT + 1;

	$content.append('<tr class="DetailsItem" id="idItemF' + RegCOUNT + '">' +
						'<td class="CellItemDetail ' + departamento + ' dCod" id="iSec'+ RegCOUNT +' ">' + RegCOUNT +' </td>' +
						'<td class="CellItemDetail ' + departamento + ' dCod" id="iCodigo'+ RegCOUNT +'">' + codigo + ' </td>' +
						'<td class="CellItemDetail ' + departamento + ' dDescrp" id="iDescripcion'+ RegCOUNT +'">' + descrp + ' </td>' +
						'<td class="CellItemDetail ' + departamento + ' dCant"> <input id="iCantidad'+ RegCOUNT +'" onkeypress="return EventosTextBox(1,'+ RegCOUNT +');" type="text" value="1" class="TextBoxes TextItems" PlaceHolder="0.00"/> </td>' +
						'<td class="CellItemDetail ' + departamento + ' dPrecio"> <input id="iPrecio'+ RegCOUNT +'" onkeypress="return EventosTextBox(2,'+ RegCOUNT+');" type="text" value="0.00" class="TextBoxes TextItems" PlaceHolder="0.00"/></td>' +
						'<td class="CellItemDetail ' + departamento + ' dDesc"> <input id="iDescuento'+ RegCOUNT +'" onkeypress="return EventosTextBox(3,'+ RegCOUNT+');" type="text" value="0.00" class="TextBoxes TextItems" PlaceHolder="0.00"/> </td>' +
						'<td class="CellItemDetail ' + departamento + ' dImporte"> <span id="idImporte'+ RegCOUNT +'"> 0.00 </span> </td>' +
						'<td class="CellDelete CellItemDetail" id="idDelete'+ RegCOUNT +'"><a href="javascript:EliminarReg(' + RegCOUNT + ')" class="DelItem icon-delete"> </a> </td>' +
						'<td class="CellDelete CellItemDetail '+ prodLS['display'] +'" id="idApartar'+ RegCOUNT +'"><a href="javascript:ApartarReg('+ RegCOUNT +')" class="ApartarItem icon-spinner"> </a> </td>' +
					'</tr>').hide().fadeIn('fast');


	//SELECCIONAR EL TEXTO COMPLETO DE LOS SIGUIENTES CAMPOS
	$('#iCantidad' + RegCOUNT).click(function(){$(this).select();});
	$('#iPrecio' + RegCOUNT).click(function(){$(this).select();});
	$('#iDescuento' + RegCOUNT).click(function(){$(this).select();});
	//*****FIN SELECCION COMPLETA DE TEXTO EN CAMPOS**********
	
	CalculaLinea(RegCOUNT);

	$('#iCantidad' + RegCOUNT).focus().select();
}
//**************************************************************

// FUNCION PARA SELECCIONAR UN CLIENTE
function agregarCliente(codigo, nombre){

	$('#iCte').val(nombre);
	prodLS['Cliente'] = codigo;
}
//**************************************************************


//FUNCION PARA PASAR DE UN TEXTBOX A OTRO AL PRESIONAR ENTER
function EventosTextBox(concepto, posicion){

	$cambio = 1;

	if ($('#iCambioF').text() != '' && $('#iPagoF').text() != ''){
		DevueltaAlCliente();
	}

	//SI ES ENTER MOVER HACIA EL PRECIO
	if (event.charCode == 13 && concepto == 1)
		$('#iPrecio' + posicion).focus().select();
	
	//SI ES ENTER MOVER HACIA EL DESCUENTO
	if (event.charCode == 13 && concepto == 2)
		$('#iDescuento' + posicion).focus().select();
	
	//SI ES ENTER MOVER HACIA LA BUSQUEDA DE PRODUCTOS
	if (event.charCode == 13 && concepto == 3)
		$('#iProd').focus().select();

	if (event.charCode > 31 && (event.charCode < 48 || event.charCode > 57)) {
        return false;
    }
    return true;
}
//************************************************************


//FUNCION PARA ELIMINAR REGISTRO
function EliminarReg(registroDEL){
	$('#idItemF'+registroDEL).html('');
	prodLS['F' + registroDEL] = '';
}
//**************************************************************


//CALCULA UNA LINEA DE LA FACTURA
function CalculaLinea(iReg){
	defaultPrevented = false;

	$('#iPrecio' + iReg).on('input',function() {CalculaNow(iReg);});
	$('#iCantidad' + iReg).on('input',function() {CalculaNow(iReg);});
	$('#iDescuento' + iReg).on('input',function() {CalculaNow(iReg);});

	function CalculaNow(registernumber)
	{
		$('#idImporte' + registernumber).text(($('#iCantidad' + registernumber).val() * $('#iPrecio' + registernumber).val()) - $('#iDescuento' + registernumber).val());

		CalculaTOTALES();
	}
}
//**************************************************************


//CALCULA EL BLOQUE COMPLETO DE LA FACTURA (TOTALES GENERALES)
function CalculaTOTALES(){
	var $t = RegCOUNT;
	var valor = 0;

	while($t > 0 )
	{
		valor = valor + parseInt($('#idImporte' + $t).text());
		--$t;
	}

	$('#iTOTAL').text(valor);
}
//**************************************************************


//CALCULA LA DEVUELTA EN DINERO QUE SE DEBE ENTRAR AL CLIENTE
function DevueltaAlCliente(){

	$('#iCambioF').text( $('#iPagoF').val() - parseInt($('#iTOTAL').text()) );
}
//**************************************************************


//VALIDAR CAMPOS ANTES DE GUARDAR
function ValidarCampos(){
	valor = true

	if ($('#iPagoF').val() == ''){
		valor = false;
	}

	if (parseFloat($('#iCambioF').text()) < 0){
		valor = false;
	}

	for(j=0; j<=RegCOUNT; j++){
		if(parseFloat($('#iImporte' + j).text()) <= 0){
			valor = false;
		}
	}

	return valor;
}
//**************************************************************

//VALIDAR CAMPOS ANTES DE GUARDAR
function ValidarCamposApartados(){
	valor = true

	for(j=0; j<=RegCOUNT; j++){
		if(parseFloat($('#iImporte' + j).text()) <= 0){
			valor = false;
		}
	}

	return valor;
}
//**************************************************************


//PARA CSRF TOKEN
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
//***********************************************************

//FUNCION PARA APARTAR REGISTRO
function ApartarReg(registroAP){

	$('#iTOTAL').text( parseInt($('#iTOTAL').text()) - parseInt($('#idImporte' + registroAP).text()) )
	DevueltaAlCliente();

	var itemA = new Object();
	itemA.Codigo 	= $('#iCodigo' + registroAP).text();
	itemA.Cantidad 	= $('#iCantidad' + registroAP).val();
	itemA.Precio 	= $('#iPrecio' + registroAP).val();
	itemA.Descuento = $('#iDescuento' + registroAP).val();

	// itemA = JSON.stringify(datos);
	prodLS['A' + registroAP] = JSON.stringify(itemA);
	itemsApartar = [];
	
	$('#idItemF' + registroAP).html('');

	for(i=1; i<=RegCOUNT; i++){
		if(prodLS['A' + i] != undefined)
		{
			itemAp = JSON.parse(prodLS['A' + i]);
			itemsApartar.push(itemAp);
		}
	}

	$dataApartar.itemsApartar = itemsApartar;
}
//**************************************************************


//FUNCION PARA GUARDAR EL GRUPO DE PRODUCTOS A FACTURAR
function ClasificarFacturados(){	

	if ($cambio == 1){
		itemsfactura = [];
		$dataFacturar = {};

		for (i=1; i<=RegCOUNT; i++){
			Codigo 		= $('#iCodigo' + i).text();
			Cantidad 	= $('#iCantidad' + i).val()
			Precio 		= $('#iPrecio' + i).val();
			Desc 		= $('#iDescuento' + i).val();

			var item = new Object();
			item.Codigo = Codigo;
			item.Cantidad = Cantidad;
			item.Precio = Precio;
			item.Descuento = Desc;

			itemsfactura.push(item);

			// prodLS['F' + i] =  JSON.stringify();			
			// itemsfactura.push(JSON.parse(prodLS.getItem(prodLS.key(i-1))));
		}

		$dataFacturar.itemsfactura = itemsfactura;
		$cambio = 0;	
	}
}
//**************************************************************


//FUNCION PARA GUARDAR EL GRUPO DE PRODUCTOS APARTADOS
function ClasificarApartados(){

	for (i=0; i<prodLS.length; i++){
		if(prodLS.key(i).substring(0,1) == 'A')
			console.log('');
			// $dataApartar.itemsapartar.push(prodLS.getItem(prodLS.key(i)));
			// $dataApartar = $dataApartar + prodLS.getItem(prodLS.key(i)) + ',';
	}
}
//**************************************************************


//FUNCION PARA GUARDAR LA FACTURA
function facturarImprimir(e){

	if(ValidarCampos()){
		ClasificarFacturados();
		ClasificarApartados();
		
		var csrftoken = getCookie('csrftoken');

		$.ajaxSetup({
		    beforeSend: function(xhr, settings) {
		        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		            xhr.setRequestHeader("X-CSRFToken", csrftoken);
		        }
		    }
		});
		
		//ENVIAR POST MEDIANTE AJAX PARA GUARDAR FACTURA EN BASE DE DATOS
		$.ajax({
		    type: "POST",
		    url: "http://127.0.0.1:8000/facturar/",
		    data: JSON.stringify({'items': $dataFacturar.itemsfactura}),
		    contentType: 'application/json; charset=utf-8',

		    success: function (data) {
		    	if (data >= 1){

		    		data = 'La factura '+ data +' se guardó con exito!';
		    		
		    		$('#btnImprimir').removeClass('AddItem');
		    		// $('#btnImprimir').removeClass('PrintFact');
		    		$('#btnImprimir').addClass('InhabilitaBoton');

		    		$('#btnImprimir').attr('href','#');
		        	$('#iMessage').addClass('Guardado');
		    	}

		        $('#iMessage').text(data);
		    }
		});

	}
	else
	{
		$('#iMessage').text('Favor verificar que los campos han sido completados.').removeClass('Guardado');

	}
}
//**************************************************************

//FUNCION PARA GUARDAR PRODUCTOS APARTADOS
function ApartarProductos(e){

	if(ValidarCamposApartados()){
		//ClasificarFacturados();
		//ClasificarApartados();
		
		var csrftoken = getCookie('csrftoken');

		$.ajaxSetup({
		    beforeSend: function(xhr, settings) {
		        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		            xhr.setRequestHeader("X-CSRFToken", csrftoken);
		        }
		    }
		});
		
		//ENVIAR POST MEDIANTE AJAX PARA GUARDAR FACTURA EN BASE DE DATOS
		$.ajax({
		    type: "POST",
		    url: "http://127.0.0.1:8000/apartados/",
		    data: JSON.stringify({'items': $dataFacturar.itemsfactura, 'cliente': prodLS['cliente']}),
		    contentType: 'application/json; charset=utf-8',

		    success: function (data) {
		    	// if (data >= 1){

		    	// 	data = 'La factura '+ data +' se guardó con exito!';
		    		
		    	// 	$('#btnImprimir').removeClass('AddItem');
		    	// 	// $('#btnImprimir').removeClass('PrintFact');
		    	// 	$('#btnImprimir').addClass('InhabilitaBoton');

		    	// 	$('#btnImprimir').attr('href','#');
		     	//  $('#iMessage').addClass('Guardado');
		     	//	$('#iMessage').text(data);
		    	//}

		        $('#iMessage').text(data);

		    }
		});

		        console.log(JSON.stringify({'items': $dataFacturar.itemsfactura, 'cliente': prodLS['cliente']}));


	}
	else
	{
		$('#iMessage').text('Favor verificar que los campos han sido completados.').removeClass('Guardado');

	}
}
//**************************************************************