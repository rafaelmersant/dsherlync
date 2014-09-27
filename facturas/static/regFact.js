$(document).ready(function() {
	$('#idApartados').addClass('Apartados');
})

$('#btAdd').click(function(){
	$Item = $('#idItem');
	$content = $('#Items');

	clone = $Item.clone();

	clone.hide();
	$content.append(clone);

	clone.fadeIn();
});

var contenido = $('#productosajax');

$('#iProd').on('input', function(e){
	e.defaultPrevented = false;

	contenido.html('<table class="tableItem">');

	$.getJSON('http://127.0.0.1:8000/api/productos/' + $('#iProd').val() +'/?format=json',
		function(data) {
			$.each(data, function(index, element) {
				contenido.append(
					'<tr class="DetailsItem">' + 
					'<td class="CellItemDetail '+ element['departamento'] +'">' + element['codigo'] 						+'</td>' +					
					'<td class="CellItemDetail '+ element['departamento'] +'"><a href="">' + element['descripcion'] 	+'</a></td>' +
					'<td class="CellItemDetail '+ element['departamento'] +'">' + element['precio'] 						+'</td>' +
					'</tr>'
					);
				console.log(element['departamento']);
			})
		});

	contenido.append('</table>').fadeIn();
});

	// $.ajax({
	// 	type: 'GET',
	// 	url: 'http://127.0.0.1:8000/api/productos/' + $('#iProd').val() +' /?format=json',
	// 	ContentType: 'application/json; charset=utf-8',
	// 	success: function(data) {
	// 		$('#productosajax').html('<h1>' + data.precio +'</H1>')
	// 		console.log(data);
	// 	}
	// })
	// $('#productosajax').html('<h1>'+ dato +'</h1>')
// })

//ACCION DE FACTURAR O APARTAR
$('#BtFacturar').click(function(){
	$('#idApartados').addClass('Apartados');
	$('#idFacturacion').removeClass('Facturacion');
})

$('#BtApartar').click(function(){
	$('#idApartados').removeClass('Apartados');
	$('#idFacturacion').addClass('Facturacion');
})