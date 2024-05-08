import base64
import json

def add_img_info():
    jsonThingy = None
    nextIdx = 0

    with open("ukol2.ipynb", encoding="UTF-8") as s:
        file_str = s.read()
        jsonThingy = json.loads(file_str)

    for cell in jsonThingy["cells"]:
        if (cell["cell_type"] != "code" or "outputs" not in cell or cell["execution_count"] == 5):
            continue
        for output in cell["outputs"]:
            if ("data" not in output):
                continue
            output["idx"] = nextIdx
            nextIdx += 1

    with open("ukol2_i_info.ipynb", "w", encoding="UTF-8") as s:
        json.dump(jsonThingy, s)

def save_images():
    jsonThingy = None

    with open("ukol2_i_info.ipynb", encoding="UTF-8") as s:
        file_str = s.read()
        jsonThingy = json.loads(file_str)

    for cell in jsonThingy["cells"]:
        if (cell["cell_type"] != "code" or "outputs" not in cell or cell["execution_count"] == 5):
            continue
        for output in cell["outputs"]:
            if ("data" not in output or output["output_type"] != "display_data"):
                continue
            id = output["idx"]
            with open(f"images/img-{id}.png", "wb") as fh:
                fh.write(base64.decodebytes(bytes(output["data"]["image/png"], "utf-8")))

# add_img_info()
#save_images()
import matplotlib.pyplot as plt
from PIL import Image

# Load the PNG image
image_path = "images/img-129.png"
image = Image.open(image_path)

# Plot the image
plt.imshow(image)
plt.axis('off')  # Hide axes for plotting
plt.text(0.54, -0.02, 'Epochs', ha='center', va='center', fontsize=9, transform=plt.gca().transAxes)
plt.text(-0.02, 0.54, 'Validation accuracy', ha='center', va='center', fontsize=9, transform=plt.gca().transAxes, rotation='vertical')

# Save the modified image
plt.savefig("modified_graph.png", bbox_inches='tight', pad_inches=0)

# Show the modified image (optional)
#plt.show()

#okej takze pro kazdy druhy obrazek od img13 dal je potreba zmena above
import os
from PIL import Image

# Directory containing the image files
image_dir = "images"

# List all PNG files
png_files = [f for f in os.listdir(image_dir) if f.startswith('img-') and f.endswith('.png')]
png_files.sort(key=lambda x: int(x.split('-')[1].split('.')[0]))
# Separate into groups
group1 = png_files[:12]  # First 15 images
group2 = png_files[12:]  # Last 15 images
print(group1)
for i,image in enumerate(group2):
    #print(image)
    image_path = os.path.join(image_dir, image)
        #print(image_path)
    image_obj = Image.open(image_path)
    #print(image)
    if i % 2 == 0:
        #image_path = f"images/{image}"
        original_size = image_obj.size
        plt.gcf().set_size_inches(original_size[0] / plt.rcParams['figure.dpi'], original_size[1] / plt.rcParams['figure.dpi'])
        plt.figure()
        # Plot the image
        plt.imshow(image_obj)
        plt.axis('off')  # Hide axes for plotting
        plt.text(0.54, -0.02, 'Epochs', ha='center', va='center', fontsize=9, transform=plt.gca().transAxes)
        plt.text(-0.02, 0.54, 'Validation accuracy', ha='center', va='center', fontsize=9, transform=plt.gca().transAxes, rotation='vertical')
        # Save the modified image
        
        modified_image_path = os.path.join(image_dir, f"modified_{image}")
        plt.savefig(modified_image_path, bbox_inches='tight', pad_inches=0.1)
        plt.close()