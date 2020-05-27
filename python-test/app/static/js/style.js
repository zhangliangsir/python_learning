function click_hello(){
    document.getElementById("left").innerHTML = "<iframe src='directory'"+"style='width: 100%;height: 100%;'"+"></iframe>";
    document.getElementById("right").innerHTML = "<iframe src='hello'"+"style='width: 100%;height: 100%;'"+"></iframe>";
}
function click_user(){
    window.parent.document.getElementById("right").innerHTML = "<iframe src='user'"+"style='width: 100%;height: 100%;'"+"></iframe>";
}
function click_baidu(){
    window.parent.document.getElementById("right").innerHTML = "<iframe src='https://www.baidu.com/'"+"style='width:100%;height:100%;'"+"></iframe>";
}
function click_caiNiao(){
    window.parent.document.getElementById("right").innerHTML = "<iframe src='https://www.runoob.com/'"+"style='width:100%;height:100%;'"+"></iframe>";
}
function click_calculator(){
    window.parent.document.getElementById("right").innerHTML = "<iframe src='http://www.zxjsq.net/'"+"style='width:100%;height:100%;'"+"></iframe>";
}
function click_translator(){
    window.parent.document.getElementById("right").innerHTML = "<iframe src='http://fanyi.youdao.com/'"+"style='width:100%;height:100%;'"+"></iframe>";
}
function click_notepad(){
    window.parent.document.getElementById("right").innerHTML = "<iframe src='http://www.txttool.com/wenben_htmleditor.asp'"+"style='width:100%;height:100%;'"+"></iframe>";
}
function click_html(){
    window.parent.document.getElementById("right").innerHTML = "<iframe src='htmlTest'"+"style='width: 100%;height: 100%;'"+"></iframe>";
}
function click_note(){
    window.parent.document.getElementById("right").innerHTML = "<iframe src='notebook'"+"style='width: 100%;height: 100%;'"+"></iframe>";
}
function click_add(){
    var ul=document.getElementById("single");
    var li=document.createElement("li");
    li.innerHTML='<ul><span onclick=\"click_user()\">message</span></ul>'
    ul.appendChild(li);
}
function click_insert(){
    clickName="";
	<!-- window.open('http://10.80.20.63:5000/insert_web','insert_web');-->
	window.location.replace('http://10.80.20.63:5000/insert_web')
}
function click_update(){
    clickName="update"
}
function click_delete(){
    clickName="delete"
}
function show_dialog(){
	var x=document.getElementById("MyDialog");
	x.show();
}
function close_dialog(){
	var x=document.getElementById("MyDialog");
	x.close();
}
