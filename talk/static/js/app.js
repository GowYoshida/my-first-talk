// app.js

var btn = document.getElementById('btn');
var content = document.getElementById('content');

//音声認識APIの使用
var speech = new webkitSpeechRecognition();
//speech.continuous = true;

//言語を日本語に設定
speech.lang = "ja";

btn.addEventListener( 'click' , function() {
    // 音声認識をスタート
    speech.start();
} );

speech.addEventListener( 'result' , function( event ) {
    // データの入力ができた場合
    //var length = event.results.length;
    //if (length > 0) {
        //text = event.results[length-1][0].transcript;

    var text = event.results[0][0].transcript;

    // 認識された「言葉(text)」を、表示用のdivタグに代入する
    content.textContent = text;

    // 音声認識で取得した情報を、コンソール画面に表示
    //console.log( e );

    // オウム返し
    var synthes = new SpeechSynthesisUtterance( text );

    synthes.lang = "ja-JP";
    // 速度 0.1-10 初期値:1 (倍速なら2, 半分の倍速なら0.5)
    synthes.rate = 1.1
    // 高さ 0-2 初期値:1
    synthes.pitch = 1.1
    // 音量 0-1 初期値:1
    synthes.volume = 1.0

    //synthes.voice = speechSynthesis
      //.getVoices()
      //.filter(voice => voice.name === voiceSelect.value)[0]

    speechSynthesis.speak( synthes );


} );
