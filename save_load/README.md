This is a demo for load and save a ML model using pickle in python
#Results

From save_model.py

```shell
Using TensorFlow backend.
2019-05-30 17:18:57.318146: I tensorflow/core/platform/cpu_feature_guard.cc:140] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
Train on 60000 samples, validate on 10000 samples
Epoch 1/10
60000/60000 [==============================] - 57s 955us/step - loss: 0.3862 - acc: 0.8820 - val_loss: 0.0889 - val_acc: 0.9719
Epoch 2/10
60000/60000 [==============================] - 57s 950us/step - loss: 0.0982 - acc: 0.9702 - val_loss: 0.0549 - val_acc: 0.9826
Epoch 3/10
60000/60000 [==============================] - 57s 949us/step - loss: 0.0728 - acc: 0.9774 - val_loss: 0.0424 - val_acc: 0.9858
Epoch 4/10
60000/60000 [==============================] - 57s 953us/step - loss: 0.0599 - acc: 0.9817 - val_loss: 0.0377 - val_acc: 0.9868
Epoch 5/10
60000/60000 [==============================] - 57s 956us/step - loss: 0.0510 - acc: 0.9838 - val_loss: 0.0351 - val_acc: 0.9885
Epoch 6/10
60000/60000 [==============================] - 57s 956us/step - loss: 0.0438 - acc: 0.9858 - val_loss: 0.0299 - val_acc: 0.9904
Epoch 7/10
60000/60000 [==============================] - 57s 956us/step - loss: 0.0391 - acc: 0.9881 - val_loss: 0.0301 - val_acc: 0.9898
Epoch 8/10
60000/60000 [==============================] - 57s 955us/step - loss: 0.0350 - acc: 0.9886 - val_loss: 0.0265 - val_acc: 0.9907
Epoch 9/10
60000/60000 [==============================] - 57s 954us/step - loss: 0.0321 - acc: 0.9903 - val_loss: 0.0244 - val_acc: 0.9923
Epoch 10/10
60000/60000 [==============================] - 57s 955us/step - loss: 0.0306 - acc: 0.9902 - val_loss: 0.0283 - val_acc: 0.9900
model saved as finalized_model.sav
```

Frome load_model.py
```shell
Using TensorFlow backend.
2019-05-30 17:42:23.608414: I tensorflow/core/platform/cpu_feature_guard.cc:140] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
Large CNN Error: 0.99%
```
