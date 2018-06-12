window.onload = function(){
    var i = 0;
    window.setInterval(function(){
        if (i < document.body.childElementCount){
            if (i != 0){
                pic = document.getElementById("f-" + (i - 1));
                pic.innerHTML = "";
            }

            pic = document.getElementById("f-" + i);
            pic.hidden = "";
            i++;
        }
    }, 1000/fps);
}
