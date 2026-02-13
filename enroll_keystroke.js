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

document.querySelector("form").onsubmit=()=>{
 document.getElementById("keystroke_data").value=JSON.stringify(keys);
};
