document.addEventListener("DOMContentLoaded", () => {
  const container = document.querySelector(".moving-container");
  const items = document.querySelector(".moving-items");

  // کلون کردن برای ادامه چرخه بی‌پایان
  items.innerHTML += items.innerHTML; // کل آیتم‌ها دوباره اضافه می‌شوند
});



document.addEventListener('DOMContentLoaded', function () {
  const commentSection = document.getElementById('comment');
  const postId = commentSection.getAttribute('data-id');  // id محصول از HTML
  const likeImageSrc = "/static/img/like.png";
  const dislikeImageSrc = "/static/img/dis .png";

  fetch(`/shop/get-comments/${postId}/`, {
    method: 'GET',
  })
    .then(response => response.json())
    .then(data => {
      const comments = data.comments;
      const container = document.getElementById('comments-container');

      if (comments.length > 0) {
        let index = 0;

        // تابعی برای نمایش کامنت‌ها
        function showComments() {
          if (index < comments.length) {
            const comment = comments[index];
            const likeCount = comment.likes || 0;
            const dislikeCount = comment.dislikes || 0;
            const commentDiv = document.createElement('div');
            commentDiv.classList.add('text-center');
            commentDiv.classList.add('container-comment');

            commentDiv.innerHTML = `
                    <div class="card card-comment" style="background-color: rgba(252, 104, 104, 0.649); border-radius: 20px;" >
                      <div class="card-hadar bg-info p-2 card-hader-comment " style="border-radius: 20px 20px 0 0 ;" >
                        <h4>${comment.User_name}</h4>
                      </div>
                      <div class="card-body text-right card-body-comment"  >
                        <h4>${comment.Title}</h4>
                        <br>
                      <h6>${comment.Comment_text} </h6>
                      </div>
  
                      <div class="card-footer card-footer-comment" style="border-radius:0 0 20px 20px;">
                      <p class="float-right pt-2"> ${comment.created_at} : نوشته شده در    </p>
  
                      <div class="float-left d-flex" dir="rtl">
                        
                      <a class=" btn likes-btn" data-comment-id="${comment.comment_id}" data-action="like">
                        <img class="likes" style="width: 20px;" src="${likeImageSrc}" alt="like"> ${likeCount}
                      </a>
                      <a class=" btn dislikes-btn" data-comment-id="${comment.comment_id}" data-action="dislike">
                        <img class="dislikes" style="width: 20px;" src="${dislikeImageSrc}" alt="dislike"> ${dislikeCount}
                      </a>
                      </div>
                      </div>
                    </div>
                    `;
            container.appendChild(commentDiv);

            setTimeout(function () {
              container.removeChild(commentDiv);
              index++;
            }, 8000);

            setTimeout(showComments, 8000);

          
          








          } else {
            index = 0;
            container.innerHTML = '';
            setTimeout(showComments, 0);
          }
        }

        showComments();
      } else {
        container.innerHTML = "<p>هیچ کامنتی برای این محصول وجود ندارد.</p>";
      }

      // اصلاح رویداد لایک و دیسلایک

    })
    .catch(error => console.error('خطا در ارسال درخواست:', error));
});









