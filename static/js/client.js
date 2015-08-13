$(function(){

  // #######################
  // ###   Client App    ###
  // #######################

  $('#cellphone').val();
  $('#cellphone').change(function () {
      $('#cellphone').unmask();
  });

  $('#cellphone').focus(function () {
      $('#cellphone').unmask();
  });

  $('#cellphone').blur(function () {
      if ($("#cellphone").val().length == 11)
          $("#cellphone").mask("(99) 99999-9999");
      else if ($("#cellphone").val().length == 10)
          $("#cellphone").mask("(99) 9999-9999");
      else
          $("#cellphone").unmask();
  });

  $('#phone').val();
  $('#phone').change(function () {
      $('#phone').unmask();
  });

  $('#phone').focus(function () {
      $('#phone').unmask();
  });

  $('#phone').blur(function () {
      if ($("#phone").val().length == 11)
          $("#phone").mask("(99) 99999-9999");
      else if ($("#phone").val().length == 10)
          $("#phone").mask("(99) 9999-9999");
      else
          $("#phone").unmask();
  });

  $('#zipcode').val();
  $('#zipcode').change(function () {
      $('#zipcode').unmask();
  });

  $('#zipcode').focus(function () {
      $('#zipcode').unmask();
  });

  $('#zipcode').blur(function () {
      if (this.value.length == 8) {
          $('#zipcode').mask('99999-999');
      }
  });

});
