$(document).ready(
    function(){
        setInterval(function(){
            // $('#coffeepic').load(document.URL +  ' #coffeepic');
            $.post("/take_pic", {}, function(data){replacePic(data);});
        },
        10000);

        $("#takePic").click(function(){
            $.post("/take_pic", {}, function(data){replacePic(data);});
        });

        /* submit time using a post request */
        var date = new Date();
        $.post('/set_time', {"date": date.getTime(), 'timezoneOffset': date.getTimezoneOffset() * 60.0});
    }
);

function replacePic(data){
    var pic = $('#coffeepic');
    var picPath = pic.prop('src');
    var newPicPath = picPath + "?" + (Math.random() * 1000000).toFixed(0);

    pic.fadeOut(200);
    pic.attr("src", newPicPath);
    pic.fadeIn(200);
}
