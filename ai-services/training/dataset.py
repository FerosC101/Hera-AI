import glob
from monai.transforms import (
    Compose, LoadImage, EnsureChannelFirst,
    Resize, ScaleIntensity, ToTensor
)

class UltrasoundDataset:

    def __init__(self, image_dir, mask_dir):

        self.images = sorted(glob.glob(image_dir + "/*.png"))
        self.masks = sorted(glob.glob(mask_dir + "/*.png"))

        self.transforms = Compose([
            LoadImage(image_only=True),
            EnsureChannelFirst(),
            Resize((256,256)),
            ScaleIntensity(),
            ToTensor()
        ])

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):

        image = self.transforms(self.images[idx])
        mask = self.transforms(self.masks[idx])

        return image, mask.long()
