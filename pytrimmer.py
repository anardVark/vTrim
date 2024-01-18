import os
import essential_py as esp
from moviepy.editor import *

def list_dir(path):
    try:
        dir_list = os.listdir(path)
        return dir_list
    except Exception as e:
        esp.wrout(f"Failed to read directory: {e}")
        pass

def strip(path, output, clip_name, trim_start, trim_end):
    # Open and trim intro
    try:
        new_clip = VideoFileClip(f'{path}/{clip_name}')
        clip = new_clip.subclip(t_start=(trim_start), t_end=(trim_end))
        
        #clip.ipython_display(width = 360)
    except Exception as e:
        esp.wrout(f"Failed trimming intro: {e}")
        pass

    # Save trimmed clip
    try:
        esp.verify_create_path(output)
        clip.write_videofile(os.path.join(output, f'trimmed_{clip_name}'))
    except Exception as e:
        esp.wrout(f"Failed to save file: {e}")
        pass
    finally:
        new_clip.close()
