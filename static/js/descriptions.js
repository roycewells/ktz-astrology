$(document).ready(function() {

    //0 for houses/planets, 1 for planets/zodiacs
    //2 for planet/planet/angle
    //3 for Stellium
    var mode;
    var numChosen;

    // var planets = ["sun", "moon", "mercury", "venus", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto", "ascendant", "medium coeli", "north node true"];
    // var zodiacs = ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricornus", "aquarius", "pisces"];
    // var angles = ["sextile", "square", "trine", "opposition"];
    // var houses = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"];

    $(".options").hide();
    $(".planets-dropdown").show();
    $(".houses-dropdown").show();
    mode = "hp";
    loadDescription();


     function loadDescription(){
        var house = $(".houses-dropdown").val();
        var planet = $(".planets-dropdown").val();
        var zodiac = $(".zodiacs-dropdown").val();
        var angle = $(".angles-dropdown").val();
        var planet2 = $(".planets2-dropdown").val();

        switch(mode){
            case "hp":
                $.get( "/admin/descriptions/hp/" + house + "/" + planet, function( data ) {
                    $("textarea").val(data);
                });
                break;
            case "pz":
                $.get( "/admin/descriptions/pz/" + planet + "/" + zodiac, function( data ) {
                    $("textarea").val(data);
                });
                break;
            case "ppa":
                $.get( "/admin/descriptions/ppa/" + planet + "/" + planet2 + "/" + angle, function( data ) {
                    $("textarea").val(data);
                });
                break;
            case "sh":
                $.get( "/admin/descriptions/s3h/" + house , function( data ) {
                    $("textarea").val(data);
                });
                break;
            case "sp":
                $.get( "/admin/descriptions/s3p/" + planet, function( data ) {
                    $("textarea").val(data);
                });
                break;
        }
    }


    //fill page for proper combination
    $(".mode").on('change', function(e){
        e.preventDefault();
        mode = $(this).val();

        //clear choices
        $(".selection").text("");

        switch(mode){
            case "hp":
                $(".options").hide();
                $(".planets-dropdown").show();
                $(".houses-dropdown").show();
                break;
            case "pz":
                $(".options").hide();
                $(".planets-dropdown").show();
                $(".zodiacs-dropdown").show();
                break;
            case "ppa":
                $(".options").hide();
                $(".planets-dropdown").show();
                $(".planets2-dropdown").show();
                $(".angles-dropdown").show();
                break;
            case "sh":
                $(".options").hide();
                $(".houses-dropdown").show();
                break;
            case "sp":
                $(".options").hide();
                $(".zodiacs-dropdown").show();
                break;
        }

        loadDescription();

    });


    $(".submit-button").click(function(e){
        e.preventDefault();
        var house = $(".houses-dropdown").val();
        var planet = $(".planets-dropdown").val();
        var zodiac = $(".zodiacs-dropdown").val();
        var angle = $(".angles-dropdown").val();
        var planet2 = $(".planets2-dropdown").val();
        var description = $("textarea").val();


        switch(mode){
            case "hp":
                $.post( "/admin/descriptions/hp/" + house + "/" + planet,  {"description" : description}, function( data ) {
                    //$("textarea").text(data);
                });
                break;
            case "pz":
                $.post( "/admin/descriptions/pz/" + planet + "/" + zodiac, {"description": description}, function( data ) {
                    //$("textarea").text(data);
                });
                break;
            case "ppa":
                $.post( "/admin/descriptions/ppa/" + planet + "/" + planet + "/" + angle, {"description": description}, function( data ) {
                    //$("textarea").text(data);
                });
                break;
            case "sh":
                $.post( "/admin/descriptions/s3h/" + house, {"description": description}, function( data ) {
                    //$("textarea").text(data);
                });
                break;
            case "sp":
                $.post( "/admin/descriptions/s3p/" + planet, {"description": description}, function( data ) {
                    //$("textarea").text(data);
                });
                break;
        }


    });


    $(".options").change(loadDescription);


});