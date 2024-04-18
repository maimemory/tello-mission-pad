from djitellopy import tello
import cv2

jkt = tello.Tello()
jkt.connect()
jkt.streamon()
jkt.enable_mission_pads()
jkt.set_mission_pad_detection_direction(1)

while True:
    img = jkt.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pad = jkt.get_mission_pad_id()

    cv2.putText(img_rgb, str(pad), (50, 100), 
    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    cv2.imshow("Live Stream", img_rgb)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        jkt.disable_mission_pads()
        break
