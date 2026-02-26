import cv2
import os
import datetime


class CameraRecorder:
    def __init__(self):
        # Create the records folder if it doesn't exist
        if not os.path.exists("records"):
            os.makedirs("records")

        # Create a VideoCapture object
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            print("❌ Error: Could not open camera")
            exit()

        # Set resolution
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # Define the video codec and create a VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.output_file = f"records/video_{timestamp}.mp4"
        self.out = cv2.VideoWriter(self.output_file, fourcc, 20.0, (640, 480))

    def record_video(self):
        try:
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    print("⚠️ Warning: Failed to capture frame")
                    break

                if frame.ndim == 2:
                    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

                # 🔹 Get current timestamp
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # 🔹 Put timestamp on frame
                cv2.putText(
                    frame,
                    current_time,
                    (10, 30),  # Position (x, y)
                    cv2.FONT_HERSHEY_SIMPLEX,  # Font
                    0.7,  # Font scale
                    (0, 255, 0),  # Color (Green)
                    2,  # Thickness
                    cv2.LINE_AA,
                )

                self.out.write(frame)
                cv2.imshow("Camera", frame)

                key = cv2.waitKey(1)
                if key == ord("q") or key == 27:
                    print("Stopping recording...")
                    break

        except KeyboardInterrupt:
            print("\nRecording stopped manually (Ctrl+C)")

        finally:
            self.cap.release()
            self.out.release()
            cv2.destroyAllWindows()
            print(f"Video saved at: {self.output_file}")


# Run the recorder
if __name__ == "__main__":
    recorder = CameraRecorder()
    recorder.record_video()
