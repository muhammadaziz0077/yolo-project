from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import cv2

app = FastAPI()

RTSP_URL = "rtsp://admin:admin123@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0"
cap = cv2.VideoCapture(RTSP_URL)

def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        _, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.get("/video")
async def video_feed():
    return StreamingResponse(generate_frames(), media_type="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
