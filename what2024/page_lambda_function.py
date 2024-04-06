import json

def lambda_handler(event, context):
    response = {
        "statusCode": 200,
        "statusDescription": "200 OK",
        "Access-Control-Allow-Origin" : "*",
        "isBase64Encoded": False,
        "headers": {
            "Content-Type": "text/html; charset=utf-8"
        }
    }

    response['body'] = """
<html>
    <head>
            <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-HZCGBT19QW"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'G-HZCGBT19QW');
        </script>
            <title>내 2024 운세는?!</title>
            <meta charset="utf-8" name="viewport" content="width=device-width, height=device-height, minimum-scale=1.0, maximum-scale=1.0, initial-scale=1.0">
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    </head>

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <div id="overlay">
    <div id="text">잠시만 기다려주세요!</div>
    </div>
    <div class="ano_novo">
    <div class="feliz">Happy new year</div>
    <span>202</span>
    <span class="seis">3</span>
    <span class="sete">4</span>
    <div class="balao"></div>
    </div>
    <div class="fogos">
    <div class="f1">
        <span><i></i></span>
        <span><i></i></span>
        <span><i></i></span>
    </div>
    <div class="f2">
        <span><i></i></span>
        <span><i></i></span>
        <span><i></i></span>
    </div>
    <div class="f3">
        <span><i></i></span>
        <span><i></i></span>
        <span><i></i></span>
    </div>
    <div class="f4">
        <span><i></i></span>
        <span><i></i></span>
        <span><i></i></span>
    </div>
    </div>
    <div class="fortune-form">
    <h2>나의 2024년 운세는?!</h2>
    <form id="fortuneForm">
        <label for="name">이름을 입력해주세요.</label><br>
        <input type="text" id="nameInput" name="nameInput" maxlength="3"><br>
        <input type="submit" value="확인">
        <label id="credit" for="credit">만든이: 이현제 <a href="https://github.com/leehjhjhj" target="_blank"><i class="fab fa-github"></i> Github</a></label>
    </form>
        <div id="resultContainer">
    <p id="fortune-result"></p>
    <div id="buttonContainer">
        <button id="copyResult" onclick="copyToClipboard()">운세복사</button>
        <button id="copyButton" onclick="copyToClipboard()">공유하기</button>
    </div>
    </div>
    </div>

</html>
        
<script type="text/javascript">
    function copyToClipboard() {
    const el = document.createElement('textarea');
    el.value = 'http://what2024.kro.kr';
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);
    alert('널리널리 퍼뜨려주세요!');
    };

    document.getElementById('fortuneForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const name = document.getElementById('nameInput').value;

    // Submit 버튼을 누르면 overlay를 보여줍니다.
    document.getElementById('overlay').style.display = "block";

    fetch('https://zqzi0n38.execute-api.ap-northeast-2.amazonaws.com/default', {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: name })
    })
    .then(response => response.json())
    .then(data => {
        // 데이터를 받은 후 overlay를 숨깁니다.
        document.getElementById('overlay').style.display = "none";
        console.log(data)
        if (data.body === undefined) {
        document.getElementById('fortune-result').textContent = '잠시 후에 다시 시도해주세요';
        } else {
        document.getElementById('fortune-result').textContent = `${data.body}`;
        // 복사 버튼을 보여줍니다.
        document.getElementById('copyButton').style.display = "block";
        document.getElementById('copyResult').style.display = "block";
        }
        document.getElementById('fortune-result').style.display = 'block';
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('overlay').style.display = "none";
    });
    });
    document.getElementById('copyResult').addEventListener('click', function() {
        var text = document.getElementById('fortune-result').innerText;
        var tempElem = document.createElement('textarea');
        tempElem.value = text;
        document.body.appendChild(tempElem);

        tempElem.select();
        document.execCommand('copy');
        document.body.removeChild(tempElem);

        alert('복사되었습니다!');
    });
</script>
<style>
    @import url('https://fonts.googleapis.com/css?family=Montserrat:700|Pacifico');

    *, *:after, *:before{
    box-sizing:border-box;
    margin:0;
    padding:0;
    -webkit-transition: all 100ms ease-in;
    transition: all 100ms ease-in;
    }
    html{
        background: #222048;
    }
    .feliz{
    width: 100%;
    font-family: 'Pacifico', cursive;
    font-size: 60px;
    font-weight: 700;
    color: #f48fb1;
    text-align: center;
    position: absolute;
    top: 50%;
    opacity: 0;
    animation: vem_feliz 2s ease-in-out 7s forwards;
    z-index: 2;
    left: 6px;
    }
    .ano_novo{
    position: relative;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    padding: 200px 100px 0px 0px;
    z-index: 1;
    text-align: center;
    align-items: center;
    }
    .ano_novo>span{
    font-family: 'Montserrat', sans-serif;
    font-size: 160px;
    font-weight: 700;
    color: #7a8fe8;
    }
    span.seis{
    position: absolute;
    top: 50%;
    right: 50%;
    margin-right: -200px;
    animation: vai_2016 5s ease-in-out 5s forwards;
    }
    span.sete{
    position: absolute;
    right: 0%;
    margin-right: -200px;
    animation: vem_2017 6s ease-in-out forwards;
    }
    span.sete:before{
    content: '';
    width: 0px;
    height: 6px;
    display: block;
    border-radius: 3px;
    background: #7a8fe8;
    transform: rotate(0deg);
    transform-origin: left top;
    position: absolute;
    top: 55px;
    left: 10px;
    z-index: -1;
    animation: entrega_balao 1s ease-in-out 4s;
    }
    .balao{
    width: 100px;
    height: 100px;
    display: block;
    background: #e8d57a;
    border-radius: 50%;
    position: absolute;
    top: 50%;
    margin-top: -165px;
    right: 0%;
    margin-right: -200px;
    animation: vem_e_vai_balao 10s ease-in-out forwards;
    }
    .balao:before{
    content: '';
    width: 0;
    height: 0;
    border-style: solid;
    border-width: 0 10px 20px 10px;
    border-color: transparent transparent #b19b32 transparent;
    position: absolute;
    left: 50%;
    margin-left: -10px;
    bottom: -10px;
    z-index: -1;
    }
    .balao:after{
    content: '';
    width: 4px;
    height: 100px;
    display: block;
    background: #fff;
    border-radius: 0px 0px 3px 3px;
    position: absolute;
    left: 50%;
    margin-left: -2px;
    bottom: -110px;
    }
    .fogos{
    width: 100%;
    height: 100%;
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    overflow: hidden;
    }
    .fogos>div{
    border: 2px solid #fff;
    position: absolute;
    opacity: 0;
    animation: solta_fogos 1.5s ease-in-out 8s forwards;
    }
    .fogos>div.f1{
    left: 20%;
    top: 40%;
    }
    .fogos>div.f2{
    left: 15%;
    top: 70%;
    }
    .fogos>div.f3{
    right: 20%;
    top: 40%;
    }
    .fogos>div.f4{
    right: 15%;
    top: 70%;
    }
    .fogos>div span{
    width: 6px;
    height: 6px;
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    opacity: 0;
    animation: estoura_fogos 0.5s ease-in-out 9s forwards;
    }
    .fogos>div span:nth-child(1){
    transform: rotate(0deg);
    }
    .fogos>div span:nth-child(2){
    transform: rotate(120deg);
    }
    .fogos>div span:nth-child(3){
    transform: rotate(240deg);
    }
    .fogos>div span:before{
    content: '';
    width: 2px;
    height: 50px;
    display: block;
    background: #f5cc06;
    position: absolute;
    top: -60px;
    left: 2px;
    }
    .fogos>div span:after{
    content: '';
    width: 2px;
    height: 50px;
    display: block;
    background: #f5cc06;
    position: absolute;
    bottom: -60px;
    left: 2px;
    }
    .fogos>div span i:before{
    content: '';
    width: 3px;
    height: 3px;
    display: block;
    border-radius: 50%;
    background: #fff;
    position: absolute;
    top: -15px;
    left: 10px;
    }
    .fogos>div span i:after{
    content: '';
    width: 3px;
    height: 3px;
    display: block;
    border-radius: 50%;
    background: #fff;
    position: absolute;
    top: -15px;
    right: 10px;
    }
    a.author{
    font-size: 12px;
    text-decoration: none;
    color: #f47c7c;
    position: fixed;
    bottom: 10px;
    right: 10px;
    }

    @keyframes vem_2017 {
    0% {
        right: 0%;
    }
    66.6666% {
        right: 50%;
        margin-right: -300px;
    }
    90% {
        right: 50%;
        margin-right: -300px;
    }
    100% {
        right: 50%;
    }
    }
    @keyframes vem_e_vai_balao {
    0% {
        right: 0%;
    }
    40% {
        right: 50%;
        margin-right: -300px;
    }
    50% {
        right: 50%;
        margin-right: -200px;
        top: 50%;
    }
    100% {
        top: -100%;
        right: 50%;
    }
    }
    @keyframes entrega_balao {
    0% {
        transform: rotate(-30deg);
        width: 40px;
    }
    100% {
        transform: rotate(-150deg);
        width: 70px;
    }
    }
    @keyframes vai_2016 {
    0% {
        top: 50%;
    }
    100% {
        top: -100%;
    }
    }
    @keyframes vem_feliz {
    0% {
        margin-top: 0px;
        opacity: 0;
    }
    100% {
        margin-top: -200px;;
        opacity: 1;
    }
    }
    @keyframes solta_fogos {
    0% {
        margin-top: 100%;
        opacity: 0;
        width: 2px;
        height: 30px;
        display: block;
        border-radius: 50%;
    }
    75% {
        margin-top: 0%;
        opacity: 1;
        width: 2px;
        height: 30px;
        display: block;
        border-radius: 50%;
    }
    80%{
        margin-top: 0px;
        margin-left: 0px;
        opacity: 1;
        width: 10px;
        height: 10px;
        display: block;
        border-radius: 50%;
        transform: scale(0.2);
    }
    100%{
        opacity: 1;
        width: 10px;
        height: 10px;
        display: block;
        border-radius: 50%;
        transform: scale(1);
    }
    }
    @keyframes estoura_fogos {
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
    }

    .fortune-form {
        width: 600px;
        margin: 0 auto;
        background: #222048;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 0 10px rgba(0,0,0,0.3);
        animation: vem_feliz 15s ease-in-out forwards;
        position: relative;
        top: 50px;  /* 이 값을 조정하여 폼의 위치를 조절하세요. */
        z-index: 0;
        width: 40%;
        margin-top: 20%;
        margin-bottom: 30%;
    }

    .fortune-form h2 {
        font-family: 'Montserrat', sans-serif;
        font-size: 32px;
        font-weight: 700;
        color: #7a8fe8;
        text-align: center;
        margin-bottom: 20px;
    }

    .fortune-form form {
        display: flex;
        flex-direction: column;
    }

    .fortune-form label {
        font-family: 'Montserrat', sans-serif;
        font-size: 24px;
        color: #f48fb1;
        margin-bottom: 10px;
    }

    .fortune-form input[type="text"] {
        padding: 10px;
        margin-bottom: 20px;
        border: none;
        border-bottom: 2px solid #000; /* 밑줄 추가 */
        background: transparent; /* 배경 투명하게 */
        outline: none; /* 아웃라인 제거 */
        text-align: center; /* 텍스트를 가운데로 정렬 */
        font-size: 30px;
        color: white;
    }
    .fortune-form input[type="text"]:focus {
        border-bottom: 2px solid #7a8fe8; /* 포커스 상태일 때 밑줄 색상 변경 */
    }
    .fortune-form input[type="submit"] {
        padding: 10px;
        background: #7a8fe8;
        border: none;
        border-radius: 5px;
        color: white;
        cursor: pointer;
        transition: background 0.3s ease;
        font-size: 24px;
    }

    .fortune-form input[type="submit"]:hover {
        background: #f48fb1;
    }
    #fortune-result {
        display: none;
        width: 80%;
        margin: 20px auto;
        padding: 20px;
        background: #7a8fe8;
        color: #fff;
        border-radius: 15px;
        box-shadow: 0 0 10px rgba(0,0,0,0.3);
        font-family: 'Montserrat', sans-serif;
        font-size: 24px;
        text-align: center;
        animation: vem_feliz 2s ease-in-out forwards;
    }
    @media (max-width: 800px) {
        .fortune-form {
            width: 90%;
            margin-top: 10%;
        }
    }
    #fortuneForm label {
        display: block;
        text-align: center;
    }
    #credit {
        font-family: 'Montserrat', sans-serif;
        font-size: 20px;
        color: white;
        margin-bottom: 10px;
        margin-top: 20px;
    }
    #overlay {
    position: fixed;
    display: none;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0,0,0,0.5);
    z-index: 2;
    cursor: pointer;
    }

    #text{
    position: absolute;
    top: 50%;
    left: 50%;
    font-size: 20px;
    color: white;
    transform: translate(-50%,-50%);
    -ms-transform: translate(-50%,-50%);
    font-family: 'Montserrat', sans-serif;
    }
    #resultContainer {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;  /* 수직으로 배치하게 변경 */
        margin-top: 20px;
    }

    /* 복사 버튼 */
    #copyButton {
        display: none;
        padding: 10px;
        background: #7a8fe8;
        border: none;
        border-radius: 5px;
        color: white;
        cursor: pointer;
        transition: background 0.3s ease;
        font-size: 18px;
        margin: 10px 5px;
    }

    #copyButton:hover {
        background: #f48fb1;
    }

    #copyResult {
        display: none;
        padding: 10px;
        background: #f48fb1;
        border: none;
        border-radius: 5px;
        color: white;
        cursor: pointer;
        transition: background 0.3s ease;
        font-size: 18px;
        margin: 10px 5px;
    }

    #copyResult:hover {
        background: #7a8fe8;
    }
    #buttonContainer {
        display: flex;
        width: 100%;
        justify-content: center;
    }
</style>
        """
        
    return response