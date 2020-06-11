import os
import json
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from PIL import Image


def save_pixplot_layout(pixplot_output_folder=None, layout_type="umap", 
                        image_zoom=0.1, file_format=".png"):

    '''
    Read json files from pix-plot output folder, save layouts as a local image file

    pixplot_output_folder: the "output" folder of pix-plot
    layout_type: which type of layout need to save ("umap","umap_jittered","rasterfairy")
    image_zoom: zoom the original images to fit the layout

    filetype: the format of the image to save (e.g. ".jpg",".png")
    '''

    imagelist_file = os.path.join(pixplot_output_folder, "data/imagelists")
    umap_file = os.path.join(pixplot_output_folder, "data/layouts")
    umap_jittered_file = os.path.join(pixplot_output_folder, "data/layouts")
    rasterfairy_file = os.path.join(pixplot_output_folder, "data/layouts")

    image_folder = os.path.join(pixplot_output_folder, "data/originals")

    with open(imagelist_file) as json_file:
        data = json.load(json_file)
        imagelist = data['images']
    
    posXlist=[]
    posYlist=[]
    with open(umap_file) as json_file:
        data = json.load(json_file)
        for i in range(len(data)):
            posXlist.append(data[i][0])
            posYlist.append(data[i][1])

    print('image num:',len(imagelist))
    print('max X =',max(posXlist),' min X =',min(posXlist),' max Y =',max(posYlist),' min Y =',min(posYlist))
    
    fig = plt.figure(figsize = (20,20),dpi = 300)
    left, bottom, width, height = 0,0,1,1

    ax = fig.add_axes([left, bottom, width, height])
    for i in range(len(imagelist)):
        img = Image.open(image_folder +'/'+ imagelist[i])

        imagebox = OffsetImage(img, zoom=0.12)
        ab = AnnotationBbox(imagebox, [(posXlist[i]+1), (posYlist[i]+1)], pad=0, frameon=False)
        ax.add_artist(ab)
    plt.xlim(0 , 2 )
    plt.ylim(0 , 2 )
    plt.axis('off')
    fig = plt.gcf()

    fig.savefig("D:/1.png",transparent=True)

