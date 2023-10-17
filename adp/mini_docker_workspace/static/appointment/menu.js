;(function () {
require([
    '/static/common/model.js',
], function (model) {
    var app = {
        init: function () {
        },

        event: function () {
            $(document).ready(function () {
                $(document).on('click', '#view_appointment', function () {
                    console.log('99999')
                    window.location.href = '/appointment/appointment_html/';
                });
            })
        }
    };

    app.init();
});

})();