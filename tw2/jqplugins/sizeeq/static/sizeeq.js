function install_sizeeq(selector, eq_width, eq_height) {
    var cells = $(selector);
    function do_eq_width() {
        var max_width = 0;
        cells.each(function(i, cell) {
            $(cell).css('width', '');
            if ($(cell).width() > max_width)
                max_width = $(cell).width();
        });
        cells.css('width', max_width);
    }
    function do_eq_height() {
        var max_height = 0;
        cells.each(function(i, cell) {
            $(cell).css('height', '');
            if ($(cell).height() > max_height)
                max_height = $(cell).height();
        });
        cells.css('height', max_height);
    }
    if (eq_width) {
        do_eq_width();
        $(window).on('resize orientationChange', do_eq_width);
    }
    if (eq_height) {
        do_eq_height();
        $(window).on('resize orientationChange', do_eq_height);
    }
}
