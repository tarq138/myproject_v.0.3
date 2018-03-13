var slideNow = 1;
var slideCount = $('#slidewrapper').children().length;
var slideInterval = 5000;
var navBtnId = 0;
var translateWidth = 0;

$(document).ready(function() {
    var switchInterval = setInterval(nextSlide, slideInterval);

    $('#viewport').hover(function() {
        clearInterval(switchInterval);
    }, function() {
        switchInterval = setInterval(nextSlide, slideInterval);
    });

    $('#next-btn').click(function() {
        nextSlide();
    });

    $('#prev-btn').click(function() {
        prevSlide();
    });

    $('.slide-nav-btn').click(function() {
        navBtnId = $(this).index();

        if (navBtnId + 1 != slideNow) {
            translateWidth = -$('#viewport').width() * (navBtnId);
            $('#slidewrapper').css({
                'transform': 'translate(' + translateWidth + 'px, 0)',
                '-webkit-transform': 'translate(' + translateWidth + 'px, 0)',
                '-ms-transform': 'translate(' + translateWidth + 'px, 0)',
            });
            slideNow = navBtnId + 1;
        }
    });
});


function nextSlide() {
    if (slideNow == slideCount || slideNow <= 0 || slideNow > slideCount) {
        $('#slidewrapper').css('transform', 'translate(0, 0)');
        slideNow = 1;
    } else {
        translateWidth = -$('#viewport').width() * (slideNow);
        $('#slidewrapper').css({
            'transform': 'translate(' + translateWidth + 'px, 0)',
            '-webkit-transform': 'translate(' + translateWidth + 'px, 0)',
            '-ms-transform': 'translate(' + translateWidth + 'px, 0)',
        });
        slideNow++;
    }
}

function prevSlide() {
    if (slideNow == 1 || slideNow <= 0 || slideNow > slideCount) {
        translateWidth = -$('#viewport').width() * (slideCount - 1);
        $('#slidewrapper').css({
            'transform': 'translate(' + translateWidth + 'px, 0)',
            '-webkit-transform': 'translate(' + translateWidth + 'px, 0)',
            '-ms-transform': 'translate(' + translateWidth + 'px, 0)',
        });
        slideNow = slideCount;
    } else {
        translateWidth = -$('#viewport').width() * (slideNow - 2);
        $('#slidewrapper').css({
            'transform': 'translate(' + translateWidth + 'px, 0)',
            '-webkit-transform': 'translate(' + translateWidth + 'px, 0)',
            '-ms-transform': 'translate(' + translateWidth + 'px, 0)',
        });
        slideNow--;
    }
}

var check_roof = $('#roof');
var check_water = $('#water');
var check_front = $('#front');
var total_price = check_roof.data("price");
function func_roof(){
    var checkBox = document.getElementById("roof");
    var price_poof = check_roof.data("roof");
    if (checkBox.checked == true){
       total_price = Number(total_price) + Number(price_poof);
    } else {
       total_price = Number(total_price) - Number(price_poof);
    }
    $(".price h2").html('<h2 style="color: #28a745; text-align: right">'+total_price+'</h2>');
}
function func_water(){
    var checkBox = document.getElementById("water");
    var price_water = check_water.data("water");
    if (checkBox.checked == true){
       total_price = Number(total_price) + Number(price_water);
    } else {
       total_price = Number(total_price) - Number(price_water);
    }
    $(".price h2").html('<h2 style="color: #28a745; text-align: right">'+total_price+'</h2>');
}
function func_front(){
    var checkBox = document.getElementById("front");
    var price_front = check_front.data("front");
    if (checkBox.checked == true){
       total_price = Number(total_price) + Number(price_front);
    } else {
       total_price = Number(total_price) - Number(price_front);
    }
    $(".price h2").html('<h2 style="color: #28a745; text-align: right">'+total_price+'</h2>');
    //console.log(total_price);
}