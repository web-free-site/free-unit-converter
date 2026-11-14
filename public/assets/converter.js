"use strict";
const CATS = [
{ name:"Acceleration", base:"m/s²", units:[
  ["Centimeters/sec² (gal)",0.01],["Feet/sec²",0.3048],["Free fall (g)",9.80665],
  ["Inches/sec²",0.0254],["Kilometers/hour-second",1/3.6],["Kilometers/sec²",1000],
  ["Knots/second",0.514444444444],["Meters/sec²",1],["Miles/hour-minute",0.44704/60],
  ["Miles/hour-second",0.44704]
]},
{ name:"Angle", base:"degrees", units:[
  ["Arcminutes",1/60],["Arcseconds",1/3600],["Degrees",1],["Grads (gons)",0.9],
  ["Mils (NATO)",360/6400],["Octants",45],["Quadrants",90],["Radians",180/Math.PI],
  ["Revolutions (turns)",360],["Sextants",60],["Signs",30]
]},
{ name:"Area", base:"m²", units:[
  ["Acres",4046.8564224],["Ares",100],["Barns",1e-28],["Circular mils",5.067074790975e-10],
  ["Hectares",10000],["Roods",1011.7141056],["Sections",2589988.110336],
  ["Square centimeters",1e-4],["Square chains",404.68564224],["Square feet",0.09290304],
  ["Square inches",0.00064516],["Square kilometers",1e6],["Square meters",1],
  ["Square miles",2589988.110336],["Square millimeters",1e-6],["Square rods (perches)",25.29285264],
  ["Square yards",0.83612736],["Townships",93239571.972096]
]},
{ name:"Density", base:"kg/m³", units:[
  ["Grains/gallon (US)",0.017118061],["Grams/cubic centimeter",1000],["Grams/liter",1],
  ["Grams/milliliter",1000],["Kilograms/cubic meter",1],["Kilograms/liter",1000],
  ["Milligrams/milliliter",1],["Ounces/cubic inch",1729.99404],["Pounds/cubic foot",16.018463374],
  ["Pounds/cubic inch",27679.904710],["Pounds/cubic yard",0.593276421],
  ["Pounds/gallon (UK)",99.776372663],["Pounds/gallon (US)",119.826427317],
  ["Slugs/cubic foot",515.378818393],["Tons (short)/cubic yard",1186.552843]
]},
{ name:"Distance", base:"m", units:[
  ["Angstroms",1e-10],["Astronomical units",149597870700],["Centimeters",0.01],
  ["Chains",20.1168],["Cubits",0.4572],["Decimeters",0.1],["Fathoms",1.8288],
  ["Feet",0.3048],["Furlongs",201.168],["Hands",0.1016],["Inches",0.0254],
  ["Kilometers",1000],["Leagues (statute)",4828.032],["Light-years",9460730472580800],
  ["Meters",1],["Microns (µm)",1e-6],["Miles (statute)",1609.344],["Millimeters",0.001],
  ["Mils (thou)",2.54e-5],["Nanometers",1e-9],["Nautical miles",1852],
  ["Parsecs",3.0856775814913673e16],["Picas",0.0254/6],["Points (typographic)",0.0254/72],
  ["Rods",5.0292],["Yards",0.9144]
]},
{ name:"Flow", base:"m³/s", units:[
  ["Acre-feet/day",1233.48183754752/86400],["Barrels (oil)/day",0.158987294928/86400],
  ["Cubic feet/hour",0.028316846592/3600],["Cubic feet/minute (CFM)",0.028316846592/60],
  ["Cubic feet/second (CFS)",0.028316846592],["Cubic inches/minute",1.6387064e-5/60],
  ["Cubic meters/hour",1/3600],["Cubic meters/minute",1/60],["Cubic meters/second",1],
  ["Gallons (UK)/minute",0.00454609/60],["Gallons (US)/day",0.003785411784/86400],
  ["Gallons (US)/hour",0.003785411784/3600],["Gallons (US)/minute (GPM)",0.003785411784/60],
  ["Gallons (US)/second",0.003785411784],["Liters/hour",0.001/3600],
  ["Liters/minute",0.001/60],["Liters/second",0.001],["Milliliters/minute",1e-6/60]
]},
{ name:"Force", base:"N", units:[
  ["Dynes",1e-5],["Grams-force",0.00980665],["Kilograms-force (kp)",9.80665],
  ["Kilonewtons",1000],["Kips",4448.2216152605],["Millinewtons",0.001],["Newtons",1],
  ["Ounces-force",4.4482216152605/16],["Poundals",0.138254954376],
  ["Pounds-force",4.4482216152605],["Sthenes",1000],["Tons-force (long)",9964.01641818352],
  ["Tons-force (metric)",9806.65],["Tons-force (short)",8896.443230521]
]},
{ name:"Light", base:"lux", units:[
  ["Foot-candles",10.76391041671],["Lumens/sq centimeter",10000],["Lumens/sq foot",10.76391041671],
  ["Lumens/sq meter",1],["Lux",1],["Meter-candles",1],["Milliphots",10],["Nox",0.001],["Phots",10000]
]},
{ name:"Mass", base:"kg", units:[
  ["Atomic mass units",1.66053906892e-27],["Carats",0.0002],["Drams (avdp)",0.0017718451953125],
  ["Grains",6.479891e-5],["Grams",0.001],["Hundredweights (long, UK)",50.80234544],
  ["Hundredweights (short, US)",45.359237],["Kilograms",1],["Micrograms",1e-9],
  ["Milligrams",1e-6],["Ounces (avdp)",0.028349523125],["Ounces (troy)",0.0311034768],
  ["Pennyweights",0.00155517384],["Pounds (avdp)",0.45359237],["Pounds (troy)",0.3732417216],
  ["Quarters (UK)",12.70058636],["Slugs",14.593902937206],["Stones",6.35029318],
  ["Tonnes (metric)",1000],["Tons (long, UK)",1016.0469088],["Tons (short, US)",907.18474]
]},
{ name:"Power", base:"W", units:[
  ["BTU/hour",0.29307107],["BTU/minute",17.5842642],["BTU/second",1055.05585262],
  ["Calories/second",4.1868],["Ergs/second",1e-7],["Foot-pounds/minute",1.3558179483314/60],
  ["Foot-pounds/second",1.3558179483314],["Gigawatts",1e9],["Horsepower (boiler)",9809.5],
  ["Horsepower (electric)",746],["Horsepower (mechanical)",745.69987158227],
  ["Horsepower (metric)",735.49875],["Joules/hour",1/3600],["Joules/second",1],
  ["Kilocalories/hour",1.163],["Kilowatts",1000],["Megawatts",1e6],["Milliwatts",0.001],
  ["Tons of refrigeration",3516.8528420667],["Watts",1]
]},
{ name:"Pressure", base:"Pa", units:[
  ["Atmospheres (standard)",101325],["Atmospheres (technical)",98066.5],["Bars",100000],
  ["Centimeters of mercury (0°C)",1333.22387415],["Centimeters of water (4°C)",98.0665],
  ["Dynes/sq centimeter",0.1],["Feet of water (4°C)",2989.0669],["Gigapascals",1e9],
  ["Hectopascals",100],["Inches of mercury (0°C)",3386.388640341],
  ["Inches of water (4°C)",249.08891],["Kilograms-force/sq centimeter",98066.5],
  ["Kilograms-force/sq meter",9.80665],["Kilopascals",1000],["Megapascals",1e6],
  ["Millibars",100],["Millimeters of mercury (0°C)",133.322387415],
  ["Millimeters of water (4°C)",9.80665],["Pascals",1],["Pounds/sq foot (psf)",47.880258980336],
  ["Pounds/sq inch (psi)",6894.757293168],["Torrs",101325/760]
]},
{ name:"Speed", base:"m/s", units:[
  ["Centimeters/second",0.01],["Feet/hour",0.3048/3600],["Feet/minute",0.00508],
  ["Feet/second",0.3048],["Inches/second",0.0254],["Kilometers/hour",1/3.6],
  ["Kilometers/minute",1000/60],["Kilometers/second",1000],["Knots",1852/3600],
  ["Mach (standard atmosphere)",340.2933],["Meters/hour",1/3600],["Meters/minute",1/60],
  ["Meters/second",1],["Miles/hour",0.44704],["Miles/minute",26.8224],
  ["Miles/second",1609.344],["Speed of light (vacuum)",299792458]
]},
{ name:"Temperature", type:"temp", base:"K", units:[
  ["Celsius (°C)",     v=>v+273.15,                k=>k-273.15],
  ["Delisle (°De)",    v=>373.15 - v*2/3,          k=>(373.15-k)*3/2],
  ["Fahrenheit (°F)",  v=>(v+459.67)*5/9,          k=>k*9/5-459.67],
  ["Kelvin (K)",       v=>v,                       k=>k],
  ["Newton (°N)",      v=>v*100/33+273.15,         k=>(k-273.15)*33/100],
  ["Rankine (°R)",     v=>v*5/9,                   k=>k*9/5],
  ["Réaumur (°Ré)",    v=>v*5/4+273.15,            k=>(k-273.15)*4/5],
  ["Rømer (°Rø)",      v=>(v-7.5)*40/21+273.15,    k=>(k-273.15)*21/40+7.5]
]},
{ name:"Time", base:"s", units:[
  ["Centuries",3155695200],["Days",86400],["Decades",315569520],["Fortnights",1209600],
  ["Hours",3600],["Microseconds",1e-6],["Milliseconds",0.001],["Millennia",31556952000],
  ["Minutes",60],["Months (average)",2629746],["Nanoseconds",1e-9],["Seconds",1],
  ["Shakes",1e-8],["Weeks",604800],["Years (average)",31556952],["Years (365 days)",31536000]
]},
{ name:"Volume", base:"L", units:[
  ["Acre-feet",1233481.83754752],["Barrels (oil, 42 US gal)",158.987294928],
  ["Barrels (US liquid)",119.240471196],["Board feet",2.359737216],["Centiliters",0.01],
  ["Cords",3624.556363776],["Cubic centimeters",0.001],["Cubic decimeters",1],
  ["Cubic feet",28.316846592],["Cubic inches",0.016387064],["Cubic meters",1000],
  ["Cubic millimeters",1e-6],["Cubic yards",764.554857984],["Cups (US)",0.2365882365],
  ["Deciliters",0.1],["Drops (metric)",5e-5],["Fluid ounces (UK)",0.0284130625],
  ["Fluid ounces (US)",0.0295735295625],["Gallons (UK)",4.54609],["Gallons (US liquid)",3.785411784],
  ["Liters",1],["Milliliters",0.001],["Minims (US)",6.1611519921875e-5],
  ["Pints (UK)",0.56826125],["Pints (US liquid)",0.473176473],["Quarts (UK)",1.1365225],
  ["Quarts (US liquid)",0.946352946],["Tablespoons (US)",0.01478676478125],
  ["Teaspoons (US)",0.00492892159375]
]},
{ name:"Volume - Dry", base:"L", units:[
  ["Barrels (US dry)",115.62712358363],["Bushels (UK)",36.36872],["Bushels (US)",35.23907016688],
  ["Cubic feet",28.316846592],["Cubic inches",0.016387064],["Gallons (US dry)",4.40488377086],
  ["Liters",1],["Pecks (UK)",9.09218],["Pecks (US)",8.80976754172],
  ["Pints (US dry)",0.5506104713575],["Quarts (US dry)",1.101220942715]
]},
{ name:"Custom", type:"custom" }
];

