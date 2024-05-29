from moviepy.editor import *
from pathlib import Path

def main(input_file, output_file_stem):
    clip1 = VideoFileClip(input_file)

    # 切り出し
    top = 124
    clip2 = (clip1.fx(vfx.crop, x1=0, y1=top, x2=320, y2=top+220))

    # 保存
    clip2.write_videofile(f"{output_file_stem}.mp4")
    clip2.write_gif(f"{output_file_stem}.gif", fps=20)


if __name__=='__main__':
    movie_file = Path('./data/mv2.mp4')
    # 出力ファイルの拡張子手前まで
    # ※ 複数の拡張子を変えていくつかのファイルを作りたいので、拡張子手前までの文字列
    out_file_stem = str(movie_file.parent / f"{movie_file.stem}_out")

    main(str(movie_file), out_file_stem)
