$(document).ready(function(){
    $.extend({
        hintForTrigger: {
            "weibo-new": ["微博用户名", "状态里的关键字，可以为空", ""],
            "renren-new": ["人人帐号", "状态里的关键字，可以为空", ""],
            "fudan-new": ["复旦邮箱地址", "标题里的关键字，可以为空", ""],
            "wangyi-new": ["网易邮箱地址", "标题里的关键字，可以为空", ""],
            "weather-rain": ["地点", "", ""],
            "weather-larger": ["地点", "温度", ">"],
            "weather-smaller": ["地点", "温度", "<"],
            "stock-larger": ["股票代码", "价格", ">"],
            "stock-smaller": ["股票代码", "价格", "<"],
        }, 
        hintForAction: {
            "weibo-post": ["", "发送的微博内容"],
            "sinablog-post": ["", "发送的博客标题 & 内容"],
            "renren-post": ["", "发送的人人内容"],
            "fudan-send2me": ["", "发送的邮件标题 & 内容"],
            "fudan-send2others": ["收件人地址", "发送的邮件标题 & 内容"],
            "wangyi-send2me": ["", "发送的邮件标题 & 内容"],
            "wangyi-send2others": ["收件人地址", "发送的飞信内容"],
            "fetion-send2me": ["", "发送的飞信"],
            "fetion-send2others": ["收件人飞信号", "发送的飞信内容"],
        },
        dataFromTrigger: {
            "weibo-new": {"username": "微博用户名", "content": "微博内容", "createdAt": "发表日期"},
            "renren-new": {"username": "人人用户名", "content": "人人状态内容", "createdAt": "发布日期"},
            "fudan-new": {"username": "邮件发信人", "title": "邮件标题", "createdAt": "发信日期"},
            "wangyi-new": {"username": "邮件发信人", "title": "邮件标题", "createdAt": "发信日期"},
            "weather-rain": {"weather":"天气", "temperature":"温度", "createdAt":"日期"},
            "weather-larger": {"weather":"天气", "temperature":"温度", "createdAt":"日期"},
            "weather-smaller": {"weather":"天气", "temperature":"温度", "createdAt":"日期"},
            "stock-larger": {"id":"股票代码", "name":"股票名称", "price":"股票价格"},
            "stock-smaller": {"id":"股票代码", "name":"股票名称", "price":"股票价格"},
        },
    });
    $.fn.extend({
        freezeInput: function(hint) {
            if (hint) {
                $(this).removeClass("uneditable-input").removeAttr("readonly");
                $(this).attr("placeholder", hint);
            } else {
                $(this).addClass("uneditable-input").attr("readonly", "readonly");
                $(this).removeAttr("placeholder");
            }
        },
        updateAddOn: function(text) {
            if (text) {
                if ($(this).prev().hasClass("hide")) {
                    $(this).prev().removeClass("hide");
                    $(this).width($(this).width() - 27);
                }
                $(this).prev().text(text);
            } else {
                if (!$(this).prev().hasClass("hide")) {
                    $(this).prev().addClass("hide");
                    $(this).width($(this).width() + 27);
                }
            }
        },
        updateOptions: function(hash) {
            selects = ["<option>插入信号中的数据</option>"];
            for (var key in hash) {
                selects.push("<option value=" + key + ">" + hash[key] + "</option>");
            }
            $(this).html(selects.join(","));
        },
    });
});