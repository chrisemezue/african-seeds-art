# African Dawa Art
African Dawa Art  is committed to amplifying Indigenous African seeds through the medium of mixed media artworks. Dawa seeds which was used for this model is an African millet seed. Dawa seeds were used to create concepts in arts, and this is a source of inspiration to train the model to learn about the dawa concept to create AI artworks.

## Description
Dawa seeds art 2021  is an artificial intelligence (AI) procreated creation with mixed media artworks made with African seeds. Dawa seeds which was used to create the mixed media artworks is a class of the African millet seed. Nefertiti Emezue used the Dawa seeds to create mixed media artworks and together with Chris Emezue, they trained the model to assimilate and interpret the artwork to create an AI artwork. For this project, we used [Deep Daze model](https://github.com/lucidrains/DALLE-pytorch), a text to image generation model that uses [OpenAI's CLIP](https://arxiv.org/abs/2103.00020) and [Siren (Implicit neural representation network)](https://vsitzmann.github.io/siren/). By configuring the model on a joint optimization task of both the image and the text (interpretation of the dawa image), the model learns to create abstract interpretations of the text while trying represent an art close to the dawa art as possible.

## Idea
1. We give the model our _dawa picture_ as well as a one-sentence interpretation (we shall call text) of the dawa picture.
2. The model learns from both _the text_ and _dawa picture_ through a joint optimization task.
3. The model outputs an abstract art (or series of abstract pictures during its learning process which we compile into a video) which is the model’s interpretation of the _dawa picture_ and _the text_.
