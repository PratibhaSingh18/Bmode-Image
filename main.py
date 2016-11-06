
if __name__ == "__main__":
    from manipulate import reshape_rf
    from envelope_detection import detect
    from output_generation import calc_b_geometry, generate_image

    # user input parameters <<integrate into argparse>>
    units = 'cm'
    save_png = True
    display = False
    save_path = './outputs/image.png'
    drange = [-50, 0]

    # load in rf data from binary and scan parameters from JSON

    # reshape the data based on scan geometry
    rf_image = reshape_rf(rf_vector, axial_samples, num_beams)
    """
    read in 1-d vector of rf data and shape into 2-d image based on number
    of axial samples and number of transmit beams

    :param rf_vector: 1-d float array of rf data read from binary
    :param axial_samples: number of samples in axial dimension
    :param num_beams: number of transmit beams
    :return: matrix (np.array [num_beams][axial_samples])
    """

    # perform envelope detection on rf image
    env_image = detect(rf_image)
    """
    perform envelope detection on input data by calculating the magnitude of
    the analytic signal

    :param data: input data to envelope detect
    :param axis: dimension along which detection is performed, default: -1
    :return: env_data (np.array)
    """

    # log compress envelope detected image
    log_image = None

    # save/display final B-mode image
    dz, dx = calc_b_geometry(fs, beam_spacing, c, units)
    """
    calculate b-mode sample spacing with user specified units

    :param fs: rf sampling frequency (Hz)
    :param c: speed of sound (m/s)
    :param beam_spacing: spacing between lateral beams (m)
    :param units: units of output values
    :return: dz, dx (float)
    """

    generate_image(log_image, dz=dz, dx=dx, dynamic_range=drange,
                   z_label=units, x_label=units, filename=save_path,
                   save_flag=save_png, display_flag=display)
    """
    display/save output image with user-specified dynamic range

    :param image: input image for display
    :param dz: axial sampling interval
    :param dx: lateral sampling interval
    :param dynamic_range: displayed dynamic range
    :param z_label: label for z (axial) axis
    :param x_label: label for x (lateral) axis
    :param filename: location and name of saved .png
    :param save_flag: enable to save .png
    :param display_flag: enable to display image
    """