/* ---------- state ---------- */
const state = {
  cat: 0,
  sel: CATS.map(() => ({inIdx:0, outIdx:0})),
  lastEdited: "in",
  precision: 10
};

/* ---------- helpers ---------- */
const $ = id => document.getElementById(id);
const els = {
  tabs:$("tabs"), listIn:$("listIn"), listOut:$("listOut"),
  valIn:$("valIn"), valOut:$("valOut"), nameIn:$("nameIn"), nameOut:$("nameOut"),
  status:$("status"), lists:$("lists"), customdef:$("customdef"),
  cNameA:$("cNameA"), cNameB:$("cNameB"), cFactor:$("cFactor")
};

function parseNum(s){
  if (typeof s !== "string") return NaN;
  s = s.trim().replace(/,/g,"").replace(/\u2212/g,"-");
  if (s === "" ) return NaN;
  const v = Number(s);
  return isFinite(v) ? v : NaN;
}

function fmt(x){
  if (!isFinite(x)) return "";
  if (x === 0) return "0";
  const sig = state.precision;
  let s;
  const a = Math.abs(x);
  if (a >= 1e15 || a < 1e-9) {
    s = x.toExponential(sig - 1);
  } else {
    s = x.toPrecision(sig);
  }
  if (s.indexOf("e") !== -1){
    let [m,e] = s.split("e");
    if (m.indexOf(".") !== -1) m = m.replace(/0+$/,"").replace(/\.$/,"");
    s = m + "e" + e;
  } else if (s.indexOf(".") !== -1){
    s = s.replace(/0+$/,"").replace(/\.$/,"");
  }
  return s;
}

