function ajax_filter_animal_name(owner_id)
{
   $("#id_animal").html('<option value="">Carregando...</option>');
   $.ajax({
       type: "GET",
       url: "/physical_examination/select_animal",
       dataType: "json",
       data: {'owner':owner_id},
       success: function(retorno) {
           $("#id_animal").empty();
           $("#id_animal").append('<option value="">--------</option>');
           $.each(retorno, function(i, item){
               $("#id_animal").append('<option value="'+item.pk+'">'+item.valor+'</option>');
           });
       },
       error: function(erro) {
           alert('Erro: Sem retorno de requisição.');
       }
   });
}
