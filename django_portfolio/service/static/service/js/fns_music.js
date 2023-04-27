var music = new AudioContext(),
    AudioSource = music.createMediaElementSource(document.getElementById('music'));
    filter = music.createBiquadFilter();

audioSource.connect(filter);
filter.connect(context.destination);
