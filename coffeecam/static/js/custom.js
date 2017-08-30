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
                        var allUsers = data["num_of_users"];
                        var currentUsers = data["current_users"];

                        $("#numOfUsers").text(allUsers.toString());
                        $("#currentUsers").text(currentUsers.join(", "));
                    }
                );
            },
            5000
        )
    }
);
