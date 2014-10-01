// SELECCIONAR TEXTO COMPLETO CUANDO ENTRA EL FOCUS
$("input[type='text']").click(function () {
   $(this).select();
});


// SECCION DE APARTADOS
$(document).ready(function() {
	$('#idApartados').addClass('Apartados');
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

	clone.find('#iCodigo').text(codigo);
	clone.find('#iDescripcion').text(descrp);
	clone.find('#iPrecio').val(varprecio);
	clone.find('#iCantidad').val('1');

	clone.addClass(departamento);
	clone.find('#iPrecio').addClass(departamento);
	clone.find('#iCantidad').addClass(departamento);
	clone.find('#iDescuento').addClass(departamento);
	clone.find('#iImporte').addClass(departamento);

	$content.append(clone);

	clone.fadeIn();

}

// FUNCION DEL BOTON AGREGAR
$('#btAdd').click(function(){
	// agregarProducto('BLU01','Blusa con manga','150');
});


// VARIABLE PARA EL CONTENIDO DE LA TABLA DE PRODUCTOS
var contenido = $('#productosajax');

// FUNCION PARA BUSCAR LOS PRODUCTOS EN LA API Y DIBUJAR LA TABLA CON LOS PRODUCTOS ENCONTRADOS
$('#iProd').on('input', function(e){
	e.defaultPrevented = false;

	$.getJSON('http://127.0.0.1:8000/api/productos/' + $('#iProd').val() +'/?format=json',
		function(data) {
			contenido.html('');

			$.each(data, function(index, element) {
				contenido.append(
					'<tr class="DetailsItemSearch">' + 
					'<td class="CellItemDetailSearch '+ element['departamento'] +'">' + element['codigo'] +'</td>' +					
					'<td class="CellItemDetailSearch '+ element['departamento'] +'">'
						+'<a href="javascript:void(0);" class="aProd"' 	
						+'onclick="agregarProducto(&quot;' 
							+ element['codigo'] + '&quot;, &quot;' 
							+ element['descripcion'] + '&quot;, &quot;'
							+ element['departamento'] + '&quot;, &quot;'
							+ element['precio'] + '&quot;); return false;">' + element['descripcion'] +'</a></td>' +
					'<td class="CellItemDetailSearch '+ element['departamento'] +'">' + element['precio'] +'</td>' +
					'</tr>'
					);
			})
			contenido.hide();
			contenido.fadeIn('1');	
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