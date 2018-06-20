$(function () {
    var $spay_neuter = $('#id_spay_neuter');

    $spay_neuter.each(function() {
        if($(this).val() == 'yes'){
            $('#id_spay_neuter_date').prop('disabled', false);
        } else{
            $('#id_spay_neuter_date').prop('disabled', true);
        }
    });

    $spay_neuter.on('change', (function () {
       if($(this).val() == 'yes'){
           $('#id_spay_neuter_date').prop('disabled', false);
       } else {
           $('#id_spay_neuter_date').prop('disabled', true);
       }
    }));
});

function ajax_to_filter_breed_and_color(specie_id) {
    $("#id_breed").html('<option value="">Loading...</option>');
    $("#id_color").html('<option value="">Loading...</option>');
    $.ajax({
        type: "GET",
        url: "/animal/select_specie",
        dataType: "json",
        data: {'specie':specie_id},
        success: function(retorno) {
            $("#id_breed").empty();
            $("#id_color").empty();
            $("#id_breed").append('<option value="">--------</option>');
            $("#id_color").append('<option value="">--------</option>');
            $.each(retorno[0], function(i, item){
                $("#id_breed").append('<option value="'+item.pk+'">'+item.animal_name+'</option>');
            });
            $.each(retorno[1], function(i, item){
                $("#id_color").append('<option value="'+item.pk+'">'+item.animal_name+'</option>');
            });
        },
        error: function(erro) {
            alert('Ops, we have a problem!');
        }
    });
}