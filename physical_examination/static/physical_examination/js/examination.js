$(function () {
    var id_pulmonary_auscultation = $('#id_pulmonary_auscultation');
    var id_pulmonary_auscultation_note = $('#id_pulmonary_auscultation_note');

    var id_cardiac_auscultation = $('#id_cardiac_auscultation');
    var id_cardiac_auscultation_note = $('#id_cardiac_auscultation_note');

    var id_pulse = $('#id_pulse');
    var id_pulse_note = $('#id_pulse_note');

    var id_attitude = $('#id_attitude');
    var id_attitude_note = $('#id_attitude_note');

    var id_face = $('#id_face');
    var id_face_note = $('#id_face_note');

    var id_eye = $('#id_eye');
    var id_eye_note = $('#id_eye_note');

    var id_ear = $('#id_ear');
    var id_ear_note = $('#id_ear_note');

    var id_nose = $('#id_nose');
    var id_nose_note = $('#id_nose_note');

    var id_mouth = $('#id_mouth');
    var id_mouth_note = $('#id_mouth_note');

    var id_superficial_lymph_nodes = $('#id_superficial_lymph_nodes');
    var id_superficial_lymph_nodes_note = $('#id_superficial_lymph_nodes_note');

    var id_palpable_thyroid = $('#id_palpable_thyroid');
    var id_palpable_thyroid_note = $('#id_palpable_thyroid_note');

    var id_abdominal_palpation = $('#id_abdominal_palpation');
    var id_abdominal_palpation_note = $('#id_abdominal_palpation_note');

    var id_coat = $('#id_coat');
    var id_coat_note = $('#id_coat_note');

    var id_musculoskeletal_system = $('#id_musculoskeletal_system');
    var id_musculoskeletal_system_note = $('#id_musculoskeletal_system_note');

    var id_skin = $('#id_skin');
    var id_skin_note = $('#id_skin_note');

    //Pulmonary auscultation
    id_pulmonary_auscultation.each(function() {
        if($(this).val() == 'abnormal'){
            $(id_pulmonary_auscultation_note).prop('disabled', false);
        } else{
            $(id_pulmonary_auscultation_note).prop('disabled', true);
        }
    });

    id_pulmonary_auscultation.on('change', (function () {
       if($(this).val() == 'abnormal'){
           $(id_pulmonary_auscultation_note).prop('disabled', false);
       } else {
           $(id_pulmonary_auscultation_note).prop('disabled', true);
       }
    }));

    //Cardiac auscultation
    id_cardiac_auscultation.each(function() {
        if($(this).val() == 'abnormal'){
            $(id_cardiac_auscultation_note).prop('disabled', false);
        } else{
            $(id_cardiac_auscultation_note).prop('disabled', true);
        }
    });

    id_cardiac_auscultation.on('change', (function () {
       if($(this).val() == 'abnormal'){
           $(id_cardiac_auscultation_note).prop('disabled', false);
       } else {
           $(id_cardiac_auscultation_note).prop('disabled', true);
       }
    }));

    //Pulse
    id_pulse.each(function() {
        if($(this).val() == 'abnormal'){
            $(id_pulse_note).prop('disabled', false);
        } else{
            $(id_pulse_note).prop('disabled', true);
        }
    });

    id_pulse.on('change', (function () {
       if($(this).val() == 'abnormal'){
           $(id_pulse_note).prop('disabled', false);
       } else {
           $(id_pulse_note).prop('disabled', true);
       }
    }));

    //Attitude
    id_attitude.each(function() {
        if($(this).val() == 'other'){
            $(id_attitude_note).prop('disabled', false);
        } else{
            $(id_attitude_note).prop('disabled', true);
        }
    });

    id_attitude.on('change', (function () {
       if($(this).val() == 'other'){
           $(id_attitude_note).prop('disabled', false);
       } else {
           $(id_attitude_note).prop('disabled', true);
       }
    }));

    //Face
    id_face.each(function() {
        if($(this).val() == 'abnormal'){
            $(id_face_note).prop('disabled', false);
        } else{
            $(id_face_note).prop('disabled', true);
        }
    });

    id_face.on('change', (function () {
       if($(this).val() == 'abnormal'){
           $(id_face_note).prop('disabled', false);
       } else {
           $(id_face_note).prop('disabled', true);
       }
    }));

    //Eye
    id_eye.each(function() {
        if($(this).val() == 'abnormal'){
            $(id_eye_note).prop('disabled', false);
        } else{
            $(id_eye_note).prop('disabled', true);
        }
    });

    id_eye.on('change', (function () {
       if($(this).val() == 'abnormal'){
           $(id_eye_note).prop('disabled', false);
       } else {
           $(id_eye_note).prop('disabled', true);
       }
    }));

    //Ear
    id_ear.each(function() {
        if($(this).val() == 'abnormal'){
            $(id_ear_note).prop('disabled', false);
        } else{
            $(id_ear_note).prop('disabled', true);
        }
    });

    id_ear.on('change', (function () {
       if($(this).val() == 'abnormal'){
           $(id_ear_note).prop('disabled', false);
       } else {
           $(id_ear_note).prop('disabled', true);
       }
    }));

    //Nose
    id_nose.each(function() {
        if($(this).val() == 'abnormal'){
            $(id_nose_note).prop('disabled', false);
        } else{
            $(id_nose_note).prop('disabled', true);
        }
    });

    id_nose.on('change', (function () {
       if($(this).val() == 'abnormal'){
           $(id_nose_note).prop('disabled', false);
       } else {
           $(id_nose_note).prop('disabled', true);
       }
    }));

    //Mouth
    id_mouth.each(function() {
        if($(this).val() == 'abnormal'){
            $(id_mouth_note).prop('disabled', false);
        } else{
            $(id_mouth_note).prop('disabled', true);
        }
    });

    id_mouth.on('change', (function () {
       if($(this).val() == 'abnormal'){
           $(id_mouth_note).prop('disabled', false);
       } else {
           $(id_mouth_note).prop('disabled', true);
       }
    }));

    //Superficial lymph nodes
    id_superficial_lymph_nodes.each(function() {
        if($(this).val() == 'abnormal'){
            $(id_superficial_lymph_nodes_note).prop('disabled', false);
        } else{
            $(id_superficial_lymph_nodes_note).prop('disabled', true);
        }
    });

    id_superficial_lymph_nodes.on('change', (function () {
       if($(this).val() == 'abnormal'){
           $(id_superficial_lymph_nodes_note).prop('disabled', false);
       } else {
           $(id_superficial_lymph_nodes_note).prop('disabled', true);
       }
    }));

    //Palpable thyroid
    id_palpable_thyroid.each(function() {
        if($(this).val() == 'abnormal'){
            $(id_palpable_thyroid_note).prop('disabled', false);
        } else{
            $(id_palpable_thyroid_note).prop('disabled', true);
        }
    });

    id_palpable_thyroid.on('change', (function () {
       if($(this).val() == 'abnormal'){
           $(id_palpable_thyroid_note).prop('disabled', false);
       } else {
           $(id_palpable_thyroid_note).prop('disabled', true);
       }
    }));

    //Abdominal palpation
    id_abdominal_palpation.each(function() {
        if($(this).val() == 'abnormal'){
            $(id_abdominal_palpation_note).prop('disabled', false);
        } else{
            $(id_abdominal_palpation_note).prop('disabled', true);
        }
    });

    id_abdominal_palpation.on('change', (function () {
       if($(this).val() == 'abnormal'){
           $(id_abdominal_palpation_note).prop('disabled', false);
       } else {
           $(id_abdominal_palpation_note).prop('disabled', true);
       }
    }));

    //Coat
    id_coat.each(function() {
        if($(this).val() == 'abnormal'){
            $(id_coat_note).prop('disabled', false);
        } else{
            $(id_coat_note).prop('disabled', true);
        }
    });

    id_coat.on('change', (function () {
       if($(this).val() == 'abnormal'){
           $(id_coat_note).prop('disabled', false);
       } else {
           $(id_coat_note).prop('disabled', true);
       }
    }));

    //Musculoskeletal system
    id_musculoskeletal_system.each(function() {
        if($(this).val() == 'abnormal'){
            $(id_musculoskeletal_system_note).prop('disabled', false);
        } else{
            $(id_musculoskeletal_system_note).prop('disabled', true);
        }
    });

    id_musculoskeletal_system.on('change', (function () {
       if($(this).val() == 'abnormal'){
           $(id_musculoskeletal_system_note).prop('disabled', false);
       } else {
           $(id_musculoskeletal_system_note).prop('disabled', true);
       }
    }));

    //Skin
    id_skin.each(function() {
        if($(this).val() == 'abnormal'){
            $(id_skin_note).prop('disabled', false);
        } else{
            $(id_skin_note).prop('disabled', true);
        }
    });

    id_skin.on('change', (function () {
       if($(this).val() == 'abnormal'){
           $(id_skin_note).prop('disabled', false);
       } else {
           $(id_skin_note).prop('disabled', true);
       }
    }));

});