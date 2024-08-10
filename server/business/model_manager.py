from model.model_structure import Model
from model.foods import Foods, class_labels

import torch
from torchvision import transforms
from PIL import Image
import torch.nn.functional as F
import matplotlib.pyplot as plt
from torchvision import transforms, models
import torch.nn as nn
import base64

def save_image_from_json(bytes, output_filename):
	# Decode the base64-encoded bytes
	image_bytes = base64.b64decode(bytes)
	
	# Write the bytes to a new image file
	with open(output_filename, 'wb') as image_file:
		image_file.write(image_bytes)
	print(f"Image saved as {output_filename}")

class ModelManager:
	def __init__(self):
		self.model = Model()
	
	def classify_image(self, image_data):

		format = image_data.get('format')
		data = image_data.get('bytes')

		image_path = f'C:/Users/Vlad Talpiga.VLR_PROJAMZ/OneDrive - Valrom Industrie SRL/Desktop/Licenta/server/images/output.{format}'

		save_image_from_json(data, image_path)
		image = self.preprocess_image(image_path)

		state_dict = torch.load('C:/Users/Vlad Talpiga.VLR_PROJAMZ/OneDrive - Valrom Industrie SRL/Desktop/Licenta/server/model/model_105.pkl')
		self.model.load_state_dict(state_dict)		

		device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
		self.model.to(device)
		image = image.to(device)
		
		self.model.eval()

		with torch.no_grad():
			output = self.model(image)
		
		probabilities = F.softmax(output, dim=1)
		
		_, best_class_index = torch.topk(probabilities, 1)
	
		food_enum_member_name = class_labels[best_class_index[0][0]].upper()
		response = getattr(Foods, food_enum_member_name, None).value

		return response

	@staticmethod
	def preprocess_image(image_path):
		transform = transforms.Compose([
			transforms.Resize((512, 512)),
			transforms.ToTensor(),
			transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
		])
		image = Image.open(image_path).convert('RGB')
		image = transform(image)
		# Add batch dimension
		image = image.unsqueeze(0)
		return image

# if __name__ == '__main__':

#     # image_path = "images/chicken_wings.jpg"
#     # image_path = "images/sp_bol.jpg"
#     image_path = "images/apple_pie.jpg"

#     model = Model()

#     output_class = model.classify_image(image_path, model)

#     print(output_class)
		