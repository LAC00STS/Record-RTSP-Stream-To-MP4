# Record-RTSP-Stream-To-MP4

Python script that prompts you for a RTSP stream URL then records the stream to MP4 files in 10 minute increments
`RTSPtoMP4-10min.py`

For a hard coded URL version - edit the script and add your RTSP URL 
`RTSP2MP4Hardcoded.py`

# Requirements  

- Python 3
- You must have `ffmpeg` installed and on `PATH`

# USAGE  

For Using `RTSPtoMP4-10min.py` which will prompt you for your RTSP URL.

Copy script into directory youwant the MP4 files saved to.
Run the scipt
```
python RTSPtoMP4-10min.py
```
The script will prompt you for the URL to an RTSP stream.
This is the format that works for me and my RTSP stream.
```
rtsp://USERNAME:PASSWORD@IP_ADDRESS:PORT/cam/realmonitor?channel=1&subtype=1
```
The script will then record the stream to an MP4 file and save the MP4 file every 10 minutes.  

In the end you will have 10 minute long MP4 files of the RTSP stream.


For using the hard coded URL script

Open `RTSP2MP4Hardcoded.py` in an IDe or text editor
Edit the following line adding your RTSP URL 
`# Hardcoded RTSP stream URL --- REPLACE WITH YOUR RTSP URL`
Save the scipt
Run the script



