$(function () {
    $('#send-guess').bind ('click', function () {
        // alert ('clicked!');
        $.get ('/process', { guess : $('input[name="number"]').val()}, function (returned_data) {
            console.log (''+returned_data.val);
            if (returned_data.val=='too_high') {
                $('#result').html (`
                    <h1>Too high!<h1>
                `);
            }
            else if (returned_data.val=='too_low') {
                $('#result').html (`
                    <h1>Too low!<h1>
                `);
            }
            else {
                $('#result').html (`
                    <h1>You got it!<h1>
                    <a href="/new_number"><input type="submit" value='Play again'></input></a>
                `);
                // $('#result input').bind ('click', function () {
                //     $('#result').html ('');
                //     $('#number-form').css('display', 'block');
                // })
                //$('#play-again').css('display', 'inline')
                $('#number-form').css('display', 'none');

            }
        });
        return false;
    });
    
});