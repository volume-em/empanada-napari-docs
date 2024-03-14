.. _tutorials:

Tutorials
--------------

.. grid:: 2
    :gutter: 3 3 4 5
    :padding: 2 2 0 0

    .. grid-item-card:: Step by step guide for 2D image inference.
        :shadow: md
        :img-top: ../_static/2d-tutorial-updated.png

        Learn how to run 2D inference with this step-by-step guide.

        +++
        .. button-ref:: 2d-inference-tutorial
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            2D Inference Tutorial

    .. grid-item-card:: Step by step guide for volumetric inference.
        :shadow: md
        :img-top: ../_static/3d-labels.png

        Apply similar techniques from the 2D inference tutorial for running inference on volumetric data.

        +++
        .. button-ref:: 3d-inference-tutorial
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            3D Inference Tutorial

    .. grid-item-card:: Finetune an existing model
        :img-top: ../_static/ft_updated.png
        :shadow: md

        Follow the finetuning a model's step-by-step guide to help you learn how to tailor MitoNet and MitoNet_mini for
        your specific dataset needs.

        +++

        .. button-ref:: finetune-model
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            Finetuning Tutorial

    .. grid-item-card:: Train a panoptic segmentation model
        :img-top: ../_static/panoptic_result.png
        :shadow: md

        Use the training a panoptic segmentation model tutorial to go through the steps of creating training patches, adding
        panoptic labels, and other useful steps to fully train a model in empanada-napari.

        +++

        .. button-ref:: train-panoptic-model
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            Training Tutorial


.. toctree::
    :hidden:

    Inference on 2D images <../tutorials/2d_tutorial>
    Inference on volumetric data <../tutorials/3d_tutorial>
    Finetune an existing model <../tutorials/finetune_tutorial>
    Training a panoptic segmentation model <../tutorials/train_panop>
