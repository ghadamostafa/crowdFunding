 $(document).ready(function () {

    $("#reportProject").on('click', function(event){
        console.log("add report");
          var csrftoken = $.cookie('csrftoken');
            function csrfSafeMethod(method) {
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }
            $.ajaxSetup({
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
            });
            reportedid=$("#reportProject").val();
            console.log(reportedid)
            $.ajax({
                   url: "/report/",
                   method: "POST",
                   data: {'reportedid':reportedid},
                   success: function (jason) {

                        console.log(jason);
                   },
                    error : function(xhr,errmsg,err) {

                        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                    }

                });
 });
});

