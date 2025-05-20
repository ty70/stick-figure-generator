import cv2
import mediapipe as mp
import numpy as np
import argparse

# 引数のパース
parser = argparse.ArgumentParser(description='人物画像から棒人間を生成')
parser.add_argument('--input', required=True, help='入力画像のパス')
parser.add_argument('--output', required=True, help='出力画像のパス')
parser.add_argument('--overlay', default="True", help='元画像に重ねるかどうか (True or False)')
args = parser.parse_args()

overlay = args.overlay.lower() == "true"

# MediaPipe 初期化
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# 入力画像読み込み
image = cv2.imread(args.input)
if image is None:
    raise ValueError("画像が読み込めませんでした: " + args.input)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 姿勢推定
results = pose.process(image_rgb)
pose_landmarks = results.pose_landmarks

# 出力用キャンバス準備
if overlay:
    output_image = image.copy()
else:
    output_image = np.ones_like(image) * 255  # 白背景

# 棒人間の線を描く関数
def draw_stick_figure(image, landmarks, connections, visibility_th=0.5):
    mp_drawing.draw_landmarks(
        image,
        landmarks,
        connections,
        landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
        connection_drawing_spec=mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2)
    )

    # image_height, image_width, _ = image.shape
    # for connection in connections:
    #     start_idx, end_idx = connection
    #     start = landmarks[start_idx]
    #     end = landmarks[end_idx]
    #     if start.visibility > visibility_th and end.visibility > visibility_th:
    #         x1, y1 = int(start.x * image_width), int(start.y * image_height)
    #         x2, y2 = int(end.x * image_width), int(end.y * image_height)
    #         cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

# 棒人間描画
if pose_landmarks:
    # draw_stick_figure(output_image, pose_landmarks.landmark, mp_pose.POSE_CONNECTIONS)
    draw_stick_figure(output_image, pose_landmarks, mp_pose.POSE_CONNECTIONS)
else:
    print("姿勢が検出できませんでした。")

# 出力画像保存
cv2.imwrite(args.output, output_image)
print(f"出力画像を保存しました: {args.output}")
