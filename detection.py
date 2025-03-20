import aircv as ac


def locate_image(screenshot, reference_array, threshold):
    for reference in reference_array:
        print(f"Looking for {reference}...")
        result = ac.find_template(screenshot, ac.imread(f"images/{reference}"), threshold)
        if result:
            print(f"Found {reference}!")
            return result['result'][:2]