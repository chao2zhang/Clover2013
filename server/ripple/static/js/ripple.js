$(document).ready(function(){
    $.extend({
        hintForTrigger: {
            "weibo-new": ["微博用户名", "状态里的关键字，可以为空", ""],
            "renren-new": ["人人帐号", "状态里的关键字，可以为空", ""],
            "fudan-new": ["复旦邮箱地址", "标题里的关键字，可以为空", ""],
            "weather-rain": ["地点", "", ""],
            "weather-larger": ["地点", "温度", ">"],
            "weather-smaller": ["地点", "温度", "<"],
            "stock-larger": ["股票代码", "价格", ">"],
            "stock-smaller": ["股票代码", "价格", "<"],
        }, 
        hintForAction: {
            "weibo-post": ["", "发送的微博内容"],
            "renren-post": ["", "发送的人人内容"],
            "fudan-send2me": ["", "发送的邮件标题 & 内容"],
            "fudan-send2others": ["收件人地址", "发送的邮件标题 & 内容"],
            "fetion-send2me": ["", "发送的飞信"],
            "fetion-send2others": ["收件人飞信号", "发送的飞信内容"],
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
        updateAddOn: function(element) {
            if (element) {

            } else {
                $(this).
            }
        }
    });
});