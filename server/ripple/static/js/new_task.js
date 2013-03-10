$(document).ready(function(){
    $("input#id_trigger_tag").parent().addClass("input-prepend");
    $("textarea#id_action_content").parent().parent().attr("id", "parent_action_content");
    $("<span class='add-on hide'></span>").insertBefore("input#id_trigger_tag");
    $("<div class='control-group'><select id='data_from_trigger'</select></div>").insertAfter("#parent_action_content");
    $("#data_from_trigger").change(function() {
        if ($(this).prop("selectedIndex") == 0)
            return;
        var variable = $(this).find("option:selected").attr("value");
        var str = "{{" + variable + "}}";
        $("textarea#id_action_content").val(function(index, val) {
            return val + str;
        });
        $(this).prop("selectedIndex", 0);
    });
    
    var updateTriggerKind = function(trigger_kind) {
        $("input#id_trigger_kind").val(trigger_kind);
        hints = $.hintForTrigger[trigger_kind];
        $("input#id_trigger_source").freezeInput(hints[0]);
        $("input#id_trigger_tag").freezeInput(hints[1]);
        $("input#id_trigger_tag").updateAddOn(hints[2]);
        $("select#data_from_trigger").updateOptions($.dataFromTrigger[trigger_kind]);
    };
    var updateActionKind = function(action_kind) {
        $("input#id_action_kind").val(action_kind);
        hints = $.hintForAction[action_kind];
        $("input#id_action_destination").freezeInput(hints[0]);
        $("textarea#id_action_content").freezeInput(hints[1]);
    };
    $(".trigger-grid").click(function() {
        $(".trigger-grid").removeClass("chosen");
        $(this).addClass("chosen");
        updateTriggerKind($(this).attr("id"));
        if ($("#action-panel").is(":hidden")) {
            $("#action-panel").removeClass("hide");
            $("#action-panel").fadeIn("slow");
        }
        $('html, body').animate({
            scrollTop: $("#action-panel").offset().top
        }, 1000);
    });
    $(".action-grid").click(function() {
        $(".action-grid").removeClass("chosen");
        $(this).addClass("chosen");
        updateActionKind($(this).attr("id"));
        if ($("#form-panel").is(":hidden")) {
            $("#form-panel").removeClass("hide");
            $("#form-panel").fadeIn("slow");
        }
        $('html, body').animate({
            scrollTop: $("#form-panel").offset().top
        }, 1000);
    });
});