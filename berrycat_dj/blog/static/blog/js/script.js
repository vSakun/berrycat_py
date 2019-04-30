/* Slider */
$(document).ready(function(){
	$(".foto_bloc .info_item_slide:gt(0)").addClass("vis").addClass("hid");
});
function slider(){
	$(".next").on('click', function(){
		var slide = $(".foto_bloc [class=info_item_slide]");
		if(slide.next().hasClass("hid")){
			slide.addClass("vis");
			setTimeout(function () {
				slide.addClass("hid");
				slide.next().removeClass("hid");
			}, 500);
			setTimeout(function () {
				slide.next().removeClass("vis");
			}, 550);
		}
	});
	$(".prev").on('click', function(){
		var slide = $(".foto_bloc [class=info_item_slide]");
		if(slide.prev().hasClass("hid")){
			slide.addClass("vis");
			setTimeout(function () {
				slide.addClass("hid");
				slide.prev().removeClass("hid");
			}, 500);
			setTimeout(function () {
				slide.prev().removeClass("vis");
			}, 550);
		}
	});
};
slider();

/*Функция POPUP. На блок который надо увеличивать необходимо установить name="box"*/
function popup(){
	$(".box").on('click', function(){
		var copy = $(this).clone();
		console.log($(this).parent().append('<div class="popup"></div>'));
		$(copy).appendTo(".popup");
		$(".popup").append('<i class="fa fa-times"></i>');
		$(document).mouseup(function (e){ // событие клика по веб-документу
			var div = $(".box");
			var cl = $(".popup i[class=pe-7s-close]"); // тут указываем ID элемента
			if (!div.is(e.target) && div.has(e.target).length === 0){ // и не по его дочерним элементам
				$("div.popup").remove(); // скрываем его
			}
			if(cl.is(e.target) && cl.has(e.target).length ===0){
				$("div.popup").remove();
			}
		});
	});
	$(document).bind('keydown', function(eventObject){
		if(eventObject.keyCode == 27){
			$("div.popup").remove();
		}
	});
}
popup();
/* Всплывающие окно */
function popButton(){
	$(".linkButton").on('click', function(){
		$(".windFree").removeClass("hid");


		$(document).mouseup(function (e){ // событие клика по веб-документу
			var div = $("#sentMess");
			var cl = $("i[class=pe-7s-close]"); // тут указываем ID элемента
			if (!div.is(e.target) && div.has(e.target).length === 0){ // и не по его дочерним элементам
				$(".windFree").addClass("hid"); // скрываем его
			}
			if(cl.is(e.target) && cl.has(e.target).length ===0){
				$(".windFree").addClass("hid");
			}
		});
	});
	$(document).bind('keydown', function(eventObject){
		if(eventObject.keyCode == 27){
			$(".windFree").addClass("hid");
		}
	});
}
popButton();
function sentMessWin(){
	$("#sentMess > .linkButton").on('click', function(){
		$(".sentMessOff").removeClass("hid");
	});
}
sentMessWin();
/* Buttom up*/
/*Кнопка вверх с плавным появлением и плавным скролом*/
/*topBottom - id элемента, на который надо нажать что бы вернуться на верх*/
document.onscroll = my_func;
function my_func(){
	var sc = $(document).scrollTop();/*текуще значение скрола*/
	if(sc > 500 && $("#topBottom").css("display") != "block"){ /*если проскройлили более 500 пикселей И кнопка скрыта то выполнять*/
		$("#topBottom").css({"display":"block"});
		block_in(0.1,$("#topBottom")); /*устанавливается первым параметром значение прозрачности, вторым на какой элемент будет применена функиця*/
	}
	else if( sc < 500 && $("#topBottom").css("display") != "none"){
		block_out($("#topBottom").css("opacity"),$("#topBottom"));
	}
}
function toTop(){/*данная вункция вызывается из html разментки по событию onclick на элементе с id topBottom*/
	var root = $(document);/*выбрали весь документ*/
	var scrol = root.scrollTop();/*значение скрола на данный момент*/
	scrol -=50;/*текущее значение скрола -10px*/
	root.scrollTop(scrol);/*проскролить до указанного значения*/
	if(scrol > 0){
		setTimeout(toTop,1);/*запуск рекурсии с интервалом в 1 милисекунду*/
	}
}
function block_in(op,elem){
	elem.css({"opacity":op})/*установить переданное в функцию значение прозрачности*/
	op += 0.3;/*шаг изменения прозрачности*/
	if(op < 1){
		setTimeout(
			function(){
				block_in(op,elem)/*запуск рекурсии через 100мс*/
			},
			100);
	}
}
function block_out(op,elem){
	elem.css({"opacity":op})
	op -= 0.3;
	if(op > 0){
		setTimeout(
			function(){
				block_out(op,elem)
			},
			100);
	}
	else{
		$("#topBottom").css({"display":"none"});/*после того как прозрачность стала 0, убрать элемент со страницы*/
	}
}
/* Прилоадер */
$(window).load(function(){
	$(".loader_inner").fadeOut();
	$(".loader").delay(250).fadeOut("slow");
});
