import cv2

RTSP_URL = "rtsp://admin:admin123@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0"

def get_camera_stream():
    cap = cv2.VideoCapture(RTSP_URL)
    if not cap.isOpened():
        print("Kamera ulanmayapti! RTSP URL-ni tekshiring.")
        return None
    return cap
