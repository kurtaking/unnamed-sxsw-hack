function createWave(wName, wFile){
  // Create an instance
  var [mName] = Object.create(WaveSurfer);
  // Init & load audio file
  document.addEventListener('DOMContentLoaded', function () {
      var options = {
          container     : document.querySelector('#waveform'),
          waveColor     : '#0c2340',
          progressColor : '#f15122',
          cursorColor   : 'navy'
      };

      if (location.search.match('scroll')) {
          options.minPxPerSec = 100;
          options.scrollParent = true;
      };

      // Init
      [mName].init(options);
      // Load audio from URL
      [mName].load([wFile]);

  // Won't work on iOS until you touch the page
  [mName].on('ready', function () {wavesurfer.play(){ });

  // Report errors
  [mName].on('error', function (err) {console.error(err);});


  // Do something when the clip is over
  [mName].on('finish', function () {console.log('Finished playing');});

};
