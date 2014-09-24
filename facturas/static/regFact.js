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

$('#iProd').on('input', function(){
	// $('')alert(valor);
})

//ACCION DE FACTURAR O APARTAR
$('#BtFacturar').click(function(){
	$('#idApartados').addClass('Apartados');
	$('#idFacturacion').removeClass('Facturacion');
})

$('#BtApartar').click(function(){
	$('#idApartados').removeClass('Apartados');
	$('#idFacturacion').addClass('Facturacion');
})