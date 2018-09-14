$(function () {
    var id_exam_type = $('#id_exam_type');

    id_exam_type.each(function() {
        if($(this).val() == 'annex'){
            $('label[for=id_exam_file], input#id_exam_file').show();
        } else{
            $('label[for=id_exam_file], input#id_exam_file').hide();
        }
    });

    id_exam_type.on('change', (function () {
       if($(this).val() == 'annex'){
           $('label[for=id_exam_file], input#id_exam_file').show();
       } else {
           $('label[for=id_exam_file], input#id_exam_file').hide();
       }
    }));
});
