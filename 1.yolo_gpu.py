import cv2
from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")

# # Train the model
# if __name__ == '__main__':
#     train_results = model.train(
#         data="coco8_custom.yaml",  # path to dataset YAML
#         epochs=3,  # number of training epochs
#         imgsz=640,  # training image size
#         device=0,  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
#         workers=2,
#         batch=1
#     )

# run detect with GPU
# results = model("video1.mp4", device=0, stream=True)

# run detect with CPU
results = model("video1.mp4", device="cpu", stream=True)

# results[0].show()
for result in results:
    # original image
    orig_img = result.orig_img
    # after predict image
    predict_img = result.plot()
    if result:
        # run with GPU
        # boxes = result.cpu().boxes.numpy()  # Boxes object for bbox outputs

        # run with CPU
        boxes = result.boxes.numpy()  # Boxes object for bbox outputs

        for box in boxes:  # there could be more than one detection
            print("class", box.cls)
            print("conf", box.conf)
            print("xyxy", box.xyxy)

    # show original image
    # cv2.imshow("predict img", orig_img)

    # show image after predict
    cv2.imshow("predict img", predict_img)
    cv2.waitKey(1)