import h5py
from keras.models import load_model
import matplotlib.pyplot as plt

def main():
	with open("input.txt") as f: inputs = [[list([(ch=='X')-0.5] for ch in f.readline()[:28]) for b in range(28)] for i in range(10)]

	model = load_model('chicken.h5')
	print(model.summary())	
	output = model.predict(inputs)
	
	print(output.shape)
	
	output = output.reshape(100, 10)
	imgplot = plt.imshow(output)
	plt.show()
	

if __name__ == "__main__":
	main()
	

