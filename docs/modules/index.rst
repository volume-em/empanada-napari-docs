.. _modules:
.. raw:: html

   <style type="text/css">
        h1 {display: none;}
   </style>

empanada-napari modules
-----------------------

.. important::

    **empanada-napari version 1.1.1 is now available!** This latest version has minor bug fixes regarding the Filter Labels and Count Labels modules.

.. _new-features:

========================
New and updated modules
========================

.. grid:: 2
    :gutter: 2 2 4 4
    :padding: 2 2 0 0

    .. grid-item-card:: Export Segmentations
        :shadow: md

        Exports 2D stack segmentations or a single 3D volume label mask.

        +++
        .. button-ref:: export-seg
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            Export Segmentations


    .. grid-item-card:: Morph Labels
        :shadow: md

        Applies morphological operations to specific labels or to the entire label layer.

        +++

        .. button-ref:: morph-labels
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            Morph Labels


    .. grid-item-card:: Count Labels
        :shadow: md

        Counts the number of label IDs in the dataset and export the list of label IDs in an Excel workbook.

        +++

        .. button-ref:: count-labels
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            Count Labels

    .. grid-item-card:: Filter Labels
        :shadow: md

        Removes small pixel/voxel valued labels from the label mask and/or labels touching the border of the image.

        +++

        .. button-ref:: filter-labels
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            Filter Labels

    .. grid-item-card:: Split Labels
        :shadow: md

        Allows the placement of multiple markers for distance watershed-based instance splitting.

        +++

        .. button-ref:: split-labels
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            Split Labels

    .. grid-item-card:: Export a model
        :shadow: md

        Locally exports an empanada model. Useful for
        sharing models locally or over the internet.

        +++

        .. button-ref:: export-model
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            Export a Model

    .. grid-item-card:: Import a model
        :shadow: md

        Makes a new model accessible in all other training and inference modules.

        +++

        .. button-ref:: import-model
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            Import a Model


.. _inference-modules:

=================================
Inference modules
=================================


.. grid:: 2
    :gutter: 2 2 4 4
    :padding: 2 2 0 0

    .. grid-item-card:: 2D Inference (Parameter testing)
        :shadow: md

        Runs model inference on 2D images. Supports batch mode for
        predicting segmentations on a series of unrelated images or can be used to segment arbitrary 2D slices
        from volumetric data.

        +++
        .. button-ref:: 2d-inference
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            2D Inference (Parameter Testing)


    .. grid-item-card:: 3D Inference
        :shadow: md

        Implements stack and ortho-plane inference functionality for volumetric datasets.

        +++

        .. button-ref:: 3d-inference
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            3D Inference

.. _finetune-train-mods:

=================================
Finetune and training  modules
=================================

.. grid:: 2
    :gutter: 2 2 4 4
    :padding: 2 2 0 0


    .. grid-item-card:: Pick finetune/training patches
        :shadow: md

        Automatically picks patches of data to annotate from 2D or
        3D images. Also gives the option for uses for manually select ROIs using placed points.

        +++

        .. button-ref:: pick-patches
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            Pick Patches

    .. grid-item-card:: Save finetune/training patches
        :shadow: md

        Stores training patch segmentations in the correct format
        expected for model finetuning and training.

        +++

        .. button-ref:: save-patches
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            Save Patches

    .. grid-item-card:: Finetune a model
        :shadow: md

        Allows users to finetune any registered model on a specialized
        segmentation dataset.

        +++

        .. button-ref:: finetune-model
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            Finetune a Model

    .. grid-item-card:: Train a model
        :shadow: md

        Train models from scratch for arbitrary panoptic segmentation tasks.
        Optionally, initialize training from CEM pre-trained weights for faster convergence
        and greater robustness.

        +++

        .. button-ref:: train-model
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            Train a Model

    .. grid-item-card:: Register a model
        :shadow: md

        Make a new model accessible in all other training and inference
        modules. Models can be registered from .pth files or from web URLs. Useful for
        sharing models locally or over the internet.

        +++

        .. button-ref:: register-model
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            Register a Model

    .. grid-item-card:: Get model info
        :shadow: md

        Get information about registered models to help decide which one
        is appropriate for inference or finetuning.

        +++

        .. button-ref:: get-model-info
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            Get Model Info

.. _proofreading-tools:

=================================
Proofreading modules
=================================

.. grid:: 2
    :gutter: 2 2 4 4
    :padding: 2 2 0 0

    .. grid-item-card:: Merge Labels
        :shadow: md

        Allows the selection of multiple instances and merges them all to
        the same label.

        +++

        .. button-ref:: merge-labels
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            Merge Labels

    .. grid-item-card:: Delete Labels
        :shadow: md

        Allows the selection of multiple instances and allows the removal of selected labels

        +++

        .. button-ref:: delete-labels
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            Delete Labels

    .. grid-item-card:: Jump to label
        :shadow: md

        Given a label ID, moves the napari viewer to the first 2D slice where an object appears.

        +++

        .. button-ref:: jump
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            Jump to Label

    .. grid-item-card:: Find next available label
        :shadow: md

        Returns the next available label ID for manual annotation.

        +++

        .. button-ref:: find-next
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            Find Next Label




.. toctree::
    :caption: Inference
    :hidden:

    2D Inference (Parameter Testing) <../modules/_2d_seg>
    3D Inference <../modules/_3d_seg>
    Export Segmentations <../modules/_export_segmentation>


.. toctree::
    :caption: Finetuning and Training a Model
    :hidden:

    Pick finetune/training patches <../modules/_pick_patches>
    Save finetune/training patches <../modules/_save_patches>
    Finetune a model  <../modules/_finetune>
    Train a model <../modules/_train>
    Register a model <../modules/_register_model>
    Get model info <../modules/_get_info>
    Export a model <../modules/_export>
    Import a model <../modules/_import>



.. toctree::
    :caption: Proofreading Tools
    :hidden:

    Count Labels  <../modules/_count>
    Merge Labels <../modules/_merge>
    Delete Labels <../modules/_delete>
    Morph Labels <../modules/_morph>
    Split Labels  <../modules/_split>
    Filter Labels <../modules/_filter>
    Jump to Label <../modules/_jump>
    Find Next Available Label <../modules/_find_next>


