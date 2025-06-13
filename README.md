# Stick Figure Generator from Human Photos

This project uses Python and MediaPipe to detect human poses in photos and render them as simple stick figures.

## Features

* Uses MediaPipe pose estimation to detect human landmarks (joints)
* Draws stick figures based on the detected keypoints
* Optionally overlays the stick figure on the original image, or outputs a standalone figure on a white background

## Requirements

* Python 3.7 or higher
* mediapipe
* opencv-python
* numpy

You can install the required packages with:

```bash
pip install -r requirements.txt
```

## Directory Structure

```
.
├── inputs/
│   └── input.jpg
├── outputs/
│   └── output.jpg
├── scripts/
│   └── stick_figure.py
├── .gitignore
├── LICENSE
├── README_ja.md
├── README.md (you are here)
└── requirements.txt
```

## Usage

Run the following command from the project root directory:

```bash
python scripts/stick_figure.py --input inputs/input.jpg --output outputs/output.jpg --overlay True
```

Setting the `--overlay` option to `True` will overlay the stick figure on the original image. Setting it to `False` will draw the stick figure on a white background instead.

## Notes

* Input images should clearly contain a person. To ensure accurate pose detection, it is recommended to use images where the full body and face are visible.
* The output image will be saved to `outputs/output.jpg`.

## License

MIT [License](./LICENSE)

---

Special thanks to MediaPipe and OpenCV ❤️
