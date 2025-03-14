from camera import Camera
import cv2

def main():
    camera = Camera()
    try:
        camera.start()
        print("Camera menyala, tekan 'q' untuk keluar")
        while True:
            frame = camera.read_frame()
            camera.drawer_box(frame)
            cv2.imshow("Camera", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        camera.stop()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
