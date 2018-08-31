$(document).ready(function () {
    $("#select_all_services").change(function () {
        $(".checkbox_services").not(":disabled").prop('checked', $(this).prop("checked"));
    });
});