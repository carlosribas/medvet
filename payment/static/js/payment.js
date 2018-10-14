$(function () {
    var id_installment = $('#id_installment');
    var id_installment_value = $('#div_installment_value');

    id_installment.each(function() {
        if($(this).val() === '1x'){
            $(id_installment_value).hide();
        } else{
            $(id_installment_value).show();
        }
    });

    id_installment.on('change', (function () {
       if($(this).val() === '1x'){
           $(id_installment_value).hide();
       } else {
           $(id_installment_value).show();
       }
    }));
});
