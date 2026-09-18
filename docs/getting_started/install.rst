.. _installation:

Installation
------------

Napari is still considered alpha phase software and may not install correctly on the
first attempt, if that happens please reach out to the napari developers directly `here <https://github.com/napari/napari/issues>`_.
If you're having issues with empanada-napari, you can reach out to the developers `here <https://github.com/volume-em/empanada-napari/issues>`_.

.. important::

    **empanada-napari version 1.2.4** includes models for mitochondria, nuclei, and lipid droplets, plus updated 2D and 3D inference modules.


.. admonition:: Suggested

    Check that git, gcc and g++ compilers are installed before proceeding.

    1. Mac users please read `this <https://mac.install.guide/commandlinetools/4>`_.

    2. Windows users please read `this <https://code.visualstudio.com/docs/cpp/config-mingw#_installing-the-mingww64-toolchain>`_.


Conda Installation
===================

1. If not already installed, you can `install miniconda here <https://docs.conda.io/en/latest/miniconda.html>`_.

2. Download the correct installer for your OS (Mac, Linux, Windows).

3. After installing `conda`, open a new terminal or command/anaconda prompt window.

4. Verify conda installed correctly with::

    conda --version

.. note::
      If you get a "conda not found error" the most likely cause is that the path wasn't updated correctly. Try restarting
      the terminal or command prompt window. If that doesn't work then
      see `fixing conda path on Mac/Linux <https://stackoverflow.com/questions/35246386/conda-command-not-found>`_
      or `fixing conda path on Windows <https://stackoverflow.com/questions/44597662/conda-command-is-not-recognized-on-windows-10>`_.


.. _new-install:

New & Existing User Installation
=================================

.. note::

    Users working with GPUs on Windows machines, please see our :ref:`FAQ <general-faqs>` section regarding installation steps.

.. note::

    Since the release of empanada-napari version 1.2.4, Python 3.9 and below are no longer supported. If you have an existing installation, we recommend creating a new environment with a supported Python version (3.10-3.13) to avoid conflicts.

.. tab-set::

   .. tab-item:: Windows

    #. Create a new virtual environment::

        conda create -y -n empanada -c conda-forge python=3.11

    #. Activate the new environment::

        conda activate empanada

    #. Install napari 0.6.6 with pip::

        pip install napari[all]==0.6.6

    #. Install empanada-napari 1.2.4 with pip::

        pip install empanada-napari==1.2.4

    For alternative and more detailed napari installation instructions, see the `official napari installation tutorial <https://napari.org/0.6.6/tutorials/fundamentals/installation.html>`_.

   .. tab-item:: Linux

    #. Create a new virtual environment::

        conda create -y -n empanada -c conda-forge python=3.11

    #. Activate the new environment::

        conda activate empanada

    #. Install napari 0.6.6 with pip::

        pip install napari[all]==0.6.6

    #. Install empanada-napari 1.2.4 with pip::

        pip install empanada-napari==1.2.4

    For alternative and more detailed napari installation instructions, see the `official napari installation tutorial <https://napari.org/0.6.6/tutorials/fundamentals/installation.html>`_.

   .. tab-item:: MacOS (Apple Silicon)

    .. note::

        **September 2026:** Temporary fix because of JIT deprecation.

    #. Create a new virtual environment::

        conda create -y -n empanada -c conda-forge python=3.11

    #. Activate the new environment::

        conda activate empanada

    #. Install napari 0.6.6 with pip::

        pip install "napari[all]==0.6.6"

    #. Install empanada-napari 1.2.4 with pip::

        pip install empanada-napari==1.2.4

    For alternative and more detailed napari installation instructions, see the `official napari installation tutorial <https://napari.org/0.6.6/tutorials/fundamentals/installation.html>`_.

   .. tab-item:: MacOS (Intel)

    .. note::

        **September 2026:** Temporary fix because of JIT deprecation.

    #. Create a new virtual environment::

        conda create -y -n empanada -c conda-forge python=3.11

    #. Activate the new environment::

        conda activate empanada

    #. Install pinned packages with pip::

        pip install --only-binary=:all: \
          "numpy==1.26.4" \
          "torch==2.2.2" "torchvision==0.17.2" \
          "numba==0.60.0" "llvmlite==0.43.0" \
          "opencv-python==4.11.0.86" "opencv-python-headless==4.11.0.86" \
          "imagecodecs==2026.1.14" \
          "triangle==20230923" \
          "napari[all]==0.6.6" \
          "empanada-napari==1.2.4"

    For alternative and more detailed napari installation instructions, see the `official napari installation tutorial <https://napari.org/0.6.6/tutorials/fundamentals/installation.html>`_.

    .. note::
        Newer versions of dependencies such as PyTorch no longer support MacOS with Intel chips. If you are still having issues, we recommend creating an environment with python=3.9, then installing empanada-napari==1.2.1 and napari==0.4.18.

        For step-by-step instructions, :ref:`click here <older-empanada-napari>`.


.. _update-install:

Updating an existing installation
=================================

If you already have empanada-napari installed, activate your conda environment and run::

    pip install --upgrade empanada-napari==1.2.4

Then restart napari. To check your installed version::

    pip show empanada-napari


To verify installation, run::

    napari &

If installation was successful you should see empanada-napari in the Plugins menu. If you don't, restart napari.
For further troubleshooting, please see the :ref:`FAQ <faqs>`.
