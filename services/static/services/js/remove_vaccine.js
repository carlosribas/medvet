function disableRemoveButton() {
    $('#removeVaccine').prop('disabled', true);
}

function show_modal_remove_vaccine(item_id) {
    $('#removeVaccine').prop('disabled', false);
    var modal_remove = document.getElementById('removeVaccine');
    modal_remove.setAttribute("value", 'remove_vaccine-' + item_id);
    $('#modalRemoveVaccine').modal('show');
}