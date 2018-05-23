function disableRemoveButton() {
    $('#remove_button').prop('disabled', true);
}

function showDialogAndEnableRemoveButton() {
    $('#remove_button').prop('disabled', false);
    $('#modalRemove').modal('show');
}