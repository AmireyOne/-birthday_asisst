
$(document).ready(function () {
   
    $(document).on('click', '.send_remind', function () {
        

        $.ajax({
            url: "http://" + window.location.host + "/reminder/SaveRemind",
            type: "POST",
            data: $("#reminder-form").serialize(),
            beforeSend: function() {
                $("#resualt").html("...در حال انجام");
            },
            success: function(response) {
                if(response == "true") {
                    $("#resualt").html("یادآور شما با موفقیت ثبت شد✔");
                    setTimeout(function() {
                        location.reload(); // رفرش کردن صفحه بعد از 3 ثانیه
                    }, 3000); // 3000 میلی‌ثانیه (3 ثانیه)
                }
                else if (response == "Duplicate data")  {
                    $("#resualt").html("این یادآور از قبل وجود دارد ‼ ");
                }  
                else if (response == "edit true")  {
                    $("#resualtedit").html("ویرایش با موفقیت انجام شد ✔");
                }  
                
                else {
                    console.log(response);
                    $("#resualt").html("ثبت یادآور با خطا مواجه شد❌");
                }
            },
            error: function (xhr, status, error) {
                // خطا در درخواست
                $("#resualt").html(`<p style="color:red;">خطا: ${error}</p>`);
            },
        });
    });

    $(document).on('click', '.edit_remind', function () {
        
        
        $.ajax({
            url: "http://" + window.location.host + "/reminder/editRemind",
            type: "POST",
            data: $("#reminder-formedit").serialize(),
            beforeSend: function() {
                $("#resualtedit").html("...در حال انجام");
            },
            success: function(response) {
                if(response == "edit true") {
                    $("#resualtedit").html("ویرایش با موفقیت انجام شد ✔");
                    setTimeout(function() {
                        location.reload(); // رفرش کردن صفحه بعد از 3 ثانیه
                    }, 3000); // 3000 میلی‌ثانیه (3 ثانیه)
                }
                else if (response == "erorr") {
                    $("#resualtedit").html("خطا");
                }
               
                else {
                    console.log(response);
                    $("#resualtedit").html("ثبت یادآور با خطا مواجه شد❌");
                }
            },
            error: function (xhr, status, error) {
                // خطا در درخواست
                $("#resualtedit").html(`<p style="color:red;">خطا: ${error}</p>`);
            },
        });
    });



    $(document).on('click', '.deleteremind', function () {
        
        
        $.ajax({
            url: "http://" + window.location.host + "/reminder/deleteRemind",
            type: "POST",
            data: $(".formdelete").serialize(),
            beforeSend: function() {
                $(".resualt_delete").html("...در حال انجام");
            },
            success: function(response) {
                if(response == "true") {
                    $(".resualt_delete").html("حذف یادآور با موفقیت انجام شد ✔");
                    setTimeout(function() {
                        location.reload(); // رفرش کردن صفحه بعد از 3 ثانیه
                    }, 3000); // 3000 میلی‌ثانیه (3 ثانیه)
                }
               
                else {
                    console.log(response);
                    $(".resualt_delete").html("حذف یادآور با خطا مواجه شد❌");
                }
            },
            error: function (xhr, status, error) {
                // خطا در درخواست
                $(".resualt_delete").html(`<p style="color:red;">خطا: ${error}</p>`);
            },
        });
    });
});


