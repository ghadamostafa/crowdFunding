
 $(document).ready(function () {
 	console.log("ready");

$('#add').on('click', function(event){
	console.log("add comment");
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
        comment_body=$("textarea").val()
        pid=$("#pid").val()

	$.ajax({
        url : "/addComment/",
        type : "POST", 
        data : { "comment_body":comment_body,"pid":pid}, 
        success : function(json) {
        	comment_body=json.comment_body;
        	user_name=json.user_name;
        	$("#commentsBody").append(`
        		<div class="media g-mb-30 media-comment">
            <img class="d-flex g-width-50 g-height-50 rounded-circle g-mt-3 g-mr-15" src="https://bootdey.com/img/Content/avatar/avatar7.png" alt="Image Description">
            <div class="media-body u-shadow-v18 g-bg-secondary g-pa-30">
              <div class="g-mb-15">
                <h5 class="h5 g-color-gray-dark-v1 mb-0">${user_name}</h5>
                <span class="g-color-gray-dark-v4 g-font-size-12">5 days ago</span>
              </div>
        
              <p>${comment_body}</p>
        
              <ul class="list-inline d-sm-flex my-0">
                <li class="list-inline-item g-mr-20">
                  <a class="u-link-v5 g-color-gray-dark-v4 g-color-primary--hover" href="#!">
                    <i>Report</i>
                    
                  </a>
                </li>
                <li class="list-inline-item ml-auto">
                  <a class="u-link-v5 g-color-gray-dark-v4 g-color-primary--hover" href="#!">
                    <i class="fa fa-reply g-pos-rel g-top-1 g-mr-3"></i>
                    Reply
                  </a>
                </li>
              </ul>
            </div>
        </div>

        	`)
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {

            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });

});

// //delete Post
// $("#deletePost").on('click',function(event){
// 	project_id=$("#deletePost").val();
// 	console.log(project_id);
// 	$.ajax({
//         url : "/deletePost/",
//         type : "POST", 
//         data : { "project_id":project_id}, 
//         success : function(json) {

//         },
//         error : function(xhr,errmsg,err) {

//             console.log(xhr.status + ": " + xhr.responseText); 
//         }
//     });

// });




 
});
