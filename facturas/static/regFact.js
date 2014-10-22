//var $prodLS = localStorage;
var RegCOUNT = 0;
var $i = 0;
var $dataFacturar = [];
var $dataApartar = [];

// SELECCIONAR TEXTO COMPLETO CUANDO ENTRA EL FOCUS
$('#iProd').click(function () {
   $(this).select();
});

// SECCION DE APARTADOS
$(document).ready(function() {
	localStorage.clear();

	// VARIABLE QUE CONTIENE TODOS LOS PRODUCTOS EN UNA TUPLA
	prodLS = localStorage;
	RegCOUNT = 0;
})

// CUANDO SEA QUITADO EL FOCUS DE LA BUSQUEDAD DE PRODUCTOS
$('#iProd').blur(function(){
	$('#productosajax').fadeOut('fast');
});

// FUNCION PARA AGREGAR UN PRODUCTO A LA TABLA
function agregarProducto(codigo, descrp, departamento, varprecio){

	$('#Items').removeClass('HideItem');

	$content = $('#Items');

	RegCOUNT = RegCOUNT + 1;
	
	Cantidad = '1';
	Codigo = codigo;
	Precio = varprecio;

	var item = new Object();
	item.Codigo = Codigo;
	item.Cantidad = Cantidad;
	item.Precio = Precio;

	prodLS['F' + RegCOUNT] =  JSON.stringify(item);

	$content.append('<tr class="DetailsItem" id="idItemF' + RegCOUNT + '">' +
						'<td class="CellItemDetail ' + departamento + ' dCod" id="iSec'+ RegCOUNT +' ">' + RegCOUNT +' </td>' +
						'<td class="CellItemDetail ' + departamento + ' dCod" id="iCodigo'+ RegCOUNT +'">' + codigo + ' </td>' +
						'<td class="CellItemDetail ' + departamento + ' dDescrp" id="iDescripcion'+ RegCOUNT +'">' + descrp + ' </td>' +
						'<td class="CellItemDetail ' + departamento + ' dCant"> <input id="iCantidad'+ RegCOUNT +'" onkeypress="return EventosTextBox(1,'+ RegCOUNT +');" type="text" value="1" class="TextBoxes TextItems" PlaceHolder="0.00"/> </td>' +
						'<td class="CellItemDetail ' + departamento + ' dPrecio"> <input id="iPrecio'+ RegCOUNT +'" onkeypress="return EventosTextBox(2,'+ RegCOUNT+');" type="text" class="TextBoxes TextItems" PlaceHolder="0.00"/></td>' +
						'<td class="CellItemDetail ' + departamento + ' dDesc"> <input id="iDescuento'+ RegCOUNT +'" onkeypress="return EventosTextBox(3,'+ RegCOUNT+');" type="text" class="TextBoxes TextItems" PlaceHolder="0.00"/> </td>' +
						'<td class="CellItemDetail ' + departamento + ' dImporte"> <span id="idImporte'+ RegCOUNT +'"> 0.00 </span> </td>' +
						'<td class="CellDelete CellItemDetail" id="idDelete'+ RegCOUNT +'"><a href="javascript:EliminarReg(' + RegCOUNT + ')" class="DelItem icon-delete"> </a> </td>' +
						'<td class="CellDelete CellItemDetail" id="idApartar'+ RegCOUNT +'"><a href="javascript:ApartarReg('+ RegCOUNT +')" class="ApartarItem icon-spinner"> </a> </td>' +
					'</tr>').hide().fadeIn('fast');


	//SELECCIONAR EL TEXTO COMPLETO DE LOS SIGUIENTES CAMPOS
	$('#iCantidad' + RegCOUNT).click(function(){$(this).select();});
	$('#iPrecio' + RegCOUNT).click(function(){$(this).select();});
	$('#iDescuento' + RegCOUNT).click(function(){$(this).select();});
	//*****FIN SELECCION COMPLETA DE TEXTO EN CAMPOS**********
	
	CalculaLinea(RegCOUNT);

	$('#iCantidad' + RegCOUNT).focus().select();
}