function cat(){ return CATS[state.cat]; }
function isCustom(){ return cat().type === "custom"; }
function isTemp(){ return cat().type === "temp"; }

/* ---------- core conversion (works both directions) ---------- */
function convert(value, fromIdx, toIdx){
  const c = cat();
  if (isCustom()){
    const f = parseNum(els.cFactor.value);
    if (!isFinite(f) || f === 0) return NaN;
    return fromIdx === 0 ? value * f : value / f;
  }
  if (isTemp()){
    const from = c.units[fromIdx], to = c.units[toIdx];
    return to[2]( from[1](value) );
  }
  const base = value * c.units[fromIdx][1];
  return base / c.units[toIdx][1];
}

/* ---------- recompute fields ---------- */
function recompute(){
  const s = state.sel[state.cat];
  const src = state.lastEdited === "in" ? els.valIn : els.valOut;
  const dst = state.lastEdited === "in" ? els.valOut : els.valIn;
  const fromIdx = isCustom()
      ? (state.lastEdited === "in" ? 0 : 1)
      : (state.lastEdited === "in" ? s.inIdx : s.outIdx);
  const toIdx = isCustom()
      ? (state.lastEdited === "in" ? 1 : 0)
      : (state.lastEdited === "in" ? s.outIdx : s.inIdx);

  const v = parseNum(src.value);
  if (!isFinite(v)) {
    dst.value = "";
    updateStatus();
    return;
  }
  dst.value = fmt(convert(v, fromIdx, toIdx));
  updateStatus();
}

