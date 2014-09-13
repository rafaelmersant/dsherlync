$('#btAdd').click(function(){
	$Item = $('#idItem');
	$content = $('#Items');

	clone = $Item.clone();

	
	clone.hide();
	$content.append(clone);

	clone.fadeIn();
});

// $('#idProd')