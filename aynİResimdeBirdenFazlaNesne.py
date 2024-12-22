def collate_fn(batch):
    images, targets = zip(*batch)  # Görüntüleri ve hedefleri ayır
    images = torch.stack(images, 0)  # Görüntüleri birleştir
    # Hedefleri doldur
    max_boxes = 10  # Maksimum nesne sayısı
    padded_targets = torch.zeros(len(targets), max_boxes, 5)  # 5 eleman: class, x_center, y_center, width, height
    for i, target in enumerate(targets):
        num_boxes = target.size(0)
        padded_targets[i, :num_boxes, :] = target  # Doldurulmuş tensörlere kopyala
    return images, padded_targets

# DataLoader oluşturma
dataloader = DataLoader(dataset, batch_size=16, shuffle=True, collate_fn=collate_fn)