function unitName(which){
  if (isCustom()) return which === "in" ? (els.cNameA.value || "Unit A") : (els.cNameB.value || "Unit B");
  const s = state.sel[state.cat];
  return cat().units[which === "in" ? s.inIdx : s.outIdx][0];
}

function updateStatus(){
  const inName = unitName("in"), outName = unitName("out");
  if (isTemp()){
    els.status.textContent = inName + "  \u2192  " + outName;
    return;
  }
  const s = state.sel[state.cat];
  const one = isCustom() ? convert(1,0,1) : convert(1, s.inIdx, s.outIdx);
  els.status.innerHTML = "";
  if (isFinite(one)){
    const b = document.createElement("b");
    b.textContent = fmt(one);
    els.status.append("1 " + inName + " = ", b, " " + outName);
  } else {
    els.status.textContent = "Enter a valid factor to convert";
  }
}

/* ---------- listboxes ---------- */
function buildList(el, which){
  el.innerHTML = "";
  if (isCustom()) return;
  const s = state.sel[state.cat];
  cat().units.forEach((u,i)=>{
    const d = document.createElement("div");
    d.className = "item" + ((which==="in"?s.inIdx:s.outIdx)===i ? " sel":"");
    d.textContent = u[0];
    d.setAttribute("role","option");
    d.dataset.idx = i;
    d.addEventListener("click", ()=> selectUnit(which, i));
    el.appendChild(d);
  });
}

function selectUnit(which, idx){
  const s = state.sel[state.cat];
  if (which==="in") s.inIdx = idx; else s.outIdx = idx;
  const el = which==="in" ? els.listIn : els.listOut;
  [...el.children].forEach((c,i)=> c.classList.toggle("sel", i===idx));
  el.children[idx] && el.children[idx].scrollIntoView({block:"nearest"});
  els.nameIn.textContent = unitName("in");
  els.nameOut.textContent = unitName("out");
  recompute();
}

function listKeydown(e, which){
  if (isCustom()) return;
  const s = state.sel[state.cat];
  const cur = which==="in" ? s.inIdx : s.outIdx;
  const max = cat().units.length - 1;
  let next = null;
  if (e.key==="ArrowDown") next = Math.min(cur+1,max);
  else if (e.key==="ArrowUp") next = Math.max(cur-1,0);
  else if (e.key==="Home") next = 0;
  else if (e.key==="End") next = max;
  if (next!==null){ e.preventDefault(); selectUnit(which,next); }
}

