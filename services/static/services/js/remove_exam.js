function disableRemoveButton() {
    $('#removeExam').prop('disabled', true);
}

function show_modal_remove_exam(item_id) {
    $('#removeExam').prop('disabled', false);
    var modal_remove = document.getElementById('removeExam');
    modal_remove.setAttribute("value", 'remove_exam-' + item_id);
    $('#modalRemoveExam').modal('show');
}