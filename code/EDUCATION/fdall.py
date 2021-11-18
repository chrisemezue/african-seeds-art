from tqdm.notebook import trange
from IPython.display import Image, display
import os
from gif import convert_to_video
from deep_daze import Imagine

TEXT = '''This artwork represents the connections of education and the globe. It represents the idea that education serves as a unifying factor between countries of the World.'''
NUM_LAYERS = 32
SAVE_EVERY =  20
IMAGE_WIDTH = 512
SAVE_PROGRESS = True 
LEARNING_RATE = 1e-5
EPOCHS=20
ITERATIONS = 1050
PICTURES_DIR = '/home/mila/c/chris.emezue/dall2/dawaFULL2'


model = Imagine(
    text = TEXT,
    num_layers = NUM_LAYERS,
    save_every = SAVE_EVERY,
    image_width = IMAGE_WIDTH,
    lr = LEARNING_RATE,
    iterations = ITERATIONS,
    save_progress = SAVE_PROGRESS,
    img = '/home/mila/c/chris.emezue/dall2/dawamain.jpg',
    save_gif=True,
    gradient_accumulate_every=1,
    create_story=True,
    story_separator='.'
)

for epoch in trange(EPOCHS, desc = 'epochs'):
    for i in trange(ITERATIONS, desc = 'iteration'):
        model.train_step(epoch, i)

        if i % model.save_every != 0:
            continue

        filename = TEXT.replace(' ', '_')
        image = Image(os.path.join(PICTURES_DIR,f'{filename}.jpg'))
        #display(image)



OUTPUT_GIF_SAVE=  '/home/mila/c/chris.emezue/dall2/dawaFULL2'
convert_to_video(TEXT,PICTURES_DIR,OUTPUT_GIF_SAVE)