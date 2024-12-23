if __name__ == '__main__':

    import Tkinter, tkFileDialog
    from os import path
    import motive as m

    root = Tkinter.Tk()
    root.withdraw()
    profile_file_u=tkFileDialog.askopenfilename(title='Choose a profile file to load: ', filetypes=[('motive profilefiles', '*.motive')])
    profile_file = profile_file_u.encode("ascii")
    m.load_profile(profile_file)

    for cam in m.get_cams():
        cam.frame_rate = 30

        if 'Prime 13' in cam.name:
            cam.set_settings(videotype=0, exposure=33000, threshold=40, intensity=0)  #check if 480 corresponds to these thousands described in motive
            cam.image_gain = 8  # 8 is the maximum image gain setting
            cam.set_filter_switch(False)
        else:
            cam.set_settings(0, cam.exposure, cam.threshold, cam.intensity)

    directory, extension = path.splitext(profile_file)
    saved_profile_pathname = ''.join([directory, '_vislight', extension])
    m.save_profile(saved_profile_pathname)
    m.shutdown()







