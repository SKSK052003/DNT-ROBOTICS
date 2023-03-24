import cv2
input_vid = cv2.VideoCapture('video/input.mp4')
fps = input_vid.get(cv2.CAP_PROP_FPS)
frame_count = int(input_vid.get(cv2.CAP_PROP_FRAME_COUNT))
frame_width = int(input_vid.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(input_vid.get(cv2.CAP_PROP_FRAME_HEIGHT))

desired_fps = fps/4
skip_interval = int(round(fps / desired_fps)*4)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_vid = cv2.VideoWriter('output_video.mp4', fourcc, desired_fps, (frame_width, frame_height))

frame_num = 0
while input_vid.isOpened():
    ret, frame = input_vid.read()
    if not ret:
        break
    frame_num += 1
    if frame_num % skip_interval == 0:
        output_vid.write(frame)
input_vid.release()
output_vid.release()
cv2.destroyAllWindows()
