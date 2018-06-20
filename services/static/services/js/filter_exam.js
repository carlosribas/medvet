function filter_category_type(category_id)
{
   $("#id_exam_type").html('<option value="">Carregando...</option>');
   $.ajax({
       type: "GET",
       url: "/service/filter_exam",
       dataType: "json",
       data: {'category':category_id},
       success: function(retorno) {
           $("#id_exam_type").empty();
           $("#id_exam_type").append('<option value="">--------</option>');
           $.each(retorno[0], function(i, item){
               $("#id_exam_type").append('<option value="'+item.pk+'">'+item.valor+'</option>');
           });
       },
       error: function(erro) {
           alert('Erro: Sem retorno de requisição.');
       }
   });
}