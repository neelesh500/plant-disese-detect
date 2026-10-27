import os
import tensorflow as tf
# pyrefly: ignore [missing-import]
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, Dropout, GlobalAveragePooling2D, RandomFlip, RandomRotation, RandomZoom
from tensorflow.keras.models import Model, Sequential
import json

logger = tf.get_logger()
logger.setLevel('INFO')

def create_model(num_classes=38):
    input_shape = (224, 224, 3)
    
    # Data Augmentation Layer
    data_augmentation = Sequential([
        RandomFlip("horizontal_and_vertical"),
        RandomRotation(0.2),
        RandomZoom(0.2),
    ], name="data_augmentation")

    base_model = MobileNetV2(weights="imagenet", include_top=False, input_shape=input_shape)
    
    # Freeze base model layers
    base_model.trainable = False

    # Build the model using Functional API
    inputs = tf.keras.Input(shape=input_shape)
    x = data_augmentation(inputs)
    x = base_model(x, training=False)
    x = GlobalAveragePooling2D()(x)
    x = Dropout(0.5)(x)
    predictions = Dense(num_classes, activation="softmax")(x)
    
    model = Model(inputs=inputs, outputs=predictions)
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4),
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )
    return model

if __name__ == "__main__":
    print("🌿 Initializing Plant Disease Detection Model...")

    model = create_model(num_classes=38)
    model.summary()
    os.makedirs("models", exist_ok=True)

    DATASET_PATH = "dataset" # Update this path to where extracted dataset is
    if os.path.exists(DATASET_PATH):
        print(f"Dataset found at {DATASET_PATH}. Initiating training pipeline...")
        
        train_ds = tf.keras.preprocessing.image_dataset_from_directory(
            DATASET_PATH,
            validation_split=0.2,
            subset="training",
            seed=123,
            image_size=(224, 224),
            batch_size=32
        )
        
        val_ds = tf.keras.preprocessing.image_dataset_from_directory(
            DATASET_PATH,
            validation_split=0.2,
            subset="validation",
            seed=123,
            image_size=(224, 224),
            batch_size=32
        )
        
        # Save class names for app.py
        class_names = train_ds.class_names
        with open("models/class_names.json", "w") as f:
            json.dump(class_names, f)
        print("✅ Saved class mapping to models/class_names.json")
        
        # Callbacks for robust training
        callbacks = [
            tf.keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True),
            tf.keras.callbacks.ModelCheckpoint("models/plant_disease_model.h5", save_best_only=True)
        ]
        
        print("Training Started!")
        model.fit(train_ds, validation_data=val_ds, epochs=15, callbacks=callbacks)
        print("✅ Training Complete. Best model saved to models/plant_disease_model.h5")
        
    else:
        raise SystemExit(f"Dataset folder '{DATASET_PATH}' not found. No model was trained or saved.")
