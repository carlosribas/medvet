$(document).ready(function () {
    $("#select_all_services").change(function () {
        $(".checkbox_services").prop('checked', $(this).prop("checked"));
    });
});