$(document).ready(function(){
    $("<span class='add-on hide'></span>").insertBefore("input#id_trigger_tag");
    $("input#id_trigger_tag").parent().addClass("input-prepend");
    
    var updateTriggerKind = function(trigger_kind) {
        $("input#id_trigger_kind").val(trigger_kind);
        hints = $.hintForTrigger[trigger_kind];
        $("input#id_trigger_source").freezeInput(hints[0]);
        $("input#id_trigger_tag").freezeInput(hints[1]);
        $("input#id_trigger_tag").updateAddOn(hints[2]);
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
        if ($("#action-panel").is(":hidden"))
            $("#action-panel").fadeIn("slow");
        $('html, body').animate({
            scrollTop: $("#action-panel").offset().top
        }, 1000);
    });
    $(".action-grid").click(function() {
        $(".action-grid").removeClass("chosen");
        $(this).addClass("chosen");
        updateActionKind($(this).attr("id"));
        if ($("#form-panel").is(":hidden"))
            $("#form-panel").fadeIn("slow");
        $('html, body').animate({
            scrollTop: $("#form-panel").offset().top
        }, 1000);
    });
    $("#id_action_content").tooltip({"title":"title"});
});