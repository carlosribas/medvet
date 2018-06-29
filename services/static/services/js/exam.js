$(function () {
    var id_exam_request = $('#id_exam_request');

    id_exam_request.each(function() {
        if($(this).val() == 'annex'){
            $('label[for=id_exam_file], input#id_exam_file').show();
        } else{
            $('label[for=id_exam_file], input#id_exam_file').hide();
        }
    });

    id_exam_request.on('change', (function () {
       if($(this).val() == 'annex'){
           $('label[for=id_exam_file], input#id_exam_file').show();
       } else {
           $('label[for=id_exam_file], input#id_exam_file').hide();
       }
    }));
});
