console.log("reached here")
var promise = navigator.mediaDevices.getUserMedia({audio: true, video: false});
var recordButton = document.getElementById('record');
var stopButton = document.getElementById('stop');
var playButton = document.getElementById('play');
var saveButton = document.getElementById('save');
var audio = document.getElementById('js-audio');

promise.then(function(stream){
    var recorder = new MediaRecorder(stream);
    chunks = [];

    recorder.ondataavailable=function(e){
        chunks.push(e.data);
    }

    recordButton.addEventListener("click",function(){
        console.log("record button pressed")
        recordButton.disable = true;
        stopButton.disable = false;
        playButton.disable = true;
        recorder.start();
    });

    stopButton.addEventListener("click",function(){
        console.log("stop button pressed")
        stopButton.disable = true;
        recordButton.disable = false;
        playButton.disable = false;
        recorder.stop();
    });

    playButton.addEventListener("click",function(){
        console.log(this.chunks);
        recordButton.disable = true;
        stopButton.disable = true;
        playButton.disable = true;
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