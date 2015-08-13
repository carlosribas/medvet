$(document).ready(function () {
    // For fields with "normal" or "abnormal" as possible answer:
    // 1 - With empty fields, the note field is always hidden.
    // 2 - If "abnormal" answer is selected,  the note field is enable.
    // 3 - When editing an examination, checks if "abnormal" is selected to enable a note field.

    // ### pulmonary_auscultation field ###
    if (!id_pulmonary_auscultation_0.checked && !id_pulmonary_auscultation_1.checked){
        $("#id_pulmonary_auscultation_note").parents('.row').hide();
    }
    $("#id_pulmonary_auscultation_0").click(function () {
        $("#id_pulmonary_auscultation_note").parents('.row').hide();
    });
    $("#id_pulmonary_auscultation_1").click(function () {
        $("#id_pulmonary_auscultation_note").parents('.row').show();
    });
    if (id_pulmonary_auscultation_0.checked){$("#id_pulmonary_auscultation_note").parents('.row').hide();}


    // ### cardiac_auscultation field ###
    if (!id_cardiac_auscultation_0.checked && !id_cardiac_auscultation_1.checked){
        $("#id_cardiac_auscultation_note").parents('.row').hide();
    }
    $("#id_cardiac_auscultation_0").click(function () {
        $("#id_cardiac_auscultation_note").parents('.row').hide();
    });
    $("#id_cardiac_auscultation_1").click(function () {
        $("#id_cardiac_auscultation_note").parents('.row').show();
    });
    if (id_cardiac_auscultation_0.checked){$("#id_cardiac_auscultation_note").parents('.row').hide();}


    // ### pulse field ###
    if (!id_pulse_0.checked && !id_pulse_1.checked){
        $("#id_pulse_note").parents('.row').hide();
    }
    $("#id_pulse_0").click(function () {
        $("#id_pulse_note").parents('.row').hide();
    });
    $("#id_pulse_1").click(function () {
        $("#id_pulse_note").parents('.row').show();
    });
    if (id_pulse_0.checked){$("#id_pulse_note").parents('.row').hide();}


    // ### attitude field ###
    // Check if attitude is "other" to enable attitude_note field
    if (!id_attitude_0.checked && !id_attitude_1.checked && !id_attitude_2.checked && !id_attitude_3.checked && !id_attitude_4.checked && !id_attitude_5.checked){
        $("#id_attitude_note").parents('.row').hide();
    }
    $('#id_attitude').click(function(){
       if ($('#id_attitude_5').is(':checked')) {
          $('#id_attitude_note').parents('.row').show();
       } else {
          $('#id_attitude_note').parents('.row').hide();
       }
    });
    // When editing an examination, check if attitude is "other" to enable attitude_note.
    if (id_attitude_5.checked){
        $('#id_attitude_note').parents('.row').show();
    } else {
        $('#id_attitude_note').parents('.row').hide();
    }


    // ### face field ###
    // Check if face is normal, head tilt or abnormal to enable face_note field
    if (!id_face_0.checked && !id_face_1.checked && !id_face_2.checked){
        $("#id_face_note").parents('.row').hide();
    }
    $('#id_face').click(function(){
       if ($('#id_face_2').is(':checked')) {
          $('#id_face_note').parents('.row').show();
       } else {
          $('#id_face_note').parents('.row').hide();
       }
    });
    // When editing an examination, check if face is abnormal to enable face_note.
    if (id_face_2.checked){
        $('#id_face_note').parents('.row').show();
    } else {
        $('#id_face_note').parents('.row').hide();
    }


    // ### eye field ###
    if (!id_eye_0.checked && !id_eye_1.checked){
        $("#id_eye_note").parents('.row').hide();
    }
    $("#id_eye_0").click(function () {
        $("#id_eye_note").parents('.row').hide();
    });
    $("#id_eye_1").click(function () {
        $("#id_eye_note").parents('.row').show();
    });
    if (id_eye_0.checked){$("#id_eye_note").parents('.row').hide();}


    // ### ear field ###
    if (!id_ear_0.checked && !id_ear_1.checked){
        $("#id_ear_note").parents('.row').hide();
    }
    $("#id_ear_0").click(function () {
        $("#id_ear_note").parents('.row').hide();
    });
    $("#id_ear_1").click(function () {
        $("#id_ear_note").parents('.row').show();
    });
    if (id_ear_0.checked){$("#id_ear_note").parents('.row').hide();}


    // ### nose field ###
    if (!id_nose_0.checked && !id_nose_1.checked){
        $("#id_nose_note").parents('.row').hide();
    }
    $("#id_nose_0").click(function () {
        $("#id_nose_note").parents('.row').hide();
    });
    $("#id_nose_1").click(function () {
        $("#id_nose_note").parents('.row').show();
    });
    if (id_nose_0.checked){$("#id_nose_note").parents('.row').hide();}


    // ### mouth field ###
    if (!id_mouth_0.checked && !id_mouth_1.checked){
        $("#id_mouth_note").parents('.row').hide();
    }
    $("#id_mouth_0").click(function () {
        $("#id_mouth_note").parents('.row').hide();
    });
    $("#id_mouth_1").click(function () {
        $("#id_mouth_note").parents('.row').show();
    });
    if (id_mouth_0.checked){$("#id_mouth_note").parents('.row').hide();}


    // ### superficial_lymph_nodes field ###
    if (!id_superficial_lymph_nodes_0.checked && !id_superficial_lymph_nodes_1.checked){
        $("#id_superficial_lymph_nodes_note").parents('.row').hide();
    }
    $("#id_superficial_lymph_nodes_0").click(function () {
        $("#id_superficial_lymph_nodes_note").parents('.row').hide();
    });
    $("#id_superficial_lymph_nodes_1").click(function () {
        $("#id_superficial_lymph_nodes_note").parents('.row').show();
    });
    if (id_superficial_lymph_nodes_0.checked){$("#id_superficial_lymph_nodes_note").parents('.row').hide();}


    // ### palpable_thyroid field ###
    if (!id_palpable_thyroid_0.checked && !id_palpable_thyroid_1.checked){
        $("#id_palpable_thyroid_note").parents('.row').hide();
    }
    $("#id_palpable_thyroid_0").click(function () {
        $("#id_palpable_thyroid_note").parents('.row').hide();
    });
    $("#id_palpable_thyroid_1").click(function () {
        $("#id_palpable_thyroid_note").parents('.row').show();
    });
    if (id_palpable_thyroid_0.checked){$("#id_palpable_thyroid_note").parents('.row').hide();}


    // ### abdominal_palpation field ###
    if (!id_abdominal_palpation_0.checked && !id_abdominal_palpation_1.checked){
        $("#id_abdominal_palpation_note").parents('.row').hide();
    }
    $("#id_abdominal_palpation_0").click(function () {
        $("#id_abdominal_palpation_note").parents('.row').hide();
    });
    $("#id_abdominal_palpation_1").click(function () {
        $("#id_abdominal_palpation_note").parents('.row').show();
    });
    if (id_abdominal_palpation_0.checked){$("#id_abdominal_palpation_note").parents('.row').hide();}


    // ### coat field ###
    if (!id_coat_0.checked && !id_coat_1.checked){
        $("#id_coat_note").parents('.row').hide();
    }
    $("#id_coat_0").click(function () {
        $("#id_coat_note").parents('.row').hide();
    });
    $("#id_coat_1").click(function () {
        $("#id_coat_note").parents('.row').show();
    });
    if (id_coat_0.checked){$("#id_coat_note").parents('.row').hide();}


    // ### skin field ###
    if (!id_skin_0.checked && !id_skin_1.checked){
        $("#id_skin_note").parents('.row').hide();
    }
    $("#id_skin_0").click(function () {
        $("#id_skin_note").parents('.row').hide();
    });
    $("#id_skin_1").click(function () {
        $("#id_skin_note").parents('.row').show();
    });
    if (id_skin_0.checked){$("#id_skin_note").parents('.row').hide();}


    // ### musculoskeletal_system field ###
    if (!id_musculoskeletal_system_0.checked && !id_musculoskeletal_system_1.checked){
        $("#id_musculoskeletal_system_note").parents('.row').hide();
    }
    $("#id_musculoskeletal_system_0").click(function () {
        $("#id_musculoskeletal_system_note").parents('.row').hide();
    });
    $("#id_musculoskeletal_system_1").click(function () {
        $("#id_musculoskeletal_system_note").parents('.row').show();
    });
    if (id_musculoskeletal_system_0.checked){$("#id_musculoskeletal_system_note").parents('.row').hide();}


    // ### central_and_peripheral_nervous_system field ###
    if (!id_central_and_peripheral_nervous_system_0.checked && !id_central_and_peripheral_nervous_system_1.checked){
        $("#id_central_and_peripheral_nervous_system_note").parents('.row').hide();
    }
    $("#id_central_and_peripheral_nervous_system_0").click(function () {
        $("#id_central_and_peripheral_nervous_system_note").parents('.row').hide();
    });
    $("#id_central_and_peripheral_nervous_system_1").click(function () {
        $("#id_central_and_peripheral_nervous_system_note").parents('.row').show();
    });
    if (id_central_and_peripheral_nervous_system_0.checked){$("#id_central_and_peripheral_nervous_system_note").parents('.row').hide();}
});

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