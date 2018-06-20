$(function () {
    var $spay_neuter = $('#id_spay_neuter');

    $spay_neuter.each(function() {
        if($(this).val() == 'y'){
            $('#id_spay_neuter_date').prop('disabled', false);
        } else{
            $('#id_spay_neuter_date').prop('disabled', true);
        }
    });

    $spay_neuter.on('change', (function () {
       if($(this).val() == 'y'){
           $('#id_spay_neuter_date').prop('disabled', false);
       } else {
           $('#id_spay_neuter_date').prop('disabled', true);
       }
    }));
});
