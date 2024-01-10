$(function (){
	$('#add_item').click(funtion () {
		$('ul.my_list').append('<li>Item</li>');
	});
});

$(function () {
	$('#remove-Item').click(function () {
		  $('ul.my_list').last().remove();
	});
});

$(function  () {
	$('#clear_list').click(function (){
		$('ul.my_list').empty();
	});
});
