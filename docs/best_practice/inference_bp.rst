.. _inference-best-practice:

Inference Best Practices
--------------------------

2D inference best practices
============================

When running the 2D inference module on images of a given size for the first
time, results can be slow. After inference is run twice on a particular size, it will
be much faster. This is because pytorch is performing optimization in the background to
make the model faster on your system's hardware.

.. note::

  When using **Multi-GPU** inference there's some overhead associated with the
  creation of a process group. This overhead can make Multi-GPU inference slower
  on small volumes. Therefore, we don't recommend using it unless working with datasets
  larger than 1 GB.


  However, in such cases, the inference speed-up is nearly linear
  (segmentation will be 4x faster with 4 GPUs than with 1). As more GPUs are added,
  inference starts to become CPU bound (i.e., the segmentations are being created
  faster on GPU than they can be processed on CPU). There can be a long delay between
  inference and backward matching as the CPU processes work to catch up.

We've found that models can give considerably different results based on the nanometer
resolution of the input image and model inference is faster for smaller input images.
Ideally you'll want to find and use the biggest **Image Downsampling** factor that still gives
satisfactory results (see example below).

.. dropdown:: Downsampling example:

    .. image:: ../_static/downsampling_better.png
      :align: center
      :width: 100%

    Here downsampling by a factor of 2 significantly reduces over-splitting errors and results in a better pixel-level
    segmentation. Plus, the smaller image size means that model inference will be faster and use less memory! The takeaway
    is that it’s important to test different downsampling factors on new datasets to see which is best.

    .. note::
        Always opt to use the largest downsampling factor that gives satisfactory results. Too much downsampling will
        result in more false positive detections and more false negatives for small objects
        in particular.


Tweaking the **Segmentation Confidence Threshold** is often just a proxy for erosion and dilation of labels.
Because ortho-plane inference averages segmentations from 3 views, using a lower confidence
threshold is sometimes beneficial: try 0.3 instead of 0.5.

The **Center Confidence Threshold** and **Centers Minimum Distance** parameters both control how "split up"
instances will be in 2D. Raising the confidence threshold will result in fewer object centers
and therefore fewer instances in the segmentation. Increasing the minimum distance
will filter out centers that are too close together. This can help if long objects are being over-split. If you notice
that the borders between instances are too "blocky", selecting the **Fine boundaries** option may be useful.
However, this comes at the cost of 4x more memory usage during postprocessing, so use it wisely!

The **Max objects per class** can also be thought of as the label divisor. That means, when the model used to run inference has a label divisor
of *None*, simply put 0 in this box. This will start the label IDs at 1 (see note). To determine label divisor used by the model, open the
:ref:`Get model info <get-model-info>` module and print the model's description in the terminal.

.. note::

    You can keep the **Max objects per class** at the preset value of 10,000 even if the model's label divisor is *None*. This will just
    start the label IDs at 10001.


2D inference using batch mode and output to layer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Selecting the **Batch mode** option in the :ref:`2D Inference (Parameter Testing) <2d-inference>` module, will apply the adjusted
parameters to each image in the stack. The label ID values for each image in the stack, will begin at the **Max objects per class** + 1.
(See above for more details).

The **Output to layer** and **output layer** box are used when running inference on patches or flipbooks created in the
:ref:`Pick finetune/training patches <pick-patches>` module. However, you can not use **Batch mode** with the **Output to layer**
option. Instead, you can simply run 2D inference using batch mode, then create the finetune/training patches and select the **Pick paired data** option.

.. note::

    Remember when applying any edits to your segmentations after using batch mode, keep the **Apply in 3D** box **unchecked**!
    See :ref:`Proofreading Best Practices <proofreading_tips>` for best practices and other tips and tricks!


3D inference best practices
============================

Depending on the size of the volume, 3D inference can take some time even with a GPU,
therefore it's highly recommended to test out inference parameters beforehand using the
2D inference module. The 2D inference module will run inference on whatever image slice
the viewer is pointed at in napari. This means that parameters can be tested on xy, xz and yz
slices by flipping the volume and scrolling through the stack.

.. tip::

    If results appear substantially better on slices from a particular plane, then use this as the **Inference plane** for
    3D inference. Similarly, if results on xy slices are good but results on xz and yz slices are poor,
    then using ortho-plane inference is not recommended.

The most important 3D parameter is the **Median Filter Size**. This smooths out the stacked
segmentations. The best kernel size is typically a function of voxel size. Lower-resolution
volumes (>20 nm) that have relatively more change between consecutive slices usually benefit from a smaller
kernel size like 3. Higher-resolution volumes (<10 nm) have much less change across slices and a kernel
size of 7 or 9 can work well.

The **Min Size** and **Min Extent** parameters filter out small objects and segmentation "pancakes". The
optimal size is strongly data-dependent. As a rough estimate, try drawing a bounding box around a small
object that you see. Divide the volume of the box by 2 to get the approximate volume of a sphere that
would fit inside that box. Pick some number a few hundred voxels below that threshold as your min size.
Likewise, the min extent should be a few increments less than the smallest dimension of the bounding box.

The **Voxel Vote Threshold Out of 3** and **Permit detections found in 1 stack into consensus** are options
for when there are too many false negatives after ortho-plane segmentation. Decreasing the voxel
vote threshold to 1 will fill in more voxels but should not increase the number of false positive detections
very much. This is because the voxel vote threshold only affects detections that were picked up in more than 1 of the
inference stacks. **Permit detections found in 1 stack into consensus**, on the other hand, can increase false positives because
it will allow detections picked up by just a single stack into the consensus segmentation (what a well named parameter!).

When running ortho-plane inference it's recommended to also **Return xy, xz, yz stacks**
segmentations. In some cases, inference results are better on just a single plane (i.e., xz)
than they are in the consensus. Returning the intermediate panoptic results for each stack
will help you to decide whether that applies to your dataset or not.

