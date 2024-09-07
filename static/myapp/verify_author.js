(function($) {
    $(document).ready(function() {
        $(".verify-button").click(function() {
            var button = $(this); // Store the button element
            var authorId = button.data("author-id");
            var verifyUrl = button.data("verify-url");
            var csrftoken = $("[name=csrfmiddlewaretoken]").val();
            var isVerified = button.text().trim() === "Unverify";
            $.ajax({
                url: verifyUrl,
                type: "POST",
                data: {
                    author_id: authorId,
                    csrfmiddlewaretoken: csrftoken,
                },
                success: function(data) {
                    if (data.status === 'success') {
                        if (isVerified) {
                            button.text("Verify"); // Toggle button text
                            alert("Author unverified successfully.");
                        } else {
                            button.text("Unverify"); // Toggle button text
                            alert("Author verified successfully.");
                        }
                        location.reload(); // Reload the page
                    } else {
                        alert("Failed to verify author.");
                    }
                },
                error: function(xhr, errmsg, err) {
                    alert("Failed 987654to verify author.");
                }
            });
        });
    });
})(django.jQuery);
