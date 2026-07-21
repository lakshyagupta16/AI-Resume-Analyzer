import streamlit.components.v1 as components

def circular_score(score):

    if score >= 80:
        color = "#22c55e"
        status = "EXCELLENT"
    elif score >= 60:
        color = "#3b82f6"
        status = "GOOD"
    elif score >= 40:
        color = "#f59e0b"
        status = "AVERAGE"
    else:
        color = "#ef4444"
        status = "POOR"

    html = f"""
<!DOCTYPE html>
<html>

<head>

<style>

body {{
    margin:0;
    background:transparent;
    font-family:Arial,sans-serif;
}}

.card{{
    width:340px;
    height:340px;
    margin:auto;
    display:flex;
    justify-content:center;
    align-items:center;
}}

.circle{{
    position:relative;
    width:260px;
    height:260px;
    border-radius:50%;
    display:flex;
    justify-content:center;
    align-items:center;
}}

.circle svg{{
    position:absolute;
    width:260px;
    height:260px;
    transform:rotate(-90deg);
}}

circle{{
    fill:none;
    stroke-width:12;
}}

.bg{{
    stroke:#263248;
}}

.progress{{
    stroke:{color};
    stroke-linecap:round;
    stroke-dasharray:754;
    stroke-dashoffset:754;
    filter:drop-shadow(0 0 10px {color});
}}

.content{{
    text-align:center;
    z-index:10;
}}

.score{{
    font-size:58px;
    color:white;
    font-weight:bold;
}}

.status{{
    color:{color};
    font-size:18px;
    letter-spacing:2px;
}}

.label{{
    color:#94a3b8;
    margin-top:8px;
}}

.rotating{{
    position:absolute;
    width:300px;
    height:300px;
    border:2px dashed rgba(59,130,246,.4);
    border-radius:50%;
    animation:spin 18s linear infinite;
}}

.glow{{
    position:absolute;
    width:220px;
    height:220px;
    border-radius:50%;
    background:{color};
    filter:blur(70px);
    opacity:.15;
}}

@keyframes spin{{
    from{{transform:rotate(0deg);}}
    to{{transform:rotate(360deg);}}
}}

</style>

</head>

<body>

<div class="card">

<div class="rotating"></div>

<div class="glow"></div>

<div class="circle">

<svg>

<circle
class="bg"
cx="130"
cy="130"
r="120">
</circle>

<circle
id="progress"
class="progress"
cx="130"
cy="130"
r="120">
</circle>

</svg>

<div class="content">

<div class="score" id="score">0%</div>

<div class="status">{status}</div>

<div class="label">
ATS SCORE
</div>

</div>

</div>

</div>

<script>

let score={score};

let circle=document.getElementById("progress");

let text=document.getElementById("score");

let radius=120;

let circumference=2*Math.PI*radius;

circle.style.strokeDasharray=circumference;

let current=0;

let animation=setInterval(()=>{{

if(current>=score)
{{
clearInterval(animation);
}}

text.innerHTML=current+"%";

let offset=circumference-(current/100)*circumference;

circle.style.strokeDashoffset=offset;

current++;

}},20);

</script>

</body>

</html>
"""

    components.html(html, height=360)