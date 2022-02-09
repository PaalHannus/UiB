# Plot and compare the fine-tuning of two models.
import numpy as np
import matplotlib.pyplot as plt


# Load the data.
# The data is a list of tuples, where each tuple contains the following:
# The first element is the current epoch
# The second element is the training loss
# The third element is the validation loss
# The fourth element is the precision
# The fifth element is the recall
# The sixth element is the F1 score
# The seventh element is the accuracy
data_ner = np.array([
    [1,	0.113600,	0.091842,	0.509547,	0.553318,	0.530531,	0.971212],
    [2,	0.072000,	0.074753,	0.609260,	0.639218,	0.623880,	0.977783],
    [3,	0.055900,	0.071990,	0.629909,	0.693720,	0.660276,	0.978306],
    [4,	0.041000,	0.069015,	0.655250,	0.691351,	0.672816,	0.980203],
    [5,	0.030700,	0.068949,	0.680936,	0.706754,	0.693605,	0.981385],
    [6,	0.023300,	0.075143,	0.712603,	0.716825,	0.714708,	0.981990],
    [7,	0.018000,	0.075876,	0.679117,	0.710900,	0.694645,	0.981055],
    [8,	0.014200,	0.078169,	0.682844,	0.716825,	0.699422,	0.981083],
    [9,	0.011800,	0.079455,	0.683380,	0.718602,	0.700549,	0.981138],
    [10, 0.010000,	0.081080,	0.695379,	0.722156,	0.708515,	0.981413],
])

data_pos = np.array([
    [1,	0.428800,	0.158514,	0.943617,	0.939393,	0.941500,	0.951030],
    [2,	0.151100,	0.130036,	0.953982,	0.950904,	0.952441,	0.959663],
    [3,	0.107600,	0.116720,	0.958807,	0.956689,	0.957746,	0.964173],
    [4,	0.086800,	0.106699,	0.964788,	0.962909,	0.963848,	0.969205],
    [5,	0.069400,	0.104559,	0.964808,	0.962677,	0.963741,	0.969260],
    [6,	0.058600,	0.103479,	0.967019,	0.964799,	0.965908,	0.970964],
    [7,	0.051600,	0.105408,	0.967089,	0.965206,	0.966146,	0.971184],
    [8,	0.044600,	0.106707,	0.967722,	0.965612,	0.966666,	0.971624],
    [9,	0.041100,	0.107641,	0.968127,	0.965932,	0.967028,	0.972092],
    [10,	0.037800,	0.108067,	0.967961,	0.966019,	0.966989,	0.972064],
])
# Create a function that plots the data in two subplots.
# The first subplot is the training loss and validation loss.
# The second subplot is the precision, recall, F1 score and accuracy.


def plot_data_subplots(data, task, lanugage):
    # Create a figure.
    fig, ax = plt.subplots(2, 1)

    # Add grid lines.
    ax[0].grid(True)
    ax[1].grid(True)

    # Compact the subplots.
    fig.subplots_adjust(hspace=0.5)

    # Plot the data.
    ax[0].plot(data[:, 0], data[:, 1], '.-', label='Training loss')
    ax[0].plot(data[:, 0], data[:, 2], '.-', label='Validation loss')
    ax[0].set_title(f'{task}-{lanugage}-loss')
    ax[0].set_xlabel('Epoch')
    ax[0].set_ylabel('Loss')
    ax[0].legend()

    # Make legends outside of the subplots.
    ax[0].legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
                 fancybox=True, shadow=True, ncol=2)

    # Create some space between the subplots.
    plt.subplots_adjust(hspace=0.5)

    ax[1].plot(data[:, 0], data[:, 3], '.-', label='Precision')
    ax[1].plot(data[:, 0], data[:, 4], '.-', label='Recall')
    ax[1].plot(data[:, 0], data[:, 5], '.-', label='F1 score')
    ax[1].plot(data[:, 0], data[:, 6], '.-', label='Accuracy')
    ax[1].set_title(f'{task}-{lanugage}-metric')
    ax[1].set_xlabel('Epoch')
    ax[1].set_ylabel('Score')
    ax[1].legend()

    # Make legends outside of the subplots.
    ax[1].legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
                 fancybox=True, shadow=True, ncol=2)

    # Show the figure.
    plt.show()


# Create a function to plot the loss-data.


def plot_data_loss(data, title, xlabel, ylabel):
    # Create a figure.
    fig, ax = plt.subplots()

    # Plot the data.
    ax.plot(data[:, 0], data[:, 1], label='Training loss')
    ax.plot(data[:, 0], data[:, 2], label='Validation loss')

    # Set the title and labels.
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Add a legend.
    ax.legend()

    # Show the figure.
    plt.show()


# Plot the data.
def plot_data_score(data, title, xlabel, ylabel):
    # Create a figure.
    fig, ax = plt.subplots()

    # Plot the data.
    ax.plot(data[:, 0], data[:, 3], label='Precision')
    ax.plot(data[:, 0], data[:, 4], label='Recall')
    ax.plot(data[:, 0], data[:, 5], label='F1 score')
    ax.plot(data[:, 0], data[:, 6], label='Accuracy')

    # Set the title and labels.
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Add a legend.
    ax.legend()

    # Show the figure.
    plt.show()


# plot_data_subplots(data_ner, "NER", "Norwegian")
plot_data_loss(data_ner, 'Fine-tuning Norwegian model (NER)', 'Epoch', 'Loss')
plot_data_score(data_ner, 'Fine-tuning Norwegian model (NER)',
                'Epoch', 'Score')

# plot_data_subplots(data_pos, "POS", "Norwegian")
plot_data_loss(data_pos, 'Fine-tuning Norwegian model (POS)', 'Epoch', 'Loss')
plot_data_score(data_pos, 'Fine-tuning Norwegian model (POS)',
                'Epoch', 'Score')
