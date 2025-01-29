function setdatadelete(id)
{
    $("#delete_id").val(id);
}   

$(document).on('click', '.deletecart', function () {
        
        
    $.ajax({
        url: "http://" + window.location.host + "/shop/deletecart",
        type: "POST",
        data: $(".formdelete").serialize(),
        beforeSend: function() {
            $(".resualt_delete").html("...در حال انجام");
        },
        success: function(response) {
            if(response == "true") {
                $(".resualt_delete").html("حذف محصول با موفقیت انجام شد ✔");
                setTimeout(function() {
                    location.reload(); // رفرش کردن صفحه بعد از 3 ثانیه
                }, 1000); // 1000 میلی‌ثانیه (3 ثانیه)
            }
            else if(response == "none") {
                $(".resualt_delete").html("محصول وجود ندارد !!");
            }
            else if(response == "valid") {
                $(".resualt_delete").html("درخواست نامعتبر است");
            }
           
            else {
                console.log(response);
                $(".resualt_delete").html("حذف محصول با خطا مواجه شد❌");
            }
        },
        error: function (xhr, status, error) {
            // خطا در درخواست
            $(".resualt_delete").html(`<p style="color:red;">خطا: ${error}</p>`);
        },
    });
});
