.. _installation:

Installation
------------

napari is still considered alpha phase software and may not install correctly on the
first attempt, if that happens please reach out to the napari developers directly `here <https://github.com/napari/napari/issues>`_.

.. important::

    **empanada-napari version 1.1.1 is now available!** This latest version has minor bug fixes regarding the Filter Labels and Count Labels modules.
    We have also frozen the numba (0.59.0) and napari (0.4.18) versions to avoid dependency conflicts.


.. note::

  **Only Python 3.7, 3.8, 3.9 are supported, 3.10 and later are not.**


Conda Installation
===================

1. If not already installed, you can `install miniconda here <https://docs.conda.io/en/latest/miniconda.html>`_.

2. Download the correct installer for your OS (Mac, Linux, Windows).

3. After installing `conda`, open a new terminal or command prompt window.

4. Verify conda installed correctly with::

    conda --version

.. note::
      If you get a "conda not found error" the most likely cause is that the path wasn't updated correctly. Try restarting
      the terminal or command prompt window. If that doesn't work then
      see `fixing conda path on Mac/Linux <https://stackoverflow.com/questions/35246386/conda-command-not-found>`_
      or `fixing conda path on Windows <https://stackoverflow.com/questions/44597662/conda-command-is-not-recognized-on-windows-10>`_.


.. _new-install:

New User Installation
=====================

.. note::

    Users working with GPUs on Windows machines, please see our :ref:`FAQ <general-faqs>` section regarding installation steps.

1. If you've previously installed and used conda, it's recommended (but optional) to create a new virtual environment in order to avoid dependency conflicts::

    conda create -y -n empanada -c conda-forge python=3.9

#. Activate the new environment::

    conda activate empanada

#. Install pyqt with conda::

    conda install pyqt

#. Install napari with pip::

    pip install "napari[all]"

#. To verify installation, run::

    napari

For alternative and more detailed installation instructions, see the
`official napari installation tutorial <https://napari.org/tutorials/fundamentals/installation>`_.

From here the easiest way to install empanada-napari is directly in napari.

1. From the “Plugins” menu, select “Install/Uninstall Plugins...”.

.. image:: ../_static/plugin-menu.png
  :align: center
  :width: 200px
  :alt: Napari Plugin menu

2. In the resulting window that opens, where it says “Install by name/URL”, type "empanada-napari".

.. image:: ../_static/plugin-install-dialog.png
  :align: center
  :width: 500px
  :alt: Plugin installation dialog

3. Click the “Install” button next to the input bar.

If installation was successful you should see empanada-napari in the Plugins menu. If you don't, restart napari.

If you still don't see it, try installing the plugin with pip::

    pip install empanada-napari


.. _update-install:

Existing User Version Update
==============================

To update to the newest version of empanada-napari, you must uninstall the older version.

If you installed napari into a virtual environment as suggested in the original release documentation, be sure to activate it::

    conda activate empanada

From here, you will need to update your current version of empanada-napari::

    pip empanada-napari --upgrade

.. note::

    You can also update to the current version by uninstalling empanada-napari::

        pip uninstall empanada-napari


    Then you will need to install the latest version using pip::

        pip install empanada-napari==1.1.1

Now you can launch napari with the latest version of empanada-napari::

    napari


