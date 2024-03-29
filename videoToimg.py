import os
import subprocess 

def convert_videos_to_images(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through all files in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith(('.mp4', '.avi', '.mkv', '.mov')):  # Add more video file extensions as needed
            video_file = os.path.join(input_folder, file_name)

            # Extract the file name without extension
            file_base_name = os.path.splitext(file_name)[0]

            # Create a subfolder for each video file
            output_subfolder = os.path.join(output_folder, file_base_name)
            os.makedirs(output_subfolder, exist_ok=True)

            # Define the FFmpeg command
            ffmpeg_cmd = [
                'ffmpeg',
                '-i', video_file,  # Input video file
                '-vf', 'fps=1,scale=1280:720,crop=iw:ih/2:0:ih/2',  # Video filter options
                os.path.join(output_subfolder, file_base_name + '_frame_%04d.png')  # Output image file pattern
            ]

            try:
                # Run the FFmpeg command
                subprocess.run(ffmpeg_cmd, check=True)
                print(f"Video conversion completed successfully for {file_name}.")
            except subprocess.CalledProcessError as e:
                print(f"Error converting video to images for {file_name}:", e)

input_folder = 'D:/Taken_Videos'
output_folder = 'D:/FRAMES/Taken_Videos_MSOs/'

convert_videos_to_images(input_folder, output_folder)
