function updateCartCount() {
    $.ajax({
        url: '/shop/cart/count', // مسیر ویو
        method: 'GET',
        success: function(data) {
            // به‌روزرسانی مقدار در DOM
            $('.cart-count').text(data.count);
        },
        error: function(xhr, status, error) {
            console.error("Error fetching cart count:", error);
        }
    });
}

// صدا زدن تابع در بارگذاری صفحه
$(document).ready(function() {
    updateCartCount();


});