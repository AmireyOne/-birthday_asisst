$(document).ready(function() {
    $('#add-comment').click(function() {

        $.ajax({
            type: "POST",
            url: "http://" + window.location.host + "/SaveComment",
            data: $(".form_comment").serialize(),
            beforeSend: function(){

                $(".resualt-comment").html("...در حال انجام")

             },
            success: function(response) {
                if (response=="true")
                    $(".resualt-comment").html("نظر شما با موفقیت ثبت شد و پس از تایید مدیر در قسمت نظرات نمایش داده خواهد شد ✔")
                
                else if (response=="false")
                    $(".resualt-comment").html("برای ثبت نظر ابتدا باید عضوی از سایت ما بشوید ❤")

                else 
                    $(".resualt-comment").html("فرم نا معتبر است 404")


            },
            error: function(xhr, status, error) {
               
                $(".resualt-comment").html("خطا رخ داد");
                
              
            }
        });
    });
});


