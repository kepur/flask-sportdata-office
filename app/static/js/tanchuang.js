$(document).ready(function(){
    $('.close-btn').click(function(){
        $('.popbox').fadeOut(function(){ $('.screen').hide(); });
        $('.popbox2').fadeOut(function(){ $('.screen').hide(); });
        return false;
    });

    $('.popbox-link').click(function(){
        var img = $(this).attr('rel');
        var weixin = $(this).attr('rel1');
        if(img){
            $(".mainlist").html('<img style="max-width:100%;display:block;margin:0 auto;" src="'+img+'">');
        }else{
            $(".mainlist").html('<p><span>添加亚盘分析微信：</span><span>'+weixin+'</span></p><p>点击立即注册亚盘合作网站</p>');
        }
        var h = $(document).height();
        $('.screen').css({ 'height': h });
        $('.screen').show();
        $('.popbox').center();
        $('.popbox').fadeIn();
        return false;
    });
    $('.popbox-link2').click(function(){
        var h = $(document).height();
        $('.screen').css({ 'height': h });
        $('.screen').show();
        $('.popbox2').center();
        $('.popbox2').fadeIn();
        return false;
    });

});

jQuery.fn.center = function(loaded) {
    var obj = this;
    body_width = parseInt($(window).width());
    body_height = parseInt($(window).height());
    block_width = parseInt(obj.width());
    block_height = parseInt(obj.height());

    left_position = parseInt((body_width/2) - (block_width/2)  + $(window).scrollLeft());
    if (body_width<block_width) { left_position = 0 + $(window).scrollLeft(); };

    top_position = parseInt((body_height/2) - (block_height/2) + $(window).scrollTop());
    if (body_height<block_height) { top_position = 0 + $(window).scrollTop(); };
    console.log( $(window).scrollTop());
    if(!loaded) {

        obj.css({'position': 'fixed'});
        $(window).bind('resize', function() {
            obj.center(!loaded);
        });
        $(window).bind('scroll', function() {
            obj.center(!loaded);
        });

    } else {
        obj.stop();
        obj.css({'position': 'fixed'});

    }
}