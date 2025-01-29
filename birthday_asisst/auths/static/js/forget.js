$('#send_codes').click(function () {



    $.ajax({
      url: "http://" + window.location.host + "/auth/sendcode",
      type: "POST",
      data: $("#send_code_phone").serialize(),
      beforeSend: function () {
        $("#resualt_code").html("...در حال انجام");
      },
      success: function (response) {
        if (response == "true") {

            const container = document.getElementById("container");
            container.classList.add("right-panel-active");
            


            $("#resualt_code").html("انجام شد");
        }
        else if (response == "not_valid") {

          $("#resualt_code").html("این شماره تلفن وجود ندارد ❌");
        }
        else if (response == "not_send_code") {

          $("#resualt_code").html("کد ارسال نشد ❌");
        }
        else {
          console.log(response);
          $("#resualt_code").html("ارسال کد با خطا مواجه شد❌");
        }
      },
      error: function (xhr, status, error) {
        // خطا در درخواست
        $("#resualt_code").html(`<p style="color:red;">خطا: ${error}</p>`);
      },
    });
  });


  $('#send_change').click(function () {



    $.ajax({
      url: "http://" + window.location.host + "/auth/pass_edit",
      type: "POST",
      data: $("#change_pass").serialize(),
      beforeSend: function () {
        $("#resualt_change").html("...در حال انجام");
      },
      success: function (response) {
        if (response == "true") {


            $("#resualt_change").html("انجام شد");

            setTimeout(function() {
              window.location.href = '/auth';
            }, 2000); // هدایت پس از ۵ ثانیه

        }
        else if (response == "wrong_code") {

          $("#resualt_change").html("کد تایید اشتباه است ، دوباره امتحان کنید ❌" );
          setTimeout(function() {
            window.location.href = '/auth';
          }, 2000); // هدایت پس از ۵ ثانیه


        }
        else if (response == "wrong_pass") {

          $("#resualt_change").html("رمز عبور با تکرار رمز عبور متفاوت است ، لطفا دوباره امتحان کنید ❌" );
          setTimeout(function() {
            window.location.href = '/auth';
          }, 2000); // هدایت پس از ۵ ثانیه


        }
       
        else {
          console.log(response);
          $("#resualt_change").html("تغییر رمز با خطا مواجه شد ❌");
          setTimeout(function() {
            window.location.href = '/auth';
          }, 2000); // هدایت پس از ۵ ثانیه

        }
      },
      error: function (xhr, status, error) {
        // خطا در درخواست
        $("#resualt_change").html(`<p style="color:red;">خطا: ${error}</p>`);
      },
    });
  });
