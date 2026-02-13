let keys=[], down={}, last=null;

document.addEventListener("keydown",e=>{
 if(e.repeat) return;
 down[e.key]=performance.now();
});

document.addEventListener("keyup",e=>{
 let now=performance.now();
 let dwell=now-down[e.key];
 let flight=last?now-last:0;
 keys.push({key:e.key,dwell,flight,time:now});
 last=now;
 delete down[e.key];
});

setInterval(async()=>{
 if(keys.length<20) return;

 let payload=[...keys];
 keys=[];

 let res=await fetch("/exam",{
  method:"POST",
  headers:{"Content-Type":"application/json"},
  body:JSON.stringify(payload)
 });

 let data=await res.json();
 document.getElementById("status").innerText=`Confidence: ${data.confidence}%`;
 if(data.action==="alert") alert("Suspicious typing detected");
},10000);
