/* Logo orb — compact adaptation, Free Unit Converter palette */
(function init(){
  if (document.readyState === "loading"){
    document.addEventListener("DOMContentLoaded", init, {once:true});
    return;
  }
  const c = document.getElementById("logoOrb");
  if (!c) return;
  const ctx = c.getContext("2d");
  const W = c.width, H = c.height, CX = W/2, CY = H/2;
  const R = W*0.36, PERSP = W*1.3;

  const rings = [];
  for (let i = 0; i < 7; i++){
    const t = i/7, dots = [], count = 16 + (i % 3) * 4;
    for (let j = 0; j < count; j++){
      dots.push({ a:(j/count)*Math.PI*2,
                  speed:0.00035 + i*0.00004 + (j%5)*0.00002,
                  size:1.1 + (j%3)*0.5 });
    }
    rings.push({ dots, tiltA:-0.95 + t*1.9, tiltB:t*Math.PI,
                 rs:0.75 + (i%4)*0.07, po:i*0.9, ps:0.95 + i*0.05 });
  }

  const rX=(p,a)=>{const q=Math.cos(a),s=Math.sin(a);return{x:p.x,y:p.y*q-p.z*s,z:p.y*s+p.z*q};};
  const rY=(p,a)=>{const q=Math.cos(a),s=Math.sin(a);return{x:p.x*q+p.z*s,y:p.y,z:-p.x*s+p.z*q};};
  const rZ=(p,a)=>{const q=Math.cos(a),s=Math.sin(a);return{x:p.x*q-p.y*s,y:p.x*s+p.y*q,z:p.z};};
  const proj=p=>{const s=PERSP/(PERSP-p.z);return{x:CX+p.x*s,y:CY+p.y*s,s};};

  function frame(time){
    ctx.clearRect(0,0,W,H);
    const gY=time*0.0005, gX=Math.sin(time*0.00021)*0.26, gZ=Math.cos(time*0.00017)*0.12;

    const glow = ctx.createRadialGradient(CX,CY,2,CX,CY,R*1.45);
    glow.addColorStop(0,"rgba(201,124,93,0.45)");
    glow.addColorStop(1,"rgba(123,164,208,0)");
    ctx.fillStyle = glow;
    ctx.fillRect(0,0,W,H);

    const pts=[];
    for (const r of rings){
      for (const d of r.dots){
        const a = d.a + time*d.speed;
        let p = { x:Math.cos(a)*R*r.rs, y:0, z:Math.sin(a)*R*r.rs };
        p = rX(p,r.tiltA); p = rY(p,r.tiltB + time*0.0002);
        p = rX(p,gX); p = rY(p,gY); p = rZ(p,gZ);
        const pr = proj(p);
        const trav = (a*1.2 + time*0.001*r.ps + r.po) % (Math.PI*2);
        const pulse = Math.pow(Math.max(0,Math.cos(trav)),14);
        const front = Math.max(0.18, Math.min(1,(p.z+R)/(R*2)));
        pts.push({ x:pr.x, y:pr.y, z:p.z,
                   rad:d.size*pr.s*(1+pulse*1.6),
                   alpha:0.2 + front*0.7 + pulse*0.3 });
      }
    }
    pts.sort((a,b)=>a.z-b.z);
    for (const pt of pts){
      ctx.fillStyle = "rgba(231,226,217," + Math.min(1,pt.alpha) + ")";
      ctx.beginPath();
      ctx.arc(pt.x, pt.y, Math.max(0.5,pt.rad), 0, Math.PI*2);
      ctx.fill();
    }
  }

  /* Reduced-motion users get a slow, gentle version instead of a frozen frame */
  let speedFactor = 1;
  try {
    if (window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches) speedFactor = 0.15;
  } catch(e){}

  /* Robust animation loop: rAF with a setInterval fallback, driven by its own clock
     so throttled/paused rAF in sandboxed iframes cannot freeze the orb permanently */
  let virtual = 0, lastReal = null;
  function tick(real){
    if (lastReal === null) lastReal = real;
    virtual += Math.min(64, real - lastReal) * speedFactor;
    lastReal = real;
    frame(virtual);
  }
  if (typeof requestAnimationFrame === "function"){
    requestAnimationFrame(function loop(t){ tick(t); requestAnimationFrame(loop); });
  } else {
    setInterval(function(){ tick(Date.now()); }, 33);
  }
})();
