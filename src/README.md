# Object Recognition Application

This project is an object recognition application that utilizes a camera to capture video frames and identify objects in real-time. The application is structured to separate concerns, with dedicated modules for camera handling, object recognition, and utility functions.

## Project Structure

```
object-recognition-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── camera.py        # Handles camera operations
│   ├── recognition.py    # Contains object recognition logic
│   └── utils
│       └── __init__.py  # Utility functions and classes
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Setup Instructions

1. **Clone the repository:**

   ```
   git clone <repository-url>
   cd object-recognition-app
   ```

2. **Install dependencies:**
   Make sure you have Python installed. Then, install the required packages using pip:
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines

1. **Run the application:**
   To start the object recognition application, execute the following command:

   ```
   python src/main.py
   ```

2. **Camera Permissions:**
   Ensure that your application has permission to access the camera on your device.

3. **Model Loading:**
   The application will automatically load the pre-trained model specified in the `recognition.py` file. Make sure the model file is available in the expected directory.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
