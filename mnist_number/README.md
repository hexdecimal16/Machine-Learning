#Results for various models

Result for basline_model.py(multilayer perception model)

```shell
Using TensorFlow backend.
Train on 60000 samples, validate on 10000 samples
Epoch 1/10
2019-05-18 13:33:27.784619: I tensorflow/core/platform/cpu_feature_guard.cc:140] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
 - 3s - loss: 0.2782 - acc: 0.9211 - val_loss: 0.1415 - val_acc: 0.9573
Epoch 2/10
 - 3s - loss: 0.1115 - acc: 0.9675 - val_loss: 0.0923 - val_acc: 0.9706
Epoch 3/10
 - 3s - loss: 0.0717 - acc: 0.9799 - val_loss: 0.0786 - val_acc: 0.9767
Epoch 4/10
 - 3s - loss: 0.0504 - acc: 0.9857 - val_loss: 0.0741 - val_acc: 0.9774
Epoch 5/10
 - 3s - loss: 0.0373 - acc: 0.9891 - val_loss: 0.0673 - val_acc: 0.9796
Epoch 6/10
 - 3s - loss: 0.0269 - acc: 0.9927 - val_loss: 0.0627 - val_acc: 0.9805
Epoch 7/10
 - 3s - loss: 0.0206 - acc: 0.9949 - val_loss: 0.0622 - val_acc: 0.9801
Epoch 8/10
 - 3s - loss: 0.0139 - acc: 0.9968 - val_loss: 0.0630 - val_acc: 0.9801
Epoch 9/10
 - 3s - loss: 0.0109 - acc: 0.9977 - val_loss: 0.0590 - val_acc: 0.9809
Epoch 10/10
 - 3s - loss: 0.0078 - acc: 0.9987 - val_loss: 0.0587 - val_acc: 0.9817
Baseline Error: 1.83%
```

Result for simple_cnn.py(A simple convolution neural network)

```shell
Using TensorFlow backend.
2019-05-18 13:50:45.204951: I tensorflow/core/platform/cpu_feature_guard.cc:140] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
Train on 60000 samples, validate on 10000 samples
Epoch 1/10
 - 62s - loss: 0.2233 - acc: 0.9367 - val_loss: 0.0788 - val_acc: 0.9748
Epoch 2/10
 - 62s - loss: 0.0712 - acc: 0.9786 - val_loss: 0.0452 - val_acc: 0.9850
Epoch 3/10
 - 61s - loss: 0.0512 - acc: 0.9841 - val_loss: 0.0451 - val_acc: 0.9853
Epoch 4/10
 - 61s - loss: 0.0395 - acc: 0.9878 - val_loss: 0.0403 - val_acc: 0.9877
Epoch 5/10
 - 61s - loss: 0.0327 - acc: 0.9895 - val_loss: 0.0342 - val_acc: 0.9888
Epoch 6/10
 - 61s - loss: 0.0267 - acc: 0.9916 - val_loss: 0.0332 - val_acc: 0.9892
Epoch 7/10
 - 62s - loss: 0.0223 - acc: 0.9929 - val_loss: 0.0340 - val_acc: 0.9886
Epoch 8/10
 - 61s - loss: 0.0193 - acc: 0.9939 - val_loss: 0.0331 - val_acc: 0.9886
Epoch 9/10
 - 62s - loss: 0.0159 - acc: 0.9948 - val_loss: 0.0320 - val_acc: 0.9891
Epoch 10/10
 - 62s - loss: 0.0141 - acc: 0.9959 - val_loss: 0.0337 - val_acc: 0.9892
CNN Error: 1.08%
```

Results for large_cnn.py(A larger two layer convolution neural network model)

```shell
Using TensorFlow backend.
        2019-05-18 14:07:16.504181: I tensorflow/core/platform/cpu_feature_guard.cc:140] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
Train on 60000 samples, validate on 10000 samples
Epoch 1/10
60000/60000 [==============================] - 59s 980us/step - loss: 0.3868 - acc: 0.8821 - val_loss: 0.0867 - val_acc: 0.9723
Epoch 2/10
60000/60000 [==============================] - 58s 968us/step - loss: 0.0996 - acc: 0.9701 - val_loss: 0.0570 - val_acc: 0.9819
Epoch 3/10
60000/60000 [==============================] - 58s 967us/step - loss: 0.0730 - acc: 0.9774 - val_loss: 0.0418 - val_acc: 0.9864
Epoch 4/10
60000/60000 [==============================] - 58s 969us/step - loss: 0.0598 - acc: 0.9818 - val_loss: 0.0389 - val_acc: 0.9868
Epoch 5/10
60000/60000 [==============================] - 58s 969us/step - loss: 0.0509 - acc: 0.9842 - val_loss: 0.0343 - val_acc: 0.9894
Epoch 6/10
60000/60000 [==============================] - 58s 967us/step - loss: 0.0442 - acc: 0.9861 - val_loss: 0.0295 - val_acc: 0.9901
Epoch 7/10
60000/60000 [==============================] - 58s 968us/step - loss: 0.0387 - acc: 0.9879 - val_loss: 0.0288 - val_acc: 0.9901
Epoch 8/10
60000/60000 [==============================] - 58s 968us/step - loss: 0.0352 - acc: 0.9887 - val_loss: 0.0261 - val_acc: 0.9909
Epoch 9/10
60000/60000 [==============================] - 58s 967us/step - loss: 0.0315 - acc: 0.9901 - val_loss: 0.0228 - val_acc: 0.9924
Epoch 10/10
60000/60000 [==============================] - 58s 969us/step - loss: 0.0300 - acc: 0.9904 - val_loss: 0.0257 - val_acc: 0.9917
Large CNN Error: 0.83%
```
