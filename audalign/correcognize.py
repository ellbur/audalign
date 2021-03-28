import audalign.fingerprint as fingerprint
from audalign.filehandler import read, find_files
import scipy.signal as signal
import matplotlib.pyplot as plt


def correcognize(
    target_file_path: str,
    against_file_path: str,
    start_end_target: tuple = None,
    start_end_against: tuple = None,
    filter_matches: int = 0,
    sample_rate: int = fingerprint.DEFAULT_FS,
    plot: bool = False,
):

    target_array, _ = read(target_file_path, sample_rate=sample_rate)
    against_array, _ = read(against_file_path, sample_rate=sample_rate)

    # target_array = signal.butter(fingerprint.threshold)
    # correlation = signal.convolve(target_array, against_array)
    # correlation = signal.correlate(target_array, against_array)
    correlation = target_array
    # signal.coh
    # plt.xcorr(target_array, against_array)
    # plt.show()

    if plot:
        plot_cor(
            array_a=target_array,
            array_b=against_array,
            corr_array=correlation,
            sample_rate=sample_rate,
            arr_a_title=target_file_path,
            arr_b_title=against_file_path,
        )
    ...


def correcognize_directory(
    target_file_path: str,
    against_directory: str,
    start_end: tuple = None,
    filter_matches: int = 0,
    sample_rate: int = fingerprint.DEFAULT_FS,
    plot: bool = False,
):
    print(f"{target_file_path} : {against_directory}")
    ...


def plot_cor(
    array_a,
    array_b,
    corr_array,
    sample_rate,
    title="Comparison",
    arr_a_title=None,
    arr_b_title=None,
):
    new_vis_wsize = int(fingerprint.DEFAULT_WINDOW_SIZE / 44100 * sample_rate)
    fig = plt.figure(title)

    fig.add_subplot(3, 2, 1)
    plt.plot(array_a)
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    # plt.gca().invert_yaxis()
    if arr_a_title:
        plt.title(arr_a_title)

    arr2d_a = fingerprint.fingerprint(
        array_a, fs=sample_rate, wsize=new_vis_wsize, retspec=True
    )
    fig.add_subplot(3, 2, 2)
    plt.imshow(arr2d_a)  # , cmap=plt.cm.gray)
    plt.gca().invert_yaxis()
    if arr_a_title:
        plt.title(arr_a_title)

    fig.add_subplot(3, 2, 3)
    plt.plot(array_b)
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    # plt.gca().invert_yaxis()
    if arr_b_title:
        plt.title(arr_b_title)

    arr2d_b = fingerprint.fingerprint(
        array_b, fs=sample_rate, wsize=new_vis_wsize, retspec=True
    )
    fig.add_subplot(3, 2, 4)
    plt.imshow(arr2d_b)
    plt.gca().invert_yaxis()
    if arr_b_title:
        plt.title(arr_b_title)

    fig.add_subplot(3, 2, 5)
    plt.plot(corr_array)
    plt.title(f"Correlation")
    plt.xlabel("Sample Index")
    plt.ylabel("Offset")

    fig.tight_layout()

    plt.show()