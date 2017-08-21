$(document).ready(
    function(){
        setInterval(function(){
            $.post("/take_pic", {}, function(data){replacePic(data);});
        },
        10000);

        /* submit time using a post request */
        var date = new Date();
        $.post('/set_time', {"date": date.getTime(), 'timezoneOffset': date.getTimezoneOffset() * 60.0});
    }
);

function replacePic(data){
    var pic = $('#coffeepic');

    pic.fadeOut(200);
    pic.attr("src", data['src']);
    pic.fadeIn(200);
}
