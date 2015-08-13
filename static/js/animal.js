$(function(){

  // #######################
  // ###   Animal App    ###
  // #######################

  // ### spay_neuter field ###
  // Check if spay_neuter is enabled or not to enable spay_neuter_date field
  $("#id_spay_neuter_0").click(function () {
      $("#id_spay_neuter_date").parents('.row').hide();
  });
  $("#id_spay_neuter_1").click(function () {
      $("#id_spay_neuter_date").parents('.row').show();
  });

  // When editing an animal, check if spay_neuter is "No" to hide spay_neuter_date field.
  if (id_spay_neuter_0.checked){
      $("#id_spay_neuter_date").parents('.row').hide();
  }
});

function ajax_filter_specie_breed(specie_id)
{
   $("#id_breed").html('<option value="">Carregando...</option>');
   $("#id_color").html('<option value="">Carregando...</option>');
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
               $("#id_breed").append('<option value="'+item.pk+'">'+item.valor+'</option>');
           });
           $.each(retorno[1], function(i, item){
               $("#id_color").append('<option value="'+item.pk+'">'+item.valor+'</option>');
           });
       },
       error: function(erro) {
           alert('Erro: Sem retorno de requisição.');
       }
   });
}