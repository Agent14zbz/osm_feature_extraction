import os
import json
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from PIL import Image


def save_pixplot_layout(pixplot_output_folder=None, layout_type=None, 
                        image_zoom=0.1, figsize=(10,10), dpi=300, transparent=False,
                        bgcolor="white", filename="default", file_format="png"):

    '''
    Read json files from pix-plot output folder, save layouts as a local image file

    Parameters:
    ------
    pixplot_output_folder:
        the "output" folder of pix-plot
    layout_type:
        which type of layout need to save ("umap","umap_jittered","rasterfairy")
    image_zoom:
        zoom the original images to fit the layout size
    figsize:
        tuple, size of the image in inch
    dpi:
        dpi of the output image
    transparent:
        background transparancy of the output image
    bgcolor:
        background color of the output image
    filename:
        output image name
    file_format:
        the format of the image to save (e.g. "jpg","png")

    '''
    
    # load all layout files from pixplot output folder
    imagelist_root = os.path.join(pixplot_output_folder, "data/imagelists")
    for file in os.listdir(imagelist_root):
        if "imagelist" in file:
            imagelist_file = os.path.join(imagelist_root,file)
    layouts_root = os.path.join(pixplot_output_folder, "data/layouts")
    for file in os.listdir(layouts_root):
        if "umap-jittered" in file:
            umap_jittered_file = os.path.join(layouts_root, file)
        elif "umap" in file:
            umap_file = os.path.join(layouts_root, file)
        elif "rasterfairy" in file:
            rasterfairy_file = os.path.join(layouts_root, file)
    image_folder = os.path.join(pixplot_output_folder, "data/originals")
    
    # load all image names from imagelist
    with open(imagelist_file) as json_file:
        data = json.load(json_file)
        imagelist = data['images']
    posXlist=[]
    posYlist=[]

    #
    temp = Image.open(image_folder +'/'+ imagelist[0])

    # save layouts
    fig = plt.figure(figsize = figsize,dpi = dpi)
    left, bottom, width, height = 0,0,1,1
    ax = fig.add_axes([left, bottom, width, height])

    if layout_type == "umap":
        print("******saving umap******")
        with open(umap_file) as json_file:
            data = json.load(json_file)
            for i in range(len(data)):
                posXlist.append(data[i][0])
                posYlist.append(data[i][1])

        for j in range(len(imagelist)):
            img = Image.open(image_folder +'/'+ imagelist[j])
            imagebox = OffsetImage(img, zoom=image_zoom)
            ab = AnnotationBbox(imagebox, [(posXlist[j]+1), (posYlist[j]+1)], pad=0, frameon=False)
            ax.add_artist(ab)
    elif layout_type == "umap_jittered":
        print("******saving umap_jittered******")
        with open(umap_jittered_file) as json_file:
            data = json.load(json_file)
            for i in range(len(data)):
                posXlist.append(data[i][0])
                posYlist.append(data[i][1])

        for j in range(len(imagelist)):
            img = Image.open(image_folder +'/'+ imagelist[j])
            imagebox = OffsetImage(img, zoom=image_zoom)
            ab = AnnotationBbox(imagebox, [(posXlist[j]+1), (posYlist[j]+1)], pad=0, frameon=False)
            ax.add_artist(ab)
    elif layout_type == "rasterfairy":
        print("******saving rasterfairy******")
        with open(rasterfairy_file) as json_file:
            data = json.load(json_file)
            for i in range(len(data)):
                posXlist.append(data[i][0])
                posYlist.append(data[i][1])
        for j in range(len(imagelist)):
            img = Image.open(image_folder +'/'+ imagelist[j])
            imagebox = OffsetImage(img, zoom=image_zoom)
            ab = AnnotationBbox(imagebox, [(posXlist[j]+1), (posYlist[j]+1)], pad=0, frameon=False)
            ax.add_artist(ab)
    else:
        raise Exception("Please input proper layout type: umap, umap_jittered, rasterfairy !")

    plt.xlim(-0.1 , 2.1)
    plt.ylim(-0.1 , 2.1)
    plt.axis('off')
    fig = plt.gcf()
    imagefile = filename + "." + file_format
    fig.savefig(os.path.join(pixplot_output_folder,imagefile),facecolor=bgcolor,transparent=transparent)

# test running        
save_pixplot_layout(pixplot_output_folder="C:/Users/zhangbz/output_", layout_type="umap_jittered", image_zoom=0.05, 
                    filename="test",bgcolor="black")
