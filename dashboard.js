async function load(){
 let res=await fetch("/api/admin/sessions");
 let data=await res.json();
 let table=document.getElementById("table");
 table.innerHTML="<tr><th>User</th><th>Confidence</th><th>Status</th></tr>";
 data.forEach(s=>{
  table.innerHTML+=`<tr><td>${s.user_id}</td><td>${s.confidence}</td><td>${s.status}</td></tr>`;
 });
}
setInterval(load,5000);
load();
