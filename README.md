# Random Video Clip Generator

This Python script generates a random video clip using a main video file and a music file. The generated video clip is a concatenation of randomly selected portions of the main video, each with a duration of 5 to 10 seconds. The total duration of the generated clip is capped at 10 seconds. The audio from the provided music file is overlaid onto this video.

## How to Run the Script

1. **Prepare your files**: Place the main video file and music file in the same directory as the script.

2. **Run the script**: Open a terminal or command prompt, navigate to the directory containing the script and the files, and run the script using Python:

```bash
python main.py
```

The generated video clip will be saved as "output.mp4" in the same directory as the script.

## Configuration

You can adjust several variables in the script to customize its behavior:

- `max_duration`: The maximum duration of the generated video clip in seconds.
- `start_time_min` and `start_time_max`: The range of possible start times for each clip, in seconds.
- `duration_min` and `duration_max`: The range of possible durations for each clip, in seconds.
- `fps`: The frames per second of the generated video clip.

## License

This script is licensed under the MIT License. Enjoy creating your random video clips! 😊
