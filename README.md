# Simple Speaker Recognizer

It is a simple speaker recognition program with MFCC as feature quantity


## Quick Install


```sh
$ pip install -r reqirements.txt
```


## Generate speech audio data

```sh
$ python create_voice.py
```


## Generate features JSON

```sh
$ python create_features.py
```

## Testing Recognizer (Score calculation)
```sh
$ python recognizer.py
```

## Classification with original audio file
```sh
$ python recognizer.py my_say.wav
```

## Realtime Classfication(Use a microphone)
```sh
$ python realtime.py
```