function disableRemoveButton() {
    $('#removeConsultation').prop('disabled', true);
}

function show_modal_remove_consultation(item_id) {
    $('#removeConsultation').prop('disabled', false);
    var modal_remove = document.getElementById('removeConsultation');
    modal_remove.setAttribute("value", 'remove_consultation-' + item_id);
    $('#modalRemoveConsultation').modal('show');
}