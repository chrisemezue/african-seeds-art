from imageio import imread, mimsave
import os


def convert_to_video(TEXT,PICTURES_DIR,OUTPUT_GIF_SAVE):
    textpath = '_'.join(TEXT.split(' '))
    images = []
    for file_name in sorted(os.listdir(PICTURES_DIR)):
        if file_name.startswith(textpath) and file_name != f'{textpath}.jpg':
            images.append(imread(os.path.join(PICTURES_DIR, file_name)))


    mimsave(f'{OUTPUT_GIF_SAVE}.mp4', images)
    print(f'Generated image generation animation at ./{OUTPUT_GIF_SAVE}.mp4')
