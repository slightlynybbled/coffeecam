$(document).ready(
    function(){
        /* submit time using a post request */
        var date = new Date();
        $.post(
            '/set_time',
            {
                "date": date.getTime(),
                'timezoneOffset': date.getTimezoneOffset() * 60.0
            }
        );
    }
);
