$(document).ready(function (){
    $('#infl').change(function(e){ 
        // var geekss = e.target.files[0].name;
        var path = (window.URL || window.webkitURL).createObjectURL(file);
        alert(path + ' is the selected file.');
    });
    
    $("#butt1").click(function () {
        $(this).hide();
        $("#btn2").show();
        $("#waitttAmazingLover").css("display", "block");
        var Body = $('body');
        Body.addClass('preloader-site');
    });

    $('#typeText').tooltip({
        track:true,
        content:"Enter here File name as per your wish or just leave it blank",
        show:{effect:"highlight",duration:3000}
    });
});