  var wsAUDIO = document.getElementById("audioWSURL").value.toString();
  var wsVIDEO = document.getElementById("videoWSURL").value.toString();
  var btnMedia = document.getElementById("btnMedia");
  var btnRecVideo = document.getElementById("btnRecVideo");
  var btnRecAudio = document.getElementById("btnRecAudio");
  var localVideo = document.getElementById("localVideo");
  var localAudioRec;
  var localVideoRec;
  var localStream;
  var audioContext = new AudioContext;
  var Success = function (stream) {
    console.log("got the local stream");
    localStream = stream;
    attachMediaStream(localVideo, stream);
  };
  var Failure = function (error) {
    alert("Could not get media");
  };

  btnRecVideo.onclick = function () {
    if (localStream == 'undefined') {
      alert("please start stream first");
    } else {
      localVideoRec = new WSVideoRecorder(localStream, wsVIDEO, 'video-protocol');
      setTimeout(function () { localVideoRec.record(); }, 500);
    }
  }

  btnRecAudio.onclick = function () {
    if (localStream == 'undefined') {
      alert("please start stream first");
    } else {
      var input = audioContext.createMediastreamSource(localStream);
      localAudioRec = new WSAudioRecorder(input, wsAUDIO, 'audio-protocol');
      setTimeout(function () { localAudioRec.record(); }, 500);
    }
  }

  btnMedia.onclick = function () {
    getUserMedia({"audio": true, "video": true}, Success, Failure);
  }
