$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('.plus-cart,.minus-cart').click(function(){
    var id = $(this).attr('pid').toString();
    var action=$(this).hasClass('plus-cart')?'pluscart':'minuscart'
console.log(id)
$.ajax({
    url:"pluscart",
    type:'GET',
    data:{'id':id,'action':action},
    success:function(data){
        console.log(data)
        $('#quantity').text(data.new_quantity)
        $('.amount').text(data.amount)
        $('.tamount').text(data.tamount)
    }
})
})

$('.removecart').click(function() {
    var id = $(this).attr("cid").toString();
    var row = $(this).closest(".row");// Find the closest parent <tr> element
    console.log(id);

    $.ajax({
        type: 'GET',
        url: '/removecart',
        data: { 'id': id },
        success: function(data) {
            console.log(data);
            $('.amount').text(data.amount);
            $('.tamount').text(data.tamount);
            row.remove(); // Remove the entire <tr> element
        }
    });
});

// $(document).ready(function() {
//     $(".plus-cart").slideUp(1000).delay(500).slideDown(1000);
// });