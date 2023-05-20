from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import cv2
import numpy as np
from send_telegram import send_telegram
import datetime
import threading
import tensorflow as tf
from object_detection.utils import ops as utils_ops
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
from imutils import face_utils
import dlib
import blink_detection as blink
import asyncio

def isInside(points, centroid):
    polygon = Polygon(points)
    centroid = Point(centroid)
    return polygon.contains(centroid)


def run_inference_for_single_image(model, image):
    image = np.asarray(image)
    input_tensor = tf.convert_to_tensor(image)
    input_tensor = input_tensor[tf.newaxis, ...]

    model_fn = model.signatures['serving_default']
    output_dict = model_fn(input_tensor)

    num_detections = int(output_dict.pop('num_detections'))
    output_dict = {key: value[0, :num_detections].numpy()
                   for key, value in output_dict.items()}
    output_dict['num_detections'] = num_detections
    output_dict['detection_classes'] = output_dict['detection_classes'].astype(np.int64)

    if 'detection_masks' in output_dict:
        detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(
            output_dict['detection_masks'], output_dict['detection_boxes'],
            image.shape[0], image.shape[1])
        detection_masks_reframed = tf.cast(detection_masks_reframed > 0.5,
                                           tf.uint8)
        output_dict['detection_masks_reframed'] = detection_masks_reframed.numpy()

    return output_dict





class SSDMobileNet():
    def __init__(self, detect_class=[]):
        # Parameters
        self.classnames_file = "label_map.txt"
        self.model = tf.saved_model.load("export_model/saved_model")
        # load file landmarks
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor('file_dlib/shape_predictor_68_face_landmarks.dat')
        self.conf_threshold = 0.5
        self.nms_threshold = 0.4
        self.detect_class = detect_class
        self.scale = 1 / 255
        self.last_alert = None
        self.alert_telegram_each = 30  # seconds

    # đọc tập tin chứa danh sách tên lớp của các đối tượng cần phát hiện trong mô hình.
    def read_class_file(self):
        with open(self.classnames_file, 'r') as f:
            self.classes = [line.strip() for line in f.readlines()]

    def draw_prediction(self, img, left, right, top, bottom, points):
        color1 = (0, 0, 255)
        color2 = (0, 255, 0)
        """ tính toán centroid bouding box"""
        # Tinh toan centroid
        # center_top = round((right - left) / 2)
        # center_bottom = round((bottom - top) / 2)
        # centroid_x = center_top + left
        # centroid_y = center_bottom + top
        # cv2.circle(img, (centroid_x, centroid_y), 5, (color), -1)
        # centroid = (centroid_x, centroid_y)
        """tính toán tọa độ bouding box mới"""
        pixcel_plus = 40
        left_top = (left + pixcel_plus, top + pixcel_plus)
        left_bottom = (left + pixcel_plus, bottom - pixcel_plus)
        right_top = (right - pixcel_plus, top + pixcel_plus)
        right_bottom = (right - pixcel_plus, bottom - pixcel_plus)
        # các điểm góc của bouding box
        cv2.circle(img, left_top, 5, color1, -1)  # A
        cv2.circle(img, right_top, 5, color1, -1)  # B
        cv2.circle(img, right_bottom, 5, color1, -1)  # C
        cv2.circle(img, left_bottom, 5, color1, -1)  # D
        # các cạnh của bouding box
        cv2.line(img, left_top, right_top, color2, 2)  # AB
        cv2.line(img, right_top, right_bottom, color2, 2)  # BC
        cv2.line(img, left_top, left_bottom, color2, 2)  # AD
        cv2.line(img, left_bottom, right_bottom, color2, 2)  # DC

        if isInside(points, left_top) == False:
            self.alert(img)
            return isInside(points, left_top)
        elif isInside(points, left_bottom) == False:
            self.alert(img)
            return isInside(points, left_bottom)
        elif isInside(points, right_top) == False:
            self.alert(img)
            return isInside(points, right_top)
        elif isInside(points, right_bottom) == False:
            self.alert(img)
            return isInside(points, right_bottom)

    def alert(self, img):
        cv2.putText(img, "ALARM!!!!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        # New thread to send telegram after 15 seconds
        if (self.last_alert is None) or (
                (datetime.datetime.utcnow() - self.last_alert).total_seconds() > self.alert_telegram_each):
            self.last_alert = datetime.datetime.utcnow()
            cv2.imwrite("file_test/alert.png", cv2.resize(img, dsize=None, fx=1, fy=1))
            thread = threading.Thread(target=send_telegram)
            thread.start()
        return img

    def detect(self, frame, points):
        im_height, im_width, chanel = np.shape(frame)
        category_index = label_map_util.create_category_index_from_labelmap("label_map.txt", use_display_name=True)
        # detection landmark
        faces = self.detector(frame)
        output_dict = run_inference_for_single_image(self.model, frame)
        # Loc cac object trong khung hinh
        vis_util.visualize_boxes_and_labels_on_image_array(
            frame,
            output_dict['detection_boxes'],
            output_dict['detection_classes'],
            output_dict['detection_scores'],
            category_index,
            instance_masks=output_dict.get('detection_masks_reframed', None),
            use_normalized_coordinates=True,
            line_thickness=8)
        print("Done draw on image ")
        ymin, xmin, ymax, xmax = output_dict['detection_boxes'][0]
        (left, right, top, bottom) = (round(xmin * im_width), round(xmax * im_width), round(ymin * im_height), round(ymax * im_height))
        id_max_score = np.argmax(output_dict['detection_scores'])
        class_id = output_dict['detection_classes'][id_max_score]
        confidence = output_dict['detection_scores'][id_max_score]
        if (confidence >= self.conf_threshold) and (category_index[class_id]['name'] in self.detect_class):
            self.draw_prediction(frame, left, right, top, bottom, points)
            if category_index[class_id]['name'] == 'lie':
                for face in faces:
                    landmarks = self.predictor(frame, face)
                    landmarks = np.array([[p.x, p.y] for p in landmarks.parts()])  # lấy các điểm mốc trên khuôn mặt
                    left_eye_ratio = blink.calculate_eye_ratio(36, 41, landmarks)  # tỉ lệ mắt trái
                    right_eye_ratio = blink.calculate_eye_ratio(42, 47, landmarks)  # tỉ lệ mắt phải
                    eye_ratio = (left_eye_ratio + right_eye_ratio) / 2
                    if eye_ratio < blink.eye_threshold:
                        if not blink.timer_started:
                            blink.timer_started = True
                            blink.timer_start = cv2.getTickCount()
                        else:
                            # tính thời gian thực thi
                            if (cv2.getTickCount() - blink.timer_start) / cv2.getTickFrequency() > blink.blink_time:
                                blink.blink_count += 1
                                blink.timer_started = False
                    else:
                        blink.timer_started = False
                    if blink.blink_count >= blink.blink_threshold:
                        print('Sleepy alert!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                        blink.blink_count = 0
                        blink.is_sleeping = True
                    if blink.is_sleeping is True:
                        if eye_ratio >= blink.eye_threshold:
                            blink.is_sleeping = False
                            print('Awake alert!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                            # gửi cảnh báo
                            self.alert(frame)
                for (i, rect) in enumerate(faces):
                    # dự đoán và chuyển về mảng
                    shape = self.predictor(frame, rect)
                    shape = face_utils.shape_to_np(shape)
                    # vẽ các điểm
                    for (x, y) in shape:
                        cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
            else:
                pass
        return frame
