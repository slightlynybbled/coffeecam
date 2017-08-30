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

        /* using this interval to update user stats */
        setInterval(
            function(){
                $.post(
                    '/users',
                    {},
                    function(data){
                        var users = data["current_user_list"];
                        $("#currentUsers").text(users.join(", "));
                    }
                );
            },
            5000
        )
    }
);
