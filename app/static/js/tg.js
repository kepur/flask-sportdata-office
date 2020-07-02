arr_wx = ['jgadmin911', 'guanren4214'];
let wx_index = Math.floor(Math.random() * arr_wx.length);
let stxlwx = arr_wx[wx_index];
let img = arr_wx[wx_index];
let rwx1 = img + ".png";
let rqr = "<center ><img  src='images/" + rwx1 + "' style='margin:0 auto;'></center>";

//复制
function copyText() {
    const input = document.createElement('input');
    input.setAttribute('readonly', 'true');
    input.setSelectionRange(0, input.value.length);
    input.setAttribute('value', stxlwx);
    document.body.appendChild(input);
    input.setSelectionRange(0, 9999999);
    if (document.execCommand('copy')) {
        input.select();
        document.execCommand('copy');
        alert('成功复制微信号:' + stxlwx);
    }
    document.body.removeChild(input);
};
// 加入收藏 兼容360和IE6
function shoucang(sTitle, sURL) {
    try {
        window.external.addFavorite(sURL, sTitle);
    } catch (e) {
        try {
            window.sidebar.addPanel(sTitle, sURL, "");
        } catch (e) {
            alert("加入收藏失败，请使用Ctrl+D进行添加");
        }
    }
};

$(function () {
    $(".point_sele a").click(function () {
        var index = $(this).index();
        var eqnum = index / 2;
        $(this).addClass("sel_a").siblings().removeClass("sel_a");
        // $(".banner_c a").eq(eqnum).addClass("sele_show").siblings().removeClass('sele_show');
    });
    $(".del_btn").click(function () {
        $(".b_wei").css("display", "none");
    });
    $(".del_btn2").click(function () {
        $("#aa").css("display", "none");
    });
})

//唤起手机QQ

function chatQQ(){
    window.location.href = "mqqwpa://im/chat?chat_type=wpa&uin=503224455&version=1&src_type=web&web_src=oicqzone.com";
}