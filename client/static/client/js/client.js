function disableRemoveButton() {
    $('#remove_button').prop('disabled', true);
}

function showDialogAndEnableRemoveButton() {
    $('#remove_button').prop('disabled', false);
    $('#modalRemove').modal('show');
}

// $(document).ready(function () {
//     $("#more_contacts").click(function () {
//         document.getElementById('action').value = "more_contacts";
//         $("#form_id").submit();
//     });
// });