function EventosTextBox(concepto, posicion){

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

function ClasificarFacturados(){	

	for (i=0; i<prodLS.length; i++){
		if(prodLS.key(i).substring(0,1) == 'F')
			$dataFacturar.push(prodLS.getItem(prodLS.key(i)));
			// $dataFacturar = $dataFacturar + prodLS.getItem(prodLS.key(i)) + ',';
	}
}

function ClasificarApartados(){

	for (i=0; i<prodLS.length; i++){
		if(prodLS.key(i).substring(0,1) == 'A')
			$dataApartar.push(prodLS.getItem(prodLS.key(i)));
			// $dataApartar = $dataApartar + prodLS.getItem(prodLS.key(i)) + ',';
	}
}

//FUNCION PARA ELIMINAR REGISTRO
function EliminarReg(registroDEL){
	$('#idItemF'+registroDEL).html('');
	prodLS['F' + registroDEL] = '';
}

//FUNCION PARA APARTAR REGISTRO
function ApartarReg(registroAP){

	$('#iTOTAL').text( parseInt($('#iTOTAL').text()) - parseInt($('#idImporte' + registroAP).text()) )
	DevueltaAlCliente();

	var datos = new Object();
	datos.Codigo = $('#iCodigo' + registroAP).text();
	datos.Cantidad = $('#iCantidad' + registroAP).val();
	datos.Precio = $('#iPrecio' + registroAP).val();
	datos.Descuento = $('#iDescuento' + registroAP).val();

	itemA = JSON.stringify(datos);
	prodLS['A' + registroAP] = itemA;
	prodLS.removeItem('F' + registroAP);
	$('#idItemF' + registroAP).html('');
}

// FUNCION DEL BOTON AGREGAR
$('#btNew').click(function(){
	$(document).refresh();
});


// VARIABLE PARA EL CONTENIDO DE LA TABLA DE PRODUCTOS
var contenido = $('#productosajax');

$('#iPrecio').on('input',CalculaLinea);

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

//CADA VEZ QUE SE DIGITE EN LA CASILLA DE PAGO ACTUALIZA LA DEVUELTA AL CLIENTE.
$('#iPagoF').on('input', function(){

	DevueltaAlCliente();
})

//CALCULA LA DEVUELTA EN DINERO QUE SE DEBE ENTRAR AL CLIENTE
function DevueltaAlCliente(){

	$('#iCambioF').text( $('#iPagoF').val() - parseInt($('#iTOTAL').text()) );
}

// FUNCION PARA BUSCAR LOS PRODUCTOS EN LA API Y DIBUJAR LA TABLA CON LOS PRODUCTOS ENCONTRADOS
$('#iProd').on('input', function(e){
	e.defaultPrevented = false;

	$.getJSON('http://127.0.0.1:8000/api/productos/' + $('#iProd').val() +'/?format=json',
		function(data) {
			contenido.html('');

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
			})
			contenido.hide();
			contenido.fadeIn('fast');
		});
});

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


//FUNCION PARA GUARDAR LA FACTURA
function facturarImprimir(e){

	ClasificarFacturados();
	ClasificarApartados();

	
	var csrftoken = getCookie('csrftoken');

	//var csrftoken = $.cookie('csrftoken');

	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    }
	});


	$.ajax('http://127.0.0.1:8000/facturar/', {
	    type : 'POST', 
	    contentType : 'json',
	    data : {
	    // data : {itemsToAdd: JSON.stringify($dataFacturar)
	    		 'itemsToAdd': $dataFacturar
	    		},
	    // data : {items: JSON.stringify($dataFacturar)},
	    success: function (data) {
	        $('#iMessage').text(data);
	    }
	    

});
	// console.log($dataFacturar);
	// $.post("/facturar/", $dataFacturar, function(returnedData) {
	// 	$('#iMessage').text('La factura fue guardada con exito.');
	// })
}
