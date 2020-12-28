$(document).ready(function (){
    $("#butt").click(function () {
        $(this).hide();
        $("#btn1").show();
        $("#waitttAmazingLover").css("display", "block");
        var Body = $('body');
        Body.addClass('preloader-site');
        alert('start download');
    });
});
