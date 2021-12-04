function edit_row(num)
{
 document.getElementById("edit_button"+num).style.display="none";
	
 var ticket=document.getElementById("ticket"+num);
 var status=document.getElementById("status"+num);
 var category=document.getElementById("category"+num);
 var title=document.getElementById("title"+num);
 var description=document.getElementById("description"+num);
 var pointofcontact=document.getElementById("point of contact"+num);
 var assignee=document.getElementById("assignee"+num);
 var dateopened=document.getElementById("dateopened"+num);
 var dateresolved=document.getElementById("dateresolved"+num);

	
 var t=ticket.innerHTML;
 var s=status.innerHTML;
 var c=category.innerHTML;
 var t=title.innerHTML;
 var d=description.innerHTML;
 var poc=pointofcontact.innerHTML;
 var a=assignee.innerHTML;
 var dopen=dateopened.innerHTML;
 var dr=dateresolved.innerHTML;



	
 ticket.innerHTML="<input type='text' id='textticket"+num+"' value='"+t+"'>";
 status.innerHTML="<input type='text' id='textstatus"+num+"' value='"+s+"'>";
 category.innerHTML="<input type='text' id='textcategory"+num+"' value='"+c+"'>";
 title.innerHTML="<input type='text' id='texttitle"+num+"' value='"+t+"'>";
 description.innerHTML="<input type='text' id='textdescription"+num+"' value='"+d+"'>";
 pointofcontact.innerHTML="<input type='text' id='textpointofcontact"+num+"' value='"+poc+"'>";
 assignee.innerHTML="<input type='text' id='textassignee"+num+"' value='"+a+"'>";
 dateopened.innerHTML="<input type='text' id='textdateopened"+num+"' value='"+dopen+"'>";
 dateresolved.innerHTML="<input type='text' id='textdateresolved"+num+"' value='"+dr+"'>";

}
function save_row(num)
{
 var tval=document.getElementById("textticket"+num).value;
 var sval=document.getElementById("textstatus"+num).value;
 var cval=document.getElementById("textcategory"+num).value;
 var t2val=document.getElementById("texttitle"+num).value;
 var dval=document.getElementById("textdescription"+num).value;
 var pocval=document.getElementById("textpointofcontact"+num).value;
 var aval=document.getElementById("textassignee"+num).value;
 var doval=document.getElementById("textdateopened"+num).value;
 var drval=document.getElementById("textdateresolved"+num).value;


 document.getElementById("ticket"+num).innerHTML=tval;
 document.getElementById("status"+num).innerHTML=sval;
 document.getElementById("category"+num).innerHTML=cval;
 document.getElementById("title"+num).innerHTML=t2val;
 document.getElementById("description"+num).innerHTML=dval;
 document.getElementById("pointofcontact"+num).innerHTML=pocval;
 document.getElementById("assignee"+num).innerHTML=aval;
 document.getElementById("dateopened"+num).innerHTML=doval;
 document.getElementById("dateresolved"+num).innerHTML=drval;


 document.getElementById("edit_button"+num).style.display="block";
 document.getElementById("save_button"+num).style.display="none";
}




