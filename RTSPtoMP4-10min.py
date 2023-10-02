import subprocess
import os

def record_rtsp(rtsp_url, output_filename_pattern):
    # Get the current working directory
    cwd = os.getcwd()

    # Use ffmpeg's segment option to split output every 10 minutes (600 seconds)
    # The %03d format will number the files sequentially, starting from 000
    output_filepath_pattern = os.path.join(cwd, output_filename_pattern)

    # Build the ffmpeg command
    command = [
        'ffmpeg', 
        '-i', rtsp_url, 
        '-c:v', 'copy', 
        '-c:a', 'copy', 
        '-f', 'segment',
        '-segment_time', '600',  # 600 seconds = 10 minutes
        '-reset_timestamps', '1',
        output_filepath_pattern
    ]

    # Try running the command
    try:
        print("Attempting to connect to RTSP stream...")
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        print("Failed to connect to RTSP stream or encountered an error during recording.")
    except KeyboardInterrupt:
        print("\nRecording interrupted by user.")

# Prompt the user for the RTSP stream URL
rtsp_stream_url = input("Please enter the RTSP stream URL: ")

# Call the function to start recording with a pattern, it will save as output_000.mp4, output_001.mp4, and so on.
record_rtsp(rtsp_stream_url, 'output_%03d.mp4')

# Keep the terminal open
input("Press Enter to exit...")
