# Simple Speaker Recognizer

It is a simple speaker recognition program with MFCC as feature quantity


## Quick Install


```python
$ pip install -r reqirements.txt
```


## Generate speech audio data

```python
$ python create_voice.py
```


## Generate features JSON

```python
$ python create_features.py
```

## Testing Recognizer (Score calculation)
```python
$ python recognizer.py
```

## Classification with original audio file
```python
$ python recognizer.py my_say.wav
```

## Realtime Classfication(Use a microphone)
```python
$ python realtime.py
```