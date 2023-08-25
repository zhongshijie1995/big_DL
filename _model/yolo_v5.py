import torch


class YoloV5Ctl(object):
    def __init__(self):
        self.model = None

    def init(self):
        # 加载模型
        if self.model is None:
            self.model = torch.hub.load('_model/yolo_v5', 'custom', path='_model/yolo_v5.pt', source='local')
        return

    def detect_by_url(self, img: str):
        # 模型识别
        results = self.model(img)
        # 返回结果
        return str(results.pandas())
