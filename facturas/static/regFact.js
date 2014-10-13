var $prodLS = localStorage;
var RegCOUNT = 0;

// SELECCIONAR TEXTO COMPLETO CUANDO ENTRA EL FOCUS
$("input[type='text']").click(function () {
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

	$Item = $('#idItem');
	$content = $('#Items');

	clone = $Item.clone();

	clone.hide();
	clone.removeClass('HideItem');
	clone.addClass('IDITEM');

	RegCOUNT = RegCOUNT + 1;

	//Cambiar los IDs para el nuevo registro
	clone.find('#idItem').html($('#idItem' + RegCOUNT).html());
	clone.find('#iCantidad').html($('#iCantidad' + RegCOUNT).html());
	clone.find('#iPrecio').html($('#iPrecio' + RegCOUNT).html());
	clone.find('#iDescuento').html($('#iDescuento' + RegCOUNT).html());
	clone.find('#iImporte').html($('#iImporte' + RegCOUNT).html());

	console.log('#idItem' + RegCOUNT);

	clone.find('#iSec').text(RegCOUNT);
	clone.find('#iCodigo').text(codigo);
	clone.find('#iDescripcion').text(descrp);
	//clone.find('#iPrecio').val(varprecio); //USADA PARA CUANDO VA A TRAER EL PRECIO DE BASE DE DATOS
	
	clone.find('#iCantidad' + RegCOUNT).val('1');
	clone.find('#iImporte' + RegCOUNT).text(($('#iCantidad' + RegCOUNT).val() * $('#iPrecio' + RegCOUNT).val()) - $('#iDescuento' + RegCOUNT).val() );
	
	console.log(clone);
	console.log(RegCOUNT);

	Cantidad = '1';
	Codigo = codigo;
	Precio = varprecio;

	item = {'Codigo': Codigo, 'Cantidad': Cantidad, 'Precio': Precio};

	prodLS[RegCOUNT] =  JSON.stringify(item);

	///clone.find('#iPrecio' + RegCOUNT).blur(CalculaLinea(RegCOUNT));

	clone.addClass(departamento);
	clone.find('#iPrecio' + RegCOUNT).addClass(departamento);
	clone.find('#iCantidad' + RegCOUNT).addClass(departamento);
	clone.find('#iDescuento' + RegCOUNT).addClass(departamento);
	clone.find('#iImporte' + RegCOUNT).addClass(departamento);

	clone.find('#iPrecio' + RegCOUNT).focus(function(){$(this).select();});

	$content.append(clone);

	clone.fadeIn();

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
	alert('CALCULA LINEA' + iReg);
}

// FUNCION PARA BUSCAR LOS PRODUCTOS EN LA API Y DIBUJAR LA TABLA CON LOS PRODUCTOS ENCONTRADOS
$('#iProd').on('input', function(e){
	e.defaultPrevented = false;

	$.getJSON('http://127.0.0.1:8000/api/productos/' + $('#iProd').val() +'/?format=json',
		function(data) {
			contenido.html('');

			$.each(data, function(index, element) {
				contenido.append(
					'<tr class="DetailsItemSearch" id=\"' + RegCOUNT +'\">' + 
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