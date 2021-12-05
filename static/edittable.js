// Import the functions you need from the SDKs you need
// import { initializeApp } from "firebase/app";
// import { getAnalytics } from "firebase/analytics";
// // TODO: Add SDKs for Firebase products that you want to use
// // https://firebase.google.com/docs/web/setup#available-libraries
//
// // Your web app's Firebase configuration
// // For Firebase JS SDK v7.20.0 and later, measurementId is optional
// const firebaseConfig = {
//   apiKey: "AIzaSyClJ09Xuohg0AGyYuJ4iUPMMuz8_hLiIh8",
//   authDomain: "it-tickets-51e5b.firebaseapp.com",
//   databaseURL: "https://it-tickets-51e5b-default-rtdb.firebaseio.com",
//   projectId: "it-tickets-51e5b",
//   storageBucket: "it-tickets-51e5b.appspot.com",
//   messagingSenderId: "215099357702",
//   appId: "1:215099357702:web:f73c6f27413a5ac581e187",
//   measurementId: "G-EMF6HX575Y"
// };
//
// // Initialize Firebase
// const app = initializeApp(firebaseConfig);
// const analytics = getAnalytics(app);





function edit_row(rowNumber)
{
    // var plzWork = rowNumber
    // console.log(plzWork)
 document.getElementById("edit_button"+rowNumber).style.display="";
 document.getElementById("save_button"+rowNumber).style.display="block";


 var ticket=document.getElementById("ticket"+rowNumber);
 var status=document.getElementById("status"+rowNumber);
 var category=document.getElementById("category"+rowNumber);
 var title=document.getElementById("title"+rowNumber);
 var assignee=document.getElementById("assignee"+rowNumber);
 var details=document.getElementById("details"+rowNumber);
 var pointofcontact=document.getElementById("pointofcontact"+rowNumber);
 var dateticket=document.getElementById("date"+rowNumber);
 var dateresolved=document.getElementById("dateresolved"+rowNumber);



 var ti=ticket.innerHTML;
 var s=status.innerHTML;
 var c=category.innerHTML;
 var t=title.innerHTML;
 var a=assignee.innerHTML;
 var d=details.innerHTML;
 var poc=pointofcontact.innerHTML;
 var dt=dateticket.innerHTML;
 var dr=dateresolved.innerHTML;


 ticket.innerHTML="<input type='text' id='textticket"+rowNumber+"' value='"+ti+"'>";
 status.innerHTML="<input type='text' id='textstatus"+rowNumber+"' value='"+s+"'>";
 category.innerHTML="<input type='text' id='textcategory"+rowNumber+"' value='"+c+"'>";
 title.innerHTML="<input type='text' id='texttitle"+rowNumber+"' value='"+t+"'>";
 assignee.innerHTML="<input type='text' id='textassignee"+rowNumber+"' value='"+a+"'>";
 details.innerHTML="<input type='text' id='textdetails"+rowNumber+"' value='"+d+"'>";
 pointofcontact.innerHTML="<input type='text' id='textpointofcontact"+rowNumber+"' value='"+poc+"'>";
 dateticket.innerHTML="<input type='date' id='textdate"+rowNumber+"' value='"+dt+"'>";
 dateresolved.innerHTML="<input type='date' id='textdateresolved"+rowNumber+"' value='"+dr+"'>";

}

function save_row(rowNumber)
{




    var tval=document.getElementById("textticket"+rowNumber).value;
    var sval=document.getElementById("textstatus"+rowNumber).value;
    var cval=document.getElementById("textcategory"+rowNumber).value;
    var t2val=document.getElementById("texttitle"+rowNumber).value;
    var asval=document.getElementById("textassignee"+rowNumber).value;
    var dval=document.getElementById("textdetails"+rowNumber).value;
    var pocval=document.getElementById("textpointofcontact"+rowNumber).value;
    var dtval=document.getElementById("textdate"+rowNumber).value;
    var drtval=document.getElementById("textdateresolved"+rowNumber).value;



    document.getElementById("ticket"+rowNumber).innerHTML=tval;
    document.getElementById("status"+rowNumber).innerHTML=sval;
    document.getElementById("category"+rowNumber).innerHTML=cval;
    document.getElementById("title"+rowNumber).innerHTML=t2val;
    document.getElementById("assignee"+rowNumber).innerHTML=asval;
    document.getElementById("details"+rowNumber).innerHTML=dval;
    document.getElementById("pointofcontact"+rowNumber).innerHTML=pocval;
    document.getElementById("dateticket"+rowNumber).innerHTML=dtval;
    document.getElementById("dateresolved"+rowNumber).innerHTML=drtval;





}
