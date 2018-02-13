// $(function () {
//
//     $(".js-create-course").click(function () {
//         $.ajax({
//             url: '/course/courses/create',
//             type: 'get',
//             dataType: 'json',
//             beforeSend: function () {
//                 $("#modal-course").modal("show");
//             },
//             success: function (data) {
//                 $("#modal-course .modal-content").html(data.html_form);
//             }
//         });
//     });
//
// });


$("#modal-course").on("submit", ".js-course-create-form", function () {
    var form = $(this);
    $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
            if (data.form_is_valid) {
                $("#course-table tbody").html(data.html_course_list);  // <-- Replace the table body
                $("#modal-course").modal("hide");  // <-- Close the modal
            }
            else {
                $("#modal-course .modal-content").html(data.html_form);
            }
        }
    });
    return false;
});