setTimeout(function(){
    $('#message').fadeOut();
},4000)

const defaultPrice = $('#price').val().split("$")[1] * 1
$('#persons').change( function(){
   let price_tag = ('#price')
   let people = $(this).val() * 1
   let totalPrice = defaultPrice * people
   $(price_tag).val(totalPrice)



}

);



        