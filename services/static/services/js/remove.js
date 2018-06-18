function disableRemoveButton() {
    $('#removeConsultation').prop('disabled', true);
    $('#removeVaccine').prop('disabled', true);
    $('#removeExam').prop('disabled', true);
}

function show_modal_remove_vaccine(item_id) {
    $('#removeVaccine').prop('disabled', false);
    var modal_remove = document.getElementById('removeVaccine');
    modal_remove.setAttribute("value", 'remove_vaccine-' + item_id);
    $('#modalRemoveVaccine').modal('show');
}

function show_modal_remove_exam(item_id) {
    $('#removeExam').prop('disabled', false);
    var modal_remove = document.getElementById('removeExam');
    modal_remove.setAttribute("value", 'remove_exam-' + item_id);
    $('#modalRemoveExam').modal('show');
}

function show_modal_remove_consultation(item_id) {
    $('#removeConsultation').prop('disabled', false);
    var modal_remove = document.getElementById('removeConsultation');
    modal_remove.setAttribute("value", 'remove_consultation-' + item_id);
    $('#modalRemoveConsultation').modal('show');
}