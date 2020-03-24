 $(document).ready(function () {
 	console.log("hi")
 	$('.category_id').on('click', function(event){
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
 		console.log("li")
 		category_id=$(this).val();
 		currentRow=this
 		$.ajax({
        url : `/categoryProjects/`,
        type : "POST", 
        data : { "category_id":category_id}, 
        success : function(json) {
        	console.log()
        	$(currentRow).append(`<div class="display-block">
        		<ul class="projects">
        		</ul>
        		</div>`);
        	json.forEach(function(item){
        		console.log(item.id)
        		$(".projects").append(`<li><a href="/project/${item.id}">${item.Title}</a></li>`)
        	});
        	
        	$(".projects").removeClass("projects")
		
        },
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
        });
        $(this).off();
		$(this).click(function () {
			console.log("first ajax second click");
			console.log($(this).after("div"));
			$(this).children("div").toggleClass("display-block display-none");
			});
 });
 });