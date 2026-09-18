.. _getting_started:

Getting Started
---------------

The empanada-napari plugin is designed to make deep learning image segmentation more accessible for researchers working
with electron microscopy (EM). Included in this plugin is MitoNet, a versatile model specifically tailored for segmenting
mitochondria instances. Alongside this, users will find tools for efficiently creating and annotating training datasets,
training generalist panoptic segmentation models, finetuning existing models, and running inference on both
2D and 3D data. To enhance the speed and reliability of segmentation model training, the plugin utilizes CEM pre-trained
weights as the default option. These weights have been trained using an unsupervised learning algorithm on a vast dataset
of over 1.5 million EM images sourced from numerous unique EM datasets, ensuring their broad applicability and robust performance.
(Conrad and Narayan, Cell Syst 2023 `<https://www.cell.com/cell-systems/fulltext/S2405-4712(22)00494-X>`_)


.. grid:: 1
    :padding: 4

    .. grid-item-card:: Installation Guides
        :shadow: md

        Follow step-by-step instructions to install empanada-napari and its dependencies on your system. Also learn how to
        update your current version to the newest version of the empanada-napari plugin.

        +++

        .. button-ref:: installation
            :ref-type: ref
            :click-parent:
            :color: primary
            :expand:

            INSTALL EMPANADA-NAPARI


.. toctree::
    :maxdepth: 3
    :hidden:

    Installation <../getting_started/install>
    Model Background <../getting_started/background>
    Configuration <../getting_started/config>
