import torch

def run_dl_model(train_loader, test_loader, model, optimizer, loss_function, epochs, device=None):
    """
    train_loader, test_loader : DataLoader
    model                     : nn.Module
    optimizer                 : torch.optim.Optimizer
    loss_function             : loss criterion, e.g. nn.CrossEntropyLoss()
    epochs                    : int
    device                    : "cpu" or "cuda" (auto‑detected if None)

    Prints per‑epoch train/test loss & accuracy, and returns a dict of lists.
    """
    device = device or ("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    results = {
        "train_loss": [],
        "test_loss": [],
        "train_accuracy": [],
        "test_accuracy": []
    }

    for epoch in range(epochs):
        # — Training phase —
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0

        for imgs, labels in train_loader:
            imgs, labels = imgs.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(imgs)
            loss = loss_function(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            preds = outputs.argmax(dim=1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)

        train_loss = running_loss
        train_acc  = (correct / total) * 100

        # — Evaluation phase —
        model.eval()
        running_loss = 0.0
        correct = 0
        total = 0

        with torch.no_grad():
            for imgs, labels in test_loader:
                imgs, labels = imgs.to(device), labels.to(device)
                outputs = model(imgs)
                loss = loss_function(outputs, labels)

                running_loss += loss.item()
                preds = outputs.argmax(dim=1)
                correct += (preds == labels).sum().item()
                total += labels.size(0)

        test_loss = running_loss
        test_acc  = (correct / total) * 100

        # — Print & record —
        print(f"Epoch: {epoch}")
        print(f"Train loss: {train_loss}")
        print(f"Test loss: {test_loss}")
        print(f"Train Accuracy: {train_acc}")
        print(f"Test Accuracy: {test_acc}")

        results["train_loss"].append(train_loss)
        results["test_loss"].append(test_loss)
        results["train_accuracy"].append(train_acc)
        results["test_accuracy"].append(test_acc)

    return results
