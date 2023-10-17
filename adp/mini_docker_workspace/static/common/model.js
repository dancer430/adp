define([], function () {
    var jsonContentType = 'application/json;charset=utf-8';
    var modelApp = {

        /**
         * 登录
         **/
        submitLogin: function (condition) {
            return $.ajax({
                url: '/do_login',
                data: condition
            })
        },

        appointmentList: function (condition) {
            return $.ajax({
                url: '/appointment/appointment_list',
                data: condition
            })
        },


    };
    return modelApp;
});