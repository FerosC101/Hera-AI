import torch
from torch.utils.data import DataLoader
from monai.losses import DiceLoss
from models.unet import get_model
from training.dataset import UltrasoundDataset

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

dataset = UltrasoundDataset("data/images", "data/masks")
loader = DataLoader(dataset, batch_size=4, shuffle=True)

model = get_model().to(device)

loss_fn = DiceLoss(to_onehot_y=True, softmax=True)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)

EPOCHS = 30

for epoch in range(EPOCHS):

    model.train()
    total_loss = 0

    for images, masks in loader:

        images = images.to(device)
        masks = masks.to(device)

        optimizer.zero_grad()

        outputs = model(images)

        loss = loss_fn(outputs, masks)

        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch+1} Loss: {total_loss/len(loader)}")

torch.save(model.state_dict(), "model.pth")
