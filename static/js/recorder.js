console.log("reached here")
var promise = navigator.mediaDevices.getUserMedia({audio: true, video: false});
var recordButton = document.getElementById('record');
var stopButton = document.getElementById('stop');
var playButton = document.getElementById('play');
var saveButton = document.getElementById('save');
var audio = document.getElementById('js-audio');
const timer = document.getElementById('stopwatch');

var hr = 0;
var min = 0;
var sec = 0;
var stoptime = true;

function startTimer(){
    console.log("this was called");
    if(stoptime==true){
        stoptime = false;
        timerCycle();
    }
}

function stopTimer(){
    if(stoptime == false){
        stoptime = true;
    }
}

function timerCycle() {
    if (stoptime == false) {
    sec = parseInt(sec);
    min = parseInt(min);
    hr = parseInt(hr);
    sec = sec + 1;
    if (sec == 60) {
      min = min + 1;
      sec = 0;
    }
    if (min == 60) {
      hr = hr + 1;
      min = 0;
      sec = 0;
    }
    if (sec < 10 || sec == 0) {
      sec = '0' + sec;
    }
    if (min < 10 || min == 0) {
      min = '0' + min;
    }
    if (hr < 10 || hr == 0) {
      hr = '0' + hr;
    }
    timer.innerHTML = hr + ':' + min + ':' + sec;
    setTimeout("timerCycle()", 1000);
    
  }
}

promise.then(function(stream){
    var recorder = new MediaRecorder(stream);
    chunks = [];

    recorder.ondataavailable=function(e){
        chunks.push(e.data);
    }

    recordButton.addEventListener("click",function(){
        console.log("record button pressed");
        // recordButton.setAttribute("disabled");
        // stopButton.removeAttribute("disabled");
        // playButton.setAttribute("disabled");
        recordButton.disabled = true;
        stopButton.disabled = false;
        playButton.disabled = true;
        startTimer();
        recorder.start();
    });

    stopButton.addEventListener("click",function(){
        console.log("stop button pressed");
        // stopButton.setAttribute("disabled");
        // recordButton.removeAttribute("disabled");
        // playButton.removeAttribute("disabled");
        stopButton.disabled = true;
        recordButton.disabled = false;
        playButton.disabled = false;
        recorder.stop();
        stopTimer();
    });

    playButton.addEventListener("click",function(){
        console.log(this.chunks);
        recordButton.disabled = false;
        stopButton.disabled = false;
        playButton.disabled = false;
        var blob = new Blob(chunks);
        const audio = new Audio(URL.createObjectURL(blob));
        audio.play();
    });

    saveButton.addEventListener("click",function(){
        var title = document.getElementById('title').value;
        document.getElementById('title').value = "";
        console.log(title);
        var blob = new Blob(chunks,{ 'type' : 'audio/wav'});
        var data = new FormData();
        data.append('audio_file',blob,title+'.wav');
        data.append("title",title);
        var xhttp = new XMLHttpRequest();
        xhttp.open("POST",window.location.href,true);
        xhttp.send(data);
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                window.location = "http://127.0.0.1:8000/dashboard/"     
             }
        };
    });

});

promise.catch(function(err) { console.log(err.name); });