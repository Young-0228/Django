//    <!--使用li下拉框，效果-->
var gender_func = function () {
        var num1 = 0
    $("#study").on("click",function () {

        if(num1==0){
        $('.s_8').css({display:'block'})
            num1++;
        } else{
        $('.s_8').css({display:'none'});
        num1=0
        }
        $(".s_8 a").on("click",function () {
            var txt = $(this).text();
            $(this).parents(".s_6").find("#study").html(txt);
        });
    })
}

var study_func = function () {
   var num = 0
    $("#gender").on("click",function () {
        if(num==0){
        $('.s_7').css({display:'block',})
            num++;
        } else{
        $('.s_7').css({display:'none'});
        num=0
        }
        $(".s_7 a").on("click",function () {
            var txt = $(this).text();
            $(this).parents(".s_5").find("#gender").html(txt);
        });
    });

        var num1 = 0
    $("#study").on("click",function () {

        if(num1==0){
        $('.s_8').css({display:'block'})
            num1++;
        } else{
        $('.s_8').css({display:'none'});
        num1=0
        }
        $(".s_8 a").on("click",function () {
            var txt = $(this).text();
            $(this).parents(".s_6").find("#study").html(txt);
        });
    })
}

//定义ajax函数
var ajax_request = function (url,type,data,callback) {
    $.ajax({
        url:url,
        type:type,
        data:data,
        success:function (res) {
            //会掉函数，用于数据操作
            callback(JSON.parse(res))
        }
    })
};

