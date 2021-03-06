        var ratedIndex = -1, uID = 0;

        $(document).ready(function () {

            resetStarColors();

            if (localStorage.getItem('ratedIndex') != null) {
                setStars(parseInt(localStorage.getItem('ratedIndex')));
                uID = localStorage.getItem('user_id');
            }

            $('.fa-star').on('click', function () {
               ratedIndex = parseInt($(this).data('index'));
               localStorage.setItem('ratedIndex', ratedIndex);
               saveToTheDB();
//               $(#avg).innerText(`${avg}`)
            });

            $('.fa-star').mouseover(function () {
                resetStarColors();
                var currentIndex = parseInt($(this).data('index'));
                setStars(currentIndex);
            });

            $('.fa-star').mouseleave(function () {
                resetStarColors();

                if (ratedIndex != -1)
                    setStars(ratedIndex);
            });
        });

        function saveToTheDB() {
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
            $.ajax({
               url: "/project/save",
               method: 'POST',
               data: {
                  // 'csrfmiddlewaretoken': "{% csrf_token %}",
                  'uID': uID,
                  'ratedIndex': ratedIndex
               },
               success: function (r) {
                    uID = r.id;
                    localStorage.setItem('user_id', uID);
                    avg=r.avg;
               }
            });
        }
        function setStars(max) {
            for (var i=0; i <= max; i++)
                $('.fa-star:eq('+i+')').css('color', 'gold');
        }
        function resetStarColors() {
            $('.fa-star').css('color', 'lightgray');
        }