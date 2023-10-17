;(function () {
require([
    '/static/common/model.js',
], function (model) {
    var app = {
        init: function () {
            //记住账户回填
            console.log('99999')
            this.event();
        },

        event: function () {
            $(document).ready(function () {
                $(document).on('click', '.login_fields__submit', function () {
                    var username = $('#username').val();
                    var password = $('#password').val();
                    var paras = {
                        'username': username,
                        'password': password
                    };
                    console.log(username);
                    console.log(password);
                    model.submitLogin(paras).then(function (res) {
                        console.log(res)
                        if (res.meta.status === 200) {
                            window.location.href = '/appointment/menu_html/';
                        } else {
                            alert("请确认用户名和密码是否正确~")
                        }
                    });
                });
            })
        }
    };

    app.init();
});

})();