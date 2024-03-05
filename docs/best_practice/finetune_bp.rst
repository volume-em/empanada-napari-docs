.. _finetune-best-practice:

Finetuning Best Practices
============================

Finetuning a model involves modifying different parts of a pre-trained model to better suit the characteristics of your data.
In empanada, a finetuned model can't be given new capabilities. That means that the **MitoNet_v1** model can only be tweaked
to better segment mitochondria in new data; it can't be used to segment a different organelle like
nuclei. New tasks call for training new models: :ref:`Training Best Practices <train-best-practice>`.

.. note::

  empanada-napari is best for finetuning models quickly and for users with limited
  coding experience. The :ref:`Finetune a model <finetune-model>` module was designed to be simple and eliminate
  the complexities of setting hyperparameters.



How much training data and finetuning are needed depends on how well existing models segment your
data. For example, if the **MitoNet_v1** model appears to be about 30% accurate in terms of intersection-over-union,
relatively brief finetuning of 100-200 iterations with 16 labeled patches should be sufficient to get satisfactory results
(though it depends on how large and diverse the data you need to segment is). When working with large volumes that have
multiple distinct "contexts" (e.g., different cell types) try running inference on 2D slices in all of those areas.
If the model only performs poorly in a subset, then select training examples by dropping points in these areas using the
:ref:`Pick finetune/training patches <pick-patches>` module.

Although by default it's required that you have 16 labeled images in order to finetune a model there are ways to skirt
that requirement. One way is to use a **Custom config** with batch size set to a number smaller than 16 (see note).
You could also duplicate images and masks after they've been saved with :ref:`Save finetune/training patches <save-patches>` until
there are at least 16. Finally, if finetuning one of the **MitoNet** models you could supplement your annotations with
relevant data from `CEM-MitoLab <https://www.ebi.ac.uk/empiar/EMPIAR-11037/>`_. With the metadata spreadsheet it's
possible to pick subdirectories with images that are related to the biological context for which you'd like to
finetune the model.

.. note::

  A batch size of 16 may seem arbitrary but it's based on experience. For the given model architectures and training
  hyperparameters, 16 is verified to be safe. Going lower may make the BatchNorm parameters in the model
  unstable, going higher is perfectly fine.

Finally, setting the **Finetunable layers** appropriately can make finetuning faster and more effective. The layers available
to finetune are all in the encoder of the network, commonly a ResNet50 (decoder parameters are always trained).
With the layer set to *none* training will be fastest but may underfit. If the model was already pretty good on your
data then this shouldn't be much of a concern. Conversely, setting the layer to *all* will make training slower and
may lead to overfitting. That won't be a concern if your data is relatively homogeneous, but could be a problem otherwise.
As a rule of thumb, start with *none*. If the validation metrics/inference results aren't as good as you'd like try
*all*.

.. tip:: In our experience, using *stage4* for finetuning tends to be the best choice between the two extremes!

