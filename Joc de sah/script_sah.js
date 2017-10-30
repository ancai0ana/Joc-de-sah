
    var id_sters='00';
    var id_unde_mut='01';
    MutarePion(id_unde_mut,id_sters);
    // id_sters=id_unde_mut;
    // id_unde_mut='20';
    // MutarePion(id_unde_mut,id_sters);
    // id_sters=id_unde_mut;
    // id_unde_mut='23';
    // MutarePion(id_unde_mut,id_sters);
    
    function MutarePion(id_unde_mut,id_sters){
        if(document.getElementById(id_unde_mut).childElementCount==0)
        {var elem=document.createElement("img");
        elem.setAttribute("src","white.png");
        elem.setAttribute("class","pion");
        elem.setAttribute("alt","pion alb");
        var ouput=document.getElementById(id_unde_mut).appendChild(elem);

        var elem2=document.getElementById(id_sters);
        var output=elem2.removeChild(elem2.childNodes[0]);
        }
        else
        //if(document.getElementById(id_unde_mut).childNodes[0].getAtribute("src")=="white.png")
        document.getElementById("done").innerHTML = "Te rog sa introduci o mutare valida";
        //else
       // document.getElementById("done").innerHTML = "nu-i bun";
    }
