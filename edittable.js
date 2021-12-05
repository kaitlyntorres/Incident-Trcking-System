function edit_row()
{
 document.getElementById("edit_button").style.display="";
 document.getElementById("save_button").style.display="block";

	
 var ticket=document.getElementById("ticket");
 var status=document.getElementById("status");
 var category=document.getElementById("category");
 var title=document.getElementById("title");
 var description=document.getElementById("details");
 var pointofcontact=document.getElementById("pointofcontact");
 var dateticket=document.getElementById("date");


	
 var t=ticket.innerHTML;
 var s=status.innerHTML;
 var c=category.innerHTML;
 var t=title.innerHTML;
 var d=details.innerHTML;
 var poc=pointofcontact.innerHTML;
 var dt=dateticket.innerHTML;
 



	
 ticket.innerHTML="<input type='text' id='textticket"+"' value='"+t+"'>";
 status.innerHTML="<input type='text' id='textstatus"+"' value='"+s+"'>";
 category.innerHTML="<input type='text' id='textcategory"+"' value='"+c+"'>";
 title.innerHTML="<input type='text' id='texttitle"+"' value='"+t+"'>";
 details.innerHTML="<input type='text' id='textdetails"+"' value='"+d+"'>";
 pointofcontact.innerHTML="<input type='text' id='textpointofcontact"+"' value='"+poc+"'>";
 dateticket.innerHTML="<input type='date' id='textdate"+"' value='"+dt+"'>";

}
function save_row()
{
    
    var tval=document.getElementById("textticket").value;
    var sval=document.getElementById("textstatus").value;
    var cval=document.getElementById("textcategory").value;
    var t2val=document.getElementById("texttitle").value;
    var dval=document.getElementById("textdetails").value;
    var pocval=document.getElementById("textpointofcontact").value;
    var dtval=document.getElementById("textdate").value;


    document.getElementById("ticket").innerHTML=tval;
    document.getElementById("status").innerHTML=sval;
    document.getElementById("category").innerHTML=cval;
    document.getElementById("title").innerHTML=t2val;
    document.getElementById("details").innerHTML=dval;
    document.getElementById("pointofcontact").innerHTML=pocval;
    document.getElementById("dateticket").innerHTML=dtval;

    document.getElementById("edit_button").style.display="block";
    document.getElementById("save_button").style.display="none";



}




