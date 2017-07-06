from keras.models import load_model

model = load_model('model.hdf5')
layers = model.layers
for x in layers:
    print(x)
