$(document).ready(function() {
    $('#send-info').click(function() {

        $.ajax({
            type: "POST",
            url: "http://" + window.location.host + "/SaveComment",
            data: $(".form-info").serialize(),
            beforeSend: function(){

                $(".resualt").html("...در حال انجام")

             },
            success: function(response) {
                if (response=="true")
                    $(".resualt").html("اطلاعات شما ثبت شد ✔")
                
                else if (response=="false")
                    $(".resualt").html("در ثبت اطلاعات شما مشکل پیش آمد ")

                else 
                    $(".resualt").html("فرم نا معتبر است 404")


            },
            error: function(xhr, status, error) {
               
                $(".resualt").html("خطا رخ داد");
                
              
            }
        });
    });
});