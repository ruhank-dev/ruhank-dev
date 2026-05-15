
<style>
@import url('https://fonts.googleapis.com/css2?family=Archive&family=Bebas+Neue&family=Calligraffitti&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
html{background:#000}
body{background:#000;color:#fff;font-family:'Archive',sans-serif;overflow-x:hidden}

#c{display:block;width:100%;height:400px;background:#000}

.hero-meta{display:flex;flex-direction:column;align-items:center;padding:16px 32px 44px;border-bottom:1px solid #333}
.hero-sub{font-size:11px;color:#aaa;letter-spacing:5px;text-transform:uppercase;margin-bottom:6px}
.hero-loc{font-size:10px;color:#666;letter-spacing:3px;text-transform:uppercase}

.stats{display:grid;grid-template-columns:repeat(3,1fr);border-bottom:1px solid #333}
.stat{padding:30px 16px;text-align:center;border-right:1px solid #333}
.stat:last-child{border-right:none}
.stat-n{font-family:'Bebas Neue',sans-serif;font-size:42px;color:#fff;letter-spacing:2px;display:block}
.stat-l{font-size:9px;color:#888;letter-spacing:4px;text-transform:uppercase;margin-top:3px}

.sec{padding:48px 28px 32px}
.sec-head{display:flex;align-items:center;gap:14px;margin-bottom:32px}
.sec-line{flex:1;height:1px;background:#333}
.sec-title{font-size:13px;color:#fff;letter-spacing:3px;text-transform:uppercase;white-space:nowrap;font-family:'Archive',sans-serif}
.sec-title-cal{font-size:32px;color:#fff;white-space:nowrap;font-family:'Calligraffitti',cursive;line-height:1}

/* BELT */
.belt-wrap{border-top:1px solid #2a2a2a;border-bottom:1px solid #2a2a2a;overflow:hidden;position:relative;padding:20px 0}
.belt-wrap::before,.belt-wrap::after{content:'';position:absolute;top:0;bottom:0;width:80px;z-index:2;pointer-events:none}
.belt-wrap::before{left:0;background:linear-gradient(90deg,#000,transparent)}
.belt-wrap::after{right:0;background:linear-gradient(270deg,#000,transparent)}
.belt{display:flex;gap:12px;width:max-content;animation:scrolll 30s linear infinite}
.belt:hover{animation-play-state:paused}
@keyframes scrolll{from{transform:translateX(0)}to{transform:translateX(-50%)}}
.b-item{display:flex;flex-direction:column;align-items:center;justify-content:center;width:84px;height:72px;border:1px solid #2a2a2a;background:#000;flex-shrink:0;transition:border-color .2s;position:relative}
.b-item::before{content:'';position:absolute;top:3px;left:3px;width:6px;height:6px;border-top:1px solid #333;border-left:1px solid #333}
.b-item::after{content:'';position:absolute;bottom:3px;right:3px;width:6px;height:6px;border-bottom:1px solid #333;border-right:1px solid #333}
.b-item:hover{border-color:#666}
.b-icon{width:26px;height:26px;filter:invert(1) brightness(.7);transition:filter .2s}
.b-item:hover .b-icon{filter:invert(1) brightness(1)}
.b-label{font-size:7px;color:#666;letter-spacing:2px;margin-top:7px;text-transform:uppercase;transition:color .2s}
.b-item:hover .b-label{color:#aaa}

/* PROJECTS */
.projects{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1px;background:#222;border:1px solid #222}
.pcard{background:#000;padding:28px 22px 26px;position:relative;overflow:hidden;cursor:pointer;transition:background .2s}
.pcard:hover{background:#0a0a0a}
.pcard:hover .parrow{opacity:1;transform:translateX(0)}
.pnum{
  position:absolute;right:14px;top:8px;
  font-family:'Bebas Neue',sans-serif;font-size:76px;line-height:1;
  color:transparent;pointer-events:none;
  -webkit-text-stroke:1px rgba(255,255,255,0.1);
  background:linear-gradient(135deg,rgba(255,255,255,.18) 0%,rgba(120,220,255,.12) 30%,rgba(255,255,255,.05) 50%,rgba(180,100,255,.1) 75%,rgba(255,255,255,.15) 100%);
  -webkit-background-clip:text;background-clip:text;
  animation:holo 5s ease infinite alternate;background-size:200% 200%;
}
@keyframes holo{0%{background-position:0% 50%;opacity:.7}50%{background-position:100% 50%;opacity:1}100%{background-position:0% 50%;opacity:.7}}
.pcontent{position:relative;z-index:1}
.ptag{font-size:15px;color:#aaa;margin-bottom:8px;font-family:'Calligraffitti',cursive;line-height:1.3}
.pname{font-size:22px;color:#eee;margin-bottom:9px;line-height:1.2;font-family:'Calligraffitti',cursive}
.pdesc{font-size:14px;color:#888;line-height:1.7;font-family:'Calligraffitti',cursive}
.pstack{display:flex;flex-wrap:wrap;gap:6px;margin-top:14px}
.ptagi{font-size:13px;color:#888;font-family:'Calligraffitti',cursive;padding:2px 8px;border:1px solid #2a2a2a}
.parrow{position:absolute;bottom:20px;right:20px;font-size:16px;color:#888;opacity:0;transform:translateX(-5px);transition:all .2s;z-index:1}

/* BALLOONS */
.balloons-section{padding:48px 28px 60px}
.balloons-sec-head{display:flex;align-items:center;gap:14px;margin-bottom:48px}
.balloons-wrap{
  display:flex;flex-wrap:wrap;justify-content:center;align-items:flex-end;
  gap:20px 28px;min-height:260px;padding:20px 0 0;
}
.balloon-item{
  display:flex;flex-direction:column;align-items:center;
}
.balloon-body{
  position:relative;
  display:flex;align-items:center;justify-content:center;
  border-radius:50% 50% 50% 50% / 55% 55% 45% 45%;
  box-shadow:inset -6px -10px 18px rgba(0,0,0,0.3), 0 8px 32px rgba(255,255,255,0.06);
  transform:scale(0);
  animation:pop-in 0.65s cubic-bezier(0.34,1.56,0.64,1) forwards, bob ease-in-out infinite;
}
@keyframes pop-in{to{transform:scale(1)}}
@keyframes bob{0%,100%{transform:scale(1) translateY(0) rotate(-1.2deg)}50%{transform:scale(1) translateY(-14px) rotate(1.2deg)}}
.balloon-body::after{
  content:'';position:absolute;bottom:-9px;left:50%;transform:translateX(-50%);
  border-left:5px solid transparent;border-right:5px solid transparent;
  border-top:10px solid var(--knot);
}
.balloon-string{width:1px;height:42px;background:linear-gradient(to bottom,rgba(255,255,255,0.35),rgba(255,255,255,0.04))}
.balloon-label{
  font-size:20px;color:#ccc;margin-top:7px;
  font-family:'Calligraffitti',cursive;
  text-align:center;max-width:120px;line-height:1.2;
}

/* ABOUT */
.about-grid{display:grid;grid-template-columns:1fr 1fr;gap:32px}
@media(max-width:520px){.about-grid{grid-template-columns:1fr}}
.about-t{font-size:26px;color:#ccc;margin-bottom:16px;padding-bottom:10px;border-bottom:1px solid #222;font-family:'Calligraffitti',cursive}
.about-row{display:flex;justify-content:space-between;padding:9px 0;border-bottom:1px solid #111}
.ak{font-size:17px;color:#888;font-family:'Calligraffitti',cursive}
.av{font-size:17px;color:#ccc;font-family:'Calligraffitti',cursive;text-align:right}

/* CONNECT */
.connect-row{display:flex;gap:1px;flex-wrap:wrap}
.cbtn{display:flex;align-items:center;gap:10px;padding:16px 24px;border:1px solid #2a2a2a;background:#000;color:#aaa;font-family:'Calligraffitti',cursive;font-size:20px;text-decoration:none;cursor:pointer;transition:all .2s;flex:1;min-width:160px;justify-content:center}
.cbtn:hover{background:#080808;color:#eee;border-color:#444}
.cicon{width:14px;height:14px;filter:invert(1) brightness(.5);transition:filter .2s}
.cbtn:hover .cicon{filter:invert(1) brightness(.9)}

.ain{opacity:0;transform:translateY(12px)}
.ain.vis{animation:rise .65s forwards}
@keyframes rise{to{opacity:1;transform:translateY(0)}}
</style>

<canvas id="c"></canvas>

<div class="hero-meta">
  <div class="hero-sub">Software Engineer &nbsp;·&nbsp; AI Engineer &nbsp;·&nbsp; Systems Programmer</div>
  <div class="hero-loc">FAST NUCES &nbsp;·&nbsp; Islamabad, PK &nbsp;·&nbsp; BSCS 2027</div>
</div>

<div class="stats ain">
  <div class="stat"><span class="stat-n" data-t="10">0</span><span class="stat-l">Projects</span></div>
  <div class="stat"><span class="stat-n" data-t="8">0</span><span class="stat-l">Languages</span></div>
  <div class="stat"><span class="stat-n" data-t="4">0</span><span class="stat-l">Years Coding</span></div>
</div>

<div style="padding:40px 0 0" class="ain">
  <div class="sec-head" style="padding:0 28px;margin-bottom:22px">
    <div class="sec-line"></div><div class="sec-title">Tech Stack</div><div class="sec-line"></div>
  </div>
  <div class="belt-wrap"><div class="belt" id="belt"></div></div>
</div>

<div class="sec ain">
  <div class="sec-head"><div class="sec-line"></div><div class="sec-title">Featured Projects</div><div class="sec-line"></div></div>
  <div class="projects">
    <div class="pcard"><div class="pnum">01</div><div class="pcontent">
      <div class="ptag">GPU Computing</div>
      <div class="pname">Video Analytics Engine</div>
      <div class="pdesc">Real-time KLT optical flow tracking parallelized across GPU cores. Live motion vector extraction at scale.</div>
      <div class="pstack"><span class="ptagi">C++</span><span class="ptagi">CUDA</span><span class="ptagi">OpenACC</span><span class="ptagi">OpenCV</span></div>
    </div><div class="parrow">→</div></div>
    <div class="pcard"><div class="pnum">02</div><div class="pcontent">
      <div class="ptag">AI · Full Stack</div>
      <div class="pname">Property CRM</div>
      <div class="pdesc">AI-powered lead management with NVIDIA Nemotron 3, real-time socket events, and role-based access control.</div>
      <div class="pstack"><span class="ptagi">Next.js</span><span class="ptagi">MongoDB</span><span class="ptagi">Socket.io</span><span class="ptagi">NVIDIA AI</span></div>
    </div><div class="parrow">→</div></div>
    <div class="pcard"><div class="pnum">03</div><div class="pcontent">
      <div class="ptag">Civic Tech</div>
      <div class="pname">Civanta</div>
      <div class="pdesc">Geo-tagged civic issue reporting with full-stack routing, interactive maps, and real-time updates.</div>
      <div class="pstack"><span class="ptagi">React</span><span class="ptagi">Spring Boot</span><span class="ptagi">Leaflet.js</span></div>
    </div><div class="parrow">→</div></div>
    <div class="pcard"><div class="pnum">04</div><div class="pcontent">
      <div class="ptag">Compiler Design</div>
      <div class="pname">Compiler + Parser</div>
      <div class="pdesc">Full pipeline — Lexer → LL(1) → SLR(1)/LR(1) → JSON to XML translator, built from scratch.</div>
      <div class="pstack"><span class="ptagi">C++</span><span class="ptagi">Flex</span><span class="ptagi">Yacc</span><span class="ptagi">Bison</span></div>
    </div><div class="parrow">→</div></div>
  </div>
</div>

<!-- BALLOONS -->
<div class="balloons-section ain">
  <div class="balloons-sec-head">
    <div class="sec-line"></div><div class="sec-title">Expertise</div><div class="sec-line"></div>
  </div>
  <div class="balloons-wrap" id="balloons"></div>
</div>

<!-- ABOUT -->
<div class="sec ain">
  <div class="sec-head"><div class="sec-line"></div><div class="sec-title-cal">About</div><div class="sec-line"></div></div>
  <div class="about-grid">
    <div>
      <div class="about-t">Education</div>
      <div class="about-row"><span class="ak">University</span><span class="av">FAST NUCES</span></div>
      <div class="about-row"><span class="ak">Degree</span><span class="av">BS Computer Science</span></div>
      <div class="about-row"><span class="ak">Expected</span><span class="av">2027</span></div>
      <div class="about-row"><span class="ak">A-Levels</span><span class="av">PAEC Science School</span></div>
    </div>
    <div>
      <div class="about-t">Info</div>
      <div class="about-row"><span class="ak">Location</span><span class="av">Islamabad, PK</span></div>
      <div class="about-row"><span class="ak">GitHub</span><span class="av">ruhank-dev</span></div>
      <div class="about-row"><span class="ak">Focus</span><span class="av">AI · Systems · Fullstack</span></div>
      <div class="about-row"><span class="ak">Status</span><span class="av">Open to opportunities</span></div>
    </div>
  </div>
</div>

<!-- CONNECT -->
<div class="sec ain" style="padding-top:0">
  <div class="sec-head"><div class="sec-line"></div><div class="sec-title-cal">Connect</div><div class="sec-line"></div></div>
  <div class="connect-row">
    <a href="https://github.com/ruhank-dev" class="cbtn" target="_blank">
      <svg class="cicon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/></svg>
      GitHub
    </a>
    <a href="https://linkedin.com/in/ruhan-kamran-b99007372" class="cbtn" target="_blank">
      <svg class="cicon" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
      LinkedIn
    </a>
  </div>
</div>

<script>
/* ══ PARTICLE HERO ══ */
(function(){
  const cv=document.getElementById('c');
  const ctx=cv.getContext('2d');
  cv.width=cv.offsetWidth||800;cv.height=400;
  const W=cv.width,H=cv.height,FS=Math.min(W*0.17,120);
  const off=document.createElement('canvas');off.width=W;off.height=H;
  const oc=off.getContext('2d');
  function renderText(c,alpha){
    c.save();c.clearRect(0,0,W,H);
    c.font=`900 ${FS}px "Bebas Neue",Impact,"Arial Black",sans-serif`;
    c.textAlign='center';c.textBaseline='middle';
    c.fillStyle=`rgba(255,255,255,${alpha})`;c.fillText('RUHAN-K-DEV',W/2,H/2);c.restore();
  }
  function go(){
    renderText(oc,1);
    const id=oc.getImageData(0,0,W,H).data;const pts=[];
    for(let y=0;y<H;y+=3)for(let x=0;x<W;x+=3)if(id[(y*W+x)*4+3]>80)pts.push([x,y]);
    if(pts.length<10){
      oc.clearRect(0,0,W,H);oc.font=`900 ${FS}px Impact`;oc.fillStyle='#fff';
      oc.textAlign='center';oc.textBaseline='middle';oc.fillText('RUHAN-K-DEV',W/2,H/2);
      const id2=oc.getImageData(0,0,W,H).data;
      for(let y=0;y<H;y+=3)for(let x=0;x<W;x+=3)if(id2[(y*W+x)*4+3]>80)pts.push([x,y]);
    }
    const N=pts.length;
    const px=new Float32Array(N),py=new Float32Array(N),pvx=new Float32Array(N),pvy=new Float32Array(N);
    const ptx=new Float32Array(N),pty=new Float32Array(N),pdx=new Float32Array(N),pdy=new Float32Array(N);
    const pdd=new Float32Array(N),pa=new Float32Array(N);
    for(let i=0;i<N;i++){
      ptx[i]=pts[i][0];pty[i]=pts[i][1];
      const a=Math.random()*Math.PI*2,d=150+Math.random()*Math.max(W,H)*.7;
      px[i]=W/2+Math.cos(a)*d;py[i]=H/2+Math.sin(a)*d;
      pvx[i]=(Math.random()-.5)*.3;pvy[i]=(Math.random()-.5)*.3;pa[i]=0;
    }
    function setupDust(){for(let i=0;i<N;i++){pdd[i]=(ptx[i]/W)*1800;const a=(Math.random()-.5)*.8+.08,d=80+Math.random()*300;pdx[i]=ptx[i]+Math.cos(a)*d+120;pdy[i]=pty[i]+(Math.random()-.5)*80;}}
    let phase=0,phaseT=0,last=null;const DUR=[5000,2600,2600,700];
    function loop(now){
      requestAnimationFrame(loop);if(!last)last=now;
      const dt=Math.min(now-last,50);last=now;phaseT+=dt;
      if(phase===0&&phaseT>DUR[0]){phase=1;phaseT=0;}
      else if(phase===1&&phaseT>DUR[1]){setupDust();phase=2;phaseT=0;}
      else if(phase===2&&phaseT>DUR[2]){phase=3;phaseT=0;}
      else if(phase===3&&phaseT>DUR[3]){
        for(let i=0;i<N;i++){const a=Math.random()*Math.PI*2,d=150+Math.random()*Math.max(W,H)*.7;px[i]=W/2+Math.cos(a)*d;py[i]=H/2+Math.sin(a)*d;pvx[i]=(Math.random()-.5)*.3;pvy[i]=(Math.random()-.5)*.3;pa[i]=0;}
        phase=0;phaseT=0;
      }
      ctx.fillStyle='rgba(0,0,0,0.25)';ctx.fillRect(0,0,W,H);
      if(phase===1)renderText(ctx,Math.min(1,phaseT/200));
      ctx.save();ctx.font='400 10px monospace';ctx.fillStyle='rgba(255,255,255,0.35)';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('GITHUB.COM / RUHAN-K-DEV',W/2,H/2-FS*.78);ctx.restore();
      const prog=Math.min(phaseT/DUR[phase],1);
      for(let i=0;i<N;i++){
        if(phase===0){const spd=0.012+prog*0.035;pvx[i]+=(ptx[i]-px[i])*spd;pvy[i]+=(pty[i]-py[i])*spd;pvx[i]*=0.77;pvy[i]*=0.77;px[i]+=pvx[i];py[i]+=pvy[i];const dist=Math.hypot(ptx[i]-px[i],pty[i]-py[i]);pa[i]+=(Math.max(0,1-dist/100)*.92-pa[i])*.04;}
        else if(phase===1){px[i]+=(ptx[i]-px[i])*.2+(Math.random()-.5)*.1;py[i]+=(pty[i]-py[i])*.2+(Math.random()-.5)*.1;pa[i]=0;}
        else if(phase===2){if(phaseT>pdd[i]){const lp=Math.min((phaseT-pdd[i])/(DUR[2]*.38),1),e=lp*lp*lp;px[i]+=(pdx[i]-px[i])*e*.06+e*1.1;py[i]+=(pdy[i]-py[i])*e*.03+(Math.random()-.5)*e*.8;pa[i]=Math.max(pa[i]-e*.07,0);}else pa[i]=0.9;}
        else{px[i]+=(Math.random()-.5)*.5;py[i]+=(Math.random()-.5)*.5;pa[i]=Math.max(pa[i]-.012,0);}
        if(pa[i]<.01)continue;
        ctx.beginPath();ctx.arc(px[i],py[i],1,0,Math.PI*2);
        ctx.fillStyle=`rgba(255,255,255,${pa[i].toFixed(2)})`;ctx.fill();
      }
    }
    requestAnimationFrame(loop);
  }
  if(document.fonts&&document.fonts.load)document.fonts.load(`900 ${FS}px "Bebas Neue"`).then(go).catch(go);
  else setTimeout(go,500);
})();

/* ══ BALLOONS ══ */
(function(){
  const skills=[
    {name:'Systems / C++',   pct:95},
    {name:'Full-Stack Web',  pct:85},
    {name:'AI / ML',         pct:80},
    {name:'GPU / CUDA',      pct:70},
    {name:'Compiler Design', pct:78},
    {name:'Networking',      pct:72},
  ];
  const shades=[
    {fill:'#efefef',knot:'#b0b0b0'},
    {fill:'#d4d4d4',knot:'#999'},
    {fill:'#c0c0c0',knot:'#888'},
    {fill:'#e8e8e8',knot:'#aaa'},
    {fill:'#cacaca',knot:'#909090'},
    {fill:'#b8b8b8',knot:'#808080'},
  ];
  const wrap=document.getElementById('balloons');
  skills.forEach((sk,i)=>{
    const minS=68,maxS=108;
    const size=Math.round(minS+(sk.pct-70)/(95-70)*(maxS-minS));
    const s=shades[i%shades.length];
    const popDelay=i*0.13;
    const bobDur=3.0+i*0.3;
    const bobDelay=popDelay+0.65;

    const item=document.createElement('div');
    item.className='balloon-item';
    item.innerHTML=`
      <div class="balloon-body" style="
        width:${size}px;
        height:${Math.round(size*1.22)}px;
        --knot:${s.knot};
        background:
          radial-gradient(circle at 30% 26%, rgba(255,255,255,0.7) 0%, rgba(255,255,255,0.0) 48%),
          radial-gradient(circle at 70% 72%, rgba(0,0,0,0.16) 0%, transparent 42%),
          ${s.fill};
        animation:
          pop-in 0.65s cubic-bezier(0.34,1.56,0.64,1) ${popDelay}s both,
          bob ${bobDur}s ${bobDelay}s ease-in-out infinite;
      "></div>
      <div class="balloon-string"></div>
      <div class="balloon-label">${sk.name}</div>
    `;
    wrap.appendChild(item);
  });
})();

/* ══ BELT ══ */
(function(){
  const items=[
    {n:'Python',s:'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg'},
    {n:'C++',s:'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg'},
    {n:'CUDA',s:'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nvidia/nvidia-original.svg'},
    {n:'Java',s:'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg'},
    {n:'React',s:'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg'},
    {n:'Next.js',s:'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nextjs/nextjs-original.svg'},
    {n:'Docker',s:'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg'},
    {n:'Linux',s:'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg'},
    {n:'Git',s:'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg'},
    {n:'MongoDB',s:'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg'},
    {n:'SQL',s:'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg'},
    {n:'Bash',s:'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg'},
    {n:'C',s:'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg'},
    {n:'JS',s:'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg'},
  ];
  const belt=document.getElementById('belt');
  [...items,...items].forEach(it=>{
    const el=document.createElement('div');el.className='b-item';
    el.innerHTML=`<img class="b-icon" src="${it.s}" alt="${it.n}" loading="lazy"><span class="b-label">${it.n}</span>`;
    belt.appendChild(el);
  });
})();

/* ══ COUNTERS + OBSERVERS ══ */
function animateCounters(){
  document.querySelectorAll('.stat-n[data-t]').forEach(el=>{
    const t=+el.dataset.t;let c=0;
    const iv=setInterval(()=>{c=Math.min(t,c+t/30);el.textContent=Math.floor(c);if(c>=t)clearInterval(iv);},40);
  });
}
const io=new IntersectionObserver(e=>{
  e.forEach(x=>{
    if(x.isIntersecting){
      x.target.classList.add('vis');
      if(x.target.classList.contains('stats'))animateCounters();
    }
  });
},{threshold:.1});
document.querySelectorAll('.ain').forEach(el=>io.observe(el));
</script>
