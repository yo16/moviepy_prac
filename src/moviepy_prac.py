from moviepy.editor import *
from pathlib import Path

def main(movie_file):
    clip1 = VideoFileClip(movie_file)

    # 切り出し
    top = 124
    clip2 = (clip1.fx(vfx.crop, x1=0, y1=top, x2=320, y2=top+220))

    # 保存
    file_path = Path(movie_file)
    tmp = file_path.parent / f"{file_path.stem}_out.mp4"
    print(tmp)
    
    clip2.write_videofile(str(file_path.parent / f"{file_path.stem}_out.mp4"))
    clip2.write_gif(str(file_path.parent / f"{file_path.stem}_out.gif"), fps=20)

if __name__=='__main__':
    movie_file = './data/mv2.mp4'
    main(movie_file)
