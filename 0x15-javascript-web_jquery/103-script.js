$(document).ready(function () {
  $('#btn_translate, #language_code').on('click keypress', function (event) {
    if (event.type === 'click' || (event.type === 'keypress' && event.which === 13)) {
      const languageCode = $('#language_code').val();
      const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

      $.getJSON(apiUrl, function (data) {
        $('#hello').text(data.hello);
      });
    }
  });
});