/* ---------- tabs ---------- */
const TAB_FR = {
  Acceleration: "Accélération", Angle: "Angle", Area: "Surface", Density: "Densité",
  Distance: "Distance", Flow: "Débit", Force: "Force", Light: "Lumière", Mass: "Masse",
  Power: "Puissance", Pressure: "Pression", Speed: "Vitesse", Temperature: "Température",
  Time: "Temps", Volume: "Volume", "Volume - Dry": "Volume sec", Custom: "Personnalisé"
};
function tabLabel(name){
  if (document.body.classList.contains("lang-fr") && TAB_FR[name]) return TAB_FR[name];
  return name;
}

function buildTabs(){
  els.tabs.innerHTML = "";
  CATS.forEach((c,i)=>{
    const b = document.createElement("button");
    b.className = "tab"; b.textContent = tabLabel(c.name);
    b.setAttribute("role","tab");
    b.setAttribute("aria-selected", i===state.cat ? "true":"false");
    b.addEventListener("click", ()=> setCategory(i));
    els.tabs.appendChild(b);
  });
}

function setCategory(i){
  state.cat = i;
  [...els.tabs.children].forEach((t,j)=> t.setAttribute("aria-selected", j===i ? "true":"false"));
  const custom = isCustom();
  els.lists.style.display = custom ? "none" : "flex";
  els.customdef.style.display = custom ? "block" : "none";
  buildList(els.listIn,"in");
  buildList(els.listOut,"out");
  els.valIn.value = ""; els.valOut.value = "";
  state.lastEdited = "in";
  els.nameIn.textContent = unitName("in");
  els.nameOut.textContent = unitName("out");
  updateStatus();
}

/* ---------- swap (reverse conversion) ---------- */
function swap(){
  if (isCustom()){
    const a = els.cNameA.value; els.cNameA.value = els.cNameB.value; els.cNameB.value = a;
    const f = parseNum(els.cFactor.value);
    if (isFinite(f) && f !== 0) els.cFactor.value = fmt(1/f);
  } else {
    const s = state.sel[state.cat];
    [s.inIdx, s.outIdx] = [s.outIdx, s.inIdx];
    buildList(els.listIn,"in");
    buildList(els.listOut,"out");
    const selIn = els.listIn.children[s.inIdx], selOut = els.listOut.children[s.outIdx];
    selIn && selIn.scrollIntoView({block:"nearest"});
    selOut && selOut.scrollIntoView({block:"nearest"});
  }
  const t = els.valIn.value; els.valIn.value = els.valOut.value; els.valOut.value = t;
  els.nameIn.textContent = unitName("in");
  els.nameOut.textContent = unitName("out");
  recompute();
}

/* ---------- events ---------- */
$("btnSwap").addEventListener("click", swap);
$("btnClear").addEventListener("click", ()=>{
  els.valIn.value=""; els.valOut.value=""; state.lastEdited="in"; updateStatus(); els.valIn.focus();
});
$("precSel").addEventListener("change", e=>{
  state.precision = Number(e.target.value);
  recompute();
});
els.valIn.addEventListener("input", ()=>{ state.lastEdited="in"; recompute(); });
els.valOut.addEventListener("input", ()=>{ state.lastEdited="out"; recompute(); });
[els.cNameA, els.cNameB].forEach(el=> el.addEventListener("input", ()=>{
  els.nameIn.textContent = unitName("in");
  els.nameOut.textContent = unitName("out");
  updateStatus();
}));
els.cFactor.addEventListener("input", recompute);
els.listIn.addEventListener("keydown", e=> listKeydown(e,"in"));
els.listOut.addEventListener("keydown", e=> listKeydown(e,"out"));

function bootConverter(){
  buildTabs();
  const body = document.body;
  let catIdx = 0;
  const catName = body.getAttribute("data-initial-category");
  if (catName){
    const i = CATS.findIndex(c => c.name === catName);
    if (i >= 0) catIdx = i;
  }
  setCategory(catIdx);
  if (isCustom()){
    selectUnit("in",0);
    selectUnit("out",0);
    return;
  }
  const inAttr = body.getAttribute("data-initial-in");
  const outAttr = body.getAttribute("data-initial-out");
  const inIdx = inAttr != null ? parseInt(inAttr, 10) : 0;
  const outIdx = outAttr != null ? parseInt(outAttr, 10) : Math.min(1, cat().units.length - 1);
  selectUnit("in", Number.isFinite(inIdx) ? inIdx : 0);
  selectUnit("out", Number.isFinite(outIdx) ? outIdx : 0);
}

if (document.readyState === "loading"){
  document.addEventListener("DOMContentLoaded", bootConverter);
} else {
  bootConverter();
}
