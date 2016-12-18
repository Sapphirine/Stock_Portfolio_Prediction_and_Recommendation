/**
 * Created by kzhu9 on 11/12/2016.
 */
$(document).ready(function () {
    $('form').on('submit', function (event) {
        $.ajax({
            data: {
                ticker: $('#ticker').val()
            },
            type: 'GET',
            url: '/search'
        }).done(function (data) {
            if (data.error) {
                $('#errorAlert').text(data.error).show();
                $('#successAlert').hide();
            } else {
                var JSONObject = JSON.parse(data);
                $('#errorAlert').hide();
                $('#successAlert').show();
                $('#successAlert').innerHTML = '';
                var el = document.getElementById('successAlert');

                while (el.firstChild) el.removeChild(el.firstChild);
                var count = 0;
                for (var key in JSONObject) {
                    count = count + 1;
                    if (JSONObject.hasOwnProperty(key)) {
                        var val = JSONObject[key];
                        var innerDiv = document.createElement('div');
                        innerDiv.id = "success_" + key;
                        innerDiv.innerHTML = val;
                        $('#successAlert').append(innerDiv);
                    }
                }
                // if (count == 0) {
                //     var innerDiv = document.createElement('div');
                //     innerDiv.id = "success_0";
                //     innerDiv.innerHTML = "Don't buy ";
                //     $('#successAlert').append(innerDiv);
                // }
            }
        });
        event.preventDefault();

    });
});