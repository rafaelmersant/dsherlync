var $prodLS = localStorage;
var RegCOUNT = 0;
var $i = 0;

// SELECCIONAR TEXTO COMPLETO CUANDO ENTRA EL FOCUS
$('#iProd').click(function () {
   $(this).select();
});

// SECCION DE APARTADOS
$(document).ready(function() {
	$('#idApartados').addClass('Apartados');
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
	item = {'Codigo': Codigo, 'Cantidad': Cantidad, 'Precio': Precio};
	prodLS[RegCOUNT] =  JSON.stringify(item);

	$content.append('<tr class="DetailsItem" id="idItemF"' + RegCOUNT + '>' +
						'<td class="CellItemDetail ' + departamento + ' dCod" id="iSec'+ RegCOUNT +' ">' + RegCOUNT +' </td>' +
						'<td class="CellItemDetail ' + departamento + ' dCod" id="iCodigo'+ RegCOUNT +'">' + codigo + ' </td>' +
						'<td class="CellItemDetail ' + departamento + ' dDescrp" id="iDescripcion'+ RegCOUNT +'">' + descrp + ' </td>' +
						'<td class="CellItemDetail ' + departamento + ' dCant"> <input id="iCantidad'+ RegCOUNT +'" onkeypress="return event.charCode >= 48 && event.charCode <= 57" type="text" value="1" class="TextBoxes TextItems" PlaceHolder="0.00"/> </td>' +
						'<td class="CellItemDetail ' + departamento + ' dPrecio"> <input id="iPrecio'+ RegCOUNT +'" onkeypress="return event.charCode >= 48 && event.charCode <= 57" type="text" class="TextBoxes TextItems" PlaceHolder="0.00"/></td>' +
						'<td class="CellItemDetail ' + departamento + ' dDesc"> <input id="iDescuento'+ RegCOUNT +'" onkeypress="return event.charCode >= 48 && event.charCode <= 57" type="text" class="TextBoxes TextItems" PlaceHolder="0.00"/> </td>' +
						'<td class="CellItemDetail ' + departamento + ' dImporte"> <span id="idImporte'+ RegCOUNT +'"> 0.00 </span> </td>' +
						'<td class="CellDelete CellItemDetail" id="idDelete'+ RegCOUNT +'"><a href="#" class="DelItem icon-delete"> </a> </td>' +
						'<td class="CellDelete CellItemDetail" id="idApartar'+ RegCOUNT +'"><a href="#" class="ApartarItem icon-spinner"> </a> </td>' +
					'</tr>').fadeIn('fast');


	//SELECCIONAR EL TEXTO COMPLETO DE LOS SIGUIENTES CAMPOS
	$('#iCantidad' + RegCOUNT).click(function(){$(this).select();});
	$('#iPrecio' + RegCOUNT).click(function(){$(this).select();});
	$('#iDescuento' + RegCOUNT).click(function(){$(this).select();});
	//*****FIN SELECCION COMPLETA DE TEXTO EN CAMPOS**********
	
	CalculaLinea(RegCOUNT);
}


// FUNCION DEL BOTON AGREGAR
$('#btAdd').click(function(){
	// agregarProducto('BLU01','Blusa con manga','150');
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
		console.log($t);
	}

	$('#iTOTAL').text(valor);
}

$('#iPagoF').on('input', function(){
	$('#iCambioF').text($('#iPagoF').val() - parseInt($('#iTOTAL').text()));
})
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


//ACCION DE FACTURAR O APARTAR
$('#BtFacturar').click(function(){
	$('#idApartados').addClass('Apartados');
	$('#idFacturacion').removeClass('Facturacion');
})

$('#BtApartar').click(function(){
	$('#idApartados').removeClass('Apartados');
	$('#idFacturacion').addClass('Facturacion');
})