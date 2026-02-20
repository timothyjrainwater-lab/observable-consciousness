"""
Record system audio (TTS output) via WASAPI loopback.
Captures whatever is playing through your default speakers/headphones.

Usage:
    python D:/anvil_research/record_tts.py
    python D:/anvil_research/record_tts.py --duration 60
    python D:/anvil_research/record_tts.py --output my_recording.wav

Press Ctrl+C to stop recording early.

Uses WASAPI loopback on the default output device — captures Chrome TTS
regardless of whether audio routes through Realtek, Razer, or Voicemeeter.
"""

import sounddevice as sd
import numpy as np
import wave
import sys
import time
import argparse
import os

SAMPLE_RATE = 48000
CHANNELS = 2
DTYPE = "int16"
DEFAULT_OUTPUT = "D:/anvil_research/tts_capture.wav"


def find_default_wasapi_output():
    """Find the default output device on WASAPI for loopback capture."""
    devices = sd.query_devices()
    apis = sd.query_hostapis()

    # Find WASAPI host API index
    wasapi_idx = None
    for i, api in enumerate(apis):
        if "wasapi" in api["name"].lower():
            wasapi_idx = i
            break

    if wasapi_idx is None:
        return None, None, None, None

    # Get the default output device name from the system default
    default_out = sd.default.device[1]
    if default_out is not None and default_out >= 0:
        default_name = devices[default_out]["name"].lower()
    else:
        default_name = None

    # Priority 1: WASAPI version of the system default output device
    if default_name:
        for i, d in enumerate(devices):
            if d["hostapi"] == wasapi_idx and d["max_output_channels"] > 0:
                if default_name[:20] in d["name"].lower():
                    return i, d["name"], d["max_output_channels"], d["default_samplerate"]

    # Priority 2: Any WASAPI output device with "razer" or "headphone" or "speaker"
    for keyword in ["razer", "headphone", "speaker"]:
        for i, d in enumerate(devices):
            if d["hostapi"] == wasapi_idx and d["max_output_channels"] > 0:
                if keyword in d["name"].lower():
                    return i, d["name"], d["max_output_channels"], d["default_samplerate"]

    # Priority 3: WASAPI default output device from the API
    api_info = apis[wasapi_idx]
    default_dev = api_info.get("default_output_device", -1)
    if default_dev >= 0:
        d = devices[default_dev]
        return default_dev, d["name"], d["max_output_channels"], d["default_samplerate"]

    return None, None, None, None


def record(output_path, max_duration):
    dev_index, dev_name, max_ch, dev_rate = find_default_wasapi_output()
    if dev_index is None:
        print("ERROR: Cannot find a WASAPI output device for loopback.")
        print("")
        print("Available output devices:")
        devices = sd.query_devices()
        for i, d in enumerate(devices):
            if d["max_output_channels"] > 0:
                print(f"  {i}: {d['name']} ({d['max_output_channels']}ch, api:{d['hostapi']})")
        sys.exit(1)

    channels = min(CHANNELS, max_ch)
    sample_rate = int(dev_rate) if dev_rate else SAMPLE_RATE

    print(f"WASAPI Loopback from: {dev_name} (device {dev_index})")
    print(f"Output: {output_path}")
    print(f"Rate: {sample_rate}Hz, Channels: {channels}")
    if max_duration:
        print(f"Duration: {max_duration}s")
    else:
        print("Duration: until Ctrl+C")
    print("")
    print("Recording NOW -- play Aegis TTS in Chrome")
    print("Press Ctrl+C to stop")
    print("")

    frames = []
    start_time = time.time()

    def callback(indata, frame_count, time_info, status):
        if status:
            pass  # ignore overflows silently
        frames.append(indata.copy())

    try:
        wasapi_loopback = sd.WasapiSettings(exclusive=False)
        with sd.InputStream(
            device=dev_index,
            samplerate=sample_rate,
            channels=channels,
            dtype=DTYPE,
            callback=callback,
            blocksize=4096,
            extra_settings=wasapi_loopback,
        ):
            while True:
                elapsed = time.time() - start_time
                mins = int(elapsed // 60)
                secs = int(elapsed % 60)
                print(f"\r  Recording: {mins:02d}:{secs:02d}", end="", flush=True)
                time.sleep(0.5)
                if max_duration and elapsed >= max_duration:
                    break
    except KeyboardInterrupt:
        pass

    elapsed = time.time() - start_time
    print(f"\n\nStopped. Recorded {elapsed:.1f}s")

    if not frames:
        print("No audio captured.")
        return

    audio = np.concatenate(frames, axis=0)

    # Check for silence
    peak = np.max(np.abs(audio))
    if peak < 100:
        print(f"WARNING: Very low signal (peak={peak}). No audio may be playing or wrong device.")

    # Save
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with wave.open(output_path, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(sample_rate)
        wf.writeframes(audio.tobytes())

    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"Saved: {output_path} ({size_mb:.1f} MB, {elapsed:.1f}s, {sample_rate}Hz {'stereo' if channels == 2 else 'mono'})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Record system audio (TTS capture via WASAPI loopback)")
    parser.add_argument("--output", "-o", default=DEFAULT_OUTPUT, help="Output WAV path")
    parser.add_argument("--duration", "-d", type=int, default=0, help="Max duration in seconds (0=until Ctrl+C)")
    args = parser.parse_args()

    record(args.output, args.duration if args.duration > 0 else None)
