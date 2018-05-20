$(function () {
    var id_auscultation = $('#id_auscultation');
    var id_auscultation_note = $('#id_auscultation_note');

    var id_palpable_thyroid = $('#id_palpable_thyroid');
    var id_palpable_thyroid_note = $('#id_palpable_thyroid_note');

    var id_abdominal_palpation = $('#id_abdominal_palpation');
    var id_abdominal_palpation_note = $('#id_abdominal_palpation_note');

    //Auscultation
    id_auscultation.each(function() {
        if($(this).val() == 'abnormal'){
            $(id_auscultation_note).prop('disabled', false);
        } else{
            $(id_auscultation_note).prop('disabled', true);
        }
    });

    id_auscultation.on('change', (function () {
       if($(this).val() == 'abnormal'){
           $(id_auscultation_note).prop('disabled', false);
       } else {
           $(id_auscultation_note).prop('disabled', true);
       }
    }));

    //Palpable thyroid
    id_palpable_thyroid.each(function() {
        if($(this).val() == 'abnormal'){
            $(id_palpable_thyroid_note).prop('disabled', false);
        } else{
            $(id_palpable_thyroid_note).prop('disabled', true);
        }
    });

    id_palpable_thyroid.on('change', (function () {
       if($(this).val() == 'abnormal'){
           $(id_palpable_thyroid_note).prop('disabled', false);
       } else {
           $(id_palpable_thyroid_note).prop('disabled', true);
       }
    }));

    //Abdominal palpation
    id_abdominal_palpation.each(function() {
        if($(this).val() == 'abnormal'){
            $(id_abdominal_palpation_note).prop('disabled', false);
        } else{
            $(id_abdominal_palpation_note).prop('disabled', true);
        }
    });

    id_abdominal_palpation.on('change', (function () {
       if($(this).val() == 'abnormal'){
           $(id_abdominal_palpation_note).prop('disabled', false);
       } else {
           $(id_abdominal_palpation_note).prop('disabled', true);
       }
    }));
});
