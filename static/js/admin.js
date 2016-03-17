$(document).ready(function() {

    $('tr').click(function() {
        $(location).attr('href', "/admin/person/" + $(this).find(".id_string").text());
    });


});