
$(function(){

    var le = $("table tr").length;
    for(var i = 0;i<le;i++){
        var t = i;
        var bbt = $("table tr").eq(t).children(".fzred").html();
        if("输" == bbt){
            $("table tr").eq(t).children(".fzred").css({"color":"black"});
        }else if("赢" == bbt){
            $("table tr").eq(t).children(".fzred").css({"color":"red"});
        }else if("待" == bbt){
            $("table tr").eq(t).children(".fzred").css({"color":"blue"});
        }
    }
});