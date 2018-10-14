$(document).ready(function() {
    $( ".datepicker" ).datepicker({
        changeMonth: true,
        changeYear: true,
        yearRange: "-20:+0",
        autoSize: true,
        dateFormat: 'dd/mm/yy'
    });
});

$(document).ready(function() {
    $( ".future-datepicker" ).datepicker({
        minDate : 0,
        changeMonth: true,
        changeYear: true,
        autoSize: true,
        dateFormat: 'dd/mm/yy'
    });
});