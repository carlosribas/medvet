$(function(){

  // #######################
  // ### Examination App ###
  // #######################

  // ### pulse field ###
  // Check if pulse is normal or abnormal to enable pulse_note field
  $('#id_pulse').click(function(){
     if ($('#id_pulse_1').is(':checked')) {
        $('#id_pulse_note').show();
     } else {
        $('#id_pulse_note').hide();
     }
  });
  // Check if pulse_note is not null to enable this field after press "save" and get some warning or error message.
  if (id_pulse_note.value != ''){$('#id_pulse_note').show();}
  //if (id_pulse_note.value != '' && id_pulse == '0'){id_pulse_note = ';}


  // ### attitude field ###
  // Check if attitude is "other" to enable attitude_note field
  $('#id_attitude').click(function(){
     if ($('#id_attitude_5').is(':checked')) {
        $('#id_attitude_note').show();
     } else {
        $('#id_attitude_note').hide();
     }
  });
  // Check if attitude_note is not null to enable this field after press save and get some warning or error message.
  if (id_attitude_note.value != ''){$('#id_attitude_note').show();}


  // ### face field ###
  // Check if face is normal, head tilt or abnormal to enable face_note field
  $('#id_face').click(function(){
     if ($('#id_face_2').is(':checked')) {
        $('#id_face_note').show();
     } else {
        $('#id_face_note').hide();
     }
  });
  // Check if face_note is not null to enable this field after press "save" and get some warning or error message.
  if (id_face_note.value != ''){$('#id_face_note').show();}


  // ### eye field ###
  // Check if eye is normal or abnormal to enable eye_note field
  $('#id_eye').click(function(){
     if ($('#id_eye_1').is(':checked')) {
        $('#id_eye_note').show();
     } else {
        $('#id_eye_note').hide();
     }
  });
  // Check if eye_note is not null to enable this field after press "save" and get some warning or error message.
  if (id_eye_note.value != ''){$('#id_eye_note').show();}


  // ### ear field ###
  // Check if ear is normal or abnormal to enable ear_note field
  $('#id_ear').click(function(){
     if ($('#id_ear_1').is(':checked')) {
        $('#id_ear_note').show();
     } else {
        $('#id_ear_note').hide();
     }
  });
  // Check if ear_note is not null to enable this field after press "save" and get some warning or error message.
  if (id_ear_note.value != ''){$('#id_ear_note').show();}


  // ### nose field ###
  // Check if nose is normal or abnormal to enable nose_note field
  $('#id_nose').click(function(){
     if ($('#id_nose_1').is(':checked')) {
        $('#id_nose_note').show();
     } else {
        $('#id_nose_note').hide();
     }
  });
  // Check if nose_note is not null to enable this field after press "save" and get some warning or error message.
  if (id_nose_note.value != ''){$('#id_nose_note').show();}


  // ### mouth field ###
  // Check if mouth is normal or abnormal to enable mouth_note field
  $('#id_mouth').click(function(){
     if ($('#id_mouth_1').is(':checked')) {
        $('#id_mouth_note').show();
     } else {
        $('#id_mouth_note').hide();
     }
  });
  // Check if mouth_note is not null to enable this field after press "save" and get some warning or error message.
  if (id_mouth_note.value != ''){$('#id_mouth_note').show();}


  // ### superficial_lymph_nodes field ###
  // Check if superficial_lymph_nodes is normal or abnormal to enable superficial_lymph_nodes_note field
  $('#id_superficial_lymph_nodes').click(function(){
     if ($('#id_superficial_lymph_nodes_1').is(':checked')) {
        $('#id_superficial_lymph_nodes_note').show();
     } else {
        $('#id_superficial_lymph_nodes_note').hide();
     }
  });
  // Check if superficial_lymph_nodes_note is not null to enable this field after press "save" and get some warning or error message.
  if (id_superficial_lymph_nodes_note.value != ''){$('#id_superficial_lymph_nodes_note').show();}

  // ### palpable_thyroid field ###
  // Check if palpable_thyroid is normal or abnormal to enable palpable_thyroid_note field
  $('#id_palpable_thyroid').click(function(){
     if ($('#id_palpable_thyroid_1').is(':checked')) {
        $('#id_palpable_thyroid_note').show();
     } else {
        $('#id_palpable_thyroid_note').hide();
     }
  });
  // Check if palpable_thyroid_note is not null to enable this field after press "save" and get some warning or error message.
  if (id_palpable_thyroid_note.value != ''){$('#id_palpable_thyroid_note').show();}


  // ### pulmonary_auscultation field ###
  // Check if pulmonary_auscultation is normal or abnormal to enable pulmonary_auscultation_note field
  $('#id_pulmonary_auscultation').click(function(){
     if ($('#id_pulmonary_auscultation_1').is(':checked')) {
        $('#id_pulmonary_auscultation_note').show();
     } else {
        $('#id_pulmonary_auscultation_note').hide();
     }
  });
  // Check if pulmonary_auscultation_note is not null to enable this field after press "save" and get some warning or error message.
  if (id_pulmonary_auscultation_note.value != ''){$('#id_pulmonary_auscultation_note').show();}


  // ### cardiac_auscultation field ###
  // Check if cardiac_auscultation is normal or abnormal to enable cardiac_auscultation_note field
  $('#id_cardiac_auscultation').click(function(){
     if ($('#id_cardiac_auscultation_1').is(':checked')) {
        $('#id_cardiac_auscultation_note').show();
     } else {
        $('#id_cardiac_auscultation_note').hide();
     }
  });
  // Check if cardiac_auscultation_note is not null to enable this field after press "save" and get some warning or error message.
  if (id_cardiac_auscultation_note.value != ''){$('#id_cardiac_auscultation_note').show();}


  // ### abdominal_palpation field ###
  // Check if abdominal_palpation is normal or abnormal to enable abdominal_palpation_note field
  $('#id_abdominal_palpation').click(function(){
     if ($('#id_abdominal_palpation_1').is(':checked')) {
        $('#id_abdominal_palpation_note').show();
     } else {
        $('#id_abdominal_palpation_note').hide();
     }
  });
  // Check if abdominal_palpation_note is not null to enable this field after press "save" and get some warning or error message.
  if (id_abdominal_palpation_note.value != ''){$('#id_abdominal_palpation_note').show();}


  // ### coat field ###
  // Check if coat is normal or abnormal to enable coat_note field
  $('#id_coat').click(function(){
     if ($('#id_coat_1').is(':checked')) {
        $('#id_coat_note').show();
     } else {
        $('#id_coat_note').hide();
     }
  });
  // Check if coat_note is not null to enable this field after press "save" and get some warning or error message.
  if (id_coat_note.value != ''){$('#id_coat_note').show();}


  // ### skin field ###
  // Check if skin is normal or abnormal to enable skin_note field
  $('#id_skin').click(function(){
     if ($('#id_skin_1').is(':checked')) {
        $('#id_skin_note').show();
     } else {
        $('#id_skin_note').hide();
     }
  });
  // Check if skin_note is not null to enable this field after press "save" and get some warning or error message.
  if (id_skin_note.value != ''){$('#id_skin_note').show();}


  // ### musculoskeletal_system field ###
  // Check if musculoskeletal_system is normal or abnormal to enable musculoskeletal_system_note field
  $('#id_musculoskeletal_system').click(function(){
     if ($('#id_musculoskeletal_system_1').is(':checked')) {
        $('#id_musculoskeletal_system_note').show();
     } else {
        $('#id_musculoskeletal_system_note').hide();
     }
  });
  // Check if musculoskeletal_system_note is not null to enable this field after press "save" and get some warning or error message.
  if (id_musculoskeletal_system_note.value != ''){$('#id_musculoskeletal_system_note').show();}


  // ### central_and_peripheral_nervous_system field ###
  // Check if central_and_peripheral_nervous_system is normal or abnormal to enable central_and_peripheral_nervous_system_note field
  $('#id_central_and_peripheral_nervous_system').click(function(){
     if ($('#id_central_and_peripheral_nervous_system_1').is(':checked')) {
        $('#id_central_and_peripheral_nervous_system_note').show();
     } else {
        $('#id_central_and_peripheral_nervous_system_note').hide();
     }
  });
  // Check if central_and_peripheral_nervous_system_note is not null to enable this field after press "save" and get some warning or error message.
  if (id_central_and_peripheral_nervous_system_note.value != ''){$('#id_central_and_peripheral_nervous_system_note').show();}


  function ajax_filter_animal_name()
  {
       client = $("#id_name").val();
       a_id = "#id_animal_name";
       $(a_id).html('<option value="">Carregando...</option>');
       $.ajax({
           type: "POST",
           url: "/client/search_client",
           dataType: "json",
           data: {'name':client},
           success: function(retorno) {
                $(a_id).empty();
                $(a_id).append('<option value="">--------</option>');
                $.each(retorno, function(i, item){
                    $(a_id).append('<option value="'+item.pk+'">'+item.valor+'</option>');
                });
           },
           error: function(erro) {
              alert('Erro: Sem retorno de requisição.');
           }
       });
  }

  // #######################
  // ###   Animal App    ###
  // #######################

  // ### spay_neuter field ###
  // Check if the animal is spay or neuter to enable spay_neuter_date field
  $('#id_spay_neuter').click(function(){
     if ($('#id_spay_neuter_0').is(':checked')) {
        $('#id_spay_neuter_date').show();
     } else {
        $('#id_spay_neuter_date').hide();
     }
  });
  // Check if spay_neuter_date is not null to enable this field after press "save" and get some warning or error message.
  if (id_spay_neuter_date.value != ''){$('#id_spay_neuter_date').show();}

});
