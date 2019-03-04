"""
<h1>Outline of steps for attempting NLP with audio instead of text.</h1>

<h2>The thought process behind the project:</h2>

    - Tone and pitch changes inter-sentence determine importance in words far better than end markings (?, !, ., etc).

    - If the goal of NLP is to model the language as a whole, then we are inadvertently modeling the thoughts and state
        of mind behind the words. If spoken language is derived from thought, then written language would be derived
        from spoken language. Using the more rich data in audible language may help the model may help understand the
        thought.

    - TL;DR: Spoken language might be a closer example to modeling meaning behind words than text.


<h2>Possible downsides:</h2>

    - Without lemitizing and vectorizing spoken words, the model could have a much harder time understanding waveforms
        instead of vectors.

    - The processing power required.


<h2>Breaking down the process:</h2>

<h3>- (Preprocessing)</h3> Text embedding to audio challenges (Goal: transformers are fed full sentences, attempt to do the same
    with audio)

    * Train a network to detect and label sentence starts and endings of conversational audio.

        - Use similar architecture to object detection but instead with 1dimconvo layers.
                Output: [ [start point, endpoint, confidence], ... ]

        - This might have to be supervised. Could be problematic to collect training data...

    * Possibly cluster similar patterns of audio to simply data, similar to word to vec but based on some
        a form of the phonetic alphabet?

        - Big maybe.. this could result in the loss of key context and tonal data which is the whole point of going with
            audio

<h3>- (Main model)</h3> Base on proven transformer architecture (specifically GPT/GPT-2)

    * Training (unsupervised)

        - Feed model similar to how entire sentences are fed to GPT, an array of the waveform (of varying length) and
            an array the positional data for that waveform

        - The answer is next N seconds of the waveform (also varying)

<h3>- Data</h3>

    GOAL: Diverse and large dataset, mainly containing conversational data. Both formal and informal.

    * Needs to contain wide varieties of emotion, emphasis, purpose (persuasive, questioning, debating, casual)

    * Diverse amounts of accents, dialect and possible lanugages.

    * Possible sources:

        - Podcasts
        - youtube vlogs
        - infomational videos
        - news and talkshows
        - college lectures
        - audio books.


<h2>The Plan:</h2>

 1. Train preprocessing model

 2. Use model further clean dataset (removing intros, music, non-conversational audio)

 2. Cultivate dataset

 3. Train progressively larger models using the outlined training process.

"""