from bing_image_downloader import downloader

downloader.download('Tomato', limit=10,  output_dir='ActorsFaceData', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)