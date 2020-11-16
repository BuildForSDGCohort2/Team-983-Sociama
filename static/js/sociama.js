/*Scroll to top when arrow up clicked BEGIN*/
$(window).scroll(function () {
    var height = $(window).scrollTop();
    if (height > 350) {
        $('#back2Top').fadeIn();
    } else {
        $('#back2Top').fadeOut();
    }
});
$(document).ready(function () {
    $("#back2Top").click(function (event) {
        event.preventDefault();
        $("html, body").animate({ scrollTop: 0 }, "slow");
        return false;
    });

});
 /*Scroll to top when arrow up clicked END*/

$(document).ready(function () {
    var infinite = new Waypoint.Infinite({
        element: $('.infinite-container')[0],
        
        offset: 'bottom-in-view',

        onBeforePageLoad: function () {
            $('.loading').show();
        },

        onAfterPageLoad: function ($items) {
            $('.loading').hide();

        },
    });
});