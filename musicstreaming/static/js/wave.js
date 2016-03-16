'use strict';

// Create an instance
var wavesurfer = Object.create(WaveSurfer);
var wave1 = Object.create(WaveSurfer);
// Init & load audio file
document.addEventListener('DOMContentLoaded', function () {
    var options = {
        container     : document.querySelector('#waveform'),
        waveColor     : 'blue',
        progressColor : 'orange',
        cursorColor   : 'navy'
    };

    if (location.search.match('scroll')) {
        options.minPxPerSec = 100;
        options.scrollParent = true;
    }

    // Init
    wavesurfer.init(options);
    wave1.init(options);
    // Load audio from URL
    wavesurfer.load('mp3.mp3');
    wave1.load('mp31.mp3');

    // Regions
    if (wavesurfer.enableDragSelection) {
        wavesurfer.enableDragSelection({
            color: 'rgba(0, 255, 0, 0.1)'
        });
    }
    if (wave1.enableDragSelection) {
     	wave1.enableDragSelection({
	color: 'rgba(0, 255, 0, 0.1)'
        });
    } 
});

// Play at once when ready
// Won't work on iOS until you touch the page
wavesurfer.on('ready', function () {
	wavesurfer.play();
});	
wave1.on('ready', function () {
 	wave1.play();
});

// Report errors
wavesurfer.on('error', function (err) {
    console.error(err);
});

wave1.on('error', function (err){
	console.error(err);
});

// Do something when the clip is over
wavesurfer.on('finish', function () {
    console.log('Finished playing');
});

wave1.on('finish', function(){
    console.log('Finished playing');
});

