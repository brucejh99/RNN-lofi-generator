# RNN-lofi-generator
Recurrent Neural Network to generate lo-fi music for CS486. The neural network was built with Keras, and is trained on a lo-fi music dataset of at least 10,000 notes. 

Steps to run the project:
1. Copy the scripts onto Google Colab or copy onto a machine with numpy, pandas and keras installed.
2. Run the first 2 scripts to install Music21 and import relevant modules.
3. Run "Processing the midi into a notes array" script. This only needs to be run once to store the notes as an array to the file. Future use of this project does not need to repeat this operation.
4. Run the code under "Processing the notes array into the numpy array format for the NN". This will store your notes in-memory from the saved file in step 3 and get some important data such as numPitches used in the RNN model.
5. Run "Create the model and its layers" which will build the specified model (default one is the one tuned by us).
6. If you want to train the model, run "Fitting model from scratch" to train it and store weights after each epoch into a file. To load previously stored weights into the model, run "Generating model from previously trained weights" with your desired file path.
7. After training or loading weights into a model, run "Generate Music with Model" to produce some notes/chords and then run "Play the midi" to listen to the results!

- *Note:* we also provided the "Plotting Results" section which, given the model specified in its code, will create, train and print out the average validation accuracy for the model with five-fold validation strategy.

