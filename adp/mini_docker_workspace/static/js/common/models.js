define([], function () {
    var jsonContentType = 'application/json;charset=utf-8';
    var modelApp = {

        /**
         * 登录
         **/
        login: function (condition) {
            return $.ajax({
                url: '/fhtp/login_check/',
                data: condition
            });
        },

        /**
         * 注销
         **/
        loginOut: function (condition) {
            return $.ajax({
                url: '/fhtp/login_out/',
                data: condition
            });
        },

        /**
         * 版权信息
         **/
        copyRight: function (condition) {
            return $.ajax({
                url: '/fhtp/copy_right/',
                data: condition
            });
        },

        /**
         * 获取人员身份(是否为管理员)
         * @param condition: {};
         * @return {jQuery|*}
         **/
        getUserType: function (condition) {
            return $.ajax({
                url: '/fhtp/user/user_type/',
                data: condition,
                async: false
            });
        },


        /**
         * 获取所有人员信息
         * @param condition: {};
         * @return {jQuery|*}
         **/
        getAllUserInfo: function (condition) {
            return $.ajax({
                url: '/fhtp/get_all_user_info/',
                data: condition,
                async: false
            });
        },
    };
    return modelApp;
});