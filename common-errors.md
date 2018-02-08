If running:
```
!python classify_image.py
```

yields:
```
/usr/local/lib/python3.6/dist-packages/h5py/__init__.py:36: FutureWarning: Conversion of the second argument of issubdtype from `float` to `np.floating` is deprecated. In future, it will be treated as `np.float64 == np.dtype(float).type`.
  from ._conv import register_converters as _register_converters
>> Downloading inception-2015-12-05.tgz 100.0%
Successfully downloaded inception-2015-12-05.tgz 88931400 bytes.
2018-02-07 22:06:11.433260: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:892] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2018-02-07 22:06:11.433505: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Found device 0 with properties:
name: Tesla K80 major: 3 minor: 7 memoryClockRate(GHz): 0.8235
pciBusID: 0000:00:04.0
totalMemory: 11.17GiB freeMemory: 163.62MiB
2018-02-07 22:06:11.433538: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1120] Creating TensorFlow device (/device:GPU:0) -> (device: 0, name: Tesla K80, pci bus id: 0000:00:04.0, compute capability: 3.7)
2018-02-07 22:06:11.442068: E tensorflow/stream_executor/cuda/cuda_driver.cc:936] failed to allocate 163.62M (171573248 bytes) from device: CUDA_ERROR_OUT_OF_MEMORY
2018-02-07 22:06:11.761083: W tensorflow/core/framework/op_def_util.cc:334] Op BatchNormWithGlobalNormalization is deprecated. It will cease to work in GraphDef version 9. Use tf.nn.batch_normalization().
2018-02-07 22:06:11.979617: E tensorflow/stream_executor/cuda/cuda_blas.cc:366] failed to create cublas handle: CUBLAS_STATUS_ALLOC_FAILED
2018-02-07 22:06:12.055508: E tensorflow/stream_executor/cuda/cuda_dnn.cc:385] could not create cudnn handle: CUDNN_STATUS_INTERNAL_ERROR
2018-02-07 22:06:12.055596: E tensorflow/stream_executor/cuda/cuda_dnn.cc:352] could not destroy cudnn handle: CUDNN_STATUS_BAD_PARAM
2018-02-07 22:06:12.055615: F tensorflow/core/kernels/conv_ops.cc:667] Check failed: stream->parent()->GetConvolveAlgorithms( conv_parameters.ShouldIncludeWinogradNonfusedAlgo<T>(), &algorithms)
Aborted (core dumped)
```

This is Google Colab not having enough memory for the operation. The log outputs that the current freeMemory is 163.62MB.
We need at least 200MB of free memory to run our classifier. To resolve this error, delete anything from the instance that you don't need (i.e. An older version of Python).
