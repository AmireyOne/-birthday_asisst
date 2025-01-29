
$(document).ready(function () {

  
    $(document).on('click', '.send-info', function () {

          $.ajax({
              url: "http://" + window.location.host + "/SaveInformation",
              type: "POST",
              data: $("#information").serialize(),
              beforeSend: function() {
                  $("#resualt").html("...در حال انجام");
              },
              success: function(response) {
                  if(response == "true") {
                      $("#resualt").html("اطلاعات شما با موفقیت ثبت شد✔");
                  } else if (response == "phone error") {
                      $("#resualt").html("لطفا تلفن همراه را با فرمت صحیح 09123456789 وارد کنید ‼");

                  } else if (response == "phone numeric") {
                      $("#resualt").html("خطا: شماره تلفن باید فقط شامل اعداد باشد");

                  } else if (response == "exist") {
                        $("#resualt").html( " خطا: اطلاعات شما از قبل در سایت وجود دارد  ‼"  );    

                  } else if (response == "phone exist") {
                    $("#resualt").html( " خطا: این شماره تلفن از قبل در سایت وجود دارد  ‼"  );    

                  } else if (response == "email exist") {
                        $("#resualt").html( " خطا: این ایمیل از قبل در سایت وجود دارد  ‼"  );    
                  } 
                  
                  
                  else {
                      console.log(response);
                      $("#resualt").html("ثبت اطلاعات با خطا مواجه شد❌");
                  }
              },
              error: function (xhr, status, error) {
                  // خطا در درخواست
                  $("#resualt").html(`<p style="color:red;">خطا: ${error}</p>`);
              },
          });
      });

    });


        // اطمینان از اینکه دکمه send-info به رویداد مربوطه متصل شده است
    $(document).on('click', '.send-adress', function () {
       

            $.ajax({
                url: "http://" + window.location.host + "/SaveAdress",
                type: "POST",
                data: $("#information_adress").serialize(),
                beforeSend: function() {
                    $("#resualt_adress").html("...در حال انجام");
                },
                success: function(response) {
                    if(response == "true") {
                        
                        $("#resualt_adress").html("آدرس شما با موفقیت ثبت شد✔");
                    } 
                    else if (response == "postcode not 10") {
                    $("#resualt_adress").html("خطا: کدپستی باید 10 رقم باشد !!" );
                    }
                    else if (response == "not numeric") {
                        $("#resualt_adress").html("خطا: واحد ، پلاک و کدپستی باید فقط از اعداد تشکیل شوند !!" );
                        }
                    else {
                        console.log(response);
                        $("#resualt_adress").html("ثبت اطلاعات با خطا مواجه شد❌");
                    }
                },
                error: function (xhr, status, error) {
                    // خطا در درخواست
                    $("#resualt_adress").html(`<p style="color:red;">خطا: ${error}</p>`);
                },
            });
        });


    
    $(document).on('click', '#btn-send', function () {

        $.ajax({
            url: "http://" + window.location.host + "/SendMessageManagement",
            type: "POST",
            data: $("#form-message").serialize(),
            beforeSend: function() {
                $("#resualt-message").html("...در حال انجام");
            },
            success: function(response) {
                if(response == "true") {
                    $("#resualt-message").html("پیام شما با موفقیت ثبت شد✔");

                } else if (response == "false") {
                    $("#resualt-message").html("خطایی رخ داد ، لطفا بعدا امتحان کنید");
                }    

                else {
                    console.log(response);
                    $("#resualt-message").html("ثبت پیام با خطا مواجه شد❌");
                }
            },
            error: function (xhr, status, error) {
                // خطا در درخواست
                $("#resualt-message").html(`<p style="color:red;">خطا: ${error}</p>`);
            },
        });
    });



    
      




function setdata(phone , email , time  )
{
    
    $("#phone").val(phone);
    $("#email").val(email);
    $("#time").val(time); 

}   

