from moviepy.editor import *

def main(movie_file):
    clip1 = VideoFileClip(movie_file)

    # 切り出し
    top = 124
    clip2 = (clip1.fx(vfx.crop, x1=0, y1=top, x2=320, y2=top+220))

    clip2.write_videofile('./data/out.mp4')
    clip2.write_gif('./data/out.gif', fps=15)

if __name__=='__main__':
    movie_file = './data/mv1.mp4'
    main(movie_file)
