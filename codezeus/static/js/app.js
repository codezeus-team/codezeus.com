$(function() {

    footer_flush_to_bottom();

});

function footer_flush_to_bottom() {
    var docHeight = $(window).height();
    var footerHeight = $('#f').height();
    var footerTop = $('#f').position().top + footerHeight;

    if (footerTop < docHeight) {
        $('#f').css('margin-top', 10+ (docHeight - footerTop) + 'px');
    }
}
