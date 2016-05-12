/**
 * Created by irunika on 5/12/16.
 */

$(document).ready( function(){

    $(window).resize(function(){
        var width = screen.width;

        if(width < 768){
            $('.navbar-top').removeClass('navbar-fixed-top');
            $('.navbar-side').addClass('navbar-fixed-top');
        }
        else {
            $('.navbar-top').addClass('navbar-fixed-top');
            $('.navbar-side').removeClass('navbar-fixed-top');
        }
    });

});
