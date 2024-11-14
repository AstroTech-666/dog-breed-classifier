import ast
import os
from PIL import Image
import torchvision.transforms as transforms
from torch.autograd import Variable
import torchvision.models as models
from torch import __version__

# Load pre-trained models
resnet18 = models.resnet18(pretrained=True)
alexnet = models.alexnet(pretrained=True)
vgg16 = models.vgg16(pretrained=True)

models = {'resnet': resnet18, 'alexnet': alexnet, 'vgg': vgg16}

# Get the path of the current directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the relative path to the imagenet file
imagenet_file_path = os.path.join(script_dir, 'imagenet1000_clsid_to_human.txt')

# Load ImageNet labels using the relative path
with open(imagenet_file_path) as imagenet_classes_file:
    imagenet_classes_dict = ast.literal_eval(imagenet_classes_file.read())

def classifier(img_path, model_name):
    # Load the image
    img_pil = Image.open(img_path)

    # Define transformations
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    # Preprocess the image
    img_tensor = preprocess(img_pil)
    
    # Resize the tensor (add dimension for batch)
    img_tensor.unsqueeze_(0)
    
    # Handle PyTorch version differences for Variable
    pytorch_ver = __version__.split('.')
    if int(pytorch_ver[0]) > 0 or int(pytorch_ver[1]) >= 4:
        img_tensor.requires_grad_(False)
    
    # Apply the model to the image
    model = models[model_name]
    model = model.eval()  # Set model to evaluation mode
    
    # Apply image tensor to model
    if int(pytorch_ver[0]) > 0 or int(pytorch_ver[1]) >= 4:
        output = model(img_tensor)
    else:
        data = Variable(img_tensor, volatile=True)
        output = model(data)
    
    # Get the predicted class index
    pred_idx = output.data.numpy().argmax()
    return imagenet_classes_dict[pred_idx]
