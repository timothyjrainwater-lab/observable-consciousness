#!/usr/bin/env python3
"""Quick voice recorder — saves a WAV clip from the default mic.

Usage:
    python D:/anvil_research/record_voice.py

Press ENTER to start recording, ENTER again to stop.
Saves to D:/anvil_research/voice_sample.wav

Target: 10 seconds, warm narration voice, quiet room.
"""

import sys
import wave
import numpy as np
import sounddevice as sd

SAMPLE_RATE = 44100  # High quality capture; Chatterbox downsamples internally
CHANNELS = 1
DTYPE = "int16"
OUTPUT = "D:/anvil_research/voice_sample.wav"

PASSAGE = """
  Please call Stella. Ask her to bring these things
  with her from the store: six spoons of fresh snow
  peas, five thick slabs of blue cheese, and maybe
  a snack for her brother Bob. We also need a small
  plastic snake and a big toy frog for the kids.
"""

chunks = []
recording = False

def callback(indata, frames, time_info, status):
    if status:
        print(f"  Audio status: {status}", file=sys.stderr)
    if recording:
        chunks.append(indata.copy())

def main():
    global recording

    print("=" * 50)
    print("  VOICE RECORDER — Chatterbox Reference Clip")
    print("=" * 50)
    print()
    print("  TARGET: ~10 seconds, warm narration voice")
    print("  FORMAT: WAV, 44.1kHz, mono, no post-processing")
    print()
    print("  Read this passage naturally, like you're")
    print("  telling someone a story:")
    print()
    print("  +-----------------------------------------+")
    for line in PASSAGE.strip().split("\n"):
        print(f"  |{line.ljust(41)}|")
    print("  +-----------------------------------------+")
    print()
    print("  TIPS:")
    print("  - Quiet room, no echo")
    print("  - 6-12 inches from mic")
    print("  - Storytelling voice, not reading voice")
    print("  - Don't rush. Let the words breathe.")
    print()

    input("  >> Press ENTER when ready to record... ")
    print()

    recording = True
    stream = sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype=DTYPE,
        callback=callback,
        blocksize=1024,
    )
    stream.start()
    print("  [REC] Recording... Read the passage above.")
    print("  [REC] Press ENTER when done.")

    input()

    recording = False
    stream.stop()
    stream.close()

    if not chunks:
        print("  No audio captured.")
        return

    audio = np.concatenate(chunks, axis=0)
    duration = len(audio) / SAMPLE_RATE

    with wave.open(OUTPUT, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(audio.tobytes())

    print(f"\n  Saved: {OUTPUT}")
    print(f"  Duration: {duration:.1f}s")
    print(f"  Sample rate: {SAMPLE_RATE}Hz")
    print(f"  Size: {len(audio) * 2 / 1024:.0f} KB")

    if duration < 8:
        print("\n  WARNING: Short clip -- Chatterbox works best with ~10s.")
        print("  Consider re-recording if under 8 seconds.")
    elif duration > 15:
        print("\n  WARNING: Long clip -- Chatterbox only uses the first 10s.")
        print("  The extra audio will be trimmed automatically.")
    else:
        print("\n  OK: Duration looks good for Chatterbox.")

if __name__ == "__main__":
    main()
