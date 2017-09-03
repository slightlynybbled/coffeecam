$(document).ready(
    function(){
        $(window).keydown(function(event){
            if(event.keyCode === 13) {
                event.preventDefault();
                return false;
            }
        });

        /* submit time using a post request */
        var date = new Date();
        $.post(
            '/set_time',
            {
                "date": date.getTime(),
                'timezoneOffset': date.getTimezoneOffset() * 60.0
            }
        );

        /* using this interval to update user stats, message boards */
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

                getMessages();
            },
            2000
        );

        /* sending messages */
        $("#submitMessage").click(
            function(){
                var value = $("#messageInput").val();
                $.post(
                    '/message',
                    {
                        "message": value
                    },
                    function(){
                        getMessages();
                        $("#messageInput").val('');
                    }
                );
            }
        );
    }
);

function getMessages(){
    $.post(
        '/messages',
        {},
        function(messages){
            var msgs = messages['messages'];
            console.log(msgs);
            $("#messageTable").find("tr").remove();

            msgs.forEach(function(point){
                var user_html = '<td>' + point['user'] + '</td>';
                var time_html = '<td>' + point['time'] + '</td>';
                var message_html = '<td>' + point['message'] + '</td>';

                var html = "<tr>" + user_html + time_html + message_html + "</tr>";
                $('#messageTable').append(html);
            });
        }
    );
}