$(document).ready(function () {

  $('#send-comment-product').click(function () {



    $.ajax({
      url: "http://" + window.location.host + "/shop/add-comments",
      type: "POST",
      data: $("#formAddComment").serialize(),
      beforeSend: function () {
        $("#resualt-add-comment").html("...در حال انجام");
      },
      success: function (response) {
        if (response == "true") {

          $("#resualt-add-comment").html("نظر شما ثبت و پس از بررسی نمایش داده خواهد شد ❤");
        }
        else if (response == "not valid") {

          $("#resualt-add-comment").html("لطفا تمام فیلد ها را با دقت پر کنید");
        }
        else if (response == "exist") {

          $("#resualt-add-comment").html("این نظر وجود دارد");
        }
        else if (response == "erorr") {

          $("#resualt-add-comment").html(`<p style="color:red;">خطا: ${error}</p>`);
        }
        else {
          console.log(response);
          $("#resualt-add-comment").html("ثبت نظر با خطا مواجه شد❌");
        }
      },
      error: function (xhr, status, error) {
        // خطا در درخواست
        $("#resualt-add-comment").html(`<p style="color:red;">خطا: ${error}</p>`);
      },
    });
  });



  $('#send-question-product').click(function () {



    $.ajax({
      url: "http://" + window.location.host + "/shop/add-question",
      type: "POST",
      data: $("#formAddquestion").serialize(),
      beforeSend: function () {
        $("#resualt-add-question").html("...در حال انجام");
      },
      success: function (response) {
        if (response == "true") {

          $("#resualt-add-question").html("سوال شما ثبت و پس از بررسی نمایش و جواب داده خواهد شد ❤");
        }
        else if (response == "not valid") {

          $("#resualt-add-question").html("لطفا تمام فیلد ها را با دقت پر کنید");
        }
        else if (response == "exist") {

          $("#resualt-add-question").html("این نظر وجود دارد");
        }
        else if (response == "erorr") {

          $("#resualt-add-question").html(`<p style="color:red;">خطا: ${error}</p>`);
        }
        else {
          console.log(response);
          $("#resualt-add-question").html("ثبت سوال با خطا مواجه شد❌");
        }
      },
      error: function (xhr, status, error) {
        // خطا در درخواست
        $("#resualt-add-question").html(`<p style="color:red;">خطا: ${error}</p>`);
      },
    });
  });



  $('.add-to-favorite').click(function () {

    const productIdelement = document.getElementById('add-to-favorite');
    const productId = productIdelement.getAttribute('data-product-id');
    const faveImageSrc = "/static/img/favourite.png";


    $.ajax({
      url: "http://" + window.location.host + "/shop/add-favorite",
      type: "POST",
      data: {
        product_id: productId,
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(), // اضافه کردن CSRF Token
      },
      success: function (response) {
        if (response.status === "added") {
          alert(response.message);
          $('.add-to-favorite').html("حذف از علاقه مندی ها")

        } else if (response.status === "delete") {
          alert(response.message);
          $('.add-to-favorite').html(`<img src=${faveImageSrc} alt="shop" style="width: 20px; height: 20px;"  > افزودن به علاقه مندی ها`)

        } else {
          alert("خطا در افزودن به علاقه‌مندی‌ها.");
        }
      },
      error: function () {
        alert("مشکلی در ارتباط با سرور وجود دارد.");
      },
    });
  });

  $('#add-cart').click(function () {



    $.ajax({
      url: "http://" + window.location.host + "/shop/managecart",
      type: "POST",
      data: $("#cartform").serialize(),
      beforeSend: function () {
        $("#resualt-add-comment").html("...در حال انجام");
      },
      success: function (response) {
        if (response.status == "added") {

          alert(response.message)
          setTimeout(function() {
            window.location.href = '/shop/shop_page'; 
          } , 1000); 
        
        }
        else if (response.status == "exist") {

          alert(response.message)
        }
        else if (response.status == "error") {

          alert(response.message)
        }
        else {
         alert("مشکلی پیش آمد بعدا تلاش کنید");
        }
      },
      error: function (xhr, status, error) {
        // خطا در درخواست
        alert(`<p style="color:red;">خطا: ${error}</p>`);
      },
    });
  });
});



document.addEventListener('DOMContentLoaded', function () {
  // تنظیم رفتار لایک و دیسلایک
  document.querySelectorAll('.like-btn, .dislike-btn').forEach(button => {
    button.addEventListener('click', () => {
      const commentId = button.getAttribute('data-comment-id');
      const action = button.getAttribute('data-action');
      const likeImageSrc = "/static/img/like.png"; // مسیر درست تصویر لایک
      const dislikeImageSrc = "/static/img/dis .png"; // مسیر درست تصویر دیسلایک


      fetch(`/shop/comment/${commentId}/${action}/`, {
        method: 'POST',
        headers: {
          'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        },
      })
        .then(response => response.json())
        .then(data => {
          if (data.status === 'updated' || data.status === 'removed') {
              const likeBtn = document.querySelector(`.like-btn[data-comment-id="${commentId}"]`);
              const dislikeBtn = document.querySelector(`.dislike-btn[data-comment-id="${commentId}"]`);
      
              // اطمینان از مقدار پیش‌فرض 0 در صورت undefined
              const likes = data.likes || 0; 
              const dislikes = data.dislikes || 0;
      
              likeBtn.innerHTML = ` <img class="likes" style="width: 20px;" src="${likeImageSrc}" alt="like"> ${likes}`;
              dislikeBtn.innerHTML = `<img class="dislikes" style="width: 20px;" src="${dislikeImageSrc}" alt="dislike"> ${dislikes}`;
          }
      })
      
        .catch(error => console.error('خطا در ارسال درخواست:', error));
    });
  });
});

